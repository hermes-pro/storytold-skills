---
name: lightcraft
description: "Photo development and cataloguing with LightCraft (Lightroom-style): import and cull a shoot, rate / flag / keyword, develop RAW (DNG, NEF, ARW, CR2…) and JPEG photos (exposure, white balance, tone curve, HSL, B&W, crop, masks), apply presets, sync edits across a batch, HDR / panorama merge, batch export JPEG / PNG / TIFF / WebP / AVIF / DNG."
version: 0.1.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Creative, Photo, RAW, Photography, Color Grading, Catalog, Batch, Export, MCP]
    related_skills: [storytold, storytold-install, photocraft, vectorcraft, designcraft, filmcraft]
---

# LightCraft

LightCraft is a free, open-source clean-room take on Adobe Lightroom (storytold Crafting Apps): a photo
library plus a non-destructive raw developer. An agent drives it through an MCP server
(`lightcraft-cli mcp`) or one-shot CLI commands. Edits are settings stored per photo, never baked into the
original file. Pixels only change in an export.

## When to Use

Use it for **photographs as photographs**:

- developing RAW or JPEG photos: exposure, white balance, contrast, shadows/highlights, colour, B&W, crop, straighten
- the same look on many photos: presets, copy/paste or sync settings, batch export at a size and format
- culling and organising a shoot: ratings, pick/reject flags, colour labels, keywords, albums, finding duplicates
- local fixes: graduated / radial / sky / subject / luminance masks, dust spots, red eye
- HDR merges of brackets and panorama stitching (to DNG)

Pick a different Crafting App when:

| The job is… | Use |
|---|---|
| Pixel-level retouching, layers, compositing several images, text on a photo | `photocraft` |
| Logos, icons, vector art, posters | `vectorcraft` |
| Photo books, brochures, multi-page layouts | `designcraft` |
| Video or slideshows with motion | `filmcraft` |

A typical hand-off: develop and export in LightCraft (16-bit TIFF or PNG), then composite in PhotoCraft.

## Setup

1. If tools named `mcp_lightcraft_*` are available, use them. This is the preferred way.
2. Otherwise check for the CLI with `lightcraft-cli --version`. If it's missing, load the
   `storytold-install` skill and run its `setup lightcraft`. Then ask the user to start a new session
   or run `/reload-mcp` so the MCP tools appear.
3. Until the MCP tools appear, use the CLI one-shots (see **CLI** below).

`storytold-install` registers the server as `lightcraft-cli mcp --library <storytold data>/lightcraft-library`.
The data folder is `%LOCALAPPDATA%\storytold` on Windows, or `STORYTOLD_LIGHTCRAFT_LIBRARY` when that's set.
It's headless (a full engine with a CPU renderer) and **persistent**, so imports, ratings and edits survive
between sessions. Bare `lightcraft-cli mcp` is **in-memory**: the library disappears when the server exits.
Your exported files stay, but the ratings and edits don't. Other modes:

- `lightcraft-cli mcp --library DIR` opens or creates a persistent library in another folder, e.g. one per project.
- `lightcraft-cli mcp --connect 127.0.0.1:7980` drives a desktop app the user started with
  `lightcraft --control 7980`, so they can watch. Only this mode has the UI tools (`screenshot`, `inspect_ui`, `set_ui`,
  `click`, `press_key`, `type_text`, `pointer_gesture`, `list_widgets`). Unlike VectorCraft it does **not**
  connect on its own.

## Mental Model

- **Library → photos with integer ids.** `import` adds files *in place* (it doesn't copy them unless `mode: "copy"`)
  and returns the new ids. Ids start at 1 for each new in-memory session.
- **Active photo vs selection.** Develop tools edit the *active* photo. Batch commands (`photo.rate`, presets, export,
  sync) take `ids` or fall back to the selection. `select_photos {ids, active}` sets both.
- **Develop settings** are one JSON per photo (`get_develop`). Sliders have ids like `light.exposure`, `wb.temp`,
  `mixer.blue.sat`: 114 of them, in `references/controls.md`. The JSON uses snake_case (`effects.dehaze`,
  `vignette.amount`, `detail.sharpen_amount`).
- **Positions are normalized image coordinates**, 0..1 with the origin at the top-left: crop rects, mask points,
  white-balance picks, spots.
- **Every action is a command** (240). Each one is also its own tool: `photo.rate` → `mcp_lightcraft_cmd_photo_rate`,
  or use `run_command {command, params}`. Grep `references/commands.md`, or `list_commands {filter}`.
- Every edit is undoable (`cmd_edit_undo` / `cmd_edit_redo`). `cmd_history_list` shows the steps of the active photo.

## Tools (Hermes names them `mcp_lightcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `import {paths, mode?, destination?, organize?, rename?, album?}` | Files or folders (recursive). Returns `imported` ids plus `duplicates` and `failed`. The first new photo becomes active |
| `query_photos {filter?, sort?, limit?, offset?}` | List photos: id, fileName, rating, flag, label, edited, kind (raw/image), size, keywords |
| `select_photos {ids, active?, mode?}` | Selection and active photo |
| `list_controls {section?}` | Sliders with min, max, default and **current value** for the active photo |
| `set_develop {id?, values?, settings?}` | `values: {"light.exposure": 0.7}` sets sliders. `settings` deep-merges develop JSON |
| `get_develop {id?}` | The full develop JSON |
| `crop {id?, rect?, angle?, reset?}` | `rect: [x0,y0,x1,y1]` normalized, `angle` in degrees (straighten) |
| `apply_preset {preset, ids?, amount?}` | Preset ids from `cmd_presets_list` (`lc.golden-hour`…). `amount` 0..200 % |
| `render_photo {id?, size?, format?, path?}` | **Look at the result.** Long edge `size` (default 1024, max 4096) |
| `export {path \| dir, id? \| ids?, …}` | Write files (see **Export**) |
| `list_commands` / `run_command` / `cmd_*` | Everything else |

Resources: `lightcraft://library` (selection, filter, undo label), `lightcraft://photos`,
`lightcraft://photo/active`, `lightcraft://develop/active`, `lightcraft://controls`. There are no prompts.

## Develop

- **Auto first, then refine:** `cmd_develop_auto` sets exposure, contrast, highlights, shadows, whites, blacks,
  vibrance and saturation, **overwriting** those sliders. Run it before your own tweaks, not after.
- **Light:** `light.exposure` (−5..5 EV), `light.contrast|highlights|shadows|whites|blacks` (−100..100).
- **White balance:** `cmd_develop_wb {mode: asShot|auto|daylight|cloudy|shade|tungsten|fluorescent|flash|custom, temp?, tint?}`,
  or `cmd_develop_wbPick {x, y}` on something neutral. `wb.temp` is in Kelvin, and **lower = cooler/bluer** result
  (4500 on a JPEG turns it blue). A JPEG starts at 6500 / 0.
- **Colour:** `color.vibrance`, `color.saturation`; HSL per colour band: `mixer.<red|orange|yellow|green|aqua|blue|purple|magenta>.<hue|sat|lum>`.
- **Tone curve:** parametric `curve.highlights|lights|darks|shadows`, or points:
  `cmd_develop_curve {channel: master|red|green|blue, points: [[0,0.05],[0.25,0.2],[0.75,0.82],[1,1]]}`.
  `cmd_curve_presets` / `cmd_curve_applyPreset` are named curves.
- **B&W:** `cmd_develop_treatment {bw: true}` (no `bw` toggles), then the `bw.<colour>` mix or `cmd_develop_autoBwMix`.
- **Look:** `grading.<shadows|midtones|highlights|global>.<hue|sat|lum>`, `effects.texture|clarity|dehaze`,
  `vignette.amount` (negative darkens the corners), `grain.amount`, `detail.sharpenAmount`, `detail.nrLuminance`.
- **Profiles** (the base rendering, plus LUTs): `cmd_profiles_list`, `cmd_develop_profile {id: "lc.vivid", amount}`.
- **Crop and geometry:** `crop {rect, angle}`. A positive `angle` turns the picture clockwise. `cmd_crop_aspect {aspect: "16x9"|"1x1"|…}`,
  `cmd_crop_autoStraighten`, `cmd_geometry_upright {mode: auto|level|vertical|full}`.
- **Reset:** `cmd_develop_reset {ids?}`, `cmd_develop_resetSection {section}`, `cmd_develop_resetControl {control}`.

## Masks and spot fixes

`cmd_mask_add {kind, …}` creates a mask and makes it active. `cmd_mask_adjust {values}` then sets its local
sliders: `exposure, contrast, highlights, shadows, whites, blacks, temp, tint, texture, clarity, dehaze, hue,
saturation, sharpness, noise`.

| kind | Params (normalized coordinates) |
|---|---|
| `linear` | `start: [x,y]` (full effect) → `end: [x,y]` (none). Sky gradient: `start [0.5,0]`, `end [0.5,0.6]` |
| `radial` | `center: [x,y]`, `rx`, `ry` (fractions of the photo), `angle`, `feather` 0..100 (default 50). Effect is **inside** |
| `luminanceRange` | `lo`, `hi` 0..1 (default 0.6..1 = brights) |
| `colorRange` | then `cmd_mask_sampleColor {x, y}` |
| `sky`, `subject`, `background` | No params. These work without the AI model, but they're approximate, so render and check |
| `brush` | `cmd_mask_brushStroke {points, size}` |
| `object`, `prompt` | Need the 3.4 GB SAM 3 model (`cmd_segment_model_status`). Ask the user before `cmd_segment_model_download` |

Combine with `cmd_mask_addComponent {op: add|subtract|intersect, kind, …}`. Remove with `cmd_mask_invert`,
`cmd_mask_delete` or `cmd_mask_deleteAll`. Retouching: `cmd_spot_findDust`, `cmd_spot_add {mode: heal|clone, points, size}`,
`cmd_redeye_add`.

## Library, culling, batch

- **Rate, flag, label:** `cmd_photo_rate {rating, ids}`, `cmd_photo_flag {flag: pick|reject|none, ids}`, `cmd_photo_label {label: red|…, ids}`.
- **Metadata:** `cmd_photo_setMeta {ids, title, caption, keywords: [..], creator, copyright}`.
- **Filter** (`query_photos` / `cmd_catalog_query` / `cmd_library_filter`): `{rating: 3, ratingOp: "atLeast"|"exactly"|"atMost"}`,
  `{flag: "pick"}`, `{label: "red"}`, `{keyword: "sky"}`, `{kind: "raw"}`, `{edited: true}`, `{album: id}`, `{text}`.
  `cmd_library_selectBy {rating|flag|label}` selects directly.
- **Albums:** `cmd_album_create {name, addSelected: true}` → `{id}`, `cmd_album_addPhotos {id, ids}`, `cmd_albums_list`.
- **Variants of one photo:** `cmd_photo_virtualCopy {ids}` (a new id with its own settings) or
  `cmd_version_create {name}` / `cmd_version_restore {index}` (named snapshots inside one photo).
- **Same look on many photos:** `apply_preset {preset, ids}`; or, from the active photo, `cmd_develop_copy {groups?}` and
  `cmd_develop_paste {ids}`; or `select_photos {ids, active: source}` followed by `cmd_develop_sync`.
  `cmd_develop_quickAdjust {control, delta, ids}` nudges each photo from its own value.
- **Your own presets:** `cmd_preset_create {name, group}` (from the active photo) → `{id: "user.…"}`. Import Lightroom
  `.xmp`/`.lrtemplate` presets with `cmd_preset_import {paths}`.
- **Assisted culling:** `cmd_photo_analyze {rejectBelow?, pickBest?}` scores focus and clipping. `cmd_library_findSimilar`, `cmd_stack_auto`.

## Procedure

1. **Import** the files or folder. Keep the returned ids; `query_photos` re-lists them.
2. **Cull** if needed: rate, flag, filter, and settle on the ids to work on.
3. **Develop one hero photo:** `select_photos`, `cmd_develop_auto`, then `set_develop` corrections, WB, crop and masks.
4. **Look:** `render_photo {size: 800}` after each major step. Check the exposure, colour cast, horizon and crop.
5. **Spread the look:** a preset, copy/paste or sync to the rest. Render a couple of them to check.
6. **Export** and read each reply's `files[].path / width / height / bytes`.
7. If the work must outlive the session, use `--library DIR`, or export `format: "original"` (the original plus an XMP sidecar).

### Recipe: develop one photo (tested)

```text
import        {paths: ["/abs/shoot/IMG_0042.dng"]}                 → {imported: [1]}
cmd_develop_auto {}
set_develop   {values: {"light.highlights": -60, "light.shadows": 50, "color.vibrance": 20}}
cmd_develop_wb {mode: "custom", temp: 5200, tint: 5}
crop          {rect: [0.05, 0.08, 0.95, 0.92], angle: 1.5}
cmd_mask_add  {kind: "linear", start: [0.5, 0], end: [0.5, 0.6]}       → darken the sky
cmd_mask_adjust {values: {exposure: -1.0, saturation: 20}}
render_photo  {size: 800}                                             → look
export        {path: "/abs/out/IMG_0042.jpg", longEdge: 2048, quality: 90}
```

### Recipe: cull and batch-export a shoot (tested)

```text
import {paths: ["/abs/shoot"]}
cmd_photo_rate {rating: 4, ids: [1, 2]}  ·  cmd_photo_flag {flag: "pick", ids: [2]}  ·  cmd_photo_reject {ids: [4]}
query_photos {filter: {rating: 3, ratingOp: "atLeast"}}               → ids [2, 1]
apply_preset {preset: "lc.teal-orange", ids: [1, 2], amount: 80}
export {ids: [1, 2], dir: "/abs/out", naming: "{name}-{seq:2}", longEdge: 1600, quality: 85}
                                                                      → a_testsrc-01.jpg, b_gradient-02.jpg
```

### Recipe: B&W with HSL-driven tones, plus a colour variant (tested)

```text
select_photos {ids: [1]}
set_develop {values: {"mixer.blue.hue": -60, "mixer.green.sat": -100}}   → colour version
cmd_photo_virtualCopy {ids: [1]}                         → {ids: [2]}: inherits 1's settings, and is now active
cmd_develop_treatment {bw: true}                                       → the copy turns B&W, 1 stays colour
cmd_develop_curve {channel: "master", points: [[0,0.1],[0.25,0.18],[0.75,0.85],[1,0.95]]}
```

### Recipe: HDR merge of brackets (tested)

```text
import {paths: ["/abs/brackets"]}                                      → [1, 2, 3]
cmd_merge_hdr {ids: [1,2,3], preview: true, previewPath: "/abs/prev.png"}   → check alignment, nothing written
cmd_merge_hdr {ids: [1,2,3], deghost: "low"}    → writes bracket-0-HDR.dng next to the sources, imports it as id 4 (active)
```

Panoramas: `cmd_merge_panorama {ids, projection: auto|cylindrical|spherical|perspective, autoCrop: true}`.

## Export

- `path` (one photo, format from the extension) or `dir` + `naming` (batch; the folder is created). Tokens:
  `{name} {seq} {seq:N} {date:%Y%m%d} {camera} {rating} {title}`.
- Formats: `.jpg .png .tif .webp .avif`, plus `format: "dng"` (raw with edits embedded) and `format: "original"`
  (the file copied, plus an `.xmp` sidecar Lightroom can read).
- Size: nothing = **3000 px long edge**, `longEdge: 0` = full size, `longEdge|shortEdge|width+height|megapixels|percent`.
  `dontEnlarge` defaults to true, so a 1800 px photo stays 1800 px.
- Options: `quality` 1..100, `limitKb` (JPEG fits a file size), `colorSpace: srgb|displayP3|adobeRgb|proPhoto|rec2020`,
  `bitDepth` (PNG 8/16, TIFF 8/16/32), `metadata: all|copyright|none`, `removeLocation`, `sharpen: screen|matte|glossy`, `ppi`.
- **Read:** JPEG, PNG, TIFF, WebP and raws: DNG, CR2, NEF, ARW, RAF, RW2, PEF and uncompressed ORF are fully decoded.
  **CR3 and compressed Fuji/Olympus raws open as embedded previews only** (`previewOnly` in `query_photos`), and non-DNG
  raws have muted colour. XMP sidecars are read on import.

## CLI (no MCP needed)

```bash
lightcraft-cli render in.dng -o out.jpg --set light.exposure=0.3 --set light.shadows=40 --preset lc.golden-hour --size 1200
lightcraft-cli run --import /abs/a.jpg develop.auto develop.set control=light.exposure value=0.7 \
                   app.export path=/abs/a-out.jpg longEdge=800          # one JSON line per command
lightcraft-cli run --library /abs/lib --import /abs/shoot photo.rate rating=5 'ids=[1,2]'   # persists
lightcraft-cli run --library /abs/lib catalog.query 'filter={"rating":5}'
lightcraft-cli merge hdr|panorama [--preview OUT.png] FILES…        # writes <first>-HDR.dng / -Pano.dng
lightcraft-cli commands --json  ·  lightcraft-cli controls --json   # the catalogs
```

`run` exits non-zero when a command fails (`--keep-going` continues). Words without `=` start the next command.

## Pitfalls

- **`query_photos {filter: {minRating: 3}}` (the example in its own description) is silently ignored** and returns
  every photo. Use `{rating: 3, ratingOp: "atLeast"}`. Unknown filter keys never raise an error, so check `total`.
- **`set_develop` / `crop` with `id` replace the selection with just that photo.** `render_photo` and `get_develop` with
  `id` don't change the active photo. Re-`select_photos` before batch commands.
- **`cmd_photo_virtualCopy` makes the copy active**, so the next edit lands on the copy, not the original.
- **`cmd_develop_auto` overwrites** the light sliders and vibrance/saturation you set before it.
- **Values clamp silently:** `light.exposure: 9` becomes 5. An unknown id errors: `invalid parameters for
  `develop.set`: unknown control `light.bogus``.
- **`set_develop {settings}` answers `{"controls": [], "ok": true}`**, even when it worked. Its keys are snake_case
  JSON. Confirm with `get_develop`.
- **`cmd_develop_copy` leaves out crop, masks and spot removal by default.** A crop-only copy pastes nothing. Pass `groups`.
- **`cmd_develop_sync` copies to the *selected* photos.** It returns `{changed: 0}` when only the active one is selected.
- **In-memory by default:** close the server and the library is gone. A `--library` folder is locked while the desktop app has it
  open ("This library is already open in LightCraft"), so use `--connect` then.
- Re-importing a file that's already in the library skips it (`duplicates: [{existing, reason: "path"}]`). Use that id.
- `kind: "prompt"`/`"object"` masks without the model fail with `no folder is set for the SAM 3 model`.
- A merge writes its DNG **next to the source files**, so copy them first if that folder must stay untouched.
- Raws get default sharpening (40) and colour noise reduction (25); JPEGs get none.
- Paths: use absolute paths. Relative ones resolve against the server's working directory, not yours.
- Bad ids name the problem: `unknown command `photo.nope``, `unknown preset `nope``.

## Verification

- `render_photo` and look at the image before you report the work as done. Compare it with a render taken before the edits.
- `list_controls {section}` or `get_develop` shows the values actually stored (after clamping and auto).
- Each `export` reply lists `files` with `path`, `width`, `height`, `bytes > 0`. Count them against the ids you asked for.
- `query_photos {filter: {edited: true}}` lists the photos that really got edits.

## References

- `references/commands.md`: all 240 commands with params, grouped by area. Grep it (e.g. `grep -n "mask\." …`) rather than reading it whole.
- `references/controls.md`: all 114 develop slider ids with ranges and defaults, by section.
- Upstream docs: https://github.com/storytold/lightcraft/tree/main/docs (`mcp.md`, `control-protocol.md`, `ai-masks.md`, `merge.md`, `xmp-interop.md`).
