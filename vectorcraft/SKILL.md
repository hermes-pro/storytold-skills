---
name: vectorcraft
description: "Vector illustration with VectorCraft (Illustrator-style): logos, icons, posters, flyers, badges, infographics, charts, and SVG / PDF / EPS / AI / DXF artwork. Draw shapes and Bézier paths, paint, set type, apply live effects, export."
version: 0.1.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Creative, Design, Vector, Illustration, SVG, Logo, Icon, Poster, MCP]
    related_skills: [storytold, storytold-install, designcraft, photocraft, deckcraft, effectcraft]
---

# VectorCraft

VectorCraft is a free, open-source clean-room take on Adobe Illustrator (storytold Crafting Apps). An
agent drives it through an MCP server (`vectorcraft-cli mcp`) or one-shot CLI commands. Everything it
makes stays editable: live shapes, live effects and live type.

## When to Use

Use it for **resolution-independent artwork**:

- logos, icons and icon sets, badges, stickers, wordmarks
- posters, flyers, cards, simple single-page layouts, social graphics
- infographics, diagrams and charts as vector art
- opening, fixing or converting SVG, PDF, `.ai`, EPS, DXF, EMF/WMF files, and image tracing (raster → vector)

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

Without a running desktop app the server is **headless**: a full in-process engine with a CPU renderer.
Everything works except the UI-only tools (`inspect_ui`, `type_text`, `open_panel`, `screenshot {window:true}`).
For the user to watch live, they run `vectorcraft --control 7979` first, and `vectorcraft-cli mcp`
connects to it automatically.

## Mental Model

- **Coordinates** are points (1/72 in). **y points down.** The origin is the first artboard's top-left.
  A new document is US Letter, 612 × 792. For another size, run `run_command file.new {width, height}`.
- **Every edit is a command** (685 of them). The dedicated tools cover the common ones. Anything else goes
  through `run_command {command, params}`. Find commands with `list_commands {filter: "align"}`, or grep
  `references/commands.md`.
- **New objects become the selection**, and most commands act on the selection or on explicit `ids`.
  Every tool that creates something returns its `id`, so keep those ids.
- Everything is undoable (`undo` / `redo`). `inspect_document` shows the history.

## Tools (Hermes names them `mcp_vectorcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `inspect_document {depth?}` | Artboards, layer tree with ids, bounds and paint, selection, history. `depth: 0` on big files |
| `draw_shape` | `rectangle`/`ellipse` (`x,y,width,height`, rectangle `radius`), `polygon` (`cx,cy,radius,sides`), `star` (`cx,cy,radius1,radius2,points`), `line` (`x1,y1,x2,y2`), plus `fill`, `stroke`, `strokeWidth` |
| `draw_path` | Any curve: SVG `d` (`"M0 0 C …Z"`) or `points` (`[x,y]` or `{x,y,in,out}` Bézier handles), `closed` |
| `set_paint` | Fill, stroke and weight on the selection or `ids` (also becomes the default for new art) |
| `add_text` | Point type at `(x, y)`, where `x` is the **left** edge and `y` the **baseline**. Area type with `width`/`height`. `path` + `mode` puts type in or on a path. Also `font`, `size`, `color` |
| `apply_effect` | Live effects. Call it with no `effect` to get the catalog. See `references/effects.md` |
| `pathfinder {operation}` | `unite`, `minusFront`, `intersect`, `exclude`, `divide`, `trim`, `merge`, `crop`, `outline`, `minusBack` (destructive) |
| `transform` | `dx/dy`, `rotate` (degrees, counter-clockwise), `scale`/`scaleX`/`scaleY` (%), `reflect`, `shear`, `origin`, `copy` |
| `create_graph` | Column, bar, line, pie and other charts from `csv` (`",Series\nA,1\nB,2"`) or series/rows |
| `text_wrap` | Make objects push area type around them |
| `screenshot {scale?, path?}` | Render the artboard to PNG so you can **look** at it |
| `open_file` / `save_file` / `export` | Open, save natively, export (see Formats) |
| `list_commands` / `run_command` | Everything else |
| `undo` / `redo` | Edit history |
| `select_tool`, `pointer_gesture`, `press_key`, `invoke_menu` | Drive tools like a mouse and keyboard would (rarely needed) |

Resources read one thing at a time: `vectorcraft://object/{id}`, `vectorcraft://command/{id}`, `vectorcraft://effect/{id}`,
`vectorcraft://swatch/{name}`. Prompts give ready-made workflows: `poster`, `icon-set`, `recolor`,
`trace-and-style` and `export-set`.

## Paint

- A colour can be `"#rrggbb"`, `"none"`, `[r,g,b]` (0–1), `{c,m,y,k}`, `{gray}`, or `{swatch: "Name"}`.
- **Gradient:** `{"gradient": {"kind": "linear"|"radial", "angle": deg, "stops": [{"offset": 0, "color": "#…"}, {"offset": 1, "color": "#…"}]}}`.
  The angle is counter-clockwise in a y-down document:
  - `angle: -90` runs stop 0 at the **top** to stop 1 at the bottom.
  - `angle: 90` runs bottom to top.
  - `angle: 0` runs left to right.
- **Opacity and blend modes:** `run_command transparency.set {opacity, blendMode}`.
- Stroke details (caps, joins, dashes): `run_command stroke.set` / `stroke.setAdvanced`.

## Type

- `run_command text.fontList` lists the usable families: bundled fonts plus the system's. Use one of them. A
  missing font (e.g. `Helvetica` on Windows) silently falls back to **Source Sans 3**, and the export
  `warnings` say so. `run_command text.fonts` reports `status: exact|substitute|missing` for each font in the document.
- Style after creating: `run_command text.setStyle {font, style: "Bold", size, leading, tracking, justify}`.
  Use `text.setRangeStyle` for part of a story.
- **Centering a line:** create it anywhere, then `run_command object.align {horizontal: "center", to: "artboard"}`.
  The `x` in `add_text` is the left edge, so a guessed `x` puts the line off-centre or past the edge.
- Use area type (`width`/`height`) for paragraphs. Convert type to paths with `run_command type.createOutlines`,
  or export SVG with `outlineText: true` when the file must render without the fonts.

## Procedure

1. **Plan** the canvas size, a 3–5 colour palette, and the hierarchy: background → main shapes → details → type.
2. **Set up:** use the open document (`inspect_document`), or `run_command file.new {width, height}`.
3. **Build back to front.** Lock the background once it's placed (`run_command object.lock`) so `select.all`
   and alignment leave it alone.
4. **Look.** Call `screenshot {scale: 0.5}` after each major step and actually check the image: alignment,
   overflow, contrast, spacing. Fix things before moving on.
5. **Save** the editable master with `save_file {path: "….vectorcraft"}`.
6. **Export** the deliverables and **read each reply's `warnings`** (missing fonts, features a format drops).

### Recipe: poster (tested)

```text
draw_shape {shape: rectangle, x:0, y:0, width:612, height:792, stroke:"none",
            fill:{gradient:{kind:"linear", angle:-90, stops:[{offset:0,color:"#1b1046"},{offset:1,color:"#ff6a3d"}]}}}
run_command {command:"object.lock"}
draw_shape {shape: ellipse, x:186, y:260, width:240, height:240, fill:"#ffd23f", stroke:"none"}
add_text   {text:"JAZZ NIGHT", x:0, y:620, size:72, font:"Source Sans 3", color:"#ffffff"}
run_command {command:"text.setStyle", params:{style:"Bold", tracking:80}}
run_command {command:"object.align", params:{horizontal:"center", to:"artboard"}}
screenshot {scale:0.5}                       → check, adjust
save_file  {path:"/abs/poster.vectorcraft"}
export     {path:"/abs/poster.pdf"}  ·  export {path:"/abs/poster.png", scale:2}
```

### Recipe: logo mark (tested)

```text
run_command {command:"file.new", params:{width:512, height:512}}
draw_shape {shape: ellipse, x:96, y:96, width:320, height:320, fill:"#5b3df5", stroke:"none"}
draw_shape {shape: ellipse, x:176, y:56, width:300, height:300, fill:"#000000", stroke:"none"}
run_command {command:"select.all"}
pathfinder {operation:"minusFront"}              → crescent, one path
draw_path  {d:"M300 330 L330 300 L360 330 L330 360 Z", fill:"#ffb800", stroke:"none"}
transform  {rotate:15}
export {path:"/abs/logo.svg", outlineText:true}  ·  export {path:"/abs/logo.png", scale:4}
```

For a non-destructive combination, group the objects and apply a `pathfinder.*` effect instead.

### More building blocks

- **Repeat or array:** `transform {dx: 80, copy: true}`, then `run_command object.transformAgain`.
  Radial and grid repeats are under `object.repeat.*`.
- **Align and distribute:** `object.align {horizontal|vertical, to: selection|artboard|key}`, `object.distribute`, `object.distributeSpacing`.
- **Group, stacking order, layers:** `object.group`, `object.arrange.bringToFront`, `layer.new`.
- **Clipping mask:** select the art with the clip shape on top, then `object.clippingMask.make`.
- **Charts:** `create_graph {type: "column", x, y, width, height, csv}`. Bars come out **black** by default,
  so restyle them, then take a `screenshot` to confirm the colours took.
- **Tracing an image:** `open_file` a PNG/JPG (or `file.place` it), then `imageTrace.make {preset}` and `imageTrace.expand`.
  `imageTrace.presets` lists the presets.
- **Recolour artwork:** `recolor.colors`, then `recolor.apply`. The `recolor` prompt walks through it.
- **Multiple sizes:** `artboard.new`, then `export {artboard: i}` or `run_command document.exportForScreens`.

## Formats

- **Read:** .vectorcraft .svg .svgz .pdf .ai .ait .eps .dxf .emf .wmf .png .jpg .gif .webp .tif .bmp .vctemplate
- **Write:** .vectorcraft (native JSON), .svg/.svgz (artboard = viewBox), .pdf (one page per artboard),
  .eps .dxf .emf .wmf .png .jpg .webp .gif .tif .bmp .tga .psd (with layers), .txt (the stories)
- `export` takes `scale` (raster pixels per point; use 2–4 for crisp PNGs), `artboard`/`range`,
  `selection: true` (cropped to the selection), `outlineText`, and `options`. `run_command document.formats`
  lists each format's options.
- Live effects survive export: geometry is baked, and shadows, glows and blurs become SVG filters.

## CLI (no MCP needed)

```bash
vectorcraft-cli convert in.svg out.pdf [--scale N] [--artboard I | --range "1-3"] [--outline-text]
vectorcraft-cli info file.ai                         # JSON: artboards, object counts, fonts, import warnings
vectorcraft-cli run [--in FILE] --cmd shape.rectangle --params '{"x":50,"y":50,"width":200,"height":100}' \
                    --cmd paint.setFill --params '{"color":"#ff0000"}' --export out.svg   # one JSON line per step
vectorcraft-cli commands                             # the full command catalog as JSON
```

`run` takes the same command ids and params as `run_command`. That's handy for batch conversion and
scripted art without an MCP session.

## Pitfalls

- **Paths:** use absolute paths for `save_file`, `export` and `open_file`. Headless, the working directory is the
  server's, not yours.
- **`x` in `add_text` is the left edge.** Align to the artboard to center text instead of guessing.
- **Gradient direction:** remember `angle: 90` puts stop 0 at the bottom.
- **Missing fonts** fall back to Source Sans 3 without an error. Pick from `text.fontList` and check the export `warnings`.
- **`select.all` grabs everything that isn't locked**, including the background. Lock it, or pass `ids`.
- **`pathfinder` is destructive** and works back to front: `minusFront` subtracts the front objects from the backmost one.
- `run_command` errors name the problem, e.g. `unknown command`. Don't invent ids: look them up with
  `list_commands {filter}`, or read `vectorcraft://command/{id}` for the exact params.
- The UI-only tools fail in headless mode. That's expected, not a broken install.

## Verification

- `screenshot`, then look at the image before you report the work as done.
- `inspect_document` should show the expected objects, paint and no stray empty text.
- Every `export` reply should list the right `path`, `format` and `bytes > 0`. Act on its `warnings`.
- `vectorcraft-cli info <file>` independently confirms a saved file opens and lists its fonts and artboards.

## References

- `references/commands.md`: all 685 commands with params, grouped by area. Grep it rather than reading it whole.
- `references/effects.md`: all 51 live effects with params and defaults.
- Upstream docs: https://github.com/storytold/vectorcraft/tree/main/docs (`mcp.md`, `control-protocol.md`).
