---
name: photocraft
description: "Photo editing and compositing with PhotoCraft (Photoshop-style): retouch and color-grade photos, levels / curves / hue-saturation, layers and masks, selections, cut-outs, text on images, banners and thumbnails, resize / crop, filters, PSD files, data-driven variants from a CSV, batch-process folders. Export PNG / JPG / WebP / TIFF / PSD."
version: 0.4.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Creative, Design, Photo, Image, Raster, Retouch, Composite, PSD, MCP]
    related_skills: [storytold, storytold-install, lightcraft, vectorcraft, designcraft, effectcraft, figcraft]
---

# PhotoCraft

PhotoCraft is a free, open-source clean-room take on Adobe Photoshop (storytold Crafting Apps). An agent
drives it through an MCP server (`photocraft-cli mcp`) or one-shot CLI commands. Documents keep real
layers, masks, adjustment layers, smart objects, live type and layer styles, and round-trip PSD files.
This skill was tested on PhotoCraft 0.10.0.

## When to Use

Use it for **pixel work on one image (or a few) with layers**:

- retouching and colour-grading a photo, removing objects, healing spots, cut-outs and background removal
- composites: putting a logo, product or second photo onto a background, with masks, shadows and blend modes
- social graphics, banners, thumbnails and mockups built from photos plus text
- one template, many variants: a CSV of names / texts / visibility flags exported as one image per row
- resizing, cropping, converting, and opening or fixing `.psd` / `.psb` files
- applying the same edit to a folder of images (`photocraft-cli batch`)

Pick a different Crafting App when:

| The job is… | Use |
|---|---|
| Developing RAW photos, culling a shoot, the same grade on many photos with a catalog | `lightcraft` |
| Logos, icons, illustrations that must scale; SVG / PDF vector output | `vectorcraft` |
| Multi-page layouts: brochures, magazines, books | `designcraft` |
| Animation, motion graphics, video compositing | `effectcraft` |
| Slides | `deckcraft` |

## Setup

1. If tools named `mcp_photocraft_*` are available, use them. This is the preferred way.
2. Otherwise check for the CLI with `photocraft-cli --version`. If it's missing, load the `storytold-install`
   skill and run its `setup photocraft`. Then ask the user to start a new session or run `/reload-mcp`.
3. **File access needs roots.** `storytold-install` registers `photocraft-cli mcp --automation-read-root <HOME>
   --automation-write-root <HOME>` (HOME: the home folder, or `STORYTOLD_PHOTOCRAFT_ROOT`). MCP paths are
   **relative to HOME** (`Pictures/in.jpg`) or absolute inside it (`C:/Users/me/Pictures/in.jpg`). A plain
   `photocraft-cli mcp` can still edit documents, but every file tool fails with `automation filesystem access is
   not granted: read authority is absent` (or `write authority`). Then ask the user to run `storytold_tools.py
   register photocraft --replace` and `/reload-mcp`. `PHOTOCRAFT_AUTOMATION_*_ROOT` env vars are **not** honoured
   by `mcp` (tested on 0.10.0).
4. Until then, use the CLI one-shots (see **CLI**): they take ordinary paths anywhere.

Headless (no desktop app) is a full engine with a CPU renderer; only the `ui_*` tools and `control_call` need
the live app. For the user to watch, they start `photocraft --control 7878 --control-token-file <tok>
--automation-read-root <DIR> --automation-write-root <DIR>`, and the server runs as
`photocraft-cli mcp --bridge 127.0.0.1:7878 --control-token-file <tok>` (the app's roots then apply).

## Mental Model

- **Pixels, y down,** origin at the canvas top-left. Type sizes are points; at the default 72 ppi 1 pt = 1 px.
- **Session of documents.** `doc_open` / `doc_new` add a document and make it active (`index` in the reply);
  `doc_select {index}` switches; every command acts on the active document.
- **Layers have integer ids.** `doc_inspect` lists them top to bottom with `id`, `kind`, `bounds` `[x, y, w, h]`,
  `hasMask`, blend, opacity; `command_run layer.list {flat?}` is the short version. Commands take `layer: id` (or a
  layer name: `layer.setProps {layer:"logo"}`) and default to the **active layer**; a new layer becomes active.
  Ids are unique across the session, not per document (a fresh JPEG's Background is often id 2), and change when
  a file is reopened, so keep the ids replies give you. A wrong one fails with the list: `no such layer 1; the
  document's layers are 2 "Background" (a `layer` param takes an id or a name)`.
- **Every edit is an engine command** (918). `command_run {id, params}` runs one, `command_batch` several.
  Find ids with `command_list {filter: "curves"}` or grep `references/commands.md`.
- **Destructive vs non-destructive:** `image.adjustments.*` change the active pixel layer;
  `layer.newAdjustmentLayer.*` add an editable adjustment layer (change it later with `layer.setAdjustment`).
  Filters and `image.adjustments.*` on a smart object become editable smart filters.
- Everything is undoable (`edit.undo` / `edit.redo`); `doc_inspect` shows `history`. To experiment safely, run
  `image.duplicate {name}` or `history.newDocument {}` first: both make a new active copy.

## Tools (Hermes names them `mcp_photocraft_<tool>`)

| Tool | Use it for |
|---|---|
| `doc_open {path}` / `doc_new {width, height, background?, mode?, depth?, name?}` | Open a file (under the read root) / new doc (default 1920×1080 white RGB 8-bit) |
| `doc_inspect {index?}` | Layer tree with ids, bounds, masks, adjustments, text; selection, history, variables |
| `command_run {id, params?, wait?}` | Any engine command. Returns its JSON result (often the new `layer` id) |
| `command_batch {steps:[{id, params}], stop_on_error?}` | Several commands in one call; `{completed, failed, results}`. Not atomic: no rollback |
| `command_list {filter?, enabled_only?}` | Command ids, menu path, **param docs**, `enabled` and `disabledReason` |
| `doc_render_preview {max_side?, index?}` (alias `render_preview`) | Flattened PNG (default 1024 px, max 2048) so you can **look** at it |
| `doc_save {path?, quality?, tiffLayers?, tgaBits?, dpxBits?, format?}` / `doc_export` | Save native `.pcraft` or export by extension (under the write root) |
| `doc_place {path, scale?, fit?, center?}` | Place an image file as an embedded Smart Object layer |
| `doc_export_layers {dir, format?, prefix?, visible_only?}` | One file per layer (Layers to Files); refuses to overwrite |
| `doc_import_data_sets {path, delimiter?}` / `doc_export_data_sets {dir, format?, naming?, data_sets?}` | Variable data sets from a CSV / one flattened file per data set |
| `session_list`, `doc_select {index}`, `doc_close {index?}` | Manage open documents (close doesn't save; headless only). A bad `index` is an error: `no document at index 9` |
| `jobs_list`, `jobs_cancel {job?}` | Background jobs started with `wait: false` |
| `ui_inspect`, `ui_screenshot`, `ui_set`, `ui_menu_invoke`, `ui_pointer`, `control_call` | Live app only (bridge mode) |

Resources: `photocraft://document` (same JSON as `doc_inspect`) and `photocraft://commands` (same as
`command_list`). No prompts. An unknown top-level tool argument is a JSON-RPC error
(`unknown argument `bogus` for doc_open`), but unknown keys inside `params` are still ignored.

## Adjustments and colour

- Curves: `{points: [[0,0],[64,48],[192,210],[255,255]]}` (0..255; per channel under `red`/`green`/`blue`).
- Levels: `{inBlack, gamma, inWhite, outBlack, outWhite}` (0..255, gamma 0.01..9.99; below 1 darkens).
  Curves and Levels also take `eyedropper: {point: "black|gray|white", at: [x, y]}` to set points from the image.
- Hue/Saturation `{hue, saturation, lightness, colorize}`, Vibrance, Color Balance `{midtones: [cr, mg, yb]}`,
  Exposure, Photo Filter, Channel Mixer, Gradient Map `{stops: [[0,"#000"],[1,"#fff"]]}`, Color Lookup `{lut: "tealOrange"}`.
- One-stop "Camera Raw" grade on a pixel layer: `filter.cameraRaw {temperature, exposure, contrast,
  highlights, shadows, clarity, vibrance, …}`.
- For black and white use `blackWhite` (or `channelMixer {monochrome: true}`), not `hueSaturation {saturation: -100}`,
  which turns every fully saturated colour into the same mid-grey.
- Read a pixel back with `command_run document.pixel {x, y}` → `[r, g, b, a]` in 0..1.

## Selections and masks

- `select.rect {x, y, width, height, ellipse?, feather?, mode?}`, `select.lasso {points}`, `select.magicWand {x, y,
  tolerance}`, `select.colorRange {points: [[x,y]], fuzziness}`, `select.subject`, `select.sky`, then
  `select.modify.*`, `select.inverse`, `select.deselect`.
- **An active selection becomes the mask of a new adjustment or fill layer** (an active path becomes its vector
  mask). With no selection the mask is white. Deselect before adding a layer that should affect everything.
  For other layers use `layer.layerMask.revealSelection` (or `hideSelection`).
- `layer.new.layerViaCopy` lifts the selection to a new layer (cut-outs). `edit.fill {contents: "contentAware"}`
  removes what's selected. `layer.createClippingMask` clips the active layer to the one below.

## Type

- `type.create {x, y, text, font, size, color, align?}`: `y` is the **baseline**; with `align: "center"` `x` is the
  centre of the line. Paragraph text: `box: [x, y, w, h]` (wraps). Style afterwards with
  `type.setStyle {fontStyle: "Bold", tracking, leading, size, color, range?}`.
- A missing font (e.g. Helvetica on Windows) falls back, and the reply (and every `doc_save`) carries
  `font 'Helvetica' is not installed; text may render using a fallback face`. `type.fonts {family}` lists a
  family's faces; `type.resolveMissingFonts {}` lists the document's missing families. Prefer fonts the OS has.
- **Type on a path (tested):** draw the work path with `path.set {path:{subpaths:[{closed:false, knots:[{anchor:[100,380],
  in:[100,380], out:[250,80]}, {anchor:[700,380], in:[550,80], out:[700,380]}]}]}}`, `type.create` (its `x`/`y` don't
  matter), then `type.attachToPath {start:40}`. Around a shape: `type.attachToPath {layer, shape:<shape layer id>,
  flip?}` (another id: `"shape" is not a shape layer`). `type.detachFromPath` releases it. Survives a PSD round trip.

## Procedure

1. **Plan** the output size, the layer stack (background → photo → adjustments → type), and the deliverables.
2. **Open or create:** `doc_open` / `doc_new`, then `doc_inspect` to get layer ids.
3. **Edit non-destructively:** adjustment layers, masks, smart objects, layer styles, type layers.
4. **Look:** `doc_render_preview {max_side: 800}` after each major step, and check the image. Check numbers with
   `doc_inspect` (bounds, `hasMask`) or `document.pixel`.
5. **Save** the editable master (`.psd` for others, `.pcraft` native), then **export** flat deliverables and read
   each reply's `warnings`.

### Recipe: photo grade with vignette, resize and export (tested)

```text
doc_open {path:"shoot/photo.jpg"}                  → Background id from doc_inspect
command_run layer.newAdjustmentLayer.curves        {points:[[0,0],[64,48],[192,210],[255,255]]}
command_run layer.newAdjustmentLayer.hueSaturation {saturation:-20}
command_run select.rect {x:400, y:200, width:800, height:500, ellipse:true, feather:120}
command_run select.inverse
command_run layer.newAdjustmentLayer.levels {gamma:0.5}   → the selection becomes its mask: dark edges only
command_run select.deselect
command_run layer.select {layer:<Background id>}   → filters need a pixel layer
command_run image.crop {x:200, y:100, width:1200, height:800}
command_run image.imageSize {width:900, height:600, resample:"lanczos"}
command_run filter.sharpen.unsharpMask {amount:80, radius:1.2, threshold:2}
doc_render_preview {max_side:900}                  → check
doc_save {path:"out/photo.psd"} · doc_save {path:"out/photo.jpg", quality:88}
```

`image.crop` also takes `targetWidth`/`targetHeight` to crop and resample in one step.

### Recipe: logo / product composite (tested)

```text
doc_open {path:"bg.jpg"}                           → index 0
doc_place {path:"logo.png", scale:50, center:[250,700]}   → embedded Smart Object, {layer, bounds:[x0,y0,x1,y1]}
```

Or copy pixels from another open document:

```text
doc_open {path:"logo.png"}                         → index 1
command_run select.all · command_run edit.copy     → copies the trimmed opaque bounds
doc_close {} · doc_select {index:0}                → the clipboard survives the close
command_run edit.paste {center:[800,450]}          → {layer, offset}; without center it lands at (0,0)
command_run layer.setProps {name:"Logo", opacity:1, blend:"Normal"}
command_run edit.transform {quad:[[600,250],[1000,250],[1000,650],[600,650]]}   → scale/position exactly
command_run layer.layerStyle.dropShadow {color:"#000000", distance:10, size:20, opacity:60}
doc_render_preview {} · doc_save {path:"out/comp.psd"} · doc_save {path:"out/comp.png"}
doc_export_layers {dir:"out/layers"}               → comp_0000_<layer>.png … (dir must not hold those names)
```

`edit.transform` maps the layer's source frame onto `quad`; its reply `rect` is that source frame. For a relative
change use `edit.transform {scaleX:50, scaleY:50, rotate:30, dx:50, dy:0}` (percent, degrees, about the frame's
centre, then moved) (tested).

### Recipe: banner with photo-filled text (tested)

```text
doc_new {width:1200, height:630, background:"#101820", name:"banner"}
command_run layer.newFillLayer.gradient {from:"#ff5f6d", to:"#ffc371", angle:0, style:"linear"}
command_run type.create {x:600, y:380, text:"FRACTAL", font:"Segoe UI", fontStyle:"Bold", size:220,
                         color:"#ffffff", align:"center"}
(copy a photo from another open doc as above) → command_run edit.paste {center:[600,315]}
command_run layer.createClippingMask              → photo shows only inside the letters
doc_render_preview {} · doc_save {path:"out/banner.png"}
```

### Recipe: one image per CSV row (variable data sets) (tested)

```text
doc_new {width:800, height:400, background:"#203040", name:"card"}
command_run type.create {x:400, y:220, text:"Title", font:"Segoe UI", size:80, color:"#ffffff", align:"center"} → layer 3
command_run shape.create {kind:"ellipse", rect:[680,30,80,80], fill:"#ffcc00"}                                  → layer 4
command_run image.variables.define {defs:[{name:"title", layer:3, type:"textReplacement"},
                                          {name:"badge", layer:4, type:"visibility"}]}
doc_import_data_sets {path:"in/cards.csv"}         → {imported:2}
doc_export_data_sets {dir:"out/cards", naming:"card_{name}"}   → out/cards/card_alice.png, card_bob.png
doc_save {path:"out/card.pcraft"}                  → keeps the variables (PSD does not)
```

`cards.csv` (header = variable names; an **empty first header** makes column 1 the data-set name, otherwise
sets are named `Data Set 1`, `Data Set 2`…):

```text
,title,badge
alice,Hello Alice,true
bob,"Hi, Bob",false
```

Variable types: `textReplacement`, `visibility` (`true`/`false`), `pixelReplacement`. Preview one with `image.applyDataSet {name}`.

### More building blocks

- **Edit a smart object's contents (tested):** `layer.smartObjects.editContents {layer}` opens the contents as a
  new active document → edit it → `layer.smartObjects.saveContents` → `doc_close {}`. The parent updates in memory.
- **Several layers in one step:** `layer.setProps {layers:[6,7], opacity:0.5}` (tested). **Faces:** `image.detectFaces`.
- **Rotated crop, corners filled (tested):** `image.crop {x:-100, y:0, width:1700, height:900, angle:5, contentAware:true}`.
- **Text with effects:** `layer.layerStyle.dropShadow | stroke | outerGlow | colorOverlay | gradientOverlay | bevelEmboss`.
- **Arrange:** `layer.translate {dx, dy}`, `layer.moveTo {target, position}`, `layer.arrange.bringToFront`,
  `layer.align.horizontalCenters {to: "canvas"}` (selected layers; select with `layer.select {layer, mode:"add"}`).
- **Canvas:** `image.canvasSize {width, height, relative, anchor, extensionColor}`, `image.trim`,
  `image.imageRotation.90cw`, `image.mode.grayscale` / `cmyk`, `image.mode.bits16`.
- **Retouch:** `paint.spotHealing {points, size}`, `paint.cloneStamp {points, source}`, `paint.remove`, `edit.contentAwareFill`.
- **Paint:** `paint.stroke {points:[[x,y,pressure],…], size, color, hardness}`, `paint.gradient {from, to, colors}`.
  **Actions:** `actions.record` → edits → `actions.stop`, then `actions.get` gives steps for `batch`.
- **Photoshop .atn (tested):** `actions.save {action}` returns the `.atn` as base64 `data` (for `batch --actions
  x.atn`); `actions.load {data}` loads one, `actions.play {action}` runs it. Unplayable Photoshop steps fail at
  playback with their name.

## Formats

- **Read and write:** `.pcraft` (native, lossless), PSD, PSB, layered or flat TIFF, PNG, JPEG, WebP, GIF, BMP,
  TGA, ICO, QOI, PNM, OpenEXR, Radiance HDR, AVIF, DPX; Cineon (`.cin`) and HEIC (optional build feature)
  read-only. SVG opens as shape layers and places as a vector smart object.
- **PDF is write-only** (tested): `doc_save {path:"out/x.pdf"}` writes one flattened page (warning `PDF was saved
  flattened: …`); PhotoCraft can't open it again (`codec: unrecognized image format`).
- `doc_save` picks the format from the extension (`format` overrides). `quality` 1..100 for JPEG / WebP (WebP
  without `quality` is lossless). `tiffLayers: true` keeps layers in TIFF; `tgaBits: 24|32` for TGA;
  `dpxBits: 8|10|12|16` for DPX (default 8 for an 8-bit document, else 16).
- PSD / `.pcraft` keep layers, masks, adjustment layers, smart objects, smart filters and type (tested round trip).
  Only `.pcraft` keeps variables and data sets. Flat formats return the warning `N layer(s) flattened; layers,
  masks and blend modes are not kept`; JPEG adds `lossy compression` and composites transparency over white.

## CLI (no MCP needed; any path works)

```bash
photocraft-cli info file.psd --compact                       # JSON: size, mode, depth, layer tree
photocraft-cli convert in.psd out.jpg --quality 85           # any supported format to any other (also .pdf)
photocraft-cli run in.jpg --cmd image.adjustments.curves --params '{"points":[[0,0],[70,50],[190,215],[255,255]]}' \
               --cmd image.imageSize --params '{"width":800,"height":500}' --out out.jpg --quality 90
photocraft-cli run --new '{"width":600,"height":400,"background":"#223344"}' \
               --cmd type.create --params '{"x":300,"y":220,"text":"Hi","size":120,"color":"#ffcc00","align":"center"}' --out t.png
photocraft-cli batch --actions steps.json --in ./photos --out ./graded --format jpg --quality 80
photocraft-cli batch --actions grade.atn --action Grade --in ./photos --out ./graded   # a Photoshop .atn set
photocraft-cli run --new '{"width":10,"height":10}' --cmd file.automate.createDroplet \
               --params '{"path":"grade.pcdroplet","steps":[["image.imageSize",{"width":320,"height":180}]],"format":"png"}'
photocraft-cli droplet grade.pcdroplet a.jpg ./photos --out ./small   # files and folders
photocraft-cli commands --filter blur                        # the command catalog (--json for all fields)
```

All of the above were run on 0.10.0. `steps.json` is `[["image.adjustments.hueSaturation", {"saturation": -30}],
{"command": "image.imageSize", "params": {…}}]`; an Actions-panel set (`{"actions":[{name, steps}]}`) also works,
with `--action <name>`. `batch` refuses `--out` equal to `--in` unless `--in-place`, and exits 1 if any file failed.
`run` also allows the path-taking commands MCP refuses, e.g. `file.placeEmbedded {path, scale}` and
`file.export.layersToFiles {dir}` (tested). `photocraft-cli serve` keeps one headless session open over JSON lines.

## Pitfalls

- **Paths over MCP must be under the roots.** Relative paths use forward slashes (`automation path rejected:
  alternate separators are not allowed; use `/``), no `..` (`parent traversal is not allowed`), no `~`. An
  absolute path outside the root fails with `automation path rejected: absolute paths must be inside the automation
  root`. The output folder must exist: otherwise `I/O: automation write `…` failed (NotFound)`.
- **Path-taking commands are refused over MCP** (`file.placeEmbedded`, `file.saveACopy`, every `file.export.*`
  including `file.export.presets.list`, `actions.load|save {path}`, …):
  `automation command `file.placeEmbedded` uses ambient filesystem paths and is disabled; use capability-scoped
  document methods`. Use `doc_open`, `doc_save`, `doc_place`, `doc_export_layers`, the data-set tools, or the CLI `run`.
- **`doc_save` with no `path` only writes back PSD / PSB / .pcraft / OpenRaster.** On a JPEG: `pass `path`: without
  one, only a PSD, PSB, .pcraft or OpenRaster file that holds the whole document is written back, …`.
- **`doc_export_layers` never overwrites:** `I/O: automation create export `comp_0000_logo.png` failed (AlreadyExists)`.
  Use a fresh `dir` or a `prefix`.
- **Unknown command params are mostly ignored silently** (`image.imageSize {widht:100}` is a no-op that still adds
  an `Image Size` history step; `layer.setProps {bogus:1}` too). Few commands check (`layer.hideLayers {bogus:1}`:
  `invalid parameters for `layer.hideLayers`: unknown parameter `bogus` …`). Compare the reply with your request.
- **Filters and `image.adjustments.*` need a pixel layer.** A new adjustment or type layer becomes active, so the next
  filter fails with `filters need a pixel layer (active layer is an Adjustment layer)`. `layer.select` first.
  `batch` fails the same way on a PSD saved with an adjustment layer active (`… not a pixel layer`).
- **Bounds formats differ:** `doc_inspect` gives `[x, y, w, h]`; `type.create`, `edit.transform` and `doc_place`
  give `[x0, y0, x1, y1]`.
- **`wait: false` locks the document** until the job ends: other commands fail with `“Gaussian Blur” is still
  running on this document; wait for it to finish or cancel it (Esc)`. Keep the default (wait) unless you poll `jobs_list`.
- **PSD drops variables and data sets** without a warning; save `.pcraft` to keep them.
- **Bridge mode:** `doc_render_preview` returns a screenshot of the app window, not the image. Export a PNG to check
  pixels. `doc_close` fails: ``doc_close` is only available in headless mode (in the GUI use the window/tab UI or
  control_call)`. (Checked on 0.10.0.)

## Verification

- `doc_render_preview`, then look at the image before you report the work as done.
- `doc_inspect`: the expected layers, `hasMask`, adjustment values, text, and canvas `width`/`height`.
- Every `doc_save` reply names the `path`; read its `warnings` (flattening, lossy, missing fonts).
  `photocraft-cli info <file>` confirms a saved file re-opens with its layers.

## References

- `${HERMES_SKILL_DIR}/references/commands.md`: all 918 engine commands with params, grouped by area
  (`layer.newAdjustmentLayer`, `filter.blur`, `select`, `type`, `image.variables`…). Grep it rather than reading
  it whole, e.g. `grep -n "unsharp" ${HERMES_SKILL_DIR}/references/commands.md`.
- Upstream docs: https://github.com/storytold/photocraft/tree/main/docs (`mcp.md`: tools, resources, batch
  recovery, smart objects; `control-protocol.md`: control methods, automation roots, background jobs, headless `serve`).
