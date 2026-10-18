---
name: figcraft
description: "Interface design and prototyping with FigCraft (Figma-style): UI/UX design, mobile app and web mockups, wireframes, dashboards, landing pages, design systems with components, variants and variables (Light/Dark tokens), clickable prototypes, social graphics and .fig files, from scratch or from starter templates. Frames, auto layout, components and instances, styles, variables, interactions; export PNG / JPG / SVG / WebP / PDF / .fig and component code (CSS, React, Leptos, SwiftUI, Compose)."
version: 0.3.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Creative, Design, UI, UX, Prototyping, Mockup, Wireframe, DesignSystem, Figma, MCP]
    related_skills: [storytold, storytold-install, vectorcraft, photocraft, designcraft, deckcraft, effectcraft]
---

# FigCraft

FigCraft is a free, open-source clean-room take on Figma (storytold Crafting Apps). An agent drives it through an
MCP server (`figcraft-cli mcp`) or CLI one-shots. Pages hold frames, groups, shapes, text, components and instances,
with auto layout, styles, variables and prototype interactions. Everything stays editable.

## When to Use

Use it for **screens and interface work**:

- mobile app screens, web pages, dashboards, landing pages, wireframes, UI mockups
- design systems: colour/text/effect styles, variables with Light/Dark modes, components with variants and properties
- clickable prototypes (interactions, flows, device settings) and developer handoff (CSS / React / Leptos / SwiftUI code)
- social graphics and banners from size presets (Instagram, X, LinkedIn, YouTube thumbnail…)
- a fast start from a built-in starter template (mobile app, landing page, dashboard, design system, wireframe kit,
  social posts, slides, icon set)
- opening `.fig` files (best effort) and Figma REST API file JSON; exporting `.fig` (experimental)

Pick a different Crafting App when:

| The job is… | Use |
|---|---|
| A logo, icon or illustration with Bézier paths and pathfinder work | `vectorcraft` |
| Retouching or compositing photos | `photocraft` |
| Multi-page print documents with flowing text | `designcraft` |
| A slide deck | `deckcraft` |
| Animation or motion graphics | `effectcraft` |

## Setup

1. If tools named `mcp_figcraft_*` are available, use them. This is the preferred way.
2. Otherwise check for the CLI with `figcraft-cli --version`. If it's missing, or the MCP tools are, load the
   `storytold-install` skill and run its `setup figcraft`. Then ask the user to start a new session or run
   `/reload-mcp` so the MCP tools appear.
3. Until the MCP tools appear, use the CLI (`run` scripts, see **CLI** below).

The MCP server is **headless**: an in-process engine with one untitled document and a CPU renderer. `inspect_ui`
only reports the session status and `screenshot {window:true}` renders the page. For the user to watch live, they
start `figcraft --control 7979` and the server runs as `figcraft-cli mcp --attach 7979` (not tested here).

**File access.** Bare `mcp` reads and writes any path the user can. With `--automation-read-root DIR` /
`--automation-write-root DIR` (repeatable, existing folders) reads must lie in a read or write root and writes in a
write root, else: `automation path rejected: <path> is outside the folders that may be written: <roots>`. The
`initialize` instructions list the roots. `--attach` refuses them (exit 2): start the app with the flags instead.

## Mental Model

- **Units are px** (page units), **y points down**. `create_node` and `set_properties` take `x`/`y` **relative to the
  parent frame** (the page when there is none). Groups don't count as parents. `inspect_document` reports `x`/`y`
  that way plus `absoluteBounds` in page coordinates.
- **Ids are integers.** In a new document the page is `1` and the first layer `2`, then counting up. Creation
  calls return `{id}`. Keep the ids. In a `batch` (and a CLI `run` script), `{"$step": n}` anywhere in a step's
  params is the `id` step n (zero-based) returned; `{"$step": n, "field": "…"}` takes another field.
- **Auto layout** (`layout: vertical|horizontal|grid`, `gap`, `padding`, `mainAlign`, `crossAlign`) positions the
  children. Size them with `sizingH`/`sizingV`: `fixed`, `hug` or `fill`. Their x/y are ignored.
- **Every menu action is a command** (561 of them). Run one with `run_command {command, params}` or several as one
  undo step with `batch`. Find them with `list_commands {filter}` or grep `${HERMES_SKILL_DIR}/references/commands.md`. Commands act on
  `ids` when given, else on the selection. New layers become the selection.
- **Components:** `component.create` turns a frame into a COMPONENT (same id). A component set holds variants named
  `Property=Value`. Instances follow their main; overrides (text, fills, properties) stay.
- **Variables** live in collections with modes (`Light`, `Dark`). Refer to collections, variables and modes by
  name. `variable.bind` links a layer field to one. `variable.setMode` on a frame switches what it shows.
- **Styles** (`paint`, `text`, `effect`, `grid`) get ids like `S:1`. Apply them by id or name.
- `open_file` and `file.new` add a document and make it active. `doc.list` / `doc.switch {index}` move between them.

## Tools (Hermes names them `mcp_figcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `create_node {type, x, y, width, height, parent, name, text, path, props}` | Make a `frame`, `rectangle`, `ellipse`, `polygon`, `star`, `line`, `arrow`, `text`, `vector` (SVG `path`), `section`, `component` or `slice`. `props` takes any `set_properties` key. Returns `{id, node}` |
| `set_properties {ids, props}` | Geometry, fills, strokes, effects, corner radius, auto layout, sizing, constraints, text props. Keys in `${HERMES_SKILL_DIR}/references/node-properties.md` |
| `run_command {command, params}` | Any of the 561 commands |
| `batch {commands, label?}` | Several commands as one undo step, all-or-nothing. `{"$step": n}` = the id step n made |
| `list_commands {filter}` | Look up command ids and params |
| `inspect_document {depth?, allPages?}` | Layer tree with ids, sizes, fills, layout, bound variables, styles; pages, flows, styles, history |
| `get_node {id, depth?}` | One layer as JSON (overrides, component properties, interactions) |
| `select {ids}` | Replace the selection (`[]` deselects) |
| `screenshot {ids?, scale?, maxSize?}` | Render the page or layers to PNG so you can **look** at it (default max side 1600) |
| `export {ids?, path?, format?, scale? \| size?}` | png, jpg, svg, webp, pdf, or `fig` (the whole file). `size`: `2x`, `512w`, `512h`. PDF print: `bleed`, `cropMarks`, `bleedMarks`, `cmyk` |
| `open_file {path}` / `save_file {path}` | Open `.figcraft`, `.json` (FigCraft or REST API), `.fig`, `.svg`, images (reply has `opened {summary, warnings}`); save `.figcraft`. A `.fig` path writes an export copy and keeps the document's own path |
| `undo` / `redo` | Edit history |
| `pointer`, `key`, `type_text`, `inspect_ui` | Drive the canvas like a mouse and keyboard would (rarely needed). `type_text {id, text}` replaces a text layer's text |

Resources: `figcraft://document`, `figcraft://node/{id}`, `figcraft://command/{id}`. Prompts with step plans:
`mobile_screen`, `design_system`, `landing_page`, `prototype_flow`.

## Procedure

1. **Start from a template** when one fits (recipe below). Otherwise **plan** the frame size (`frame.create
   {preset}`: `iPhone 16`, `Desktop`, `Instagram post`… listed in `${HERMES_SKILL_DIR}/references/node-properties.md`),
   a palette, type scale, and the layout as nested auto layout frames.
2. **Tokens first** for a system: variables and styles, so layers can bind to them.
3. **Build outside in:** the screen frame with auto layout, then sections (frames with `sizingH: "fill"`), then
   text and shapes. Use `fill` and `hug` instead of fixed sizes.
4. **Repeatable parts become components** (buttons, rows, cards). Place instances and set their properties.
5. **Look.** `screenshot {ids:[frame]}` after each major step and check it: spacing, overflow, alignment, contrast.
   Check numbers with `get_node`.
6. **Save** `save_file {path: "/abs/x.figcraft"}`, then **export** with absolute paths.

### Recipe: start from a starter template (tested)

```text
run_command template.list    → [{id, name, description, kind, size}]: mobile-app, landing-page, dashboard,
                               design-system, wireframe-kit, social-posts, slides, icon-set
run_command file.newFromTemplate {template:"social-posts", name:"Autumn"}   → {index, template} (new, unsaved, active)
inspect_document {depth:2}   (five frames: Square, Portrait, Story, Link preview, Banner; text and paint styles)
run_command edit.findReplace {find:"SUMMER TRAIL SERIES", replace:"AUTUMN NIGHT WALKS"}   → {matches:[9,27,45,63,81]}
                               (case-insensitive: "hello" also replaces "Hello" and "HELLO")
run_command style.update {style:"Brand/Accent", value:["#FF7A45"]}   → every layer using the style follows
screenshot {ids:[2], maxSize:800}  ·  save_file {path:"/abs/autumn.figcraft"}
```

The templates are full, editable designs with styles, components (and variables in `design-system`; a prototype flow
in `mobile-app`). Read the tree before editing: ids are large (the mobile app's screens are 50, 64, 136, 166).
`figcraft-cli run` works too: `[{"command":"file.newFromTemplate","params":{"template":"dashboard"}}]` with `--out
dash.figcraft` saves the template.

### Recipe: mobile screen with auto layout (tested)

```text
run_command frame.create {preset:"iPhone 16", x:0, y:0, name:"Login",
    props:{fill:"#FFFFFF", layout:"vertical", padding:[64,24,32,24], gap:16, sizingV:"fixed"}}   → {id:2}
create_node {type:"text", parent:2, text:"Welcome back", props:{fontSize:28, fontStyle:"Bold", fill:"#1A1B1E"}}
create_node {type:"text", parent:2, text:"Sign in to continue.", props:{fontSize:16, fill:"#555555", sizingH:"fill"}}
create_node {type:"frame", parent:2, name:"Email", props:{layout:"horizontal", padding:16, cornerRadius:12,
    stroke:"#E0E0E0", strokeWeight:1, fill:"#FFFFFF", sizingH:"fill", sizingV:"hug"}}            → 5
create_node {type:"text", parent:5, text:"you@example.com", props:{fontSize:16, fill:"#8A8F98"}}
create_node {type:"frame", parent:2, name:"Sign in", props:{layout:"horizontal", mainAlign:"center",
    padding:[14,24,14,24], cornerRadius:12, fill:"#3B5BDB", sizingH:"fill", sizingV:"hug"}}     → 7
create_node {type:"text", parent:7, text:"Sign in", props:{fontSize:16, fontStyle:"Bold", fill:"#FFFFFF"}}
get_node {id:2, depth:2}  ·  screenshot {ids:[2]}
save_file {path:"/abs/login.figcraft"}  ·  export {ids:[2], path:"/abs/login@2x.png", scale:2}
```

### Recipe: button component with variants and instances (tested)

```text
create_node {type:"frame", name:"Style=Primary", props:{layout:"horizontal", padding:[12,20,12,20], cornerRadius:8,
    mainAlign:"center", crossAlign:"center", fill:"#3B5BDB", sizingH:"hug", sizingV:"hug"}}           → 2
create_node {type:"text", parent:2, name:"Label", text:"Button", props:{fontSize:16, fontStyle:"Semi Bold", fill:"#FFFFFF"}} → 3
run_command component.create {ids:[2]}                            → {id:2} (now a COMPONENT)
run_command component.combineVariants {ids:[2]}                   → {id:4} (COMPONENT_SET "Style")
run_command component.addVariant {id:2, property:"Style", value:"Secondary"}   → {id:5}, its text is 6
set_properties {ids:[4], props:{name:"Button"}}
set_properties {ids:[5], props:{fill:"#FFFFFF", stroke:"#3B5BDB", strokeWeight:1.5}}  ·  set_properties {ids:[6], props:{fill:"#3B5BDB"}}
run_command component.addProperty {id:4, name:"Label", type:"text", default:"Button", layer:3}
run_command component.bindProperty {layer:6, property:"Label", field:"characters"}
run_command instance.create {component:4, x:200, y:0}             → 7 (the default variant)
run_command instance.create {component:4, x:200, y:80}            → 9
run_command instance.setProperties {ids:[9], properties:{Style:"Secondary", Label:"Cancel"}}
set_properties {ids:[2,5], props:{cornerRadius:22}}               → both instances follow
run_command component.properties {id:9}  ·  screenshot {scale:2}
run_command inspect.code {id:4, language:"react"}                 → TSX with a props interface + CSS
```

### Recipe: design tokens with Light/Dark variables (tested)

```text
batch {label:"Tokens", commands:[
  {command:"variable.createCollection", params:{name:"Theme", modes:["Light","Dark"]}},
  {command:"variable.create", params:{collection:"Theme", name:"color/bg", type:"color", values:{Light:"#FFFFFF", Dark:"#16181D"}}},
  {command:"variable.create", params:{collection:"Theme", name:"color/fg", type:"color", values:{Light:"#1A1B1E", Dark:"#F1F3F5"}}},
  {command:"variable.create", params:{collection:"Theme", name:"radius/card", type:"number", value:16}} ]}
create_node {type:"frame", name:"Card", width:320, props:{layout:"vertical", gap:12, padding:24, sizingV:"hug"}}  → 2
create_node {type:"text", parent:2, text:"Monthly budget", props:{fontSize:20, fontStyle:"Bold"}}                 → 3
batch {commands:[
  {command:"variable.bind", params:{ids:[2], field:"fill", variable:"color/bg"}},
  {command:"variable.bind", params:{ids:[2], field:"cornerRadius", variable:"radius/card"}},
  {command:"variable.bind", params:{ids:[3], field:"fill", variable:"color/fg"}} ]}
batch {commands:[
  {command:"style.create", params:{type:"text", name:"Heading/H3", from:3}},
  {command:"style.create", params:{type:"effect", name:"Elevation/1",
      value:[{type:"dropShadow", color:"#0000001F", offset:[0,4], radius:16}]}} ]}
run_command style.apply {ids:[2], style:"Elevation/1"}
run_command edit.duplicate {ids:[2], dx:360, dy:0}                → {ids:[4]}
run_command variable.setMode {ids:[4], collection:"Theme", mode:"Dark"}   → the copy renders dark
screenshot {scale:2}  ·  run_command variable.export {format:"css"}   → :root{…} + [data-theme="Dark"]{…}
```

Other bind fields: `stroke`, `fills/<i>/color`, `width`, `height`, `opacity`, `gap`, `paddingHorizontal`,
`characters`, `visible`, `fontSize`, `effects/<i>/color`, `componentProperties/<name>`.

### Recipe: social graphic exported to PNG (tested)

```text
run_command frame.create {preset:"Instagram post", x:0, y:0, name:"Launch post",
    props:{fills:[{type:"linearGradient", stops:["#1B1046","#FF6A3D"]}]}}     → 2 (1080×1350; gradient runs top → bottom)
create_node {type:"ellipse", parent:2, x:540, y:-200, width:700, height:700,
    props:{fill:"#FFD23F", opacity:0.55, effects:[{type:"layerBlur", radius:120}]}}   (the frame clips it)
create_node {type:"star", parent:2, x:800, y:180, width:140, height:140, props:{fill:"#FFFFFF", pointCount:4, innerRadius:0.25}}
create_node {type:"text", parent:2, x:96, y:820, width:888, text:"Plan the week in five minutes.",
    props:{fontSize:104, fontStyle:"Bold", lineHeight:"105%", fill:"#FFFFFF"}}   (a width makes text wrap)
create_node {type:"frame", parent:2, x:96, y:1150, props:{layout:"horizontal", padding:[22,40,22,40], cornerRadius:999,
    fill:"#FFFFFF", sizingH:"hug", sizingV:"hug", effects:[{type:"dropShadow", color:"#00000040", offset:[0,8], radius:24}]}}
screenshot {ids:[2], maxSize:800}
export {ids:[2], path:"/abs/launch.png"}  ·  export {ids:[2], path:"/abs/launch.jpg", size:"540w"}  ·  .svg / .pdf / .webp
```

### Recipe: click-through prototype (tested: data only)

```text
proto.interaction.add {id:<button>, trigger:{type:"onClick"}, action:{type:"navigate", dest:<frame>},
                       transition:{type:"smartAnimate"}, durationMs:300, easing:"easeOut"}
proto.interaction.add {id:<back>, trigger:{type:"onClick"}, action:{type:"back"}}
proto.flow.add {start:<first frame>, name:"Main flow"}  ·  proto.settings {device:"iPhone 16"}
```

`get_node` shows `interactions`, and `inspect_document` lists the page's `flows`. Playing it (`proto.present`)
needs the app. `run_command file.exportFramesPdf {path}` writes every top-level frame as one PDF page each.

### More building blocks

- **A nested tree in one call** (tested): `batch {commands:[{command:"node.create", params:{type:"frame",
  props:{layout:"vertical", gap:12}}}, {command:"node.create", params:{type:"text", parent:{"$step":0}, text:"Hi"}},
  …]}`. A later step's `{"$step": 2}` puts layers in the third step's frame. One undo step, no id guessing.
- **Images:** `image.place {path, parent, x, y, width, height, mode: fill|fit|crop|tile}` (tested).
- **Align, distribute, group:** `align.left|hcenter|right|top|vcenter|bottom`, `distribute.horizontal`, `object.group`.
- **Booleans:** `bool.union|subtract|intersect|exclude {ids}`, then `bool.flatten`.
- **Grid layout:** `layout:"grid"`, `gridColumns`, `columnTracks:["1fr","1fr",120]`, child `gridColumnSpan`.
- **Handoff:** `inspect.code {id, language: css|html|react|leptos|swiftui|compose}` (Leptos: a `#[component]` fn with
  an enum per variant property; tested), `inspect.properties {id}` (values with their token names), `annotation.add`,
  `set_properties {devStatus:"readyForDev"}`. `codeConnect.set {id, language, importPath, name}` links a component to
  your code; Leptos imports `use <importPath>::<name>;`, so pass the module (`crate::ui`), not the item.
- **Try a component:** `component.playground {id, properties:{Style:"Secondary", Label:"Delete account"},
  language?, path?: "/abs/p.png"}` returns its code and writes a PNG; the document doesn't change (tested).
- **Variables in styles:** `style.bind {style, field, variable}`: `fill` / `fills/<i>/color` of a paint style,
  `effects/<i>/radius|color|…` of an effect style, `fontSize`… of a text style. Layers follow their own mode
  (tested: a paint and a shadow radius switch with `variable.setMode`).
- **Frame ↔ group ↔ section:** `object.convertToFrame {ids}` / `object.convertToGroup {ids}` /
  `object.convertToSection {ids}` in place (tested; a section drops auto layout and clipping, a frame made from it
  keeps the fill).
- **Pages:** `page.add {name}`, `page.select {id}`, `page.setBackground {color}`.
- **Import:** `run_command file.import {path, x?, y?}` adds an SVG/image/`.fig`/JSON to the current document.

## Formats

- **Open:** `.figcraft` (native), `.json` (FigCraft or Figma REST API file JSON, with `<name>.variables.json` next to
  it for variables), `.fig` (best effort, `warnings` list what was skipped), `.svg` (editable layers), PNG/JPG/WebP/GIF/BMP.
- **Save:** `.figcraft`. **Export:** PNG, JPG, WebP (`scale` up to 64 or `size`), SVG (text outlined by default;
  `svgOutlineText:false` keeps `<text>`), PDF (frames one page each, real text, `bleed`/`cropMarks`/`cmyk`),
  `.fig` (the whole file, experimental, by `export {format:"fig"}` or `save_file {path:"/abs/x.fig"}`; tested: it reopens in FigCraft with variables and their modes, styles and
  bindings). Without `path` you get the image back inline.
- Variables: `variable.export {format: json|css, path?}` and `variable.import {variables}`.

## CLI (no MCP needed)

```bash
figcraft-cli run steps.jsonl --out screen.figcraft       # JSON array or JSON lines of {"command","params"}; one result line per step
figcraft-cli export app.figcraft -o exports/ --scale 2   # one PNG per top-level frame, named after it (· × → _)
figcraft-cli export app.figcraft -o hero.svg --node "Hero"     # --node takes an id or a layer name
figcraft-cli export app.figcraft -o print.pdf --node 2 --bleed 3mm --crop-marks --cmyk
figcraft-cli render app.figcraft -o page.png --scale 0.5 # the whole page with its background
figcraft-cli convert in.svg out.figcraft                 # by extension; .fig/.json/.svg in, .figcraft/.json/.svg/.png/.pdf/.fig out
figcraft-cli info app.figcraft [--json]                  # pages, top-level frames, counts; import notes
figcraft-cli commands --filter variable                  # the command catalog
```

`run` uses the same ids and params as `run_command`, and `{"$step": n}` like `batch`. The script is one undo step
and all-or-nothing: a failing step prints `{"command":"nope.x","error":"unknown command \`nope.x\`","ok":false,
"rolledBack":true,"step":0}`, exits 1 and saves nothing. The CLI takes no automation roots. Every subcommand
takes `--no-system-fonts` for renders that match on every machine (built-in fonts: Inter, Roboto, Open Sans, Lato,
Montserrat, Poppins, Nunito Sans, Source Sans 3/Serif 4, Merriweather, Playfair Display, Liberation, a few more).

## Pitfalls

- **x/y of an auto layout child are ignored without an error.** `set_properties {x:10}` returns `ok` and nothing
  moves. Use `gap`/`padding`/`mainAlign`, or take the child out of the flow with `absolute: true`.
- **`fill` needs an auto layout parent:** `invalid parameters for \`node.create\`: Fill needs an auto layout parent`.
- **A lone component has no variants:** `component.addVariant` fails with `invalid parameters for
  \`component.addVariant\`: the component isn't a variant (combine as variants first)`. Name it `Property=Value`,
  run `component.combineVariants {ids:[id]}` (one component is enough), then add variants. The set is named after
  the property, wraps the variants with 20 px padding (it starts at x, y − 20) and gets a dashed purple outline.
  Rename it.
- **Missing fonts fall back silently:** `fontFamily:"Helvetica"` is kept but renders with a fallback.
  `text.fonts {family:"Helvetica"}` returns `[]` for a missing font: check first. A missing style draws the nearest
  face; only `set_properties` warns (`Inter has no \`Light\` style: it draws in Regular, the nearest (…)`).
- **Auto layout keys need a frame, component or instance:** `invalid parameters for \`node.set\`: \`gap\` is an auto
  layout property, and layer 6 “Rectangle” is a RECTANGLE (only frames, components and instances have auto layout)`.
  With a frame among the `ids`, the other layers are skipped and named in `warnings`.
- **Text defaults:** Inter Regular, 12 px, **black**. Text hugs its content; give it `width` (or `sizingH:"fill"` in
  auto layout) to wrap.
- **Template ids are exact:** `invalid parameters for \`file.newFromTemplate\`: \`template\` must be an id from \`template.list\``.
- **A failing `batch` rolls back every step** and only names the problem (`no such node 999`), not the step.
- **Opening a `.fig` renumbers ids.** A round trip came back as page 2, frame 3, variables `1:15`. Re-inspect after
  `open_file`.
- **Relative paths** resolve against the server's working directory: `nope.figcraft: The system cannot find the file
  specified. (os error 2)`. Use absolute paths everywhere (inside the roots when the server has them).
- **Page screenshots crop to the layers** (edge shadows get cut): shoot a frame. **Frames clip** (`clip: false` to overhang).
- `variable.export {format:"css"}` writes numbers without units (`--radius-card: 16;`).
- Reopening FigCraft's own SVG drops drop shadows: `filter filter1 isn't a shadow or blur: the layer is drawn without it`.
- Errors are actionable: `no such node 999`, `invalid parameters for \`variable.bind\`: no such variable`,
  `invalid parameters for \`instance.create\`: \`component\` must be a component or component set`, and an
  unknown `set_properties` key lists every known key.

## Verification

- `screenshot {ids:[frame]}` and look at the image before you report the work as done.
- `get_node {id, depth:2}`: sizes, `sizing`, `layout`, `fills`, `boundVariables`, `styles`, `componentProperties`,
  `interactions` should be what you set. `inspect.properties {id}` shows the token behind each value.
- `export` replies give `path`, `format` and `bytes > 0`. `figcraft-cli info file.figcraft` confirms a saved file
  opens and lists its frames. Open exported PDFs with `pdfcraft` or render them with `vectorcraft-cli convert`.

## References

- `${HERMES_SKILL_DIR}/references/commands.md`: all 561 commands with params, grouped by area (component, instance,
  variable, style, layout, proto, text, file, export, inspect, library…). Grep it rather than reading it whole
  (`grep -n 'variable[.]set' ${HERMES_SKILL_DIR}/references/commands.md`).
- `${HERMES_SKILL_DIR}/references/node-properties.md`: every `set_properties` key, paint/effect value forms, the
  inspect fields, and the frame presets with sizes (`grep -n 'sizingH\|Social' …`).
- Upstream docs: https://github.com/storytold/figcraft/tree/main/docs (`mcp.md`, `cli.md`).
