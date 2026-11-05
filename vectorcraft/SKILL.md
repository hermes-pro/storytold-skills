---
name: vectorcraft
description: "Vector illustration with VectorCraft (Illustrator-style): logos, icons, posters, flyers, badges, infographics, charts, and SVG / PDF / EPS / AI / DXF artwork. Draw shapes and Bézier paths, paint, set type, apply live effects, export."
version: 0.5.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Creative, Design, Vector, Illustration, SVG, Logo, Icon, Poster, MCP]
    related_skills: [storytold, storytold-install, designcraft, photocraft, deckcraft, effectcraft, figcraft]
---

# VectorCraft

VectorCraft is a free, open-source clean-room take on Adobe Illustrator (storytold Crafting Apps). An
agent drives it through an MCP server (`vectorcraft-cli mcp`) or one-shot CLI commands. Everything it
makes stays editable: live shapes, live effects and live type. This skill is tested against VectorCraft 0.21.0.

## When to Use

Use it for **resolution-independent artwork**:

- logos, icons and icon sets, badges, stickers, wordmarks
- posters, flyers, cards, simple single-page layouts, social graphics
- infographics, diagrams and charts as vector art
- opening, fixing or converting SVG, PDF, `.ai`, EPS, DXF, EMF/WMF, Affinity and PSD files, and image
  tracing (raster → vector)

Pick a different Crafting App when:

| The job is… | Use |
|---|---|
| Retouching photos, compositing pixels, painting | `photocraft` |
| Developing RAW photos or batch photo edits | `lightcraft` |
| Multi-page documents: brochures, magazines, books | `designcraft` |
| Slides | `deckcraft` |
| Technical drawings to scale, floor plans | `cadcraft` |
| Editing pages, forms or annotations of an existing PDF | `pdfcraft` |
| Animation or motion graphics | `effectcraft` |

## Setup

1. If tools named `mcp_vectorcraft_*` are available, use them. This is the preferred way.
2. Otherwise check for the CLI with `vectorcraft-cli --version`. If it's missing, load the
   `storytold-install` skill and run its `setup vectorcraft`. Then ask the user to start a new session
   or run `/reload-mcp` so the MCP tools appear.
3. Until the MCP tools appear, use the CLI one-shots (see **CLI** below) or call the MCP server from a
   script.

`storytold-install` registers the server as `vectorcraft-cli mcp --headless`: a full in-process engine with a
CPU renderer. (Bare `vectorcraft-cli mcp` first tries a running app on `127.0.0.1:7979`.) Everything works headless except the UI tools (`ui_inspect`,
`ui_screenshot`, `inspect_ui`, `type_text`, `open_panel`, `screenshot {window:true}`). For the user to
watch live, they run `vectorcraft --control 7979` first. Other Crafting Apps use port 7979 too: see
**Pitfalls** if every tool says `unknown command`. Flags: `--headless` never connects, `--connect ADDR`
always does, and `--automation-read-root DIR` / `--automation-write-root DIR` confine file access to DIR
(they imply `--headless`; each may be given more than once). Without the root flags any absolute path works.

## Mental Model

- **Coordinates** are points (1/72 in). **y points down.** The origin is the first artboard's top-left.
  A new document is US Letter, 612 × 792. For another size, run `command_run file.new {width, height}`.
- **Every edit is a command** (911 of them). The drawing tools cover the common ones. Anything else goes
  through `command_run {id, params}`, or `command_batch {steps}` for several in one call. Find commands
  with `command_list {filter: "align", brief: true}`, or grep `references/commands.md`.
- **New objects become the selection**, and most commands act on the selection or on explicit `ids`
  (a command that works on the selection selects the `ids` first). Every tool that creates something
  returns its `id`, so keep those ids.
- Everything is undoable (`undo` / `redo`). `doc_inspect` shows the history.
- **Add-ons** are built-in command families under `addon.*` (Object › Plug-ins): parametric shapes, arrange,
  artwork cleanup, colour effects, path precision tools, a smart pen. They are ordinary commands; no install.

## Tools (Hermes names them `mcp_vectorcraft_<tool>`)

Common command tools (the same names across the Crafting Apps):

| Tool | Use it for |
|---|---|
| `command_list {filter?, menu?, brief?, enabled_only?}` | Find command ids and their params. `menu: "Object > Path"` lists one menu; `brief: true` leaves out the params (the bulk of the catalog). `query` is the same as `filter` |
| `command_run {id, params?}` | Run any command. Errors come back as `isError` with the reason |
| `command_batch {steps:[{id, params?}], atomic?, label?, stop_on_error?}` | Several commands in one call (at most 256 steps). A step's `id` can also be `draw_shape` or `draw_path`, with the tool's arguments as `params`; the reply's `created` lists their ids. A param string `"$N.path"` / `"$last.path"` takes a value from an earlier step's result (`"$0.id"`, `"$2.matches.0.id"`). `atomic: true` makes the batch one undo step |
| `doc_inspect {depth?, childLimit?, ids?, kind?, limit?, offset?}` | Artboards, layer tree with ids, bounds and paint, selection, history. Opacity reads back as `opacityPct` (0–100, what the tools take) and `opacity` (0–1). On big files: `depth: 0`, `ids: [..]` for just those nodes, `kind: "Group"` for every node of that Layers-panel kind (`Rectangle`, `Ellipse`, `Path`, `Type`…; an unknown kind returns no nodes), `limit`/`offset` to page |
| `render_preview {artboard?, max_side?, traceViews?}` | PNG of an artboard (default 0, at most 1024 px; never upscaled) so you can **look** at it. `traceViews: true` draws Image Trace objects in their trace view (outlines, source) |
| `ui_inspect`, `ui_screenshot`, `answer_dialog {set, action}` | The live desktop app only. `answer_dialog` fills and confirms or cancels the open dialog |

Drawing and file tools:

| Tool | Use it for |
|---|---|
| `draw_shape` | `rectangle`/`ellipse` (`x,y,width,height`, rectangle `radius`), `polygon` (`cx,cy,radius,sides`), `star` (`cx,cy,radius1,radius2,points`), `line` (`x1,y1,x2,y2`), plus `fill`, `stroke`, `strokeWidth`, `rotation`, and (both draw tools) `dash: [12, 6]`, `cap`, `join`, `opacity` (%), `name`, `effects: [{effect, params}]` |
| `draw_path` | Any curve: SVG `d` (`"M0 0 C …Z"`) or `points` (`[x,y]` or `{x,y,in,out}` Bézier handles), `closed` |
| `set_paint` | Fill, stroke and weight on the selection or `ids` (also becomes the default for new art). Replies `objects: N`; with nothing selected it only sets the new-art paint and says so in `note` |
| `add_text` | Point type at `(x, y)`: `y` is the **baseline**, `x` the left edge (with `justify: "center"` the line's centre, `"right"` its end). Area type with `width`/`height`, plus `fit: "autoHeight"` (frame grows) or `"shrinkText"`. `path` + `mode` puts type in or on a path. Also `font`, `size`, `color`, `vertical: true`. Returns `overflow: true` when the text doesn't fit |
| `apply_effect` | Live effects. Call it with no `effect` to get the catalog. See `references/effects.md` |
| `pathfinder {operation}` | `unite`, `minusFront`, `intersect`, `exclude`, `divide`, `trim`, `merge`, `crop`, `outline`, `minusBack` (destructive) |
| `transform` | `dx/dy`, `rotate` (degrees, counter-clockwise), `scale`/`scaleX`/`scaleY` (%), `reflect`, `shear`, `origin`, `copy` |
| `create_graph` | Column, bar, line, pie and other charts from `csv` (`",Series\nA,1\nB,2"`) or series/categories/rows |
| `text_wrap` | Make objects push area type around them |
| `screenshot {scale?, path?, artboard?}` | Like `render_preview`, sized by pixels per point, and can write the PNG to `path` |
| `open_file` / `save_file` / `export` | Open, save natively, export (see Formats). `save_file` also takes `compress`, `version` (1–4, for older VectorCraft) and `preview` (embed a PNG) for native files |
| `undo` / `redo` | Edit history |
| `select_tool`, `pointer_gesture`, `press_key`, `invoke_menu` | Drive tools like a mouse and keyboard would (rarely needed) |

The older names `list_commands`, `run_command {command, params}`, `inspect_document` and `inspect_ui`
still work and do the same as `command_list`, `command_run {id, params}`, `doc_inspect` and `ui_inspect`.

Resources read one thing at a time: `vectorcraft://object/{id}`, `vectorcraft://command/{id}`,
`vectorcraft://effect/{id}`, `vectorcraft://swatch/{name}`. Prompts give ready-made workflows: `poster`,
`icon-set`, `recolor`, `trace-and-style` and `export-set`. On a big document, find objects with
`command_run document.find {name?, kind?, text?}` instead of dumping the whole tree.

## Paint

- A colour can be `"#rrggbb"`, `"none"`, `[r,g,b]` (0–1), `{c,m,y,k}`, `{gray}`, or `{swatch: "Name"}`.
  Those forms are for the tools (`draw_shape`, `set_paint`…). The `paint.setFill` / `paint.setStroke`
  commands take `{color: "#…"}`, and `{none: true}` for no paint.
- **Gradient:** `{"gradient": {"kind": "linear"|"radial", "angle": deg, "stops": [{"offset": 0, "color": "#…"}, {"offset": 1, "color": "#…"}]}}`.
  The angle is counter-clockwise in a y-down document:
  - `angle: -90` runs stop 0 at the **top** to stop 1 at the bottom.
  - `angle: 90` runs bottom to top.
  - `angle: 0` runs left to right.
- One gradient across several objects: `paint.setFill {ids, gradient, span: "selection"}`. Without `span`
  each object gets the whole gradient.
- **Opacity and blend modes:** `command_run transparency.set {opacity: 0..100, blend: "Multiply"}`.
- Stroke details (caps, joins, dashes): `command_run stroke.set` / `stroke.setAdvanced`.

## Type

- `command_run text.fontList` lists the usable families: bundled fonts plus the system's. Use one of them.
  A missing font (e.g. `Helvetica` on Windows) silently falls back to **Source Sans 3**, and the export
  `warnings` say so. `text.missingFonts` (or `text.fonts`, with `status: exact|substitute|missing`) checks
  the document.
- Style after creating: `command_run text.setStyle {font, style: "Bold", size, leading, tracking, justify}`.
  Use `text.setRangeStyle {id, start, end, …}` for part of a story.
- **Centering a line:** `add_text {x: <artboard width / 2>, justify: "center", …}` centres it on `x`. Or create it
  anywhere, then `command_run object.align {horizontal: "center", to: "artboard"}`. Without `justify`, `x` is the
  left edge, so a guessed `x` puts the line off-centre or past the edge.
- Use area type (`width`/`height`) for paragraphs. **Watch for `overflow`** in the reply of `add_text`, `text.create`,
  `text.setStyle` and `text.setText`: the lines past the frame aren't drawn. Enlarge the frame or pass
  `fit: "autoHeight"` (or `"shrinkText"`, down to `fitMinPercent`, default 50). Convert type to paths with `command_run type.createOutlines`,
  or export SVG with `outlineText: true` when the file must render without the fonts.

## Procedure

1. **Plan** the canvas size, a 3–5 colour palette, and the hierarchy: background → main shapes → details → type.
2. **Set up:** use the open document (`doc_inspect`), or `command_run file.new {width, height}`.
3. **Build back to front.** Lock the background once it's placed (`command_run object.lock`) so `select.all`
   and alignment leave it alone.
4. **Look.** Call `render_preview` after each major step and actually check the image: alignment,
   overflow, contrast, spacing. Fix things before moving on.
5. **Save** the editable master with `save_file {path: "….vectorcraft"}`.
6. **Export** the deliverables and **read each reply's `warnings`** (missing fonts, features a format drops).

### Recipe: poster (tested)

```text
command_run {id:"file.new", params:{width:612, height:792}}
draw_shape {shape: rectangle, x:0, y:0, width:612, height:792, stroke:"none",
            fill:{gradient:{kind:"linear", angle:-90, stops:[{offset:0,color:"#1b1046"},{offset:1,color:"#ff6a3d"}]}}}
command_run {id:"object.lock"}
draw_shape {shape: ellipse, x:186, y:260, width:240, height:240, fill:"#ffd23f", stroke:"none"}
apply_effect {effect:"stylize.outerGlow", params:{blur:30, color:"#ffd23f", opacity:60}}
add_text   {text:"JAZZ NIGHT", x:0, y:620, size:72, font:"Source Sans 3", color:"#ffffff"}
command_batch {steps:[{id:"text.setStyle", params:{style:"Bold", tracking:80}},
                      {id:"object.align", params:{horizontal:"center", to:"artboard"}}]}
render_preview {max_side:800}                → check, adjust
save_file  {path:"/abs/poster.vectorcraft"}
export     {path:"/abs/poster.pdf"}  ·  export {path:"/abs/poster.png", scale:2}
```

For print resolution: `export {path:"/abs/poster.png", options:{ppi:300, background:"white"}}`
(612 pt at 300 ppi = 2550 px wide).

### Recipe: logo mark (tested)

```text
command_run {id:"file.new", params:{width:512, height:512}}
draw_shape {shape: ellipse, x:96, y:96, width:320, height:320, fill:"#5b3df5", stroke:"none"}
draw_shape {shape: ellipse, x:176, y:56, width:300, height:300, fill:"#000000", stroke:"none"}
command_run {id:"select.all"}
pathfinder {operation:"minusFront"}              → crescent, one path
draw_path  {d:"M300 330 L330 300 L360 330 L330 360 Z", fill:"#ffb800", stroke:"none"}
transform  {rotate:15}
render_preview {}
export {path:"/abs/logo.svg", outlineText:true}  ·  export {path:"/abs/logo.png", scale:4}
```

For a non-destructive combination, group the objects and apply a `pathfinder.*` effect instead.

### Recipe: styled chart (tested)

`create_graph` draws a group: one subgroup per series (named after it, holding its bars and legend
swatch), plus `Axes` and `Legend`. Bars come out black and grey, so colour each series group.

```text
create_graph {type:"column", x:40, y:40, width:260, height:200, csv:",Sales,Costs\nQ1,3,2\nQ2,5,3\nQ3,4,1"}
command_batch {steps:[
  {id:"document.find", params:{kind:"Group", name:"Sales"}},
  {id:"paint.setFill", params:{ids:["$0.matches.0.id"], color:"#5b3df5"}},
  {id:"document.find", params:{kind:"Group", name:"Costs"}},
  {id:"paint.setFill", params:{ids:["$2.matches.0.id"], color:"#ffb800"}}]}
render_preview {}
command_run {id:"graph.setData", params:{id: <graph id>, csv:"…"}}   → new data keeps the colours
```

The legend sits to the right of the plot, outside `width`. Leave room for it, or turn it off with
`graph.setType {legend: false}`. `name` in `document.find` is a substring, so pick series names that
don't contain each other.

### Recipe: many shapes in one call (tested)

```text
draw_shape {shape: rectangle, x:20, y:20, width:160, height:100, fill:"none", stroke:"#1b1046",
            strokeWidth:4, dash:[12,6], cap:"round", join:"round", name:"Frame"}
command_batch {atomic:true, label:"Dots", steps:[
  {id:"draw_shape", params:{shape:"ellipse", x:40,  y:200, width:80, height:80, stroke:"none"}},
  {id:"draw_shape", params:{shape:"ellipse", x:160, y:200, width:80, height:80, stroke:"none"}},
  {id:"draw_shape", params:{shape:"ellipse", x:280, y:200, width:80, height:80, stroke:"none"}},
  {id:"paint.setFill", params:{ids:["$0.id","$1.id","$2.id"], span:"selection",
     gradient:{kind:"linear", angle:0, stops:[{offset:0,color:"#5b3df5"},{offset:1,color:"#ffb800"}]}}},
  {id:"object.group", params:{ids:["$0.id","$1.id","$2.id"]}}]}
render_preview {}                 → one gradient runs across the three dots
```

`draw_path {d, …, effects:[{effect:"stylize.dropShadow", params:{x:4, y:4, blur:3}}]}` adds live effects
in the same call.

### Recipe: parametric shapes and add-ons (tested)

`addon.pathtools.shape.create` draws a shape that stays editable by number (`kind`: `rectangle`, `ellipse`,
`polygon`, `star`, `ring`, `arrow`, `cross`, `heart`, `gear`, `bubble`) with the current paint.

```text
command_run {id:"file.new", params:{width:600, height:400}}
set_paint  {fill:"#5b3df5", stroke:"none"}            → nothing selected: sets the new-art paint
command_batch {atomic:true, label:"Shapes", steps:[
  {id:"addon.pathtools.shape.create", params:{center:[100,100], kind:"gear", width:120, height:120, count:12}},
  {id:"addon.pathtools.shape.create", params:{center:[300,100], kind:"heart", width:120, height:110}},
  {id:"addon.pathtools.shape.create", params:{center:[500,100], kind:"arrow", width:140, height:80}},
  {id:"addon.pathtools.shape.create", params:{center:[300,300], kind:"star", width:120, height:120, count:7, a:0.45}},
  {id:"addon.pathtools.shape.set", params:{id:"$0.id", count:8}}]}      → the gear now has 8 teeth
apply_effect {ids:[<heart id>], effect:"addon.color.halftone", params:{frequency:12}}
command_run {id:"select.all"}
command_run {id:"addon.arrange.grid", params:{columns:3, gapX:40, centerOnArtboard:true}}
command_run {id:"addon.cleanup.check", params:{scope:"document"}}  → findings by kind, changes nothing
render_preview {}
```

The arrow points up at `rotation: 0` (`rotation` is clockwise). `addon.color.halftone` draws black dots by
default; pass `color`, or `fromArt: true` for the art's own colours. Editing a shape's anchors makes it a plain path.

### More building blocks

- **Repeat or array:** `transform {dx: 80, copy: true}`, then `command_run object.transformAgain`.
  Radial, grid and mirror repeats are `object.repeat.radial|grid|mirror`.
- **Align and distribute:** `object.align {horizontal|vertical, to: selection|artboard|key}`, `object.distribute`, `object.distributeSpacing`.
- **Group, stacking order, layers:** `object.group`, `object.arrange.bringToFront`, `layer.new`.
- **Clipping mask:** select the art with the clip shape on top, then `object.clippingMask.make`.
- **Tracing an image:** `open_file` a PNG/JPG (or `file.place {path}` it), then `imageTrace.make {preset}` and
  `imageTrace.expand` (or `imageTrace.makeAndExpand`). `imageTrace.presets` lists the presets. Options worth
  knowing: `enhanced: true` (the preset's better version), `shapes` (circles and rectangles come out as live
  shapes), `gradients`, `ignoreWhite` / `ignoreColor`.
- **3D:** `apply_effect {effect: "threeD.extrude", params: {depth: 30}}` gives a shaded, extruded shape (also
  `threeD.inflate`, `threeD.rotate`, `threeD.revolve`; bevels and lighting in `references/effects.md`).
- **Recolour artwork:** `recolor.colors`, then `recolor.apply {map}`. The `recolor` prompt walks through it.
- **Multiple sizes:** `artboard.new {x, y, width, height}`, then `export {artboard: i}` or
  `command_run document.exportForScreens {folder}` (one file per artboard). Without `x`/`y` a new artboard
  goes right of the last one, so read its position with `doc_inspect` before drawing on it.
- **Parametric shapes, arrange, cleanup:** see the recipe above; `addon.cleanup.fix` fixes what `addon.cleanup.check`
  finds, `addon.color.swatchLegend` draws a labelled swatch chart, `addon.arrange.size` / `.swap` / `.replace` resize, swap or
  replace selected objects.
- **Look before opening:** `command_run file.list {path}` lists a folder; `document.pdfInfo {path}` reads a PDF's pages.

## Formats

- **Read:** .vectorcraft .drawcraft .svg .svgz .pdf .ai .ait .eps .epsf .ps .dxf .emf .wmf .png .jpg .gif .webp
  .tif .bmp .tga .pcx .jp2/.jpx (JPEG 2000) .psd .psb (as the merged image) .af .afdesign .afpub (Affinity) .vctemplate
- **Save** (`save_file`, the document takes the file): .vectorcraft (native JSON), .vctemplate, .svg/.svgz, .pdf,
  .ai. A `.ai` or PDF saved this way carries the native document and reopens fully editable (`restored: true`).
- **Export** (`export`, the document keeps its path): svg/svgz (artboard = viewBox), pdf (one page per artboard),
  ai, eps, dxf, emf, wmf, png, png8, jpg, webp, gif, tiff, bmp, tga, psd (with layers), txt (the stories),
  vectorcraft, template.
- `export` takes `scale` (raster pixels per point; use 2–4 for crisp PNGs), `artboard`/`range`,
  `selection: true` (cropped to the selection), `outlineText` (SVG/DXF), and `options` (raster `ppi`,
  `background`, jpg `quality`; PDF text as outlines is `options:{advanced:{outlineText:true}}`).
  `command_run document.formats` lists each format's options.
- For apps that need an old-style `.ai`: `export {path:"/abs/x.ai", options:{aiVersion:"7"}}` writes a legacy
  version 7 file (layers, groups and type kept, one file per artboard; the `warnings` list what it drops).
- A raster export of any page area: `command_run document.export {path, rect:[x, y, width, height], ppi}`.
- Live effects survive export: geometry is baked, and shadows, glows and blurs become SVG filters.

## CLI (no MCP needed)

```bash
vectorcraft-cli convert in.svg out.pdf [--scale N] [--artboard I | --range "1-3"] [--outline-text] [--decimals N]
vectorcraft-cli convert in.vectorcraft out.ai --ai-version 7    # legacy .ai (also --hidden-objects, --transparent-images)
vectorcraft-cli info file.ai                         # JSON: artboards, object counts, fonts, import warnings
vectorcraft-cli run [--in FILE] --cmd shape.rectangle --params '{"x":50,"y":50,"width":200,"height":100}' \
                    --cmd paint.setFill --params '{"color":"#ff0000"}' --export out.svg --scale 2   # one JSON line per step
vectorcraft-cli run --commands steps.jsonl --export out.png  # steps from a file (or - for stdin): a JSON array or JSON Lines of {"command"|"id", "params"}
vectorcraft-cli commands                             # the full command catalog as JSON
```

`run` takes the same command ids and params as `command_run`, and `"$N.path"` references like
`command_batch` (`--params '{"id":"$1.id"}'`). That's handy for batch conversion and scripted art
without an MCP session. A failing step stops `run` with exit code 1. `convert` replies with the export's
`warnings` and `importWarnings` (what reading the input left out); `--decimals` (1–7) sets SVG precision,
`--editing-data` opens a `.ai` from its editing copy. A PDF written by `convert` leaves out the native document
(it reopens as plain PDF art) unless you pass `--preserve-editing`; `save_file`/`export` to PDF keep it.
`convert` refuses to overwrite IN when reading it lost something, unless `--replace-lossy`.

## Pitfalls

- **Every tool fails with ``unknown command `shape.rectangle` ``** (or `` `document.export` ``): the server
  connected to another Crafting App listening on port 7979 (stderr says `MCP server on stdio (remote
  127.0.0.1:7979)`). Run the server with `--headless`, or ask the user to close that app.
- **Paths:** use absolute paths for `save_file`, `export` and `open_file`. A relative path lands in the
  server's working directory, not yours. With the root flags, a path outside them fails with
  `automation path rejected: outside the write root …`.
- **Misspelt params:** most commands now refuse them: ``invalid parameters for `file.new`: unknown parameter
  `widht`; did you mean `width`?``, and for effects ``unknown parameter `blurr`; the command takes: radius``.
  A few still **ignore them silently** in 0.21.0: `transparency.set` and `stroke.set` (`transparency.set {opacty: 50}`
  succeeds and changes nothing), and `text.setStyle` / `paint.setFill` when a valid key comes with the typo
  (alone, a typo fails with `nothing to change` / `give color, none, swatch or gradient`). Copy keys from `command_list` /
  `references/commands.md`. Unknown *tool* arguments are refused: ``unknown argument `rotat` for `transform` ``.
- **`paint.setStroke {color: "none"}` fails** with ``invalid parameters for `paint`: bad color "none" ``.
  Use `{none: true}`, or `set_paint {stroke: "none"}`.
- **A failed `command_batch` keeps the steps before the failure**, even with `atomic: true` (they become
  one undo step). It stops at the failing step and reports `completed`, `failed` and each step's `error`.
- **`x` in `add_text` is the left edge** unless you pass `justify: "center"`/`"right"`. Don't guess a centred `x`.
- **Area type that's too small cuts the text off** without an error. The reply says `overflow: true`; act on it.
- **Gradient direction:** remember `angle: 90` puts stop 0 at the bottom.
- **Missing fonts** fall back to Source Sans 3 without an error. Pick from `text.fontList` and check the export `warnings`.
- **`select.all` grabs everything that isn't locked**, including the background. Lock it, or pass `ids`.
- **`pathfinder` is destructive** and works back to front: `minusFront` subtracts the front objects from the backmost one.
- Don't invent command ids: an unknown one fails with ``command_run: unknown command `nope.cmd` ``. Look them
  up with `command_list {filter}`, or read `vectorcraft://command/{id}` for the exact params.
- The UI tools fail in headless mode. That's expected, not a broken install.

## Verification

- `render_preview`, then look at the image before you report the work as done.
- `doc_inspect` should show the expected objects, paint and no stray empty text.
- Every `export` reply should list the right `path`, `format` and `bytes > 0`. Act on its `warnings`.
- `vectorcraft-cli info <file>` independently confirms a saved file opens and lists its fonts and artboards.

## References

Grep these rather than reading them whole, e.g. `grep -n 'object.align' ${HERMES_SKILL_DIR}/references/commands.md`.

- `${HERMES_SKILL_DIR}/references/commands.md`: all 911 commands with params, grouped by area.
- `${HERMES_SKILL_DIR}/references/effects.md`: all 130 live effects with params and defaults.
- Upstream docs: https://github.com/storytold/vectorcraft/tree/main/docs (`mcp.md`, `control-protocol.md`).
  `mcp.md` on `main` can describe features newer than 0.21.0.
