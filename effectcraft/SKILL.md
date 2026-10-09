---
name: effectcraft
description: "Motion graphics and compositing with EffectCraft (After Effects-style): animated titles, title cards, lower thirds, logo reveals, kinetic type, intros, overlays with alpha, keyframes, easing, expressions, effects (glow, blur, keying, tracking), and renders to MP4 / GIF / WebM / ProRes / PNG sequence / Lottie."
version: 0.1.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Creative, Video, Motion Graphics, Animation, Compositing, VFX, Titles, Lottie, MCP]
    related_skills: [storytold, storytold-install, filmcraft, vectorcraft, photocraft, soundcraft]
---

# EffectCraft

EffectCraft is a free, open-source clean-room take on Adobe After Effects (storytold Crafting Apps). An
agent drives it through an MCP server (`effectcraft-cli mcp`), one-shot CLI commands, or After Effects-style
JavaScript (`run_script` / `effectcraft-cli script`). Projects are `.ecproj` files; everything stays editable.

## When to Use

Use it for **things that move, built from layers over time**:

- animated titles, title cards, lower thirds, end cards, logo reveals, kinetic typography, intros/outros
- overlays and graphics with transparency (WebM VP9 alpha, ProRes 4444, PNG sequence) for an editor to drop in
- compositing and VFX on footage: keying, masks, track mattes, motion/camera tracking, stabilizing, roto
- short animated GIFs and Lottie animations for the web

Pick a different Crafting App when:

| The job is… | Use |
|---|---|
| Cutting clips together, a sequence/timeline edit, trims, transitions, captions, a whole video | `filmcraft` (render EffectCraft graphics, then cut them in there) |
| A static logo, icon or vector illustration | `vectorcraft` (import its SVG/PDF here to animate it) |
| Retouching a still photo | `photocraft` |
| Audio editing, mixing, voice-over cleanup | `soundcraft` |
| Slides | `deckcraft` |

## Setup

1. If tools named `mcp_effectcraft_*` are available, use them. This is the preferred way.
2. Otherwise check for the CLI with `effectcraft-cli --version`. If it's missing, load the `storytold-install`
   skill and run its `setup effectcraft`. Then ask the user to start a new session or run `/reload-mcp`.
3. Until the MCP tools appear, use the CLI one-shots and `effectcraft-cli script` (see **CLI**).

`effectcraft-cli mcp` is **headless**: an in-process engine that starts with an **empty project** and renders
on the CPU (`mcp --gpu` for the GPU). For the user to watch live, they run `effectcraft --control 9877` and the
server is started as `effectcraft-cli mcp --bridge 9877`; that adds `screenshot` and the `ui_*` tools.

## Mental Model

- **Project → compositions → layers.** A comp has a size, frame rate, duration and background colour. Layers stack
  top to bottom (`#1` is the top). Layer kinds: text, shape, solid, null, adjustment, camera, light, footage, precomp.
- **Times are seconds.** Keyframe times are layer time (= comp time unless the layer is offset/stretched).
- **Coordinates are comp pixels, y down**, origin top-left. A new layer's position defaults to the comp centre.
- **Every layer has a property tree.** Each node has a `path`: `transform/position`, `transform/scale` (%),
  `transform/rotation` (deg), `transform/opacity` (0–100), `transform/anchor`, `effects/#1/blurriness`,
  `contents/trim/end`, `masks/mask/feather`, `text/sourceText`. `get_layer {layer, flat: true}` lists them all.
- **Layers are referenced** by id (returned on creation), `"#n"`, or **name**. Name layers when you create them
  (`name` param) and keep using the names. A name that matches nothing is an error, never a silent no-op.
- **Every edit is an engine command** (665 of them) and undoable. The dedicated tools cover the common ones;
  everything else is `execute_command {command, params}`. Unknown param keys are rejected with the accepted list.
- **Rendering is a render queue**: `renderQueue.add` then `renderQueue.render`. `render_frame` is for looking.

## Tools (Hermes names them `mcp_effectcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `get_state` / `get_project` / `get_comp {comp?}` | Orient: active comp, items, layers (id, index, name, in/out) |
| `get_layer {layer, flat?, depth?, time?}` | A layer's property tree with every `path` |
| `get_property` / `set_property` | Read; set a static value, a key (`time`), or an `expression` (`""` removes it) |
| `add_keyframe {layer, path, keys:[{time,value}], interpolation?}` | Animate. `linear`, `bezier`, `hold`, `easyEase`, `easyEaseIn`, `easyEaseOut` |
| `add_effect {layer, effect, values?}` | Apply an effect by id or AE name and set params in one undo step; returns param paths |
| `list_effects {filter?}` / `list_fonts {query?}` | Effect ids + param ids; usable font families and styles |
| `execute_command` / `list_commands {filter?}` / `describe_command` | Everything else (comps, layers, masks, render queue, export) |
| `batch {steps, label?}` | Several commands as ONE undo step; `"$1.layer"` = step 1's result |
| `run_script {code}` | After Effects-style JavaScript (`app.project`, `comp.layers.addText`, `setValueAtTime`…) |
| `render_frame {time?, max_side?, path?, transparent?}` | PNG of one frame. **Look at it** |
| `open_project {path\|new\|demo}` / `save_project {path?}` | `.ecproj` files |
| `undo` / `redo` / `history {goto?}` | Edit history (branching) |
| `script_ui` | Drive ScriptUI dialogs a script opened |
| *(bridge only)* `screenshot`, `ui_inspect`, `ui_elements`, `ui_click`, `ui_drag`, `ui_key`, `ui_type`, `ui_set`, `control` | The live window |

## Layers, text and shapes

- **Comp:** `comp.new {name, width, height, frameRate, duration, background: "#rrggbb"}`. Always pass all of them:
  the defaults are 1920×1080, **29.97 fps, 10.01 s**, black.
- **Text:** `layer.newText {text, name, font, style, size, fill, position: [x, y], justify}`. `position` is the
  **baseline** point and text is **centred on it by default**; pass `justify: "left"` for left-aligned lines
  (lower thirds). Restyle later with `layer.setText {layer, font?, size?, fill?, tracking?, justify?, range?}`.
  Pick fonts from `list_fonts`; the default family is Inter.
- **Shapes:** `layer.newShape {kind: rect|rounded|ellipse|star|polygon, name, size: [w, h], fill, stroke,
  strokeWidth, position}`. The shape is centred on the layer origin. No fill is `fill: false` (not `"none"`).
  Add operators with `layer.addShapeItem {layer, kind: trim|repeater|round|wiggle|gfill|…}` → `{path}`
  (e.g. `contents/trim`, then animate `contents/trim/end` 0→100 for a draw-on).
- **Solids / nulls / adjustment:** `layer.newSolid {name, color}`, `layer.newNull`, `layer.newAdjustment`.
- **Footage:** `file.import {paths: [abs]}` → `{items}`; then `layer.addItem {item, time?, index?}` into the active
  comp, or `project.select {items}` + `file.newCompFromSelection {}` for a comp matching the clip.
- **Grow from an edge:** scale grows around `transform/anchor`. For a bar that wipes in from the left, set
  `anchor` to `[-w/2, 0]` and `position` to the left edge, then key `transform/scale` from `[0,100]` to `[100,100]`.
- **Timing:** `layer.timing {layers: [...], in?: s, out?: s, start?: s}` trims or shifts layers.
- **Masks / mattes / parenting / blend:** `layer.addMask {layer, shape: rect|ellipse, rect: [x,y,w,h]}` (layer
  space), `layer.trackMatte {layers, op: alpha|luma|…}`, `layer.setParent {layers, parent}`, `layer.setBlendMode`.
- **Precompose:** `layer.precompose {layers, name}` → `{comp, layer}`.

## Procedure

1. **Plan** the comp size/fps/duration, palette, layer stack (background → shapes → type → overlays), and the beats
   (what moves when). Keep animations short: 0.4–0.8 s ins, a hold, then outs.
2. **Set up:** `comp.new` with every setting. Use `batch` to create the layers in one step.
3. **Animate** with `add_keyframe` (multiple keys + `interpolation: "easyEase"` in one call). Use expressions for
   loops/wiggles: `set_property {path, expression: "wiggle(2, 10)"}`; the reply's `evaluated` shows the result.
4. **Look.** `render_frame {time, max_side: 640}` at the start, mid-move and the hold. Check framing, overlap,
   contrast, cut-off text. Fix before rendering.
5. **Save** `save_project {path: "/abs/x.ecproj"}`.
6. **Render** via the render queue (below), then verify the file (see **Verification**).

### Recipe: title card (tested)

```text
execute_command comp.new {name:"Title", width:1280, height:720, frameRate:30, duration:3, background:"#101828"}
execute_command layer.newSolid {name:"BG", color:"#1b1046"}
execute_command layer.newShape {kind:"rect", name:"Bar", size:[600,12], fill:"#ff6a3d", position:[640,420]}
execute_command layer.newText  {text:"HELLO WORLD", name:"Title", size:110, fill:"#ffffff",
                                font:"Source Sans 3", style:"Bold", justify:"center", position:[640,360]}
add_keyframe {layer:"Title", path:"transform/opacity", keys:[{time:0,value:0},{time:1,value:100}], interpolation:"easyEase"}
add_keyframe {layer:"Title", path:"transform/scale",   keys:[{time:0,value:[80,80]},{time:1,value:[100,100]}], interpolation:"easyEaseOut"}
add_keyframe {layer:"Bar",   path:"transform/position",keys:[{time:0,value:[-400,420]},{time:1.2,value:[640,420]}], interpolation:"easyEase"}
add_effect   {layer:"Title", effect:"Drop Shadow", values:{distance:8, softness:12}}
render_frame {time:0.5, max_side:640} · render_frame {time:2}          → look
save_project {path:"/abs/title.ecproj"}
execute_command renderQueue.add {comp:"Title", format:"h264", output:"/abs/title.mp4"}
execute_command renderQueue.render {wait:true}                          → 1280×720, 90 frames, 3.0 s
```

### Recipe: lower third over footage (tested)

```text
execute_command file.import {paths:["/abs/clip.mp4"]}                 → {items:[1]}
execute_command project.select {items:[1]} · execute_command file.newCompFromSelection {}   → comp "clip"
batch {label:"Lower third", steps:[
  {command:"layer.newShape", params:{kind:"rect", name:"LT Bar", size:[520,110], fill:"#0b1e3f", position:[340,600]}},
  {command:"layer.newShape", params:{kind:"rect", name:"LT Accent", size:[10,110], fill:"#ffb800", position:[75,600]}},
  {command:"layer.newText",  params:{text:"Jane Doe", name:"LT Name", size:48, fill:"#ffffff", font:"Noto Sans", style:"Bold", justify:"left", position:[100,595]}},
  {command:"layer.newText",  params:{text:"Director of Photography", name:"LT Role", size:26, fill:"#c8d2e0", font:"Noto Sans", justify:"left", position:[100,635]}}]}
set_property {layer:"LT Bar", path:"transform/anchor",   value:[-260,0]}      # grow from the left edge
set_property {layer:"LT Bar", path:"transform/position", value:[80,600]}
add_keyframe {layer:"LT Bar",  path:"transform/scale",   keys:[{time:0,value:[0,100]},{time:0.6,value:[100,100]}], interpolation:"easyEase"}
add_keyframe {layer:"LT Name", path:"transform/opacity", keys:[{time:0.4,value:0},{time:0.9,value:100}], interpolation:"easyEase"}
add_keyframe {layer:"LT Role", path:"transform/opacity", keys:[{time:0.6,value:0},{time:1.1,value:100}]}
render_frame {time:1.5} → renderQueue.add {comp:"clip", format:"h264", output:"/abs/lt.mp4", timeSpan:"custom", start:0, end:2}
renderQueue.render {wait:true}                                             → H.264 + AAC (clip audio kept), 2.0 s
```

### Recipe: logo ring draw-on with glow, transparent overlay (tested)

```text
execute_command comp.new {name:"Logo", width:800, height:800, frameRate:24, duration:2, background:"#000000"}
execute_command layer.newShape {kind:"ellipse", name:"Ring", size:[400,400], fill:false, stroke:"#00e0ff", strokeWidth:24, position:[400,400]}
execute_command layer.addShapeItem {layer:"Ring", kind:"trim"}                → {path:"contents/trim"}
add_keyframe {layer:"Ring", path:"contents/trim/end", keys:[{time:0,value:0},{time:1.5,value:100}], interpolation:"easyEase"}
add_effect   {layer:"Ring", effect:"Glow", values:{radius:30, intensity:1.5}}
render_frame {time:1.9, transparent:true, path:"/abs/logo_alpha.png"}
renderQueue.add {comp:"Logo", format:"webm", channels:"rgba", output:"/abs/logo.webm"}            → VP9 with alpha
renderQueue.add {comp:"Logo", format:"prores", channels:"rgba", proresProfile:"4444", output:"/abs/logo.mov"}
renderQueue.render {wait:true}
```

### Recipe: scripted build (tested)

`run_script {code}` (or `effectcraft-cli script build.jsx --save-as /abs/out.ecproj`) takes After Effects ExtendScript:

```js
var c = app.project.items.addComp("Scripted", 640, 360, 1, 2, 30);   // name, w, h, pixelAspect, duration, fps
c.layers.addSolid([0.1,0.2,0.5], "BG", 640, 360, 1);
var t = c.layers.addText("Scripted!");
var p = t.property("ADBE Transform Group").property("ADBE Position");
p.setValueAtTime(0, [100,180]); p.setValueAtTime(1.5, [320,180]);
t.property("ADBE Transform Group").property("ADBE Opacity").expression = "linear(time,0,1,0,100)";
writeLn("layers=" + c.numLayers); c.name                       // → {ok, output:"layers=2", result:"Scripted"}
```

Script errors come back as `{ok:false, error:{message, line, column}}`, e.g. `layer index 99 is out of range 1..1`.

## Rendering and formats

- `renderQueue.add {comp, output: "/abs/file.ext", format?, timeSpan?: workArea|comp|custom, start?, end?,
  resolution?: full|half|third|quarter, channels?: rgb|rgba, proresProfile?, bitrate?, frameRate?}` then
  `renderQueue.render {wait: true}`. The format is inferred from the extension when omitted (`.gif`, `.mov` → ProRes,
  `.mp4` → H.264). Missing output folders are created.
- Formats: `h264`, `hevc`, `av1`, `prores`, `webm`, `gif`, image sequences `png|jpeg|tiff|exr`
  (`output: "/abs/seq/name_[####].png"`), audio `wav|aiff`. Alpha: `webm` or `prores` + `channels: "rgba"`, or PNG.
- The default span is the work area (= the whole comp). `end` is exclusive: `start:0, end:0.5` at 30 fps = 15 frames.
- **Lottie:** `file.exportLottie {comp, path: "x.json"|"x.lottie"}` → `{bytes, warnings}`; warnings list what Lottie can't show.
- **To an editor:** `file.exportTimeline {comp, path: "x.xml"|".fcpxml"|".otio"|".edl"}`; or just render a ProRes/WebM
  overlay for `filmcraft`. Import: footage (video/image/audio) and PSD/AI/PDF/EPS with `file.import`, Lottie with
  `file.importLottie`, FCP XML/FCPXML/OTIO/EDL/AAF with `file.importTimeline`.

## CLI (no MCP needed)

```bash
effectcraft-cli render --project p.ecproj --comp Title --out /abs/t.mp4 [--start 0 --end 1] [--format gif] [--resolution half]
effectcraft-cli render-frame p.ecproj --comp Title --time 1 --max-side 640 --out /abs/f.png
effectcraft-cli script build.jsx --save-as /abs/p.ecproj            # or: script --eval 'CODE' p.ecproj
effectcraft-cli exec comp.new --params '{"name":"Main","width":1280,"height":720}' --empty --save-as /abs/m.ecproj
effectcraft-cli run p.ecproj layer.newSolid '{"color":"#3366ff"}' time.set '{"time":1}' --save
effectcraft-cli get Title Title transform/opacity --time 0.5 --project p.ecproj --json
effectcraft-cli set Title '#1' transform/opacity 40 --project p.ecproj --save
effectcraft-cli commands --filter keys                               # the command catalog
```

Without `--project`/a positional `.ecproj`/`--empty`, the CLI opens the **demo project**. Edits are thrown away
unless you pass `--save` or `--save-as`.

## Pitfalls

- **Paths:** use absolute paths everywhere (`save_project`, `file.import`, `output`). The server's cwd is not yours.
- **Defaults bite:** `comp.new` without settings gives 1920×1080 at 29.97 fps for 10.01 s. Pass them all.
- **Text is centred on `position` by default** and `position` is the baseline. Left-aligned text needs `justify: "left"`.
- **The anchor path is `transform/anchor`**, not `anchorPoint` (`no property \`transform/anchorPoint\``).
- **No fill is `fill: false`:** `"none"` fails with `` `fill`: a colour [r, g, b] or #hex, or false for none ``.
- **Effect param ids are not the UI names.** Gaussian Blur's amount is `blurriness`; `values:{blur:5}` fails with
  `no property \`effects/#2/blur\``. Get ids from `list_effects {filter}` or grep `references/effects.md`.
  A failed `add_effect` rolls back completely ("the batch was rolled back (nothing changed)").
- **Nothing works before a comp exists:** `command \`layer.newText\` is not available right now: no composition is open`.
- **The render queue is saved in the project.** Re-opened projects keep their done items; `renderQueue.render` only
  renders `Queued` ones. Its replies are very long. Check the file instead of reading them.
- `layer.setText` and `layer.timing` return `null` on success. That's normal.
- `easyEaseOut` leaves the incoming side linear; use `easyEase` for both ends.

## Verification

- `render_frame` at key times and look at the images before saying it's done.
- `get_comp` shows the expected layers and in/out points; `get_property` shows the keys.
- After a render: `ffprobe -v error -show_entries format=duration:stream=codec_name,width,height,pix_fmt out.mp4`,
  and pull a frame (`ffmpeg -ss 1 -i out.mp4 -frames:v 1 f.png`) to look at. Alpha WebM shows `alpha_mode=1`,
  ProRes 4444 shows `yuva444p12le`.

## References

- `references/commands.md`: all 665 commands with params, grouped by prefix (`layer`, `keys`, `renderQueue`,
  `track`, `mask`, `text`…). Grep it rather than reading it whole.
- `references/effects.md`: all 306 effects by category with param ids and defaults. Grep by name.
- Upstream docs: https://github.com/storytold/effectcraft/tree/main/docs (`agents.md`: tracking, roto, warp
  stabilizer, Essential Graphics, timeline interchange; `control-protocol.md`).
