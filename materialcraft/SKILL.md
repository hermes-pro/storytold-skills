---
name: materialcraft
description: "Procedural PBR material design with MaterialCraft (Substance Designer-style node graphs): tileable bricks, stone, cobblestone, tiles, wood, metal, rust, marble, fabric, ground and other surfaces built from noises, patterns, filters and weathering nodes, rendered on a sphere or cube, and exported as base color, normal, roughness, metallic, height and ambient occlusion texture maps (PNG, JPG, TGA, TIFF, EXR…, 8/16/32 bit). Opens and saves .sbs and .mcraft packages, writes .mcmat materials for TextureCraft."
version: 0.1.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Creative, 3D, Materials, PBR, Textures, Procedural, NodeGraph, Substance, GameDev, MCP]
    related_skills: [storytold, storytold-install, texturecraft, photocraft]
---

# MaterialCraft

MaterialCraft is a free, open-source node-based material designer in pure Rust (storytold Crafting Apps), a clean-room
take on Substance Designer. A **package** holds **graphs**; each graph is a network of nodes whose **output** nodes are
the material's texture maps. An agent drives it through an MCP server (`materialcraft-cli mcp`) or CLI one-shots.
Everything is procedural and tiles seamlessly. It opens and saves `.sbs` (the default) and `.mcraft` packages, exports
maps as PNG, JPG, TGA, TIFF, BMP, WebP, EXR or HDR, and writes portable `.mcmat` materials for TextureCraft.
This skill is tested against MaterialCraft 0.1.2.

## When to Use

Use it for **tileable surface materials** where you want the maps, not a picture:

- PBR texture sets for games, 3D scenes and renderers: base color, normal, roughness, metallic, height, AO (+ emissive,
  opacity, specular)
- bricks, cobblestone, stone tiles, planks, metal plates, rust, marble, lava, fabric, wicker, mossy ground, from a
  template or from scratch
- variations of one material: exposed inputs (sliders) and presets, re-exported with other values
- turning a photo or scan into maps (normal from a grayscale), with `bitmap_import`
- opening an existing `.sbs` package to inspect it, re-export it or tweak parameters

Pick a different Crafting App when:

| The job is… | Use |
|---|---|
| Painting a material onto a specific 3D model (masks, brushes, baked mesh maps, UV-aware export) | `texturecraft` |
| Retouching or editing one image (a photo, a texture you already have) | `photocraft` |
| A logo or vector illustration | `vectorcraft` |

**Hand-off to TextureCraft (tested):** write a `.mcmat` with the CLI (`materialcraft-cli run pkg.sbs
file.exportMaterial '{"path":"brick.mcmat","graph":1,"size":1024}'`), then TextureCraft's `material.load {path:
"brick.mcmat"}` adds it as a layer; its exposed inputs stay editable there and TextureCraft re-cooks it through
`materialcraft-cli`. Plain map PNGs from `outputs_export` work in TextureCraft, PhotoCraft and any engine too.

## Setup

1. If tools named `mcp_materialcraft_*` are available, use them. This is the preferred way.
2. Otherwise check for the CLI with `materialcraft-cli --version`. If it's missing, load the `storytold-install` skill
   and run its `setup materialcraft`. Then ask the user to start a new session or run `/reload-mcp`.
3. Until the MCP tools appear, use the CLI one-shots (see **CLI**).

**File access needs roots.** The server reads only below `--read-root <dir>` and writes only below `--write-root
<dir>`. Bare `mcp` has none: every file tool fails with `file access is not granted: start the server with
--write-root <dir>`. Each flag takes one folder (a second one replaces the first), and reads come **only** from the
read root, so give both the same folder: `materialcraft-cli mcp --read-root /work --write-root /work`. All paths in
tool calls are forward-slash and **relative to the root** (`maps/stone`, not `/work/maps/stone`): `path rejected
(absolute)` / `path rejected (empty, \`.\` or \`..\` component)`. The flags are `--read-root`/`--write-root` only;
`--automation-read-root` is `unknown option`.

The server is **headless**: an in-process session with a CPU renderer (no GPU needed). For the user to watch live,
they run `materialcraft --control 7878` and the server is `materialcraft-cli mcp --bridge 7878` (not tested here).
Without the app, `--bridge` exits at startup: `no control token: set MATERIALCRAFT_CONTROL_TOKEN or start the app with
\`--control 7878\` …`. The bridge-only tools (`view_screenshot`, `ui_screenshot`, `ui_inspect`, `ui_menu_invoke`,
`ui_input`) are listed in headless mode too and fail there (`\`view.screenshot\` needs the running app …`).

## Mental Model

- **The session starts with a package that already holds the sample `Brick_wall` graph (index 0).** `graph_new` adds a
  graph and opens it (index 1, 2…). `command_run file.newPackage {name}` replaces the session with a package holding
  one PBR graph `New_graph`. Saved packages include every graph; `outputs_export` and `view_render` work on the
  **open** graph (`graph.open {graph: index or name}`).
- **Nodes** have integer ids, counted per graph from 1 (a template's nodes come first: `pbr` has `pbr_base_material` 1
  and outputs 2–7). `node_add` returns `{id}`. **Ports** have ids (`input`, `foreground`, `background`, `mask`,
  `height`, `output`, `normal`, `ambient_occlusion`…); `node_connect` defaults to the first output and first input.
- **Output nodes** (`def: "output"`) are the maps: `identifier` (file name part) and `usage` (enum index: 0 base color,
  1 normal, 2 roughness, 3 metallic, 4 height, 5 ambient occlusion, 6 emissive, 7 opacity, 8 specular, 9 any).
- **Parameters** are set by id: numbers, `[x, y]`, enum **indices**, colors as sRGB `"#rrggbb"` (stored linear;
  `[r,g,b,a]` arrays are linear), curves `[[x, y], …]`, gradients `[[pos, "#rrggbb"], …]`. Ids and defaults are in
  `${HERMES_SKILL_DIR}/references/nodes.md`.
- **Graph size** is a power of two, 16–8192 (`graph_new {size}`, default 1024). Editing cooks at the preview size (512);
  `outputs_export` and `view_render {full:true}` cook at full size. Default output format is 16 bit (`u16`).
- **Exposed inputs** (`graph.exposed.add {id, default, min, max, bind:{node, param}}`) are the material's sliders;
  presets store their values. They survive `.sbs` and `.mcmat`, and the CLI sets them with `--set id=value`.
- Everything else (selection, frames, comments, rename, duplicate, undo, view settings) is a command: `command_run
  {id, params}` / `command_batch {steps}`. 68 commands in `${HERMES_SKILL_DIR}/references/commands.md`.

## Tools (Hermes names them `mcp_materialcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `graph_new {template?, name?, size?}` | New graph from a template, opened. Templates: `empty`, `pbr` (default: six outputs fed by one `pbr_base_material`), `bricks`, `stone_tiles`, `wood`, `metal_plates`, `rusty_metal`, `lava`, `marble`, `wicker`, `fabric`, `ground`. Returns `{graph, name}` |
| `library_list {filter?, category?}` | Node definitions with ports and params (222 nodes). Grep `references/nodes.md` first |
| `node_add {def, params?, at?, connectFrom?: {node, port?}}` | Add a node (and wire `connectFrom`'s output into its first input). Returns `{id}` and selects it |
| `node_connect {from, to, fromPort?, toPort?}` | Wire an output into an input (replaces what fed it) |
| `node_param {id, param, value}` | Set one parameter. Needs a selection (see Pitfalls) |
| `session_inspect` | Package, graphs, the open graph's nodes (params, `cooked` {error, mean, size, ms}), connections, exposed inputs, presets, views, history |
| `view_render {view?, scene?, width?, height?, node?, port?, yaw?, pitch?, tiling?, full?, hq?, displacement?}` | PNG returned inline. `3d` (default) on `rounded_cube`, `cube`, `sphere`, `cylinder`, `plane`, `torus`, `material_ball`; `hq` adds displacement, AO and shadows. `view:"2d", node:<id>` shows one node's output. Max 2048 px a side. **Look at it** |
| `outputs_export {dir, format?, depth?, pattern?, graph?}` | Cook at full size and write every output. `pattern` uses `$(graph)`, `$(identifier)`, `$(usage)` |
| `package_open {path}` / `package_save {path?}` | `.sbs`, `.mcraft` (and a `.mcmat`'s source). Save is SBS unless the path ends `.mcraft`; `.sbs` is appended otherwise |
| `bitmap_import {path, name?}` | Embed an image as a resource; returns its `name` (the file stem) for a `bitmap` node's `resource` |
| `command_list {filter?}` / `command_run {id, params?}` / `command_batch {steps}` | Every other command. A batch stops at the first error: `{completed, results, failed: {index, id, error}}` |
| `view_screenshot`, `ui_*` | Bridge mode only |

## Procedure

1. **Start from a template** when one is close (`graph_new {template:"stone_tiles"}`), and `session_inspect` to learn its
   node ids. Otherwise `graph_new {template:"pbr", name, size}` and build.
2. **Height first.** Shape the surface as one grayscale height map (generators from Patterns/Noises, combined with
   `blend`, `height_blend`, `levels`, `slope_blur`, `warp`). Everything else derives from it.
3. **Derive the maps:** `height_normal_ao` (normal + AO in one node) or `normal` + `ambient_occlusion`; color with
   `gradient_map` on the height or a mask; roughness with `levels` (inverted ranges are fine); weathering with
   `dirt_mask`, `edge_wear`, `rust`, `moss`, `leaks`.
4. **Wire into the output nodes** (`node_connect {from, fromPort, to:<output id>}`).
5. **Look.** `view_render {scene:"sphere"}` after each step, `view_render {view:"2d", node}` for one map,
   `session_inspect` for cook errors. `hq:true, full:true` for the final check.
6. **Export** `outputs_export {dir, depth:8}` (or 16 for height/normal), then **save** `package_save {path:"x.sbs"}`.

### Recipe: stone from scratch on the PBR template (tested)

```text
graph_new {template:"pbr", name:"Stone", size:1024}     → {graph:1}; outputs 2 basecolor … 7 ambientocclusion
node_add {def:"stones", at:[-600,0], params:{scale:5, gap:0.04, height_random:0.5}}   → 8
node_add {def:"clouds_2", at:[-600,200], params:{scale:32}}                           → 9
node_add {def:"blend", at:[-400,100], params:{mode:4, opacity:0.15}}                  → 10  (4 = Add Sub)
node_connect {from:9, to:10, toPort:"foreground"} · node_connect {from:8, to:10, toPort:"background"}
node_add {def:"height_normal_ao", connectFrom:{node:10}, params:{normal_intensity:3, ao_spread:0.1}}   → 11
node_add {def:"gradient_map", connectFrom:{node:10}}                                  → 12
node_param {id:12, param:"gradient", value:[[0,"#2b2622"],[0.5,"#6b625a"],[1,"#a59b8e"]]}
node_add {def:"levels", connectFrom:{node:10}, params:{out_low:0.95, out_high:0.6}}   → 13  (rough gaps, smoother tops)
node_connect {from:12, to:2} · {from:11, fromPort:"normal", to:3} · {from:13, to:4}
node_connect {from:10, to:6} · {from:11, fromPort:"ambient_occlusion", to:7}         (metallic stays 0 from node 1)
view_render {scene:"sphere", width:640, height:640}  ·  view_render {view:"2d", node:2}
view_render {scene:"sphere", full:true, hq:true, width:800, height:800}
outputs_export {dir:"stone_maps"}   → stone_maps/Stone_basecolor.png … Stone_ambientocclusion.png (1024², 16 bit)
package_save {path:"stone.sbs"}  ·  package_save {path:"stone.mcraft"}
```

Reopened with `package_open {path:"stone.sbs"}` (it opens on graph 0: `command_run graph.open {graph:"Stone"}`) and
re-exported: `outputs_export {dir:"stone8", format:"jpg", depth:8, pattern:"$(graph)_$(usage)"}` →
`Stone_baseColor.jpg`, `Stone_normal.jpg`… (tested).

### Recipe: brick template with a slider and a preset (tested)

```text
graph_new {template:"bricks", name:"RedBrick"}     (1, 2 brick_generator · 6 edge_damage · 13 gradient_map · 19–24 outputs)
command_run graph.select {ids:[1]}                  (node_param needs a selection)
node_param {id:1, param:"bricks_x", value:3} · node_param {id:2, param:"bricks_x", value:3}   (keep both generators in step)
command_batch {steps:[
  {id:"graph.node.param", params:{id:13, param:"gradient", value:[[0,"#3a1a10"],[0.6,"#7a3520"],[1,"#a5583a"]]}},
  {id:"graph.exposed.add", params:{id:"wear", label:"Wear", default:0.6, min:0, max:1, bind:{node:6, param:"amount"}}} ]}
command_run graph.exposed.set {id:"wear", value:1.0}  ·  command_run graph.preset.save {name:"Worn"}
view_render {scene:"rounded_cube", hq:true, width:600, height:600}  ·  view_render {view:"2d", node:20}   (normal map)
outputs_export {dir:"brick", depth:8}  ·  package_save {path:"brick.sbs"}
```

The CLI then renders or exports other values without editing: `materialcraft-cli render brick.sbs worn.png --graph 1
--set wear=0.1` (tested).

### Recipe: maps from a photo (tested)

```text
bitmap_import {path:"photo.png"}                     → {name:"photo"}   (use the name, not the file name)
graph_new {template:"empty", name:"Photo", size:256}
node_add {def:"bitmap", params:{resource:"photo"}}                       → 1
node_add {def:"output", connectFrom:{node:1}, params:{identifier:"basecolor", usage:0}}
node_add {def:"grayscale_conversion", connectFrom:{node:1}}              → 3
node_add {def:"normal", connectFrom:{node:3}, params:{intensity:4}}      → 4
node_add {def:"output", connectFrom:{node:4}, params:{identifier:"normal", usage:1}}
view_render {view:"2d", node:4}  ·  outputs_export {dir:"photo", format:"exr", depth:32}
```

To make a photo tile first, put `make_it_tile` after the bitmap. Clean the photo up in `photocraft` before importing.

### Recipe: portable material for TextureCraft (tested)

```bash
materialcraft-cli run brick.sbs file.exportMaterial '{"path":"brick.mcmat","graph":1,"size":512,"values":{"wear":0.2}}'
texturecraft-cli batch tc.json   # {"open":"builtin:sphere","steps":[{"id":"material.load","params":{"path":"/abs/brick.mcmat"}}],"save":"/abs/tc.tcraft"}
```

The `.mcmat` is a zip: `material.json` (maps with usage and colour space, exposed `parameters` with current
values, `presets`, graph `inputs`), `maps/<usage>.png` (base color 8-bit sRGB, the rest 16-bit linear; normals OpenGL
Y+), `source.mcraft`. Over MCP it can't be written (`file.exportMaterial` with host paths is disabled), but
`package_open` reads one. `file.sendToTextureCraft` (writes into `Documents/TextureCraft/library`) was not tested.

Also tested: `view.3d {scene:"material_ball", environment:"sunset", exposure:0.3}` then `view_render` (the settings
stick for later renders), `graph_new {template:"rusty_metal", size:2048}` + 2048² export, `file.newPackage`,
`edit.undo`, `library_list {filter}` / `{category}`, `command_list {filter}`.
Not tested: the bridged app, `serve`, function graphs (`graph.node.function`, `pixel_processor`), sub-graphs
(`graph.createFromSelection`, `graph_instance`), FX-Map, `svg`/`text` nodes, graph input nodes fed by TextureCraft mesh
maps (`graph.input.bind {identifier, resource}`), and `.sbs` files written by other programs.

## Formats

- **Packages:** `.sbs` (default save; XML), `.mcraft` (MaterialCraft's own, a zip). `package_open` also takes a
  `.mcmat` (opens its source). An SBS from another program reports what it couldn't read in `package.warnings`
  (unknown nodes are kept as placeholders) and opens with no file name: save needs a `path`.
- **Maps:** `outputs_export` → png (default), jpg, tga, tif, bmp, webp, exr, hdr at `depth` 8, 16 or 32 (default: the
  graph format, 16-bit). Base color and normal come out RGBA, the others grayscale. JPG is always 8-bit (`depth:16` is
  ignored). Default names `$(graph)_$(identifier)` → `Stone_basecolor.png`; `$(usage)` gives `baseColor`,
  `ambientOcclusion`.
- **Normals** are OpenGL (Y+) by default; `normal {format:1}` gives DirectX.
- **Images in:** `bitmap_import` takes png, jpg, tga, tif, bmp, webp, exr, hdr; the package embeds them.
- **`.mcmat`** (portable material for TextureCraft): CLI `file.exportMaterial` only.

## CLI (no MCP needed)

```bash
materialcraft-cli new marble marble.sbs --size 512 --name Marble     # package with one graph from a template
materialcraft-cli info marble.sbs                                     # session JSON: graphs, nodes, cook results
materialcraft-cli render marble.sbs marble.png --size 512x512 --scene sphere --hq   # also --view 2d --node <id>
materialcraft-cli export marble.sbs maps --format png --depth 8 --pattern '$(graph)_$(usage)'
materialcraft-cli export brick.sbs out --graph 1 --set wear=0.7       # an exposed input set first
materialcraft-cli cook marble.sbs                                     # per-node timings and errors
materialcraft-cli run pkg.sbs graph.size '{"width":2048,"height":2048}' -o big.sbs
materialcraft-cli batch steps.json      # {"open":"sample","steps":[{"id","params"}…],"save":"out.mcraft"}
materialcraft-cli nodes --filter noise  ·  materialcraft-cli commands --filter preset
```

`sample` as input is the built-in brick wall. CLI paths are ordinary host paths (no roots). Errors exit 1:
`materialcraft-cli: --set nope: \`graph.exposed.set\`: no input \`nope\``, `no graph 7`, `unknown command \`bogus\``.
`batch` stops at the first error (`the batch stopped at an error`). CLI packages from `new` hold only that graph.

## Pitfalls

- **Node edits need a selection, even with an `id`.** Right after `graph_new` from a template or `package_open`,
  `node_param` and every other node command (`graph.node.rename`, `graph.node.base`, `graph.node.bind`, `edit.delete`…)
  fail with `\`graph.node.param\` is not available: no node is selected`. `node_add` selects the new node, so it works
  after one; otherwise run `command_run graph.select {ids:[<any node>]}` first. `edit.selectNone` brings it back.
- **The sample graph rides along.** The MCP session starts with `Brick_wall` as graph 0, so a saved package holds it
  too. Start with `command_run file.newPackage {name}` for a clean package (it still has one `New_graph`, PBR).
- **`package_open` opens graph 0**, not the one you worked on: `command_run graph.open {graph:"Stone"}` before
  rendering or exporting.
- **Cook errors are silent.** A broken node still renders, in magenta (mean `[1,0,1]`), and the call returns `ok`.
  Check `session_inspect` → `graph.nodes[].cooked.error`, e.g. `no bitmap resource \`photo.png\`` (the resource is
  named `photo`).
- **Silent fallbacks:** `graph_new {template:"nope"}` makes an empty graph named `Graph`; a size that isn't a power of
  two gives 512×512; `view_render {scene:"bogus"}` renders the rounded cube; `width` over 2048 is cut to 2048.
  Parameter values outside the documented range are stored as given (`scale: 1000` on a 1..256 param).
- **Template generators come in pairs.** `bricks` has two `brick_generator`s (1 height, 2 color variation); change
  `bricks_x`/`bricks_y` on both or the color stops matching the shapes.
- **Commands with host paths are refused over MCP:** `\`file.save\` with host paths is disabled for automation; use
  package_open, package_save, bitmap_import or outputs_export` (also `file.exportMaterial`, `file.importBitmap`,
  `view.3d.loadMesh`, `graph.input.bind {path}`). Use the tools, or the CLI for `.mcmat`.
- `package_save {}` on a new package: `the package has no file yet (new, or opened from another program): give a \`path\``.
- Errors name the problem: `\`graph.node.add\`: unknown node \`perlin\``, `\`perlin_noise\` has no parameter \`bogus\``,
  `\`scale\` takes a float`, `no node 999`, `no input \`nope\` on node 2 (has [])`, `no output \`x\` on node 8 (has
  ["output"])`, `node 9999 has no cooked output`.

## Verification

- `session_inspect`: every node's `cooked.error` is `null`; outputs have sensible `cooked.mean` (normal ≈ `[0.5,0.5,1]`,
  metallic 0 for non-metals); `exposed` and `presets` hold what you added.
- `view_render` on a sphere (and `hq:true, full:true`) and look: no magenta, no visible tiling seams with `tiling:2`
  or `scene:"plane"`, normals and height agree with the color.
- `outputs_export` lists every file; check sizes and bit depth (`file maps/*` shows `1024 x 1024, 16-bit`).
- `materialcraft-cli info out.sbs` confirms a saved package reopens with its graphs.

## References

- `${HERMES_SKILL_DIR}/references/nodes.md`: all 222 nodes by category with ports, params, defaults, ranges and enum
  indices. Grep it (`grep -n '^- \`height_blend\`' …`, `grep -n 'Weathering' …`).
- `${HERMES_SKILL_DIR}/references/commands.md`: all 68 commands with params.
- Upstream docs: https://github.com/storytold/materialcraft/tree/main/docs (`control-protocol.md` covers MCP, the
  function-graph ops and the `.mcmat` format). They track `main` and may list features newer than 0.1.2.
