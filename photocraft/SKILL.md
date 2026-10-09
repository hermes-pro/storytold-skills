---
name: photocraft
description: "Photo editing and compositing with PhotoCraft (Photoshop-style): retouch and color-grade photos, levels / curves / hue-saturation, layers and masks, selections, cut-outs, text on images, banners and thumbnails, resize / crop, filters, PSD files, batch-process folders. Export PNG / JPG / WebP / TIFF / PSD."
version: 0.1.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Creative, Design, Photo, Image, Raster, Retouch, Composite, PSD, MCP]
    related_skills: [storytold, storytold-install, lightcraft, vectorcraft, designcraft, effectcraft]
---

# PhotoCraft

PhotoCraft is a free, open-source clean-room take on Adobe Photoshop (storytold Crafting Apps). An agent
drives it through an MCP server (`photocraft-cli mcp`) or one-shot CLI commands. Documents keep real
layers, masks, adjustment layers, smart objects, live type and layer styles, and round-trip PSD files.

## When to Use

Use it for **pixel work on one image (or a few) with layers**:

- retouching and colour-grading a photo, removing objects, healing spots, cut-outs and background removal
- composites: putting a logo, product or second photo onto a background, with masks, shadows and blend modes
- social graphics, banners, thumbnails and mockups built from photos plus text
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
3. **File access needs roots.** `storytold-install` registers the server as
   `photocraft-cli mcp --automation-read-root <HOME> --automation-write-root <HOME>`. HOME is the user's home
   folder, or `STORYTOLD_PHOTOCRAFT_ROOT` when that's set. MCP paths are then **relative to the home folder**,
   e.g. `Pictures/in.jpg` for `~/Pictures/in.jpg`. A server started as plain `photocraft-cli mcp` can still
   create and edit documents, but every `doc_open` / `doc_save` fails with `automation filesystem access is not
   granted: read authority is absent`. If you see that, the server was registered by hand: ask the user to run
   `storytold_tools.py register photocraft --replace`, then `/reload-mcp`. The `PHOTOCRAFT_AUTOMATION_*_ROOT`
   env vars are **not** honoured by `mcp` (tested on 0.5.0).
4. Until then, use the CLI one-shots (see **CLI**): they take ordinary absolute paths.

Headless (no desktop app) is a full engine with a CPU renderer; only the `ui_*` tools and `control_call` need
the live app. For the user to watch, they start `photocraft --control 7878 --control-token-file <tok>
--automation-read-root <DIR> --automation-write-root <DIR>`, and the server runs as
`photocraft-cli mcp --bridge 127.0.0.1:7878 --control-token-file <tok>` (the app's roots then apply).

## Mental Model

- **Pixels, y down,** origin at the canvas top-left. Type sizes are points; at the default 72 ppi 1 pt = 1 px.
- **Session of documents.** `doc_open` / `doc_new` add a document and make it active (`index` in the reply);
  `doc_select {index}` switches; every command acts on the active document.
- **Layers have integer ids.** `doc_inspect` lists them top to bottom with `id`, `kind` (Pixel, Adjustment,
  Type, SmartObject, Fill…), `bounds` `[x, y, w, h]`, `hasMask`, blend, opacity. Commands take
  `layer: id` and default to the **active layer**, and a new layer becomes active. Ids are unique across the
  whole session, not per document, so never guess one (`no such layer LayerId(3)`): keep the ids replies give you.
- **Every edit is an engine command** (817). `command_run {id, params}` runs one, `command_batch` several.
  Find ids with `command_list {filter: "curves"}` or grep `references/commands.md`.
- **Destructive vs non-destructive:** `image.adjustments.*` change the active pixel layer;
  `layer.newAdjustmentLayer.*` add an editable adjustment layer (change it later with `layer.setAdjustment`).
  Filters on a smart object (`layer.smartObjects.convertToSmartObject` first) become editable smart filters.
- Everything is undoable (`edit.undo` / `edit.redo`); `doc_inspect` shows `history`.

## Tools (Hermes names them `mcp_photocraft_<tool>`)

| Tool | Use it for |
|---|---|
| `doc_open {path}` / `doc_new {width, height, background?, mode?, depth?, name?}` | Open a file (relative to the read root) / new doc (default 1920×1080 white RGB 8-bit) |
| `doc_inspect {index?}` | Layer tree with ids, bounds, masks, adjustments, text; selection, history |
| `command_run {id, params?, wait?}` | Any engine command. Returns its JSON result (often the new `layer` id) |
| `command_batch {steps:[{id, params}], stop_on_error?}` | Several commands in one call; reports `completed` / `failed` per step |
| `command_list {filter?, enabled_only?}` | Command ids, menu path and **param docs** |
| `doc_render_preview {max_side?}` | Flattened PNG (default 1024 px, max 2048) so you can **look** at it |
| `doc_save {path?, quality?, tiffLayers?}` / `doc_export` | Save native `.pcraft` or export by extension (relative to the write root) |
| `session_list`, `doc_select {index}`, `doc_close {index?}` | Manage open documents (close doesn't save) |
| `jobs_list`, `jobs_cancel {job?}` | Background jobs started with `wait: false` |
| `ui_inspect`, `ui_screenshot`, `ui_set`, `ui_menu_invoke`, `ui_pointer`, `control_call` | Live app only (bridge mode) |

The server has no MCP resources or prompts; `command_list` is the live documentation.

## Adjustments and colour

- Curves: `{points: [[0,0],[64,48],[192,210],[255,255]]}` (0..255; per channel under `red`/`green`/`blue`).
- Levels: `{inBlack, gamma, inWhite, outBlack, outWhite}` (0..255, gamma 0.01..9.99).
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
- A selection does **not** become the mask of a new adjustment layer. Create the layer, then run
  `layer.layerMask.revealSelection` (or `hideSelection`) while the selection is still active.
- `layer.new.layerViaCopy` lifts the selection to a new layer (cut-outs). `edit.fill {contents: "contentAware"}`
  removes what's selected. `layer.createClippingMask` clips the active layer to the one below.

## Type

- `type.create {x, y, text, font, size, color, align?}`: `y` is the **baseline**; with `align: "center"` `x` is the
  centre of the line. Paragraph text: `box: [x, y, w, h]` (wraps). Style afterwards with
  `type.setStyle {fontStyle: "Bold", tracking, leading, size, color, range?}`.
- A missing font (e.g. Helvetica on Windows) silently falls back. `type.fonts {family}` lists the faces of a family;
  `type.resolveMissingFonts {}` lists the document's missing families. Prefer fonts the OS has (Segoe UI, Arial…).

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
doc_open {path:"shoot/photo.jpg"}
command_run layer.newAdjustmentLayer.curves        {points:[[0,0],[64,48],[192,210],[255,255]]}
command_run layer.newAdjustmentLayer.hueSaturation {saturation:-20}
command_run select.rect {x:400, y:200, width:800, height:600, ellipse:true, feather:120}
command_run select.inverse
command_run layer.newAdjustmentLayer.levels {gamma:0.7}
command_run layer.layerMask.revealSelection        → dark edges only
command_run select.deselect
command_run layer.select {layer:<Background id>}   → filters need a pixel layer
command_run image.crop {x:200, y:100, width:1200, height:800}
command_run image.imageSize {width:900, height:600, resample:"lanczos"}
command_run filter.sharpen.unsharpMask {amount:80, radius:1.2, threshold:2}
doc_render_preview {max_side:900}                  → check
doc_save {path:"out/photo.psd"} · doc_save {path:"out/photo.jpg", quality:88}
```

### Recipe: logo / product composite (tested)

```text
doc_open {path:"bg.jpg"}                           → index 0
doc_open {path:"logo.png"}                         → index 1
command_run select.all · command_run edit.copy     → copies the trimmed opaque bounds
doc_close {} · doc_select {index:0}                → the clipboard survives the close
command_run edit.paste {center:[800,450]}          → {layer, offset}; without center it lands at (0,0)
command_run layer.setProps {name:"Logo", opacity:1, blend:"Normal"}
command_run edit.transform {quad:[[600,250],[1000,250],[1000,650],[600,650]]}   → scale/position exactly
command_run layer.layerStyle.dropShadow {color:"#000000", distance:10, size:20, opacity:60}
doc_render_preview {} · doc_save {path:"out/comp.psd"} · doc_save {path:"out/comp.png"}
```

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

### More building blocks

- **Text with effects:** `layer.layerStyle.dropShadow | stroke | outerGlow | colorOverlay | gradientOverlay | bevelEmboss`.
- **Arrange:** `layer.translate {dx, dy}`, `layer.moveTo {target, position}`, `layer.arrange.bringToFront`,
  `layer.align.horizontalCenters {to: "canvas"}` (selected layers; select with `layer.select {layer, mode:"add"}`).
- **Canvas:** `image.canvasSize {width, height, relative, anchor, extensionColor}`, `image.trim`,
  `image.imageRotation.90cw`, `image.mode.grayscale` / `cmyk`, `image.mode.bits16`.
- **Retouch:** `paint.spotHealing {points, size}`, `paint.cloneStamp {points, source}`, `edit.contentAwareFill`.
- **Paint:** `paint.stroke {points:[[x,y,pressure],…], size, color, hardness}`, `paint.gradient {from, to, colors}`.
- **Recorded actions:** `actions.record` → edits → `actions.stop`, then `actions.get` gives steps for `batch`.

## Formats

- **Read and write:** `.pcraft` (native, lossless), PSD, PSB, layered or flat TIFF, PNG, JPEG, WebP, GIF, BMP,
  TGA, ICO, QOI, PNM, OpenEXR, Radiance HDR, AVIF; HEIC read-only (optional build feature).
- `doc_save` picks the format from the extension (`format` overrides). `quality` 1..100 for JPEG / WebP (WebP
  without `quality` is lossless). `tiffLayers: true` keeps layers in TIFF.
- PSD / `.pcraft` keep layers, masks, adjustment layers, smart filters and type (tested round trip). Flat formats
  return the warning `N layer(s) flattened; layers, masks and blend modes are not kept`; JPEG adds `lossy
  compression` and composites transparency over white; WebP drops the DPI.

## CLI (no MCP needed; absolute paths work)

```bash
photocraft-cli info file.psd --compact                       # JSON: size, mode, depth, layer tree
photocraft-cli convert in.psd out.jpg --quality 85           # any supported format to any other
photocraft-cli run in.jpg --cmd image.adjustments.curves --params '{"points":[[0,0],[70,50],[190,215],[255,255]]}' \
               --cmd image.imageSize --params '{"width":800,"height":500}' --out out.jpg --quality 90
photocraft-cli run --new '{"width":600,"height":400,"background":"#223344"}' \
               --cmd type.create --params '{"x":300,"y":220,"text":"Hi","size":120,"color":"#ffcc00","align":"center"}' --out t.png
photocraft-cli batch --actions steps.json --in ./photos --out ./graded --format jpg --quality 80
photocraft-cli commands --filter blur                        # the command catalog (--json for all fields)
```

`steps.json` is `[["image.adjustments.hueSaturation", {"saturation": -30}], {"command": "image.imageSize", "params": {…}}]`.
`run` also allows the path-taking commands MCP refuses, e.g. `file.placeEmbedded {path, scale}` (places an image as a
smart object) and `file.export.layersToFiles {dir}` (tested).

## Pitfalls

- **Paths over MCP are relative, forward-slash, beneath the roots.** An absolute path fails with `automation path
  rejected: drive, device and stream prefixes are not allowed`. The output folder must exist: otherwise
  `I/O: automation write `…` failed (NotFound)`.
- **Path-taking commands are refused over MCP** (`file.openAs`, `file.saveACopy`, `file.placeEmbedded`, `file.export.*`…):
  `automation command `file.placeEmbedded` uses ambient filesystem paths and is disabled`. Use `doc_open`, `doc_save`,
  copy/paste between documents, or the CLI `run`.
- **`doc_save` with no `path` only writes back PSD / PSB / .pcraft.** On a JPEG: `pass `path`: without one, only a PSD,
  PSB or .pcraft file is written back…`.
- **Unknown params are ignored silently** (a typo like `widht` still runs the command as a no-op and adds a history
  step). Compare the reply with what you asked for.
- **Filters and `image.adjustments.*` need a pixel layer.** A new adjustment or type layer becomes active, so the next
  filter fails with `filters need a pixel layer (active layer is a Adjustment layer)`. `layer.select` first.
  The same makes `batch` fail on PSDs whose top layer is an adjustment.
- **Selections don't auto-mask adjustment layers**: use `layer.layerMask.revealSelection` (verify `hasMask: true`).
- **Bounds formats differ:** `doc_inspect` gives `[x, y, w, h]`; `type.create` and `edit.transform` give `[x0, y0, x1, y1]`.
- **`wait: false` locks the document** until the job ends: other commands fail with `“Gaussian Blur” is still
  running on this document`. Keep the default (wait) unless you poll `jobs_list`.
- **Missing fonts substitute silently**; check `type.resolveMissingFonts`.
- **Bridge mode:** `doc_render_preview` returns a screenshot of the app window, not the image. Export a PNG to check pixels.

## Verification

- `doc_render_preview`, then look at the image before you report the work as done.
- `doc_inspect`: the expected layers, `hasMask`, adjustment values, text, and canvas `width`/`height`.
- Every `doc_save` reply names the `path`; read its `warnings`. `photocraft-cli info <file>` confirms a saved file
  re-opens with its layers.

## References

- `references/commands.md`: all 817 engine commands with params, grouped by area (`layer.newAdjustmentLayer`,
  `filter.blur`, `select`, `type`…). Grep it rather than reading it whole, e.g. `grep -n "unsharp" references/commands.md`.
- Upstream docs: https://github.com/storytold/photocraft/tree/main/docs (`control-protocol.md`: control methods,
  automation roots, background jobs, headless `serve`).
