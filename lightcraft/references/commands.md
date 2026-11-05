# LightCraft command catalog

Generated from `lightcraft-cli commands --json` (LightCraft 0.18.1, 383 commands, headless). Run any of them with
`command_run {id, params}` (or the older helper `run_command {command, params}`), several in order with
`command_batch {steps: [{id, params}]}`, or call the per-command MCP tool `cmd_<id with . replaced by _>`
(`photo.rate` → `mcp_lightcraft_cmd_photo_rate`). `?` = optional, `a|b` = choices, `→ {...}` = what it returns.
Connect mode (`--connect`) adds the app's UI commands (`view.*`, `ui.*`), which are not listed here.

## activity

- `activity.cancel` Cancel Background Task: {id} | {all: true} → {cancelled: n} — ask a task (or every cancellable task) to stop; it stops at its next file or photo (a preview build also stops between a photo's own previews). An unknown id (it may have just finished) or a task that can't be cancelled is an error
- `activity.list` Background Tasks: {} → {tasks: [{id, kind, label, done, total, unit: count|bytes|percent, detail, cancellable, cancelling, ageMs}]} — the long-running tasks in flight (imports, exports, preview builds, downloads, the face scan…), oldest first; total 0 = not known yet

## album

- `album.addPhotos` Add to Album (Photo): {id: albumId, ids?: [photoIds]} (default: selection) → {added, skipped}; Local photos are skipped (albums hold library photos), only Local ones is an error; ids the library doesn't have are dropped; nothing new to add changes nothing (no undo step)
- `album.clearQuick` Clear Quick Collection: {}
- `album.create` New Album (File): {name, parent?: folderId, folder?: bool, addSelected?: bool} → {id, skipped} (skipped: Local photos of the selection, which albums can't hold)
- `album.createSmart` New Smart Album…: {name, rules?: partial Filter (rating, ratingOp, flag, flags, label, labels, kind, edited, keyword, camera, lens, dateFrom, dateTo, date, text, album, ruleSet: {match: all|any|none, rules: [{field, op, value} | {group: ruleSet}]} — see album.ruleFields), parent?: folderId} — without `rules`, saves the current view (source + filter)
- `album.delete` Delete Album: {id} — deletes the album or folder and its descendants, keeping photos in the library; one undo step
- `album.move` Move Album: {id, parent?: folderId|null}
- `album.removePhotos` Remove from Album (Photo): {id?: albumId (default: the album on screen), ids?} — takes the photos out of the album only: they stay in the library and in their folders (issue #1805; photo.delete removes them from the library) → {removed, album: name}
- `album.rename` Rename Album: {id, name}
- `album.reorder` Reorder Album: {id, parent?: folderId|null, before?: albumId|null} — places the album (or folder) in `parent` (default: where it is; null: the top level) before the sibling `before` of the same kind, or last of its kind; the folder is then ordered by hand. One undo step. → {changed}: how many edits it took (0: already there)
- `album.ruleFields` Smart Album Rule Fields: {} → [{field, label, kind (text|keywords|number|date|choice|bool|album: an album id), group (field-menu submenu, null at the top level), ops: [{op, label}], choices? (ids), choiceLabels? ({id: label})}] for ruleSet rules, in menu order
- `album.setCover` Set as Album Cover: {id: albumId, photo?: photoId}
- `album.setRules` Edit Smart Album: {id, rules?: partial Filter merged onto the current rules (null clears a field), replace?: bool, fromView?: bool (use the current view), name?: also rename it (blank keeps the name) — one undo step, both or neither}
- `album.setTarget` Set as Target Album: {id: albumId | null} (null = the Quick Collection)
- `album.sort` Sort Albums by Name: {parent?: folderId|null} — drops the hand order of the albums inside the folder (default: the top level), so they are listed by name → {changed}: how many albums lost their place
- `album.toggleTarget` Add to Target Album: {ids?} — B: adds the photos to the target album (the Quick Collection unless one is set), or removes them when they're all in it → {album, added, toggled, skipped}; Local photos are skipped, ids the library doesn't have are dropped (none left: nothing changes and `added` is null)

## albums

- `albums.list` List Albums: {}

## app

- `app.export` Export Now: {path?: output file (.jpg/.png/.tif/.webp/.avif/.jxl/.psd/.dng) | dir?, ids?, preset?, format?: jpeg|png|tiff|webp|avif|jxl|psd|dng|original, longEdge?|shortEdge?|width?|height?|megapixels?|percent? (default longEdge 3000; longEdge 0 = full size), fit?: dimensions|widthHeight (with width + height: dimensions fits either orientation, widthHeight limits the width to `width` and the height to `height`), dontEnlarge?, ppi?, quality?: 1..100, jxlLossless?, jxlEffort?: fast|normal, jxlProgressive?, limitKb?, colorSpace?: srgb|displayP3|adobeRgb|proPhoto|rec2020, bitDepth?: 8|10|16|32, hdr? (HDR output for HDR edits: gain map JPEG, PQ AVIF / PNG / JPEG XL, float TIFF), sharpen?: none|screen|matte|glossy, sharpenAmount?: low|standard|high, metadata?: all|allExceptCamera|copyright|none, removeLocation?, naming?, startNumber?, destinationMode?: specificFolder|sameAsOriginal (sameAsOriginal = each photo into its original's folder; `dir` unused), subfolder?, conflict?: unique|overwrite|skip, tiffCompression?: none|lzw|zip (default zip; lzw is usually larger and slower than zip, at 16 bit often larger than none: only for software that needs LZW), dngCompression?: lossless|deflate|uncompressed, addToPhotos?: bool (macOS: then add the files written to Apple Photos; outcome in `applePhotos`), photosAlbum?: top-level album name (made when missing), watermark?: text | {text?, vertical? (upright columns, right to left), size? (text height, 0.005..0.5 of the short edge; default 0.035), opacity? (0..1; 0.7), anchor?: topLeft|top|topRight|left|center|right|bottomLeft|bottom|bottomRight, insetX? (margin from the left/right edge, 0..0.4 of the short edge; 0.025), insetY? (from the top/bottom edge; 0.025), inset? (sets both), rotation?: 0|90|180|270 (degrees clockwise; 0), color? [r,g,b] sRGB, shadow?, image? (graphic drawn instead of the text), imageWidth? (0.01..1 of the photo's width; 0.2)}} — an unknown parameter, an out-of-range watermark size or a value of the wrong kind is an error, not a default
- `app.gpu` GPU Rendering: {enabled?: bool, wait?: bool} — allow/forbid GPU rendering (CPU fallback; LIGHTCRAFT_GPU=0 forbids it for the process); returns {enabled, available, adapter, reason (why the GPU is off), lastFallback (latest render redone on the CPU, and why)}. wait: false never waits for a device still being created (available, adapter and reason are then null and the device is created in the background; with GPU rendering off they say so at once)
- `app.memoryBudget` Memory Budget: {mb?: number} — set the memory budget shared by the caches (default: a quarter of RAM, at most 1536 MB); returns the report

## beforeAfter

- `beforeAfter.copyAfterToBefore` Copy After's Settings to Before (View › Before/After Settings): {}
- `beforeAfter.copyBeforeToAfter` Copy Before's Settings to After (View › Before/After Settings): {}
- `beforeAfter.resetBefore` Reset Before to Import State (View › Before/After Settings): {}
- `beforeAfter.setBefore` Set Before: {source: import|current|history|version, index? (history step), name? (version)} — what the before side shows (this session)
- `beforeAfter.swap` Swap Before and After Settings (View › Before/After Settings): {}

## catalog

- `catalog.query` Query Photos: {filter?: Filter, sort?: Sort, offset?, limit?} — omit filter to list the current view
- `catalog.stats` Catalog Statistics: {}

## crop

- `crop.aspect` Crop Aspect: {aspect: "original"|"free"|"current" (lock the crop's present shape)|"toggle" (lock ↔ free)|"1x1"|"4x5"|"8.5x11"|"5x7"|"2x3"|"4x3"|"16x9"|"16x10"|[w,h], orientation?: "crop"|"given"} — a named ratio takes the crop's present orientation (landscape, or portrait after X); [w,h] is used as given (taller than wide → portrait); `orientation` overrides either
- `crop.autoStraighten` Auto Straighten: {} — level the horizon (or plumb lines) with the crop angle
- `crop.drag` Drag Crop Handle: {handle: topLeft|topRight|bottomRight|bottomLeft|top|right|bottom|left|move | 0..8, from: [x,y], to: [x,y] (normalized, straightened frame), start?: [x0,y0,x1,y1] (default: the current crop), keepRatio?: bool (default false)} — drags a crop handle; stops at the image edge, keeps the opposite edges, honours the aspect lock; keepRatio holds the frame's current proportions for this drag even with the lock off (the UI sends it while Shift is held)
- `crop.reset` Reset Crop [Cmd+Alt+R]: {}
- `crop.rotateAspect` Rotate Crop Aspect [X]: {}
- `crop.set` Set Crop: {rect?: [x0,y0,x1,y1] normalized in the straightened frame, angle?: degrees}
- `crop.straighten` Straighten: {angle: degrees -45..45} — keeps the crop if it still fits, else shrinks it about its centre (the largest crop of its aspect stays the largest)

## curve

- `curve.applyPreset` Apply Point Curve Preset: {name} — sets the active photo's point curves (all four channels; the parametric curve stays)
- `curve.deletePreset` Delete Point Curve Preset: {name} — a user preset (built-ins can't be deleted)
- `curve.exportPresets` Export Point Curve Presets: {path, names?: [name] (default: every user preset)} — writes a .lccurve JSON file → {path, count}
- `curve.importPresets` Import Point Curve Presets: {path | paths: [file]} — .lccurve JSON files ({format, version, presets: [...]}, an array of presets, or one preset); same-named user presets are replaced → {imported: [name], failed: [[file, error]]}
- `curve.presets` Point Curve Presets: {} → {presets: [{name, master, red, green, blue: [[x,y],...], builtin?}], current: name of the preset the active photo's point curves match, or null}
- `curve.reset` Reset Tone Curve: {channel?: all|point|parametric|master|red|green|blue (default all)} — the active photo's tone curve (or one channel) back to linear
- `curve.savePreset` Save Point Curve Preset: {name} — the active photo's point curves under a name (replaces a user preset of that name; built-in names are reserved), saved with the library

## denoise

- `denoise.cancel` Cancel Denoise: {id?, all?} → {cancelled} — stop the photo being made and/or forget the ones waiting (all of them when `id` is omitted)
- `denoise.clear` Clear Denoise Cache: {} → {deleted, bytes} — delete every cached denoised picture of this library (they are made again when wanted)
- `denoise.models.download` Download Denoise Model: {id, acknowledged: true} → {started, from} — fetch a model LightCraft has a pinned address for (see `downloadHost` in the list) in the background over HTTPS with lightcraft-fetch. `acknowledged` must be true: the user has been shown the model's terms and accepted them. It is checked against its size and SHA-256, installed and chosen by itself; `denoise.models.downloads` shows how far it is
- `denoise.models.downloadCancel` Cancel Denoise Model Download: {id} → {discarded} — stop a download, or delete a finished one that was not installed
- `denoise.models.downloads` Denoise Model Downloads: {} → {running, downloads: [{id, state: running | done | installed | failed | cancelled, bytes, total, error, from}]} — also installs any download that has arrived
- `denoise.models.inspect` Inspect Denoise Model: {path} → model terms from an adjacent manifest; never executes the file
- `denoise.models.install` Install Denoise Model: {path, acknowledged: true, activate?: true, background?: false} → {installed, model} or {started} — install a denoise model from a file: an .onnx with a denoise-model.json beside it, or an archive LightCraft knows (the darktable `.dtmodel`). `acknowledged` must be true: the user has been shown the model's licence and accepted it. Unless `activate` is false it becomes the model in use
- `denoise.models.list` Denoise Models: {} → {dir, productsDir, model, runtime, auto, cacheGb, threads, runOn, models: [{id, name, version, licence{name, commercial, url, notice}, provenance, source, sizeBytes, sha256, tile, known, downloadHost, installed, selected, accepted}]}
- `denoise.models.remove` Remove Denoise Model: {id} → {removed, model} — delete an installed model (its cached pictures stay until they are evicted)
- `denoise.models.select` Choose Denoise Model: {id: installed model | null} → {model} — null switches denoise off
- `denoise.models.test` Test Denoise Model: {id} → {ok, result} — load an installed model and check it gives sensible pictures; needs the denoise runtime
- `denoise.pump` Denoise Pump: {pace?: pause | light | normal | full} → {active, running, queued, ready, generation, downloading} — called every frame by the app: takes in finished work and keeps one photo going
- `denoise.queue` Denoise Photos: {ids?: [photoId], scope?: selected | visible | withAmount, retry?: false} → {added, …status} — make the denoised pictures of raw photos that have none, in the background. `retry` tries photos that failed before
- `denoise.settings` Denoise Settings: {auto?: bool, cacheGb?: 1..10000, threads?: 1..64 | null, runOn?: auto | gpu | cpu} → the settings — `auto`: make the picture of the photos being looked at that have a Denoise amount; `cacheGb`: how much the cached pictures may take; `threads`: most tiles run at once; `runOn`: where the model runs — `auto` (the default) the graphics card where it is faster than the processor (both timed on this computer when the card is set up), `gpu` the card whenever it can run the model, `cpu` the processor. Setting `runOn` also lets the card be tried again after a set-up that failed or closed LightCraft
- `denoise.status` Denoise Status: {id?} → {enabled, model, runtime, productsDir, queued, running: {photo, done, total, seconds} | null, ready, made, auto, runOn, device: {kind: gpu | cpu | pending | none, adapter?, reason?, cardMs?, cpuMs?, fellBack?, remote?: {address, state: pending | unavailable | used | idle | slower | given up, device?, remoteMs?, localMs?, reason?, failures?, lastError?}}, cache: {files, bytes, limitBytes}, generation, photo?: {state: notApplicable | noModel | ready | queued | running | failed | idle, …}}
- `denoise.toggle` AI Denoise: {id?: photoId, enabled?: bool} → {id, enabled, amount} — turn AI Denoise on (50% initially) or off for one raw photo, independent of selection and Auto Sync; needs an installed model to turn on

## develop

- `develop.adjust` Nudge Develop Value: {control, delta}
- `develop.auto` Auto Settings (Photo) [Shift+A]: {}
- `develop.autoBwMix` Auto B&W Mix: {} — sets the black & white mix from the photo's colours (and switches to B&W)
- `develop.autoSync` Auto Sync (Edit) [Cmd+Alt+Shift+A]: {on?: bool} (toggles when omitted) — edits to the active photo also change the other selected photos (only the settings that changed; not spot removal / red eye) → {on}
- `develop.beginInteraction` Begin Interaction: {label}
- `develop.cancelInteraction` Cancel Interaction: {}
- `develop.controls` List Develop Controls: {section?} — every slider with range, default and current value
- `develop.copy` Copy Edit Settings (Edit) [Cmd+C]: {groups?: [settingsGroup]} (default: all but crop, masks, remove)
- `develop.curve` Set Point Curve: {channel: master|red|green|blue, points: [[x,y],...] in 0..1}
- `develop.endInteraction` End Interaction: {}
- `develop.get` Get Develop Settings: {id?} → the photo's develop settings; `process` is the rendering process they are interpreted by (see develop.updateProcess)
- `develop.hdr` HDR: {enabled?: bool (default: toggle), maxEv?: number 0..5 (headroom limit, stops above SDR white)} — HDR editing: highlights above SDR white for HDR exports and displays; every SDR render uses the SDR rendition (the hdr.sdr* controls)
- `develop.matchExposure` Match Total Exposures (Photo): {ids?} — set each selected photo's Exposure so its total exposure (shutter × ISO ÷ aperture², plus the slider) equals the active photo's; photos without exposure data are skipped → {changed, skipped}
- `develop.merge` Apply Settings JSON: {settings: partial DevelopSettings JSON, label?}
- `develop.paste` Paste Edit Settings (Edit) [Cmd+V]: {ids?, groups?: [settingsGroup] (paste only these of the copied groups)}
- `develop.pastePrevious` Paste Settings from Previous (Edit) [Cmd+Alt+V]: {ids?, groups?: [settingsGroup] (default: the copy groups)} — from the photo that was active before this one
- `develop.profile` Set Profile: {id: profile id (see profiles.list), amount?: 0..200}
- `develop.quickAdjust` Quick Develop: {control: develop control id, delta, ids?} — add `delta` to the control on every target photo (each from its own value; Quick Develop) in one undo step → {changed}
- `develop.reset` Reset Edits (Photo) [Cmd+Shift+R]: {ids?}
- `develop.resetControl` Reset Control: {control}
- `develop.resetSection` Reset Section: {section: profile|light|curve|color|mixer|grading|effects|vignette|grain|detail|optics|geometry}
- `develop.sectionEnabled` Toggle Section: {section: string, enabled: bool}
- `develop.set` Set Develop Values: {control?: controlId, value?: number, values?: {controlId: number}, ids?: [photo]} — see develop.controls; `crop.angle` turns the crop as crop.straighten does (kept if it still fits, else the largest of its aspect inside the photo)
- `develop.sync` Sync Settings: {groups?} — copy the active photo's settings to all selected photos
- `develop.targeted` Targeted Adjustment: {target: curve|hue|sat|lum, x, y (normalized image coords), delta (slider units; point curves: output levels 0..255), channel?: parametric|master|red|green|blue (curve)} — adjusts the curve region / colour-mixer bands under the point; returns the changed controls
- `develop.treatment` Black & White (Photo) [V]: {bw?: bool} (toggles when omitted)
- `develop.updateProcess` Update to Current Process (Photo): {ids?}: moves the target photos (`ids`, else the selection) that are on an older rendering process to the current one, as one undo step (their look can change; the sliders keep their values; see docs/process-versions.md). Enabled while a selected photo is on an older process; named photos are checked themselves (each must exist, one must be on an older process) → {changed, process}
- `develop.wb` White Balance: {mode: asShot|auto|daylight|cloudy|shade|tungsten|fluorescent|flash|custom, temp?, tint?}
- `develop.wbPick` White Balance Selector [W]: {x, y} normalized image coords of a neutral point

## edit

- `edit.redo` Redo (Edit) [Cmd+Shift+Z]: {}
- `edit.undo` Undo (Edit) [Cmd+Z]: {}

## export

- `export.addToPhotos` Add to Apple Photos: {paths: [absolute file paths], album?: name (an album at the top level of Photos, made when missing; default none), wait?} → once Photos is done, {job, running: false, requested, album, imported, ids: [Photos media item ids], warning?}; with wait: false, at once {job, running: true, requested, album} and the outcome later from export.photosImports {job}. wait defaults to true without a window (lightcraft-cli, the MCP server) and to false in the desktop app, where wait: true is refused (its control requests are answered on the UI thread, which never waits for Photos). macOS: asks Photos to import the files (the first time, macOS asks the user to allow LightCraft to control Photos). One import runs at a time, and an export adding to Photos reserves it before writing: another is refused until it ends. app.export does this for the files it writes with `addToPhotos: true`
- `export.checkTarget` Check Output Path: {path} — fails when writing `path` would replace a photo's original (or its XMP sidecar) in the library; front ends call it before saving a render or screenshot to a user-given path → {path}
- `export.contactSheet` Export Contact Sheet PDF: {path, ids?: photo ids (default selection), paper?: a4|letter, landscape?: bool, columns?: 1..8, rows?: 1..10, captions?: bool} → {path, pages, photos, bytes}; replaces an existing output, never an original
- `export.deletePreset` Delete Export Preset: {name} — removes a user preset → presets
- `export.photosImports` Apple Photos Imports: {job?} → {imports: [{job, running, exporting?, requested, album, imported?, ids?, warning?, error?, skipped?}]} (this session's, oldest first), or the one job: how Add to Apple Photos is getting on (exporting: reserved by an export still writing its files)
- `export.presets` Export Presets: {} → [{name, builtin, params}] (use with app.export {preset: name, …overrides})
- `export.savePreset` Save Export Preset: {name, params?: app.export params (default: the last export's)} — adds or replaces a user preset, saved with the library → presets

## faces

- `faces.detect` Detect Faces (Photo): {ids?, apply?: bool (default true), score?: 0.6, nmsIou?: 0.3, maxFaces?} → {photos: [{id, faces: [{rect, score, landmarks}]}]}. Finds faces with the YuNet detector (download it first: `faces.models.download {id: "yunet-2023mar"}`) and, unless `apply` is false, adds them as unnamed face regions (one undo step), replacing earlier detections but never regions from XMP or ones you named; the sidecar is not touched
- `faces.enable` Face Recognition On/Off: {enabled?: bool} (toggles when omitted)
- `faces.evaluate` Evaluate Face Recognition: {budgetMs?: 0, burstSecs?: 5, margin?, thresholds?: [..], scope?: "visible"} → {queries, top1, sweep: [{threshold, suggested, correct, precision, recall}]} — leave-one-out over your named faces: each is ranked against the others (ignoring shots within burstSecs of it) to show how well the chosen model recognises people in *your* photos and which threshold to trust. Faces not yet embedded are done within budgetMs (`faces.index` does them all); counts only
- `faces.gpu` Face Models on the GPU: {cpuOnly?: bool} → {cpuOnly, detection, recognition}: where the face models run, each as {checking, device, why} (null until it is loaded). The GPU is used only after a background check shows it gives the CPU's results faster; `cpuOnly: true` keeps every face model on the CPU (Settings ▸ Faces), `false` checks the GPU again
- `faces.index` Index Faces: {budgetMs?: 200, ids?: [photo ids to do first]} → {embedded, photosDone, pendingPhotos, indexedFaces, ms} — embed the faces in the library with the chosen recognition model, as many photos as fit in the time (at least one); call again until `pendingPhotos` is 0. `budgetMs: 0` only reports
- `faces.models.download` Download Face Model: {id, acknowledged: true} → {started, from} — fetch a recognition model LightCraft has a pinned address for (see `downloadHost` in the list), in the background over pure-Rust https (lightcraft-fetch). `acknowledged` must be true: the user has been shown the model's terms and accepted them. It is checked against its size and SHA-256, then installed, chosen and switched on by itself; `faces.models.downloads` shows how far it is
- `faces.models.downloadCancel` Cancel Face Model Download: {id} → {discarded} — stop a download, or delete a finished one that was not installed
- `faces.models.downloads` Face Model Downloads: {} → {running, downloads: [{id, state: running | done | installed | failed | cancelled, bytes, total, error, from}]} — also installs any download that has arrived; `installed` stays listed until `faces.models.downloadCancel` clears it
- `faces.models.inspect` Inspect Face Model File: {path} → what a .onnx file is: {kind: known | draft | unsupported, model, assumptions, reason, alreadyInstalled}; installs nothing
- `faces.models.install` Install Face Model: {path, acknowledged: true, activate?: true} → {installed, active: {embedder, enabled}} — copy a .onnx face recognition model into the models folder. `acknowledged` must be true: the user has been shown its licence (see inspect) and accepted it. Unless `activate` is false the model becomes the one in use and recognition is switched on; an earlier model stays installed
- `faces.models.list` Face Models: {} → {dir, enabled, embedder, runtime, models: [{id, name, role, licence{name, commercial, url, notice}, provenance, source, sizeBytes, known, installed, selected}]}
- `faces.models.remove` Remove Face Model: {id} — delete an installed model
- `faces.models.select` Choose Face Recognition Model: {id: installed recogniser | null}
- `faces.models.test` Test Face Model: {id} → {ok, result: {loadMs, embedMs, dimension, checks}} — load an installed recognition model and check it gives sensible faces; needs the recognition runtime
- `faces.nameFaces` Name Faces: {faces: [{photo, index}], name} → {named, photos} — name (or, with a null or empty name, clear) many face regions as one undoable step; the sidecar is not touched
- `faces.person` Faces of a Person: {name, more?: 120} → {name, total, confirmed: [{photo, index, rect}], more: [{photo, index, rect, score}], ready, pendingPhotos} — the faces named `name` across the library, and the unnamed faces that look most like them (best first, already embedded ones only, once recognition is on); confirm one with `faces.setName`
- `faces.pump` Index Faces in the Background: {pace?: pause | light | normal | full} → {active, inFlight, pendingPhotos, indexedFaces, searchedPhotos, workers} — cheap to call every frame: takes in what the background workers have finished and gives them the next photos, as many at once as the pace allows (none when paused, one when light, half the machine's threads when normal, four fifths when full); inactive until face recognition is on in Settings with a model chosen
- `faces.renamePerson` Rename Person: {from, to, merge?: bool} → {faces, photos, from, to, merged} — give every in-library face of `from` the name `to` (trimmed, any capitalization), one undo step; refused when `to` is already someone else unless `merge` is true, which combines the two; the sidecar is not touched
- `faces.setName` Name Face: {id?, index, name} — name a face region (null or empty clears it); undoable; the sidecar is not touched
- `faces.suggest` Suggest Names for Faces: {ids?, threshold?, margin?, budgetMs?} → {photos: [{id, faces: [{index, suggestion: {name, score, runnerUp} | null, candidates: [{name, score}]}]}]} — who the unnamed faces in these photos might be, from the faces already named in the library. Only suggestions: nothing is named
- `faces.unnamed` Unnamed Faces: {limit?: 600} → {total, faces: [{photo, index, rect, view, suggestion: {name, score} | null}], ordered, ready} — the faces nobody has named; with recognition running, look-alikes are next to each other and a face the named ones recognise carries the name they suggest. `view` is the box to show the face by. Name them with `faces.nameFaces`

## filter

- `filter.applyPreset` Apply Filter Preset: {name} — replaces the current filter → {photos}
- `filter.deletePreset` Delete Filter Preset: {name}
- `filter.presets` Filter Presets: {} → [{name, filter}]
- `filter.savePreset` Save Filter Preset: {name} — the current filter (library.filter), saved with the library

## focus

- `focus.pump` Read Focus Points in the Background: {pace?: pause | light | normal} → {active, running?: {done, total, found}, last?, lookedAt} — cheap to call every frame (the app does): takes in what the background focus-point reader has read and commits it in batches; reads nothing new while paused and rests between files when light. Starts the reader by itself once per library opening when photos are left to look at

## folder

- `folder.create` New Folder on Disk: {parent, name} — create a folder on disk inside `parent` (refused if the name is taken); one undo step (undo removes it again while it is empty) → {path}
- `folder.label` Set Folder Color Label: {path, label: red|yellow|green|blue|purple|none} — give a folder of the library (one its photos were imported from, see library.folders) a colour label, or take it off (also once its photos are gone); one undo step. The label follows the folder when it is renamed or moved with folder.rename / folder.move → {path, label}
- `folder.move` Move Folder: {path, into: destination folder} — move a folder on disk into another and relink the photos in it; one undo step (undo moves it back, refused if the old place is taken); refused for the home folder and its Pictures, Desktop and Downloads → {path, relinked}
- `folder.rename` Rename Folder: {path, name} — rename a folder on disk (its files and sidecars go along) and relink the photos in it; one undo step (undo renames it back, refused if the old name is taken); refused for the home folder and its Pictures, Desktop and Downloads → {path, relinked}
- `folder.scanChanges` Scan Folder for Changes: {path, disk?: bool (a whole disk or share, or a folder holding disks)} — compare a folder of the library (and the folders inside it) with the disk; changes nothing → {path, new: [{path, name, format, …}] files the library doesn't have, duplicates: files whose content it already has, unreadable: [{path, error}], missing: [{id, path}] photos whose file is gone, moved: [{id, from, to}] photos whose file is elsewhere in the folder (same content), metadata: [{id, path}] photos whose XMP sidecar was saved after they came in or were last edited here and says something the library doesn't}
- `folder.synchronize` Synchronize Folder: {path, disk?: bool, scanned?: bool, importNew?: true, relinkMoved?: true, removeMissing?: false, readMetadata?: false} — bring a folder of the library up to date with the disk (see folder.scanChanges): import its new files in place, relink photos whose file was renamed or moved within it, move photos whose file is gone to Recently Deleted, read XMP sidecars saved by other apps (the sidecar wins); acts on the last folder.scanChanges of the folder while it is current (the folder's photos unchanged), else scans again — or, with `scanned: true`, refuses; one undo step, no file is touched → {imported, relinked, removed, read, failed: [[path, error]]}

## geometry

- `geometry.guides` Guided Upright Guides: {guides: [[x0,y0,x1,y1], …] (≤ 4, normalized coords of the lens-corrected image), add?: bool (append one guide, dropping the oldest beyond 4)} — switches Upright to Guided
- `geometry.upright` Upright: {mode: off|auto|guided|level|vertical|full} — analyses the photo (line segments → vanishing points) and stores the correction; run again to update after lens changes

## history

- `history.clear` Clear History: {} — keeps the current settings as the only step
- `history.list` List History: {id?} — returns {history: labels oldest first, cursor: index of the step the settings are at (later steps can be returned to), versions}
- `history.next` Next History Step: {} — steps the History cursor forward one step
- `history.previous` Previous History Step: {} — steps the History cursor back one step
- `history.restore` Go to History Step: {index} — loads that step's settings and moves the History cursor there; later steps stay listed until a new edit

## journal

- `journal.list` Command Journal: {limit?}

## keyword

- `keyword.create` Create Keyword: {name, parent?: keyword | null (default: the default parent; null = the top level), synonyms?, includeOnExport?, exportContaining?, exportSynonyms?, person?, addToSelected?: bool, ids?} → {keyword}
- `keyword.delete` Delete Keyword: {keyword} — removes it (and the keywords below it) from every photo
- `keyword.deleteSet` Delete Keyword Set: {name}
- `keyword.edit` Edit Keyword: {keyword, name?: its new name (one level), synonyms?, includeOnExport?, exportContaining?, exportSynonyms?, person?} — what isn't given keeps its value
- `keyword.export` Export Keywords: {path?} — the keyword list as a file (Lightroom Classic's format, which Capture One, Photo Supreme and Bridge read) → {keywords, captureOneRefuses: keywords with ; , < > that Capture One's importer refuses, unwritable: keywords left out because the format can't hold them (a name in brackets or braces, a line break, deeper than 64 levels; a synonym as "path {synonym}"), text when there is no path}
- `keyword.import` Import Keywords: {path | text} — a keyword list (Lightroom Classic's format, also Capture One's and Photo Supreme's Formatted Vocabulary File): adds the keywords the library doesn't have, gives those it has the list's synonyms; one undo step → {added, updated}
- `keyword.info` Keyword Info: {keyword} → {path, listed, count, synonyms, includeOnExport, exportContaining, exportSynonyms, person}
- `keyword.list` Keywords: {} → [{name, path, count, children}] keyword tree (`a|b|c` keywords are hierarchical)
- `keyword.merge` Merge Keywords: {from: [keyword], into: keyword} — replaces each `from` keyword (children included) with `into` on every photo
- `keyword.move` Move Keyword: {keyword, parent: keyword | null (the top level), merge?: bool} — with the keywords below it; onto a name that is taken only with `merge: true`
- `keyword.nextSet` Next Keyword Set [Alt+0]: {}: the set after the current one (after the last, Recent Keywords)
- `keyword.previousSet` Previous Keyword Set [Alt+Shift+0]: {}: the set before the current one (before Recent Keywords, the last)
- `keyword.purgeUnused` Purge Unused Keywords: {} — takes off the keyword list the keywords no photo has → {purged}
- `keyword.rename` Rename Keyword: {from, to} — on every photo, children included (`a` → `b` renames `a|x` to `b|x`); renaming onto an existing keyword merges them
- `keyword.saveSet` Save Keyword Set: {name, keywords?: [up to 9, "" = an empty slot] (default: the renamed set's, else the current nine), replace?: the set it renames, new?: refuse a name another set has} — replaces a set of that name (or `replace`, in its place) and makes it current
- `keyword.setDefaultParent` Put New Keywords Inside: {keyword: keyword | null} — the parent keyword.create puts new keywords inside (null: the top level)
- `keyword.setShortcut` Set Keyword Shortcut: {keywords: [..] or "a, b" (none clears it)}: sets the keyword shortcut, a mark on its keywords in the keyword list (a new name is listed; one undo step) → {keywords}
- `keyword.sets` Keyword Sets: {} → {sets: [{name, keywords}], current, keywords: the nine ⌥1–⌥9 apply}
- `keyword.shortcut` Keyword Shortcut: {} → {keywords: the keyword shortcut's, which ⇧K adds or removes}
- `keyword.suggest` Keyword Suggestions: {prefix?: typed text, ids?, limit?: 12} → keywords to suggest for the photos (co-occurring / most used, or matching the prefix)
- `keyword.toggleFromSet` Toggle Keyword from Set: {index: 1..9, ids?} — the set's keyword N: added to the target photos, or removed when they all have it
- `keyword.toggleShortcut` Add or Remove Keyword Shortcut [Shift+K]: {ids?}: removes the keyword shortcut's keywords from the target photos when they all have every one, else adds them → {changed, keywords, added}
- `keyword.useSet` Use Keyword Set: {name} ("Recent Keywords" = the recently added ones)

## label

- `label.applySet` Apply Color Label Set: {name} — use a set's label names (undoable)
- `label.deleteSet` Delete Color Label Set: {name} — user sets only
- `label.names` Color Label Names: {} → [{label, name, custom}]
- `label.saveSet` Save Color Label Set: {name} — save the current label names as a set (replaces a user set of that name)
- `label.setNames` Edit Color Label Names: {names: {red?: name|null, yellow?, green?, blue?, purple?}} — null or empty restores the colour's name
- `label.sets` Color Label Sets: {} → {sets: [{name, names: [red, yellow, green, blue, purple], builtin}], current: name|null}

## lens

- `lens.databaseStatus` Lens Database Status: {} → {download: {state: idle|running|done|failed|cancelled, …}, dir, lenses (in the database in use)}
- `lens.downloadDatabase` Download the Lens Database: {} — fetch lensfun's lens database (CC BY-SA 3.0, pinned to one commit, checked file by file) into the app's data folder in the background, with an activity row, and read lens profiles from it once it is in place (unless LIGHTCRAFT_LENSFUN_DIR names another folder); the desktop app offers it on its first launch and in Settings. LIGHTCRAFT_LENSFUN_URL lists other places to fetch the same files from → {started, dir}

## library

- `library.autoImport` Auto Import Settings: {folder?: path | null (off), copy?: bool (copy into the library's Originals, else add in place), album?: name | null} — a watched folder whose new photos are added as they arrive (library.autoImportScan; the app scans every few seconds) → the settings
- `library.autoImportScan` Auto Import Now: {listing?: [[path, size]] (the folder as listed by the caller, e.g. on a worker thread), start?: bool (false: return the `library.import` params as `import` instead of importing)} — add the watched folder's new photos (files the library doesn't have yet; partial / still-copying files wait for the next scan) → {imported, folder, warnings?: [{path, code, profile?, mode?, fields?}], import?}
- `library.browse` Browse Folder: {path, subfolders?: bool} — show a folder's photos without adding them to the library (they're read in place; edits go to XMP sidecars) → {path, photos, new}
- `library.buildPreviews` Build Previews: {size?: standard (2048 px, or `edge`) | full (1:1), ids?, wait?: bool} — render the grid thumbnail and loupe view of the selected photos (else all in view) into the preview cache, in the background unless `wait` → {total, done, failed, running}
- `library.cancelPreviews` Cancel Preview Build: {}
- `library.clearFilter` Clear Filters (View): {}
- `library.clearPreviews` Discard Preview Cache (File): {}
- `library.compact` Optimize Library (File): {}
- `library.devices` Cameras and Cards: {} → [{name, path (its DCIM folder), root}] — mounted volumes with a DCIM folder
- `library.down` Photo Below [Down]: {rows?: n (photos to move forward; default 1, the grid passes the distance to the cell below)}
- `library.emptyRecentlyDeleted` Empty Recently Deleted (Photo): {} → {deleted} — removes every photo in Recently Deleted from the library (files on disk stay)
- `library.filter` Filter: partial Filter: {text?, rating?, ratingOp?: atLeast|exactly|atMost, flag?: pick|reject|none|null, flags?: [pick|reject|none] (any of them; [] = no constraint), label?, kind?, merged?: hdr|panorama|hdrPanorama|any, edited?, date?, libraryFolder?: a path from library.folders, keyword?, person?, camera?}
- `library.findMissing` Find Missing Photos: {folder} — relink every missing photo whose file is somewhere in the folder: same name and size (and content, when the library knows its hash), or — renamed — same size and content; or {found, missing, ambiguous} — relink what a search already found (the app searches on a worker thread; photos relinked meanwhile and files now in use are skipped) → {found: [{id, from, to, by: name|content}], missing, ambiguous: [{id, from, candidates}] (several same-name candidates and no hash to tell them apart: skipped)}
- `library.findSimilar` Find Similar Photos (Photo): {id?, similarity?: 0..1 (0.8), filter?: bool (true)} — photos that look like the active one (composition and tones), most similar first; filters the view to them (Clear Filters to go back) → {photos: [{id, similarity}]}
- `library.folders` Library Folders: {} → [{name, path, count, own, volume, selectable, label?, children}] the disks and the folders the library's photos were imported from, with photo counts (subfolders included in `count`); show one with library.source {kind: libraryFolder, path} (rows with selectable false only open)
- `library.forgetLocal` Forget Unchanged Local Photos: {dryRun?: bool, days?: n (default: the library preference, 0 = never)} — remove Local (browsed, not added) photos nobody changed, of folders not browsed for `days`, from the catalog; files and sidecars stay, browsing the folder again brings them back; not an undo step → {local, forgotten, keptRecent, keptTouched, keptInUse, foldersStamped, days, dryRun}
- `library.groups` Date Groups: {by?: day|month|year (default: the sort's grouping; auto = day)} → [{key, label, start, count}] date headers of the grid
- `library.holdView` Hold View Until Refreshed (View): {on?: bool (toggles when omitted)} → {hold} — when on, an edit that makes a photo stop matching the view (a keyword given in a smart album of photos without keywords, a flag taken off in Picks, a rating under the filter bar's) keeps it in the view until `library.refresh`, Reshuffle, or another source, filter or sort; photos that start matching still appear at once, and deleting a photo or taking it out of the album or folder shown still takes it out of the view. Changing a smart album's rules is another view too. Off (the default): the view follows every edit. Kept with the library's preferences; asking for the state it already has changes nothing
- `library.import` Import Photos (File) [Cmd+Shift+I]: {paths: [file or folder (recursive)], mode?: add|copy|move (add = reference the files in place; copy = into the library's Originals/YYYY/YYYY-MM-DD/; move = as copy, then each original and its XMP sidecars are removed from the source — only after the copy is verified (a hard link on the same volume, else copied, synced and compared byte for byte) and its catalog record is saved; failed, duplicate and unchecked files keep their sources; a taken name gets -1, -2…; undo removes the photos from the library but leaves the files at the destination), destination?: folder for copies / moves, organize?: date (YYYY/YYYY-MM-DD) | month (YYYY/YYYY-MM) | flat | a folder template, e.g. `{date:%Y}/{date:%Y%m%d}` → 2026/20260114 (the template's `/` make the folders, each level expanded with the rename tokens and made a safe folder name: never outside the destination; must be relative, no `..`; a level with missing metadata is `unknown`) — dated by capture time, else the import time, rename?: file-name template for copies, original extension added (tokens: {name} {num} {seq} {seq:N} {date} {date:%Y%m%d} {folder} {camera} {lens} {iso} {rating} {title} {creator} {ext}; photo.renameTokens explains each; blank = keep names), renameStart?: 1 (must fit this platform; later files are reported failed if the sequence runs out), metadataPreset?: name, dng?: bool (copy raws as DNG; copy only), local?: bool (browsing: the photos stay out of the library, like library.browse; not with move), album?: albumId, albumName?: new album, preset?: presetId, keywords?: [..], onDeleted?: restore|skip|fresh (a file that is in Recently Deleted: restore (default) = bring the photo back with its edits — relinked to the file when its own is gone, skip = leave it there and say so, fresh = delete the trashed record and import the file as new)} → {imported, duplicates: [{path, existing, reason, existingDeleted?}], restored?: [photoId], failed, warnings?: [{path, code: cameraProfile|uprightGeometry|unmappedXmp, profile?, mode?: off|auto|level|vertical|full|guided|unknown, fields?}], moved?: [{from, to, sidecars?}], kept?: [{path, reason}] (move: sources left in place and why), album?}
- `library.importLightroom` Import Lightroom Catalog: {path: .lrcat, updateExisting?: false}; direct import of paths, ratings, flags, metadata, keywords, collections, virtual copies & mapped edits. Archives source settings/history first. Existing edited photos are preserved unless updateExisting=true; source catalog is read-only.
- `library.importPreview` Review Import: {paths: [file or folder (recursive)]} → {candidates: [{path, name, format, kind, width, height, fileSize, captured, duplicate?: path|content, existing?, error?, previewOnly?: why a raw can only be shown from its embedded preview}], duplicates, scanned} — nothing is added
- `library.info` Library Info: {}
- `library.inspectLightroom` Inspect Lightroom Catalog: {path: .lrcat} → {photos, collections, missing, warnings}; read-only, no Lightroom required
- `library.memory` Memory Usage: {} — bytes held by each cache (decoded sources, rendered previews, GPU buffers; heap when instrumented)
- `library.missing` Missing Photos: {} → [{id, path}] — photos whose original file isn't where the library expects it (every file is looked at: on a network share that takes minutes, so the desktop app, asked over its control channel, checks on a worker thread, with a row in the activity stack that can stop it, and answers when it is done)
- `library.next` Next Photo [Right]: {}
- `library.preferences` Library Preferences: {import?: {rawPreset?: presetId|"default", otherPreset?: presetId|"default", perCamera?: bool, cameras?: [{camera: "Make Model", preset: presetId|null}], copyright?: text, creator?: text (given to imported photos without one), showOnCard?: bool (open the import review when a camera or card is connected)}, camera?: {camera, preset?, remove?: bool}, cacheMb?: n (0 = default), forgetLocalDays?: n (forget untouched Local photos of folders not browsed for n days; 0 = never)} — develop defaults applied on import (raws / other images / per camera) and the thumbnail cache size, saved with the library → {xmp, import, cacheMb, forgetLocalDays, persistent}
- `library.previewProgress` Preview Build Progress: {} → {total, done, failed, repaired, running, cancelled, what, error} | null
- `library.previous` Previous Photo [Left]: {}
- `library.recheckPreviewOnly` Recheck Preview-Only Raws: {all?: bool} — probe again the raws shown from their embedded preview whose flag another LightCraft version set (the app does this in the background when a library opens; `all` rechecks every preview-only raw, e.g. when testing a decoder build of the same version), and bring each up to date as Reload from Disk would; not an undo step, develop settings and history are kept; files that can't be read are left for next time → {checked, updated: [ids], cleared: [ids] (develop from their raw data now)}
- `library.refresh` Refresh View (View): {} — show what matches now: a view that holds its photos (`library.holdView`) lets go of the ones that stopped matching a smart album's rules, Picks or the filter bar since it was opened, sorted or last refreshed
- `library.refreshLensProfiles` Look Up Lens Profiles Again: {ids?: [photo ids], all?: bool} — library raws without a lens profile whose lens the lens database knows are read again and get their profile (the correction is switched on where the photo's settings are still as imported); with all, also raws whose profile came from the database (it may give another, or none) and raws whose file named no lens at import; the app does this by itself when the database arrives (all: when its files were replaced) and when Enable Lens Corrections is ticked; not an undo step → {checked, found: [ids], database: bool}
- `library.removeFolder` Remove Folder from Library: {path, disk?: bool} — move the library photos imported from this folder (and the folders inside it) to Recently Deleted; one undo step, no file is touched. A whole disk or share (`/Volumes/nas`, `C:\`, `\\srv\share`) goes only with `disk: true`, the startup disk never → {removed}
- `library.retrySidecars` Write Waiting XMP Sidecars: {} — writes again the automatic XMP sidecars that failed (folder offline, read-only or full) whose originals are reachable now → {written, waiting}
- `library.select` Select Photos: {ids: [id], active?: id, mode?: replace|add|toggle|range} — every id must be a photo of the library
- `library.selectAll` Select All (Edit) [Cmd+A]: {}
- `library.selectBy` Select by Flag, Rating or Label: {flag?: pick|reject|none, rating?: 0..5, ratingOp?: gte|eq|lte (default gte), label?: red|…|none, add?: bool (extend the selection)} — among the photos in view
- `library.selectNone` Deselect All (Edit) [Cmd+Shift+A]: {}
- `library.shuffle` Reshuffle (View › Sort): {seed?: 0..2^53-1} — sort at random; without `seed` a new shuffle each time
- `library.smartPreviews` Build Smart Previews: {ids?, discard?: bool, background?: bool} — build (or discard) the smart previews of the selected photos (else all in view): compact proxies in the library that keep photos editable and exportable (at proxy size) while their originals are offline; a damaged proxy (cut short) is rebuilt → {built, repaired, removed, failed}; with background (the app's menu) the files are read and written on a worker thread → {total, done, failed, repaired, running, what} like library.buildPreviews (progress: library.previewProgress, stop: library.cancelPreviews)
- `library.smartPreviewsLocation` Smart Previews Location: {path?: absolute folder, reset?: bool, existing?: move|leave|discard} — without path/reset: where this library keeps its smart previews → {path, default, custom, available, count, bytes}. With path (or reset = back to `Smart Previews` in the library): use that folder instead (must exist or have an existing parent, and accept writes; never falls back to another drive). Smart previews already in the old folder need `existing`: move them, leave them (build again), or discard them → also {handled, failed}
- `library.sort` Sort (View › Sort): {key?: captureDate|importDate|editDate|fileName|rating|fileSize|random, ascending?: bool, group?: auto|none|day|month|year, seed?: u64 (the shuffle `random` gives)}
- `library.source` Show Source: {kind: all|recentlyAdded|album|recentlyDeleted|picks|missing|libraryFolder, id?: albumId, path?: a path from library.folders (for libraryFolder)}
- `library.state` Library State: {}
- `library.toggleAutoWriteXmp` Automatically Write Changes into XMP (File): {} → {autoWrite}
- `library.toggleFilters` Enable Filters (View) [Cmd+L]: {} — with a filter set, puts it aside and shows everything; with one put aside, brings it back as it was (stars, flag, text… together). Setting or clearing a filter while it is off forgets the one put aside → {enabled, count}
- `library.up` Photo Above [Up]: {rows?: n (photos to move back; default 1, the grid passes the distance to the cell above)}
- `library.xmpPreferences` XMP Sidecar Preferences: {autoWrite?: bool, naming?: stem (IMG_1.xmp, default) | full (IMG_1.CR3.xmp)} → current preferences (saved with the library)

## mask

- `mask.add` Create New Mask: {kind: brush|linear|radial|sky|subject|background|luminanceRange|colorRange|object|prompt, ...shape params (start/end, center/rx/ry/angle/feather, lo/hi…; object: points/exclude [[x,y],…]; prompt: text; object/prompt: seg? a stored segmentation, no model needed), name?} — AI kinds need the SAM 3 model; in the app a prompt returns {pending} and the mask appears when found
- `mask.addComponent` Add/Subtract/Intersect Mask: {id?: maskId, op: add|subtract|intersect, kind, ...shape params}
- `mask.adjust` Set Mask Adjustments: {id?, values: {exposure, contrast, highlights, shadows, whites, blacks, temp, tint, texture, clarity, dehaze, hue, saturation, sharpness, noise, moire, defringe, color_hue, color_sat, amount}}
- `mask.applyEffect` Apply Mask Effect: {name, id? | ids?: [maskId] | all?: bool, photos?: "selected" (also the masks of the same names on the other selected photos, one undo step), remember?: bool (true: new masks of this kind start with it)} — sets the effect's sliders (all, or the ones it keeps; Amount only if it carries it) → {name, masks, photos, brush}
- `mask.brushStroke` Brush Stroke: {id?: maskId, points: [[x,y],…] normalized, size?: fraction of long edge (0.03), feather?, flow?, density?, erase?: bool, autoMask?: bool, pressure?: [p,…] pen pressure 0..1 per point (scales each dab's size and flow; omitted: full), connect?: bool — start from the last point of the mask's last stroke (⇧-click), size / feather / flow tapering from that stroke's to these} → {activeMask, connected}
- `mask.component` Edit Mask Component: {id?, component: index, action: invert|duplicate|delete|rename|op, name? (rename; empty clears), op?: add|subtract|intersect} — one component of a mask (deleting the last one deletes the mask)
- `mask.delete` Delete Mask: {id?}
- `mask.deleteAll` Delete All Masks: {}
- `mask.deleteEffect` Delete Mask Effect: {name | names: [name]} — removes effect presets
- `mask.duplicate` Duplicate Mask: {id?, invert?: bool (Duplicate and Invert)} — the copy goes right after the original and is selected
- `mask.duplicateEffect` Duplicate Mask Effect: {name, to?} (default "<name> copy") → list + {name}
- `mask.effects` Mask Effect Presets: {} → {effects: [{name, adjust, group?, favorite?, fields?, with_amount?, brush?, extra?}], groups: [{name, effects: [name]}] (menu order), current: the effect the selected mask matches or null, toolEffects: {tool: effect a new mask of that kind starts with}}
- `mask.exportEffects` Export Mask Effects: {path, names?: [name], group?: name (default: all)} — writes an .lceffect JSON file (groups, stars and kept Lightroom settings included) → {path, count}
- `mask.favoriteEffect` Favorite Mask Effect: {name | names, favorite?: bool (default: toggle)}
- `mask.importEffects` Import Mask Effects: {path | paths: [file or folder], group?, dryRun?} — Lightroom Classic local adjustment presets (.lrtemplate), Camera Raw local correction presets (.xmp), .lceffect files and .zip bundles of these; folders and Lightroom's divider presets ("10 ----- DETAIL ----- 10") become groups; same-named effects are replaced → {imported: [{name, group, file, unmapped}], dividers: [{name, group, file}], failed: [[file, error]]}
- `mask.invert` Invert Mask: {id?}
- `mask.move` Move Mask: {id?, to?: index (0 = top), delta?: ±n} — reorder the masks list
- `mask.objectPoint` Add Object Click: {x, y: normalized image point, exclude?: bool (⌥-click: leave this part out), id?: maskId} — a click on the selected mask's Object selection (its last Object component); SAM 3 re-segments the object → {include, exclude}
- `mask.refine` Refine Mask Edges: {id?, value: 0..100} — the mask's edges snap to the photo's (guided filter; rendered on the CPU)
- `mask.refineDetail` Refine AI Mask Detail: {id?: maskId, component?} — a zoomed-in SAM 3 pass over an Object/Describe selection (default: the mask's last one): the photo around it is analyzed again at a higher resolution, in the background; the mask updates when it's done → {started}
- `mask.rename` Rename Mask: {id?, name}
- `mask.renameEffect` Rename Mask Effect: {name, to}
- `mask.renameEffectGroup` Rename Mask Effect Group: {group, to} ("" ungroups; an existing name merges)
- `mask.sampleColor` Sample Mask Color: {x, y: normalized image point, add?: bool (⇧: add to the samples, max 5), id?, component?} — the colour range of the selected mask (its first colour-range component) samples the colour there → {samples}
- `mask.saveEffect` Save Mask Effect: {name, id?, group?, fields?: "all" (default) | "changed" | [slider], amount?: bool (carry Amount), brush?: {size, feather, flow, density, auto_mask}} — the selected mask's sliders as an effect preset (replaces one of that name), saved with the library
- `mask.select` Select Mask: {id|null}
- `mask.setEffectGroup` Move Mask Effect to Group: {name | names, group: name ("" = none)}
- `mask.toolEffect` Set Effect for New Masks: {tool: brush|linear|radial|subject|…, name?} — the effect new masks of that kind start with (no name: none)
- `mask.update` Update Mask Shape: {id?, component?: index (0), shape: MaskShape JSON}
- `mask.updateEffect` Update Mask Effect: {name, id?, fields?, amount?, brush?} — overwrite the effect with the selected mask's sliders (keeps its group, star and which sliders it carries unless given)
- `mask.visible` Show/Hide Mask: {id?, visible?: bool}

## merge

- `merge.hdr` HDR Merge: {ids?, align=true, deghost=none|low|medium|high, autoSettings=true, stack=false, preview=false, showOverlay=false, previewPath?}
- `merge.hdrBatch` HDR for Each Bracket Set (Photo › Photo Merge): {ids?, align=true, deghost=none|low|medium|high, autoSettings=true, stack=false}: an HDR merge of each bracket set among the photos (each stack, then photos taken less than a second apart at exposures ≥ ½ EV apart) → {merged: [{id, path, …}], failed: [{photos, error}]}
- `merge.hdrPanorama` HDR Panorama Merge: {ids?, bracket=0 (auto from EXIF), align, deghost, projection, boundaryWarp, autoCrop, fillEdges, autoSettings, stack, preview, previewPath?}
- `merge.panorama` Panorama Merge: {ids?, projection=auto|spherical|cylindrical|perspective, boundaryWarp=0..100, autoCrop=false, fillEdges=false, autoSettings=true, stack=false, maxMegapixels=full size (≤ 512, held to memory), preview=false, previewPath?}

## metadata

- `metadata.applyPreset` Apply Metadata Preset: {name, ids?} — text fields replace, keywords are added; one undo step
- `metadata.deletePreset` Delete Metadata Preset: {name}
- `metadata.downloadPlaceNames` Download Place Names (GeoNames) (Photo): {dataset?: folder} → {started, path, attribution} — downloads the GeoNames cities list (CC-BY 4.0, ~3 MB, from download.geonames.org) in the background for Fill Location from GPS; no photo data is sent
- `metadata.placeNamesStatus` Place Names Status: {dataset?: folder} → {downloaded, bytes, path, attribution, source}
- `metadata.presets` Metadata Presets: {} → [{name, fields}]
- `metadata.reverseGeocode` Fill Location from GPS (Photo): {ids?, overwrite?: bool (also replace place fields that already have text; default false: only empty ones are filled), dryRun?, dataset?: folder, maxDistance?: metres (past this distance from the town found, City is left empty and the town is given as nearestCity)} → {looked, found, changed, photos: [{id, place: {sublocation, city, state, country, iso, distance}, nearestCity?}], attribution} — fills City / State / Country (and Sublocation when known) from GPS with the offline GeoNames place names (download them first); one undo step. The place names list towns of 15 000 people or more (GeoNames cities15000): a photo taken in a smaller town gets the nearest larger one, up to 50 km away (`distance` says how far); `maxDistance` keeps such a town out of City
- `metadata.savePreset` Save Metadata Preset: {name, fields?: {copyright?, copyrightStatus?: unknown|copyrighted|publicDomain, usageTerms?, copyrightUrl?, creator?, title?, caption?, location?, city?, state?, country?, keywords?: [..]}, only?: [field] (from the active photo when `fields` is absent; default the copyright fields, creator, place)} — adds or replaces

## photo

- `photo.addToLibrary` Add to My Photos (Photo): {ids?} — browsed (Local) photos join the library
- `photo.allMetadata` All Metadata: {id?} → {exif: [{group, tag, name, value}], xmp: [{name, value}]} — every EXIF / TIFF / GPS tag of the file and its XMP properties
- `photo.analyze` Assisted Culling: {ids?, rejectBelow?: sharpness 0..100, pickBest?: bool, burstGap?: seconds 0..86400 (10), similarity?: 0..1 (0.93)} — score the selected photos (else all in view) for focus (0..100) and clipping, group look-alike shots (signature similarity at least `similarity`) taken at most `burstGap` seconds apart and mark the sharpest of each; optionally reject blurry photos and pick each group's best; one undo step → {photos: [{id, sharpness, clipped, group, best}], groups, rejected, picked}
- `photo.autoTagTracklog` Auto-Tag Photos from Tracklog: {path?: GPX file | gpx?: GPX text, ids?, offset?: camera clock's UTC offset for photos whose capture time has no zone (`+02:00`, or hours; default UTC), maxGap?: seconds (600), replace?: bool (also photos that already have GPS), dryRun?: bool} → {tagged, interpolated, nearest, skipped: {noTime, outside, hasGps}, assumedUtc, points, start, end, photos: [{id, gps, match}]} — positions from the track log by capture time; one undo step
- `photo.clearLabel` Clear Color Label (Photo › Set Color Label): {ids?, advance?: bool} — `photo.label` with `none`; without `ids`, the selection moves on when this takes the active photo out of the view
- `photo.convertToDng` Convert to DNG (Photo): {ids?} — write each raw photo as a lossless DNG next to it (settings embedded) and relink the photo to it; originals are kept → {converted: [{id, path, original}], skipped}
- `photo.copyMetadata` Copy Metadata (Photo) [Cmd+Alt+Shift+C]: {} — title, caption, copyright (notice, status, usage terms, info URL), creator, location and keywords of the active photo
- `photo.cycleFlag` Cycle Flag (Photo › Set Flag) [`]: {ids?, advance?: bool} — each photo's own flag: unflagged -> pick -> reject -> unflagged; without `ids`, the selection moves on when this takes the active photo out of the view
- `photo.decreaseFlag` Decrease Flag Status (Photo › Set Flag) [Cmd+Down]: {ids?, advance?: bool} — pick -> unflagged -> reject (stops at reject); without `ids`, the selection moves on when this takes the active photo out of the view
- `photo.decreaseRating` Decrease Rating: {ids?, advance?: bool} — without `ids`, the selection moves on when this takes the active photo out of the view
- `photo.delete` Delete Photo (Photo) [Delete]: {ids?} — moves to Recently Deleted
- `photo.deletePermanently` Delete Permanently (Photo): {ids?}
- `photo.duplicate` Duplicate (Photo): {ids?} — copy each photo's file next to it (`-copy`) and add it with the same settings, metadata and albums (a real file, unlike a virtual copy) → {ids}
- `photo.editExternal` Edit Copy for External Editor: {ids?, colorSpace?: adobeRgb (default) | proPhoto | displayP3 | srgb, format?: tiff (default) | psd, bitDepth?: 16 (default) | 8, dir?} — render each selected photo (or `ids`, at most 50) with its edits as `<name>-Edit.tif` (or `.psd`, flat, which PhotoCraft saves back to in place) next to it, add each stacked on its original and select the copies → {path, id, original (the first copy), copies: [{path, id, original}]} (the app then opens them in the external editor)
- `photo.flag` Set Flag (Photo › Set Flag): {flag: pick|reject|none, ids?, advance?: bool} — without `ids`, the selection moves on when this takes the active photo out of the view
- `photo.flipHorizontal` Flip Horizontal (Photo): {ids?}
- `photo.flipVertical` Flip Vertical (Photo): {ids?}
- `photo.increaseFlag` Increase Flag Status (Photo › Set Flag) [Cmd+Up]: {ids?, advance?: bool} — reject -> unflagged -> pick (stops at pick); without `ids`, the selection moves on when this takes the active photo out of the view
- `photo.increaseRating` Increase Rating: {ids?, advance?: bool} — without `ids`, the selection moves on when this takes the active photo out of the view
- `photo.inspect` Inspect Photo: {id?}
- `photo.label` Set Color Label (Photo › Set Color Label): {label: red|yellow|green|blue|purple|none, ids?, advance?: bool} — without `ids`, the selection moves on when this takes the active photo out of the view
- `photo.moveToFolder` Move to Folder: {folder, ids?} — move the photos' files (default: the selection) with their XMP sidecars into `folder` on disk and relink them; virtual copies follow their master; across volumes the file is copied, verified and only then removed; never overwrites (a name taken in `folder` refuses the whole move); missing/offline and Local photos are refused; one undo step (undo moves them back) → {moved, folder}
- `photo.pasteMetadata` Paste Metadata (Photo) [Cmd+Alt+Shift+V]: {ids?, fields?: [title|caption|copyright|copyrightStatus|usageTerms|copyrightUrl|creator|location|keywords] (default: all copied)}
- `photo.pick` Flag as Pick (Photo › Set Flag) [P]: {ids?, advance?: bool} — without `ids`, the selection moves on when this takes the active photo out of the view
- `photo.rate` Set Rating (Photo › Set Rating): {rating: 0..5, ids?, advance?: bool} — without `ids`, the selection moves on when this takes the active photo out of the view
- `photo.readFocusPoints` Read Focus Points (Photo): {ids?, wait?: false} → {queued, running, last?: {total, done, found, none, unavailable, bytesRead, seconds, cancelled}} — read the camera's focus point for photos imported before it was read (Sony α1 and A7S III raws and JPEGs), from the few KB of each file that hold it, on a background job with a row in the activity stack. Without `ids`, every photo in the library not looked at yet; with `ids`, those photos, looked at again. Photos that have a point keep it. No undo step and no sidecar write. `wait: true` returns when all are read (scripts)
- `photo.readMetadataFromFile` Read Metadata from File (Photo): {ids?} — reads each photo's XMP sidecar, or embedded XMP in raw/DNG and JPEG files when no sidecar exists: metadata and develop settings, one undo step; never writes the sidecar, even with auto-write on; JPEG uses the first complete standard XMP APP1 before SOS/EOI, within 16 MiB of headers and 4096 marker/fill steps; an unreadable sidecar fails without embedded fallback → {read, failed, warnings?: [{path, code, profile?, mode?, fields?}]}
- `photo.reject` Flag as Reject (Photo › Set Flag) [X]: {ids?, advance?: bool} — without `ids`, the selection moves on when this takes the active photo out of the view
- `photo.relink` Locate Photo: {id?, path} — point a photo at its file's new location (undo never moves files)
- `photo.reload` Reload from Disk (Photo): {ids?} — re-read photos whose files changed on disk (e.g. saved by an external editor), or raws shown from their embedded preview that can be decoded now; camera fields the catalog lacks are filled in, and so is the lens data the file carries (an untouched photo then gets its lens correction turned on as import would; an edited one keeps its settings); in the app the files are read in the background (activity row `reload`, cancellable) and the reply is {background: true, count} unless `wait: true` → {reloaded}
- `photo.removeRegion` Remove Face Box: {id?, index} — remove one face / pet region (by its position in the photo's regions) from the photo in the catalog; undoable. The XMP sidecar is never rewritten for this, even with auto-write on, so reading the metadata from the file brings the region back
- `photo.rename` Rename Photos: {template: e.g. `{date}_{name}`, `Trip-{seq:3}` (tokens: {name} {num} {seq} {seq:N} {date} {date:%Y%m%d} {folder} {camera} {lens} {iso} {rating} {title} {creator} {ext}; photo.renameTokens explains each), start?: first sequence number (1), ids?} — renames the files on disk (sidecars too, never overwriting: collisions get -1, -2…); undoable
- `photo.renamePreview` Rename Preview: {template: e.g. `{date}_{name}`, `Trip-{seq:3}` (tokens: {name} {num} {seq} {seq:N} {date} {date:%Y%m%d} {folder} {camera} {lens} {iso} {rating} {title} {creator} {ext}; photo.renameTokens explains each), start?: first sequence number (1), ids?} — renames the files on disk (sidecars too, never overwriting: collisions get -1, -2…); undoable
- `photo.renameTokens` Rename Template Tags: {} → {tokens: [{tag, aliases, meaning, example}], dateDirectives: [{directive, meaning}], notes: [..], sample} — the file-name template tags shared by photo.rename, library.import (rename) and app.export (naming); examples are for a sample photo
- `photo.restore` Restore (Photo): {ids?}
- `photo.rotateLeft` Rotate Left (Photo) [Cmd+[]: {ids?}
- `photo.rotateRight` Rotate Right (Photo) [Cmd+]]: {ids?}
- `photo.saveMetadataToFile` Save Metadata to File (Photo) [Cmd+S]: {ids?} — writes each photo's XMP sidecar (metadata + develop settings) next to the original, merged into an existing one (other apps' data kept; an unreadable one is backed up first) → {written: [path], merged: [path], backups: [{path, backup}], failed}
- `photo.setCaptureTime` Edit Capture Time: {ids?, time?: `2026-09-30T14:05:00` (the active photo gets it, the others shift by the same amount), each?: bool (every photo gets `time`), shift?: seconds, hours?: time-zone shift in hours} → {changed, captured: [..], unreadable: photos skipped because their capture time can't be read}
- `photo.setMeta` Edit Info: {ids?, title?, caption?, altText?, extendedDescription?, copyright?, copyrightStatus?: unknown|copyrighted|publicDomain, usageTerms?, copyrightUrl?, creator?, location?, city?, state?, country?, gps?: "lat, lon" | [lat, lon] | null, keywords?: [..], addKeywords?: [..], removeKeywords?: [..]}
- `photo.setRegion` Resize Face Box: {id?, index, rect: {x0, y0, x1, y1}} — set one face / pet region's box (normalized, in the photo's upright frame; clamped to the photo, at least 0.5 % each way) in the catalog; undoable. Like photo.removeRegion it never rewrites the XMP sidecar
- `photo.smartPreview` Smart Preview Status: {id?} → {smartPreview: bool, originalOnline: bool}
- `photo.unflag` Unflag (Photo › Set Flag) [U]: {ids?, advance?: bool} — without `ids`, the selection moves on when this takes the active photo out of the view
- `photo.virtualCopy` Create Virtual Copy (Photo) [Cmd+']: {ids?, name?} → {ids: [new photo ids]} — a new catalog entry sharing the original file, with independent settings; stacked with its original and named `name` or "Copy N"

## pointColor

- `pointColor.delete` Delete Point Color Sample: {index}
- `pointColor.pick` Add Point Color Sample: {x, y} normalized image coords — samples the colour there (max 8); returns {index, lum, chroma, hue}

## preset

- `preset.apply` Apply Preset: {id: presetId, amount?: 0..200 (percent), ids?}
- `preset.create` Create Preset (Photo): {name, group?, groups?: [settingsGroup]}
- `preset.delete` Delete Preset: {id}
- `preset.export` Export Presets: {path, ids?: [presetId], group?: name} (default: all user presets) → {path, count}; writes a .lcpreset JSON file
- `preset.favorite` Favorite Preset: {id, favorite?: bool}
- `preset.import` Import Presets: {paths: [file or folder], group?, dryRun?} — .lcpreset, XMP presets, .lrtemplate, photos carrying edits (DNG/JPEG/TIFF "DNG presets"), Luminar looks (.lmp, .mplumpack collections) and .zip bundles of these; folders give their name as group; crs: fields mapped per docs/xmp-interop.md; local adjustment presets (Lightroom .lrtemplate, Camera Raw local .xmp, .lceffect) become mask effects (`mask.effects`; divider presets become their groups); a profile the preset names applies when it was imported with profile.import (before or after) → {imported: [{id,name,group,file,unmapped,profile: {name, id}|null}], skipped, failed, effects: [{name,group,file,unmapped}], effectDividers: [{name,group,file}]}
- `preset.move` Move Preset to Group: {id, group}
- `preset.rename` Rename Preset: {id, name}
- `preset.update` Update Preset with Current Settings: {id, groups?: [settingsGroup] (default: the groups the preset already sets)} — from the active photo

## presets

- `presets.list` List Presets: {}

## print

- `print.cell.add` Add Print Cell: {width, height, x?, y?, page?, photo?} inches; picture/custom package → {id, cell, pages}; the cell goes to the first free spot unless x and y are given
- `print.cell.delete` Delete Print Cell: {id}
- `print.cell.move` Move Print Cell: {id, x, y, snap?: bool, threshold?: inches} → {id, rect}; snap uses the guides' snap mode
- `print.cell.page` Move Print Cell to Page: {id, page: zero-based}
- `print.cell.photo` Set Print Cell Photo: {id, photo: photo id | null} (custom package: the photo printed in the cell)
- `print.cell.resize` Resize Print Cell: {id, width?, height?, x?, y?, snap?: bool, threshold?} → {id, rect}
- `print.cell.stack` Arrange Print Cell: {id, order: toBack|backward|forward|toFront} → {order: cell ids back to front}
- `print.exportPdf` Print to PDF: {path, ids?: photo ids (default selection)} → {path, pages, photos, bytes}; prints the current print.get settings; replaces an existing output, never an original
- `print.get` Print Settings: {ids?} → {settings: {layout, image, page, guides, job}, papers, pageWidth, pageHeight, printable, pageCount, cellsPerPage, gridCells?, overlaps}; lengths are inches
- `print.layout.autoLayout` Auto Layout: {} — packs the package's cells onto as few pages as possible → {pages, cells}
- `print.layout.clear` Clear Print Layout: {} — removes every cell and extra page
- `print.layout.newPage` New Print Page: {} → {page, pages}
- `print.reset` Reset Print Settings: {} → print.get
- `print.set` Set Print Settings: {layout?: {style: singleImage|contactSheet|picturePackage|customPackage, page: {paper, customWidth, customHeight, orientation: portrait|landscape, margins: {top,right,bottom,left}}, grid: {columns, rows, spacingX, spacingY, keepSquare}, spacing}, image?: {zoomToFill, rotateToFit, borderEnabled, borderWidth, borderColor: [r,g,b], strokeEnabled, strokeWidthPt, strokeColor}, page?: {background: [r,g,b], pageNumbers, pageInfo, cropMarks} (Page Options: single image and contact sheet only), guides?: {showRulers, units: in|cm|mm|pt, snap: off|cells|grid, gridSize, showMargins, showBleed, showPageGrid, showCells, showDimensions}, job?: {ppi: 72..720, color?: {profile: {kind: managed, space: srgb|adobeRgb} | {kind: icc, path}, intent: perceptual|relative, blackPointCompensation, brightness: -100..100, contrast: -100..100, sharpen: off|low|standard|high, media: matte|glossy, sixteenBit}}} — merges into the current print; cells and pages change with print.cell.* / print.layout.*; → print.get
- `print.template.apply` Apply Print Template: {name} → print.get
- `print.template.delete` Delete Print Template: {name} → print.template.list
- `print.template.export` Export Print Template: {name, path}: writes the template as a .lcprint JSON file ({format, version, name, settings}; `.lcprint` is added when the path has no extension); replaces an existing file, never an original → {name, path}
- `print.template.import` Import Print Template: {path: a .lcprint file (at most 256 KB)}: checked like a saved template (format, version, name, every setting; cell photos and guides are dropped) and added under its name; a name taken (any case) gets " (2)"… → print.template.list + {name, renamed}
- `print.template.list` Print Templates: {} → {templates: [{name, style, settings}]}
- `print.template.save` Save Print Template: {name} — saves the layout, image settings, page and job (not the cells' photos or the guides); an existing name (any case) is replaced → print.template.list

## profile

- `profile.deleteImported` Delete Imported Profile: {id: lut:…}
- `profile.favorite` Favorite Profile: {id, favorite?: bool} (toggles when omitted)
- `profile.import` Import Profiles: {paths: [.cube file, folder or .zip]} — 3D LUTs become creative profiles (Amount 0–200 %; rendered on the CPU) in the profile browser's groups (folder / zip name, else Imported) → {imported: [{id, name, group}], failed}

## profiles

- `profiles.list` List Profiles: {} — every profile (built-in, then imported LUTs marked `imported`) with its group and favourite flag
- `profiles.menu` Profile Menu: {} — favourites, recent (newest first) and groups

## redeye

- `redeye.add` Add Red Eye Correction: {center: [x,y] normalized, rx, ry: radii as fractions of the long edge, pet?: bool, pupilSize?: 0..100, darken?: 0..100} — the pupil inside is found automatically; returns {index}
- `redeye.catchlight` Pet Eye Catchlight: {index, on?: bool (default true), offset?: [dx, dy] from the pupil centre in pupil radii (default [-0.35, -0.35])}
- `redeye.delete` Delete Red Eye Correction: {index}

## segment

- `segment.model.cancel` Cancel AI Mask Model Download: {} — stop the SAM 3 download (what has arrived is kept, and a new download resumes from it) → {cancelled}
- `segment.model.download` Download AI Mask Model: {acknowledged: true} — download the SAM 3 model (about 3.4 GB, Meta's SAM License, not LightCraft's) in the background, from the configured mirrors; only after the user agreed to it. Watch segment.model.status; segment.model.cancel stops it (it resumes later) → {started, installed, downloading}
- `segment.model.status` AI Mask Model Status: {} — whether this build has AI masks, whether the SAM 3 model is installed (and where), loaded, busy, and the download's progress → {available, installed, dir, loaded, busy, analyzing, sizeBytes, license, licenseUrl, mirrors, download: {running, done, total, file, error, finished}}
- `segment.prepare` Prepare AI Masks: {} — load SAM 3 and analyze the active photo in the background, so Object clicks are instant → {busy}

## slideshow

- `slideshow.export` Export Slideshow: {format: "pdf"|"jpeg"|"video", path: the .pdf / .mp4 / .webm file, or for jpeg the folder (created if missing), size?: pdf/jpeg the long side in pixels (64–8192, default 1920), video the frame height (64–2160 or "720p"/"1080p", default 720), quality?: 1–100 (JPEG quality, default 90; video default 75), fps?: 24|25|30|60 (video, default 30), container?: "mp4"|"webm" (video, default mp4), fullScreen?: bool (pdf: open in the viewer's full screen mode, default true), speed?: 1–10 (video encoder speed, default 10 = fastest), name?: jpeg file name prefix (default the folder's name: <name>-001.jpg…), ids?: photo ids (default the photos in view, in view order), wait?: bool (run here and reply with the result)} — the photos' slides with the slideshow layout, overlays and the intro/ending screens that are on; video is AV1 (no audio), each slide held for its duration and fades rendered as frames, at most 2 hours. Runs in the background with a row in the activity stack (activity.cancel {id: taskId} stops it; nothing is left behind: files are written as .part and renamed when complete); a photo that can't be rendered is skipped with a warning → {taskId, background, format, path, slides, seconds, total, width, height, warnings}; with wait: the result (slideshow.exportStatus)
- `slideshow.exportStatus` Slideshow Export Status: {} → the last slideshow export: {taskId, format, path, running, done, total (slides, or frames for video), cancelled, result?: {format, path, width, height, slides, skipped, warnings, pages? | files? | frames, samples, keyFrames, seconds, fps, container, codec: "av1", audio: false; bytes}, error?} | {running: false} when there was none
- `slideshow.layout` Slideshow Layout Settings: {margins?: all four, marginLeft?, marginRight?, marginTop?, marginBottom?: fractions of the slide's shorter side (0–0.45; with linkMargins one sets all four), linkMargins?: bool, showGuides?: bool (margin guides in the slide editor), aspect?: "screen"|"16:9"|"4:3" (aspect preview), zoomToFill?: bool (crop the photo to fill its cell), strokeBorder?: bool, strokeColor?: "#rrggbb"|[r,g,b], strokeWidth?: fraction of the shorter side (0–0.05), castShadow?: bool, shadowOpacity?: 0–1, shadowOffset?: 0–0.1, shadowRadius?: 0–0.1 (fractions of the shorter side), shadowAngle?: degrees counter-clockwise from the right (−45 = down right), backdropColor?: colour, colorWash?: bool, washColor?: colour, washOpacity?: 0–1, washAngle?: degrees (the side the wash colour is full at), backgroundImage?: photo id|null, backgroundOpacity?: 0–1} — omitted keys keep their value, {} reads them; out-of-range numbers are clamped, wrong types refused; saved with the library → the settings
- `slideshow.overlays` Slideshow Overlay Settings: {identityPlate?: {enabled?, text?, image?: PNG/JPEG file (drawn instead of the text; "" = the text), size?: height as a fraction of the slide's shorter side (0.005–0.5), color?: "#rrggbb"|[r,g,b], opacity?: 0–1, …placement, behind?: bool (render behind the photo)}, ratingStars?: {enabled?, color?, size?: a star's height (0.005–0.15), …placement}, texts?: [text overlay] (replaces the list, at most 16; each entry merged onto the one at its index), addText?: text overlay ({} = the default "{file}"), removeText?: index, showWatermark?: bool, watermark?: text | the export watermark object {text, vertical, size, opacity, anchor, inset, color, shadow, image, imageWidth} (merged; sizes relative to the photo)} where a text overlay is {text?: template with tokens ({file}, {name}, {title}, {caption}, {date} (YYYY-MM-DD) / {date:%d.%m.%Y}, {exposure}, {shutter}, {aperture}, {focal}, {iso}, {camera}, {lens}, {rating}, {creator}, {copyright}, {folder}, {ext}; unknown tags show as typed), size?: line height (0.005–0.3), color?, opacity?, …placement, shadow?: bool, shadowOpacity?: 0–1, shadowOffset?, shadowRadius?: 0–0.05 (fractions of the shorter side), shadowAngle?: degrees counter-clockwise from the right} and the placement keys are anchor?: topLeft|top|topRight|left|center|right|bottomLeft|bottom|bottomRight, offsetX?, offsetY?: fractions of the slide's shorter side (x right, y down; −1–1), relativeTo?: "slide"|"photo" (the overlay is kept on the slide) — omitted keys keep their value, {} reads them; out-of-range numbers are clamped, wrong types refused; saved with the library; slideshow playback and slideshow.preview draw them → the settings and warnings (an unreadable identity plate image, unknown tokens)
- `slideshow.playback` Slideshow Playback Settings: {slideDuration?: seconds (0.5–120), fadeDuration?: seconds (0 = cut; at most 10 and the slide duration), fadeColor?: "#rrggbb"|[r,g,b]|null (fade through a colour instead of crossfading), randomOrder?: bool, repeat?: bool, preparePreviews?: bool (render the next slides before they are due), manual?: bool (manual slideshow: a slide stays up until ← or → changes it)} — omitted keys keep their value, {} reads them; saved with the library → {slideDuration, fadeDuration, fadeColor, randomOrder, repeat, preparePreviews, manual}
- `slideshow.preview` Slideshow Slide Preview: {id?: photo (default: the active one) | title?: "intro"|"ending", template?: a template id (slideshow.templates.list): compose with its settings instead of the library's, which don't change (the Template Browser's hover preview), width?, height?: pixels (16–4096; one given: the other from the aspect preview; neither: 1280 wide), path?: write the PNG here} — the photo's slide composed with the slideshow layout and overlays → {id, width, height, cell: [x0,y0,x1,y1], photo: [x0,y0,x1,y1] (the visible photo, slide pixels), overlays: [{kind: identityPlate|ratingStars|textN|watermark, box: [x0,y0,x1,y1]}], path | png (base64 PNG)}; with `title`, that title screen (`slideshow.titles`; drawn even while it is off) → {title, enabled, width, height, plate: [x0,y0,x1,y1] | null (the plate or text), path | png}
- `slideshow.templates.apply` Apply Slideshow Template: {id: template id | "previous" (the settings before the last apply) | name: template name (case-insensitive)} — replaces the playback (prepare previews kept), layout, overlays and titles settings with the template's and saves them with the library; there is no undo: the replaced settings are kept as "previous" for this session → {applied, name, warnings: [a background photo not in this library, an unreadable identity plate / watermark image…], previous, settings: {playback, layout, overlays, titles}}
- `slideshow.templates.delete` Delete Slideshow Template: {id: user template} — deletes its file → {deleted, name}
- `slideshow.templates.export` Export Slideshow Template: {id: template (built-in or user), path: .json file to write} → {id, name, path}
- `slideshow.templates.import` Import Slideshow Template: {path: a template .json file (at most 256 KB)} — checked like a saved one (format, version, every setting) and saved as a user template under its name (else the file's); a name taken gets " (2)"… → {id, name, builtin, group, path, renamed, warnings}
- `slideshow.templates.list` Slideshow Templates: {} → {templates: [{id: "builtin:…"|"user:…", name, builtin, group: "builtin"|"user", description?, path? (a user template's file)}], previous: bool (the settings before the last apply can be restored with apply {id: "previous"}), folder: the user templates folder | null, problems: ["file: why it was skipped"]} — built-ins first, then user templates by name (files in <settings>/slideshow-templates, at most 1000)
- `slideshow.templates.rename` Rename Slideshow Template: {id: user template, name} — its file follows the name; a name taken is refused → {id (the new one), name, builtin, group, path}
- `slideshow.templates.save` Save Slideshow Template: {name: 1–80 characters, replace?: bool (over a user template of that name)} — the current playback, layout, overlays and titles settings as a user template, <settings>/slideshow-templates/<name>.json (path separators and other reserved characters become _); a name taken (case-insensitive) or a built-in's is refused unless replace → {id, name, builtin, group, path}
- `slideshow.templates.update` Update Slideshow Template: {id: user template} — replace its settings with the current ones (name kept); built-ins can't change → {id, name, builtin, group, path}
- `slideshow.titles` Slideshow Title Settings: {intro?: screen, ending?: screen} where a screen is {enabled?: bool, color?: background "#rrggbb"|[r,g,b], content?: "none"|"identityPlate" (the Overlays identity plate, its text or image)|"text", text?: the text shown with content "text", overrideColor?: bool (draw the plate or text in textColor instead of the identity plate's colour; an image plate keeps its colours), textColor?: colour, scale?: height of the plate or text line as a fraction of the slide's shorter side (0.005–0.5; text wider than the slide shrinks to fit), duration?: seconds (0.5–120) | null (the slide duration)} — the intro plays once before the first slide, the ending after the last one when repeat is off; both fade with the playback fade; random order never moves them. Omitted keys keep their value, {} reads them; out-of-range numbers are clamped, wrong types refused; saved with the library → the settings and warnings (an unreadable identity plate image, a screen with nothing to show)

## spot

- `spot.add` Add Remove Spot: {mode?: remove|heal|clone|fill (content-aware), points: [[x,y],…], size?: fraction of long edge, feather?, opacity?, source?: [dx,dy] (default: the best match nearby)} — selects the new spot; returns {index}
- `spot.delete` Delete Spot: {index? (the selected spot)}
- `spot.findBlemishes` Find Blemishes: {sensitivity?: 0..100 (50), add?: bool (true), maxPerFace?: 1..20 (6)} — find small blemishes (darker or redder round spots on skin) on the faces of the active photo and add a heal spot on each (one undo step); needs the YuNet face detector (`faces.models.download {id: "yunet-2023mar"}`). Faces narrower than 160 px at 1600 px, and faces with more than 12 candidates (stubble, freckles, pores), get none → {faces, spots: [{x, y, size, face}], added}
- `spot.findDust` Find Dust Spots: {sensitivity?: 0..100 (50), add?: bool (true)} — find sensor-dust spots (small soft dark spots on smooth areas) and add a heal spot on each (one undo step) → {spots: [{x, y, size}], added}
- `spot.refreshSource` Refresh Source: {index? (the selected spot)} — picks the next-best source away from the current one
- `spot.select` Select Spot: {index|null}
- `spot.update` Edit Spot: {index? (the selected spot), move?: [dx,dy] (the target, normalized), source?: [dx,dy] (offset from the target), moveSource?: [dx,dy], size?, feather?, opacity?, mode?}

## stack

- `stack.auto` Auto-Stack by Capture Time: {gap?: seconds between consecutive captures (default 60), ids? (default: the selection if several photos, else the current view), preview?: bool} → {stacks, photos}
- `stack.collapseAll` Collapse All Stacks (View › Stacks): {}
- `stack.expandAll` Expand All Stacks (View › Stacks): {}
- `stack.group` Group into Stack (Photo › Stack) [Cmd+G]: {ids?, top?: photoId (default: the active photo), collapsed?: bool (default true)} — stacks the photos are already in are merged
- `stack.moveDown` Move Down in Stack (Photo › Stack): {id?} — one place away from the top
- `stack.moveUp` Move Up in Stack (Photo › Stack): {id?} — one place towards the top
- `stack.remove` Remove from Stack (Photo › Stack): {ids?}
- `stack.setTop` Set as Top of Stack (Photo › Stack) [Shift+S]: {id?} (default: the active photo)
- `stack.split` Split Stack (Photo › Stack): {id?} — this photo and the ones after it become their own stack
- `stack.toggle` Expand/Collapse Stack (Photo › Stack) [S]: {ids?, collapsed?: bool} — the stacks of the named photos (else of the selection)
- `stack.ungroup` Ungroup Stack (Photo › Stack) [Cmd+Shift+G]: {ids?}

## version

- `version.create` Create Version (Photo) [Cmd+Shift+S]: {name?}
- `version.delete` Delete Version: {index}
- `version.rename` Rename Version: {index, name}
- `version.restore` Restore Version: {index}
- `version.update` Update Version with Current Settings: {index}
