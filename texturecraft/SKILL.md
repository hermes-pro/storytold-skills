---
name: texturecraft
description: "3D texture painting with TextureCraft (Substance Painter-style): import a mesh (glTF/GLB, FBX, OBJ, STL, PLY, USD, Alembic) or use a built-in one, bake mesh maps (AO, curvature, thickness, normal from a high poly), paint PBR channels in layers with masks, apply materials and smart materials (rust, worn paint, edge wear, dirt), place decals and text, load MaterialCraft materials, render previews, and export texture sets for glTF, Unreal, Unity, Godot, Blender or OpenPBR, plus the textured mesh as GLB / OBJ / USD."
version: 0.1.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [3D, Texturing, PBR, Texture Painting, Substance Painter, Baking, Game Assets, glTF, MCP]
    related_skills: [storytold, storytold-install, materialcraft, solidcraft, photocraft, vectorcraft]
---

# TextureCraft

TextureCraft is a free, open-source 3D texture painter in pure Rust (storytold Crafting Apps), a clean-room take on
Substance Painter. An agent drives it through an MCP server (`texturecraft-cli mcp`) or one-shot CLI commands. A
project (`.tcraft`, one file) holds a mesh, one **texture set** per mesh material, and a layer stack per set that
paints PBR channels (base color, metallic, roughness, normal, height, and more). It imports glTF/GLB, FBX, COLLADA,
USD, Alembic, OBJ, PLY and STL, and exports texture maps (PNG, JPG, TGA, TIF, BMP, WebP, EXR, HDR) and the textured
mesh (GLB, OBJ + MTL, USDA/USDC/USDZ). This skill is tested against TextureCraft 0.3.2.

## When to Use

Use it to **put surface detail on an existing 3D model**:

- texturing a game or product asset: base material, worn edges, dirt in cavities, rust, scratches, painted marks
- baking mesh maps (AO, curvature, thickness, world normal, position, ID) and a normal map from a high-poly mesh
- labels, logos and text placed on a model as decals
- texture sets for an engine (glTF, Unreal packed ORM, Unity HDRP/Standard, Godot ORM, Blender, OpenPBR + MaterialX)
- a textured GLB/OBJ/USD of a model, or a quick look-dev render (real-time or path traced)

Pick a different Crafting App when:

| The job is… | Use |
|---|---|
| Designing a tileable material as a node graph (bricks, wood, stone) | `materialcraft` (then load its `.mcmat` / `.mcraft` here) |
| Modeling a part (CAD solids, holes, fillets) | `solidcraft` (export OBJ or STL, then import it here) |
| Editing a flat image (a decal's artwork, a photo texture) | `photocraft` |
| Drawing a logo for a decal | `vectorcraft` (export PNG, then `resource_import`) |

TextureCraft does not model or edit geometry, and it does not make tileable materials from scratch (fill layers take
procedurals and images, but a graph is MaterialCraft's job).

## Setup

1. If tools named `mcp_texturecraft_*` are available, use them. This is the preferred way.
2. Otherwise check for the CLI with `texturecraft-cli --version`. If it's missing, load the `storytold-install`
   skill and run its `setup texturecraft`. Then ask the user to start a new session or run `/reload-mcp`.
3. Until the MCP tools appear, use the CLI one-shots (see **CLI**).

**File access needs roots.** The headless server reaches files only below the folders it was started with:
`texturecraft-cli mcp --read-root <dir> --write-root <dir>` (`--automation-read-root` / `--automation-write-root` are
the same flags). Every MCP path is a **forward-slash path relative to the root** (`models/chair.glb`). Without roots,
file tools fail with `file access is not granted: start the server with --write-root <dir>`; absolute paths and `..`
are refused (`path rejected (absolute): \`/etc/hosts\`; use a forward-slash path relative to the workspace root`).
Ask the user (or check the `storytold-install` registration) which folder is the root.

The headless session renders on the GPU when there is one (Metal/Vulkan/DX12), else a software adapter. For the user
to watch live, they run `texturecraft --control 7878` and the server is `texturecraft-cli mcp --bridge 7878` (token
from `--token`, `TEXTURECRAFT_CONTROL_TOKEN` or the app's token file). The app then reads and writes its own files, so
the path tools are unavailable; `viewport_screenshot`, `ui_screenshot`, `ui_inspect` and `ui_menu_invoke` work only in
bridge mode (headless: `` `ui.inspect` needs the running app: start `texturecraft --control <port>` … ``). Bridge mode
was not tested here.

## Mental Model

- **Project → texture sets → layer stacks.** Each mesh material is a texture set (`ts`, an index) with a resolution
  (128–8192, power of two) and channels (`baseColor`, `metallic`, `roughness`, `normal`, `height` by default; 21 kinds).
  Each set has its own layer stack; most commands act on the active set (`textureSet.select {ts}`).
- **Layers** (integer ids): `paint` (strokes), `fill` (uniform values, procedurals or images through UV / tri-planar /
  planar / … projection), `group` (folder; smart materials are folders), instances. A **mask** (white or black
  background) holds a stack of **effects**: generators (`edgeWear`, `dirt`, `curvature`, `ambientOcclusion`…), fills,
  paint, filters, levels. Layers blend per channel (32 modes). Ids come back from every create
  (`{"layer":3}`, `{"effect":4}`); `layer.list` / `session_inspect` show the stack top to bottom.
- **New things go above the selection** and become selected. Fill colors are `"#rrggbb"` or linear `[r,g,b]`.
- **Mesh maps** are baked per set and feed generators, smart masks and smart materials. Bake before applying them.
- **Viewport space.** `paint_stroke` points are pixels in the session viewport, 1280×800, origin top-left, seen from
  the session camera. A `viewport_render` with no size is that same image, so read stroke points straight off it.
  `viewport_render {yaw, pitch}` changes the camera for that render only; `command_run camera.set {yaw, pitch}`
  moves the session camera, which strokes use.
- **Every edit is a command** (162). `command_list {filter}` or `${HERMES_SKILL_DIR}/references/commands.md` has ids
  and params; libraries (materials, smart masks, presets, filters, alphas) are in
  `${HERMES_SKILL_DIR}/references/libraries.md`. `command_run edit.undo {steps?}` undoes.

## Tools (Hermes names them `mcp_texturecraft_<tool>`)

| Tool | Use it for |
|---|---|
| `project_new {mesh?, resolution?, name?, template?}` | New project on a built-in mesh: `material_ball` (default), `sphere`, `cube`, `rounded_cube`, `cylinder`, `torus`, `plane`, `crate`. Default 1024 px |
| `mesh_import {path, resolution?}` | New project from a mesh file (default 2048 px); one texture set per material |
| `project_open {path}` / `project_save {path?}` | Open `.tcraft` (or a mesh); save `.tcraft` (appended if missing) |
| `bake {ts?, resolution?, maps?, cpu?}` | Bake mesh maps → `{baked, tracer}`; `ts:"all"` for every set |
| `bake_mesh_add {path, cage?}` | Add a high-poly mesh for the normal/height bake, or set the cage |
| `command_run {id, params}` / `command_batch {steps}` | Any engine command; a batch stops at the first error |
| `paint_stroke {points, color?, roughness?, metallic?, height?, size?, hardness?, viewport?}` | Paint on the selected paint layer (or its mask) → `{stamps}` |
| `viewport_render {view?, width?, height?, yaw?, pitch?, samples?, bounces?, cpu?}` | PNG of the 3D view or the 2D UV view (`view:"2d"`), 16–2048 px. `samples` path traces. **Look at it** |
| `session_inspect` | Everything as JSON: mesh, sets (baked maps), layers, masks, effects, painted tile counts, camera, history |
| `material_load {path}` / `material_save {path, layer?, name?}` | Add a `.tcmat` smart material, a MaterialCraft `.mcmat` or `.mcraft`; save a layer/folder as `.tcmat` |
| `resource_import {path}` | Import an image (png, jpg, tga, tif, bmp, webp, exr, hdr) → `{name}` for decals, fills, stencils, mesh maps |
| `textures_export {dir, preset?, ts?, format?, padding?, size?}` | Write the texture set(s) with a preset → `{files, warnings}` |
| `mesh_export {path, format?}` | `.glb` (textures embedded), `.obj` (+ .mtl + PNGs), `.usda` / `.usdc` / `.usdz` |
| `mesh_reimport {path?, preserveStrokes?}` | Swap in a changed mesh; `preserveStrokes` re-projects painting when UVs changed |
| `command_list {filter?}` | The catalog with `enabled` |
| `viewport_screenshot`, `ui_screenshot`, `ui_inspect`, `ui_menu_invoke` | Bridge mode only |

There are no resources or prompts. Tool errors come back as `isError` with a plain message.

## Procedure

1. **Start:** `project_new {mesh}` or `mesh_import {path}`. Check `session_inspect`: texture set names, triangle count.
   `texturecraft-cli info model.glb` reports UV problems (`uvsGenerated`, `overlapRatio`, `uvOutOfRange`) first.
2. **Bake:** `command_run bake.settings {curvatureMethod:"mesh"}` when there is no high poly (see Pitfalls), then
   `bake {resolution: 1024}` (or `ts:"all"`).
3. **Layers bottom up:** a base fill or `material.apply`, then wear and dirt on masks (`mask.add.black` +
   `effect.add.generator`, or `mask.smart.apply`), then paint layers for hand work, then decals.
4. **Look:** `viewport_render` from two or three angles (`yaw`), and `viewport.view {mode:"mask", layer}` or
   `{mode:"map:curvature"}` to check a mask or map alone. Set the view back to `material` after.
5. **Save** `project_save {path:"x.tcraft"}`, then `textures_export {dir, preset}` and/or `mesh_export`.

### Recipe: base color + worn metal edges + painted mark (tested)

```text
project_new {mesh:"rounded_cube", resolution:1024}
command_run bake.settings {curvatureMethod:"mesh"}            (no high poly: curvature from the mesh)
bake {resolution:1024}                                        → {baked:[0], tracer:["GPU (Apple M1 Max)"]}
command_run layer.add.fill {name:"Base", color:"#2f5f8f", roughness:0.35, metallic:0}       → {layer:2}
command_run layer.add.fill {name:"Worn edges", color:"#c8c8c8", roughness:0.25, metallic:1}  → {layer:3}
command_run mask.add.black                                    (on the selected layer, 3)
command_run effect.add.generator {generator:"edgeWear", level:0.6}                          → {effect:4}
command_run layer.add.paint {name:"Doodle"}                   → {layer:5}
paint_stroke {points:[[560,330],[620,360],[680,330],[740,360]], color:"#ffcc00", size:4, hardness:90}  → {stamps:139}
viewport_render {}  ·  viewport_render {width:800, height:500, yaw:-40, pitch:30}             → look
command_run viewport.view {mode:"mask", layer:3} · viewport_render · viewport.view {mode:"material"}
project_save {path:"box.tcraft"}
textures_export {dir:"box_ue", preset:"Unreal Engine (Packed)"}
    → rounded_cube_Box_BaseColor.png, rounded_cube_Box_OcclusionRoughnessMetallic.png, rounded_cube_Box_Normal.png
```

### Recipe: smart material on an imported mesh, textured GLB (tested)

```text
mesh_import {path:"ball.obj", resolution:1024}                (one texture set per OBJ usemtl: "Ball")
bake {resolution:512}
command_run material.apply {material:"steel_painted_worn"}    → {layer:10} (a folder of fills with generator masks)
command_run layer.add.paint {name:"Stripe"}                   (lands INSIDE the folder: see Pitfalls)
paint_stroke {points:[...on the mesh...], color:"#d02020", roughness:0.4, size:10}
viewport_render {width:640, height:400}  ·  viewport_render {view:"2d", width:512, height:512}   (UV layout)
project_save {path:"ball.tcraft"}
textures_export {dir:"tex", preset:"glTF PBR Metal Roughness", size:1024}
    → tex/mesh_Ball_BaseColor.png, tex/mesh_Ball_OcclusionRoughnessMetallic.png, tex/mesh_Ball_Normal.png
mesh_export {path:"export/ball.glb"}                          → {path} (textures embedded)
mesh_export {path:"export/ball.obj"}                          → .obj, .mtl, _BaseColor/_Roughness/_Metallic/_Normal PNGs
```

Library ids are in `${HERMES_SKILL_DIR}/references/libraries.md`: 72 materials (`steel`, `wood_oak`, `concrete`,
`plastic_matte`, `leather`…), 21 smart materials (`iron_rusted`, `wood_chipped_paint`, `plastic_scuffed`…),
24 smart masks (`edge_wear`, `dirt_cavities`, `dust_top`, `rust_leaks`…).

### Recipe: normal map from a high-poly mesh (tested)

```text
mesh_import {path:"ball_low.obj"}
bake_mesh_add {path:"ball_high.obj"}       → {name:"ball_high.obj", meshes:{highPoly:[{name, parts, triangles:65536}], …}}
bake {resolution:1024}
command_run viewport.view {mode:"map:normal"} · viewport_render     → the high poly's ripples show on the low poly
command_run viewport.view {mode:"material"}
```

Ray settings (`maxFrontal`, `maxRear`, `averageNormals`, matching by `lowSuffix`/`highSuffix`, AO `rays`,
`maxDistance`…) are `bake.settings` params. `bake_mesh_add {path, cage:true}` sets a cage mesh.

### Recipe: text label as a decal (tested)

```text
command_run layer.add.fill {color:"#3a3f48", roughness:0.5}
command_run resource.text {text:"TC-01", style:"Bold", color:"#ffffff"}   → {name:"Text_TC-01.png", width:716, height:241}
command_run layer.add.decal {image:"Text_TC-01.png", size:0.5}           (x, y default to the view centre)
    → {layer, decal:{center, normal, up, size:[1.49, 0.5], depth, …}}
viewport_render                                                            → the label reads left to right
```

`size` is the height in world units. Move it with `layer.decal.set {layer, offset:[right, up]}`, `rotation`, or a new
`x`/`y`. An imported logo works the same way: `resource_import {path:"logo.png"}` → its `name` → `layer.add.decal`.

### Recipe: MaterialCraft material on a model (tested)

MaterialCraft makes the material; TextureCraft lays it on the mesh as one fill layer whose channels are the cooked
maps.

```bash
materialcraft-cli new rusty_metal rusty.mcraft --size 512
materialcraft-cli run rusty.mcraft file.exportMaterial '{"path":"/abs/root/rusty.mcmat","size":512}'
```

```text
project_new {mesh:"rounded_cube", resolution:512}  ·  bake {resolution:512}
material_load {path:"rusty.mcmat"}         → {layer:3} fill "Rusty metal 1", fill.link {graph, package, params, presets}
material_load {path:"bricks.mcraft"}       (a package is cooked first: needs materialcraft-cli)
command_run material.link.cook             → {cooked:true, layer:3, size:512} (re-cook at the set's size with its mesh maps)
command_run material.link.set {id, value}  (an exposed graph input; re-cooks) · material.link.preset {name}
```

Re-cooking runs `materialcraft-cli` from `$MATERIALCRAFT_CLI`, next to the TextureCraft binary, or `PATH`; without it:
`MaterialCraft's command line (materialcraft-cli) did not start: No such file or directory (os error 2). Install
MaterialCraft next to TextureCraft or set MATERIALCRAFT_CLI`. Loading a `.mcmat` does not need it. Graph inputs named
like a mesh map (`ambientOcclusion`, `curvature`, `thickness`, `position`…) are fed the set's baked maps. The
built-in MaterialCraft templates expose no inputs (`params:[]`), so `material.link.set` was tested only for its error
(`` `material.link.set`: `Rusty metal` has no parameter `nope` ``).

### Recipe: save and reuse a smart material (tested)

```text
material_save {layer:8, path:"patina", name:"My patina"}   → {path:"patina.tcmat"}
project_new {mesh:"torus"} · bake {resolution:512}
material_load {path:"patina.tcmat"}                         → {layer:2}
```

### More building blocks

- **Fill sources** (tested): `layer.fill.set {layer, channel:"roughness", procedural:"Clouds", scale:4, low:0.3,
  high:0.7}`, `{channel, value}`, `{channel, image:<resource>}`; projection with `layer.fill.projection {projection:
  "triplanar", scale}`. Procedural names are in `libraries.md`.
- **Masks:** `mask.add.white|black`, `mask.smart.apply {name:"dirt_cavities", layer?}` (tested: adds the smart mask to
  the selected fill), `effect.add.fill {target:"mask",
  procedural:"Grunge"}`, `effect.add.levels`, `effect.add.filter {filter:"blur", radius}`; `effect.set {effect, …}`
  edits one. `effect.histogram {effect}` shows what a levels effect reads.
- **Strokes in UV space** (tested): `command_run tool.strokeUv {points:[[0.1,0.5],[0.9,0.5]]}` paints with the current
  brush and material (`tool.material {channel, color|value}`, `tool.brush {size, hardness, alpha, …}`), no camera needed.
- **Brushes:** `brush.preset.apply {preset:"rivets"}` (tested: a stroke then stamps rivets 200 % apart), alphas `tool.brush {alpha:{library:"rivet"}}`; symmetry
  `tool.brush {symmetryX:true}`.
- **Painting the far side** (tested): `command_run camera.set {yaw:214, pitch:0}`, then `paint_stroke` and
  `viewport_render` use that view.
- **Path-traced look-dev** (tested): CLI `render … --samples 64` (`wrote rusty.png (600x400, Apple M1 Max (GPU path
  tracer), 1.65 s)`) or `viewport_render {samples:64}`; GPU when it has compute shaders, else CPU. Lighting:
  `display.set {environment:"Sunset"}` (the background stays dark unless `opacity` is raised).
- **Your own mesh maps:** `resource_import` an AO or normal image, then `textureSet.meshMap.set {map, image}`.
- **Mesh changed upstream** (tested): `mesh_reimport {path:"ball.obj", preserveStrokes:true}` → `{preserved:262144}`.

## Formats

- **Mesh in:** `.glb`, `.gltf` (with its `.bin` and images beside it), `.fbx` (binary and ASCII), `.dae`, `.usd`,
  `.usda`, `.usdc`, `.usdz`, `.abc`, `.obj`, `.ply`, `.stl` (tested: OBJ, STL). One texture set per material
  (OBJ `usemtl`; STL/PLY: one set, `Default`). A mesh **without UVs gets an automatic unwrap**
  (`info` warns `the mesh has no UVs; generated an automatic unwrap with 6 charts`). UDIM tiles are detected.
  Not read: STEP, 3MF (from SolidCraft, export OBJ or STL instead).
- **Mesh out:** `.glb` (textures embedded), `.obj` + `.mtl` + PNG maps, `.usda` / `.usdc` (textures next to it),
  `.usdz` (packaged).
- **Materials in:** `.tcmat` (TextureCraft smart material), `.mcmat` (MaterialCraft portable material), `.mcraft`
  (MaterialCraft package, cooked on load), `.mtlx` MaterialX (open_pbr_surface, standard_surface, gltf_pbr) through
  `file.importMaterialX`, CLI only (MCP refuses it: it takes a path).
- **Images in:** png, jpg, tga, tif, bmp, webp, exr, hdr (`resource_import`).
- **Textures out:** `textures_export` presets: `Document channels + Normal + AO` (default: one file per channel + AO),
  `glTF PBR Metal Roughness`, `Unreal Engine (Packed)` (DirectX normal), `Unity HDRP (Mask Map)`, `Unity Standard
  (Metallic Smoothness)`, `Blender (Principled BSDF)`, `Godot 4 (ORM)`, `OpenPBR (separate maps)`, `Separate maps`,
  `Mesh maps`. `format` png/jpg/tga/tif/bmp/webp/exr/hdr, `size`, `padding` (`none`, `dilation`, `dilationDefault`,
  `infinite`). MaterialX `.mtlx` next to the maps: CLI `run <project> file.exportTextures '{"dir":"out","preset":"OpenPBR
  (separate maps)","materialX":true}'` (tested; re-imported with `file.importMaterialX`).
- **Project:** `.tcraft`, one file with the mesh, layers, baked maps and images. `new --sample` projects are large
  (40 MB for the crate at 1024 px).

## CLI (no MCP needed)

Paths are normal paths relative to the current directory; no roots.

```bash
texturecraft-cli info model.glb                                # triangles, materials, UV report
texturecraft-cli new model.obj model.tcraft --resolution 2048
texturecraft-cli new builtin:crate crate.tcraft --resolution 1024 --sample   # baked + a smart material per set
texturecraft-cli run model.tcraft material.apply '{"material":"wood_painted"}' -o model.tcraft
texturecraft-cli bake model.tcraft --resolution 2048 --maps ambientOcclusion,curvature,thickness   # saves in place
texturecraft-cli render model.tcraft view.png --size 1280x800 --yaw 30 --pitch 15 [--view 2d] [--samples 256]
texturecraft-cli export model.tcraft out/ --preset "Godot 4 (ORM)" --format png --size 2048
texturecraft-cli batch script.json                             # {"open": "builtin:sphere", "steps": [{"id","params"}], "save": "x.tcraft"}
texturecraft-cli commands --filter mask
```

All tested. `batch` stops at the first failing step, prints the results so far, then
`` texturecraft-cli batch: error: step 1 (`nope.cmd`) failed: unknown command `nope.cmd` ``, exits 1 and saves
nothing. `run` errors: `` texturecraft-cli run: error: `layer.fill.set`: unknown channel `bogus` `` (exit 1); an
unknown subcommand prints usage and exits 2. `serve` (JSON lines on stdio or a port) exists but was not tested.

## Pitfalls

- **Edge wear and curvature masks come out flat without a high poly.** Curvature is derived from the baked normal map
  by default, which is flat when there is no high-poly mesh: the curvature map is a uniform 0.5 grey and an
  `edgeWear` generator shows nothing. Run `command_run bake.settings {curvatureMethod:"mesh"}` before `bake`.
- **Bake first.** Generators, smart masks and smart materials read the mesh maps; before a bake they read neutral
  values. Re-bake after `mesh_reimport` or a resolution change.
- **`paint_stroke` only paints between points that are on the mesh.** A segment whose start or end misses the
  mesh is dropped without an error: five points across a sphere with only the middle one on it gave `{stamps:1}`.
  Read the mesh's extent off a `viewport_render` (same pixel space) and keep every point on it; check `stamps`.
- **Paint needs a paint layer:** `"Fill layer 1" is a fill layer: paint on a paint layer or on its mask`. A new fill
  layer is selected after `layer.add.fill`; add a paint layer (or a mask) before `paint_stroke`.
- **After `material.apply` / `material_load` the selection is inside the new folder**, so the next `layer.add.*`
  lands in it (selecting the folder doesn't help). Move it out: `layer.move {layer:<new>, above:<folder>}`.
- **Color names are silently ignored.** `layer.add.fill {color:"blue"}` returns `{layer}` but sets no base color
  (`sources:{}`). Use `"#rrggbb"` or linear `[r,g,b]`.
- **`material_save` doesn't create folders**: `I/O: write \`mats/patina.tcmat\` failed: No such file or directory
  (os error 2)`. `textures_export` and `mesh_export` do.
- **`resource.text` names its image `Text_<name or text>.png`** and prefixes `2_`, `3_` on a clash
  (`2_Text_label.png`). Pass the returned `name` to `layer.add.decal`, or it fails:
  `` `layer.add.decal`: no image resource `label` (import it first) ``.
- **Inverted face winding mirrors decals** (and flips the decal normal inward). Meshes must have outward,
  counter-clockwise faces; a hand-written OBJ with clockwise faces gave a mirrored label.
- **Exported file names start with the mesh file's stem, not the project name:** `mesh_Ball_BaseColor.png` for an
  imported `ball.obj` (the project keeps its copy as `mesh.obj`), `rounded_cube_Box_…` for a built-in. Rename after
  export, or save a preset with your own `file` pattern (`export.preset.save`). `export.plan {preset}` previews names.
- **`command_batch` doesn't roll back:** a failed batch is a tool error, but the steps before the failure stay
  applied (`{completed:1, failed:{index:1, id:"bogus.x", …}}`). Undo them with `edit.undo {steps}`.
- **Host-path commands are refused through `command_run`** (`file.*`, `resource.import`, `material.save/load`,
  `bake.highPoly.add`, `brush.preset.save/load`, `file.importMaterialX`, `material.link.saveSource`, any `path`/`dir`
  param): `` `file.save` with host paths is disabled for automation; use project_open, project_save, … ``. Use the
  workspace tools, or the CLI for the rest.
- `project_save {}` on a new project: `the project has no file yet: give \`path\``.
- `viewport_render` sizes are 16–2048: `render size 4000 must be 16 to 2048 pixels`. Replies cap PNGs at 5 MiB and
  batches at 256 steps.
- `viewport_render {yaw, pitch}` doesn't move the session camera; `camera.set` does, and strokes follow it.
  `viewport.frame` keeps the camera's angle.
- `project.template.save` in a headless session returns `{path:null}`: the template isn't kept.

## Verification

- `session_inspect` (or `layer.list`): the layer order, each fill's `sources`, mask effects, and `painted` tile counts
  per channel on paint layers (0 tiles = the stroke missed). `textureSet.inspect` lists the baked maps.
- `viewport_render` from more than one `yaw`, and `{view:"2d"}` for the UV layout; `viewport.view {mode:"mask",
  layer}` and `{mode:"map:<id>"}` to see one mask or mesh map. Look at every image before calling the work done.
- `textures_export` returns the `files` it wrote and `warnings`; open one or two PNGs to check them.
  `texturecraft-cli info out.glb` confirms an exported mesh reads back (triangles, materials, UVs).

## References

- `${HERMES_SKILL_DIR}/references/commands.md`: all 162 commands with params and shortcuts, grouped (layer, mask,
  effect, tool, viewport, textureSet, bake, export, material…); host-path commands are marked. Grep it
  (`grep -n '^- `effect' ${HERMES_SKILL_DIR}/references/commands.md`).
- `${HERMES_SKILL_DIR}/references/libraries.md`: materials, smart materials, smart masks, project templates, export
  presets with their packed maps, brush presets and alphas, filters, channels, mesh maps, procedurals, blend modes.
- Upstream docs: https://github.com/storytold/texturecraft/tree/main/docs (`control-protocol.md`, `features.md`).
  They track `main` and may list features newer than 0.3.2.
