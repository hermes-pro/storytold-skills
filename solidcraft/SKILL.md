---
name: solidcraft
description: "Parametric 3D CAD with SolidCraft (Fusion 360 / SolidWorks-style): mechanical parts, brackets, mounting plates with hole patterns, flanges, bushings, enclosures and cases, 3D-printable parts, assemblies with joints. Parameters and expressions, sketches with dimensions, extrude / revolve / hole / fillet / chamfer / shell / pattern / mirror, measure volume and mass, change a size and rebuild, then export STEP, STL, 3MF, OBJ or URDF and save .sc designs."
version: 0.1.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [CAD, 3D, Parametric, Mechanical, Engineering, 3D Printing, STEP, STL, 3MF, MCP]
    related_skills: [storytold, storytold-install, cadcraft, gridcraft, vectorcraft]
---

# SolidCraft

SolidCraft is a free, open-source parametric 3D CAD app written in Rust (Tangency Labs, Apache-2.0/MIT,
`github.com/tangency-labs/solidcraft`; it is not in the storytold org but works like the Crafting Apps). An agent
drives it through an MCP server (`solidcraft-cli mcp`) or CLI one-shots. A design is a timeline of features
(sketches, extrudes, fillets, holes, patterns…) driven by named parameters, so changing one number rebuilds the
part. It opens .sc designs (and .solidcraft from older releases), STEP/IGES, 3MF/STL/OBJ/glTF meshes and DXF/SVG
drawings, saves .sc (or plain .json), and exports STEP, STL, 3MF, OBJ and URDF.
This skill is tested against SolidCraft 0.30.1.

## When to Use

Use it for **solid parts with real dimensions**, for manufacturing or 3D printing:

- brackets, plates with hole patterns, flanges, bushings, spacers, standoffs, knobs, enclosures and lids
- parts that must follow parameters ("make it 20 mm longer", "six bolt holes instead of four")
- checking volume, mass (by material), bounding box and hole positions before printing or machining
- opening a STEP or STL file to measure, section, picture or convert it
- assemblies with joints and motion (see the bundled `solidcraft-mechanisms` skill below), sheet metal, surfaces

Pick a different Crafting App when:

| The job is… | Use |
|---|---|
| A 2D drawing: floor plan, dimensioned sheet, DXF/DWG for a laser cutter | `cadcraft` |
| A bill of materials or cost sheet for the parts | `gridcraft` |
| A logo or icon (looks, not measurements) | `vectorcraft` |

SolidCraft can hand a 2D view to CADCraft: `file.export_view_dxf` (recipe below) or `sheet.flat_pattern` DXF.

## Setup

1. If tools named `mcp_solidcraft_*` are available, use them. This is the preferred way.
2. Otherwise check for the CLI with `solidcraft-cli --version`. If it's missing, load the `storytold-install`
   skill and run its `setup solidcraft`. Then ask the user to start a new session or run `/reload-mcp`.
3. Until the MCP tools appear, use the CLI one-shots (see **CLI**).

**Headless or live.** `solidcraft-cli mcp` looks for a running SolidCraft app (the app opens its control channel on
`127.0.0.1:27878` by default and writes the port and a token where the server finds them). With no app it runs a
headless in-process session with a GPU (or CPU) renderer, and every reply ends with
`Note: this is a headless session because the SolidCraft app was not found; the user cannot see this work. …`.
While the headless session has no features, the next call connects to the app if the user has started it since.
`--headless` forces headless (and drops the note); `--connect 127.0.0.1:PORT [--token T]` names an app started with
`solidcraft --control PORT`. The live (bridged) mode was not tested here. Bridged, `screenshot` defaults to the app
window and `view` turns the user's camera: pass `source:"model"`, and ask before `new_design` or `open` (they
discard the user's unsaved design).

**File access.** Tool calls only read and write inside the server's folders: SolidCraft's recovery folder, a private
temp scratch folder, the folders of designs opened or saved in the session (inside the home folder, not hidden), and
each `--allow-path DIR`. Anything else fails with
`<path>: outside the folders this agent may use (<folders>); allow another folder with \`--allow-path DIR\``.
Bare `mcp` makes **no ordinary folder writable**, so the first `save`/`export` must go to an `--allow-path`
folder. `storytold-install` registers the server with `--allow-path <home folder>` and `--param-check strict`
(`STORYTOLD_SOLIDCRAFT_ROOT` changes the folder). If a path is refused, ask the user to add `--allow-path <folder>` to the server's args (or `--allow-any-path`)
and reload; don't try to get around it. A missing `--allow-path` folder is dropped silently. The `initialize`
stderr line lists the folders. Use absolute paths (`rel.stl` is refused, not resolved).

**Parameter checking.** `--param-check warn|strict` checks the 103 commands with typed contracts (`[typed]` in the
catalog). Without it a misspelt key is ignored: `solid.box {…, operaton:"cut"}` quietly made a new body. `warn` adds
`param_warnings: ["unknown key \`operaton\`; did you mean \`operation\`?"]`; `strict` refuses the call with
`invalid parameters for \`solid.box\`: unknown key \`operaton\`; did you mean \`operation\`?`.

## Mental Model

- **Millimetres, degrees, Z up.** Any numeric field can be an expression with units and parameters: `"L/2 - inset"`,
  `"1 in"`, `"30 deg"`. Functions: `sqrt abs min max floor ceil round mod sin cos atan2 hypot pi …` (no `if`).
- **Parameters** (`parameters.add {name, expression, unit?, comment?}`) drive everything. A plain number never
  follows a parameter; an expression does. Every sketch dimension and feature input also becomes a parameter
  (`d1`, `d2`…; `parameters.list {filter:"feature"}`).
- **Timeline.** Features run in order; each has a `name` (give one, unique) and an `error`/`warning`
  (`inspect_design`). Change a feature with `timeline.edit {feature, set}` or its `dN` parameter, not by rebuilding.
- **Bodies** are named `Body1`, `Body2`… unless `body_name` is given. Feature replies list `created_bodies`,
  `changed_bodies`, `removed_bodies`: a cut with `changed_bodies: []` missed.
- **Sketch planes:** `XY` (x→+X, y→+Y), `XZ` (x→+X, **y→−Z**), `YZ` (x→+Y, y→+Z); `offset:"T"` moves the plane
  along its normal. Sketch ids count per sketch: `l1`, `c1`, `a1`, `p1`, `c1.center`, `"origin"`. Every sketch
  should end at `dof: 0` (`sketch.solve`). Points given as expressions (`["L","-T"]`) are fixed there and follow.
- **Picks are world points.** `edges:[[x,y,z]]`, `faces:[[x,y,z]]` snap to the nearest edge/face (plain numbers only)
  and then follow it when parameters change. One pick takes a whole tangent chain.
- **Primitives skip sketches:** `solid.box`, `solid.cylinder`, `solid.hole` take expression fields and
  `operation: new|join|cut|intersect`. Sketch when the profile is not a box or a circle.
- **570 commands** (`references/commands.md`); 21 MCP tools wrap them.

## Tools (Hermes names them `mcp_solidcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `batch {commands:[{command, params}], verbose?, expect?, coalesce_parameters?}` | The main build tool: steps in order, all-or-nothing (the reply names `failed.index` and `failed.error`). A step may also be `set_parameter`, `measure`, `save`, `export`, `open`, `new_design`, `undo`… |
| `execute {command, params, verbose?, expect?}` | One command |
| `expect {volume_mm3, tol?, bodies?, bbox?}` (on `batch`/`execute`) | Your computed numbers; the reply's `expectation` has `ok`, `measured`, `mismatch`; a mismatch is an error (design kept). `tol` is relative (default 0.002), bbox within 0.05 mm |
| `measure {body?, items?, summary?}` | Volume, area, COM, bbox, faces per body; `summary:true` is short. `items` measures faces/edges: diameters, distances, angles |
| `body_topology {body, faces?:"cylinders"}` | Where holes and bosses are: each cylinder's `origin`, `axis`, `radius`, `extent`. Full form (edges, face names) is 25–45 KB |
| `set_parameter {name, value}` | Change or create a parameter and rebuild; reply has `errors` |
| `check_parameters {set:{name:value}, report?}` | Try values, report volume/errors/cylinders, put the design back (`restored: true`) |
| `inspect_design {measure?, sketches?}` | Parameters, timeline with errors, bodies, sketches. Use `{measure:false, sketches:false}` (≈4 KB) |
| `screenshot {view?, camera?, width?, height?, path?, grid?, axes?, source?}` | PNG returned inline (and written to `path`). **Look at it.** Views: iso, top, front, back, left, right, bottom |
| `compare_picture {reference, view?, crop_px?, fit?}` | Outline overlap of the model against a reference photo/render (holes not compared) |
| `export {path, format?, bodies?}` | `.step`/`.stp`, `.stl` (binary; `format:"stla"` ASCII), `.3mf`, `.obj`, `.urdf` |
| `save {path?}` / `open {path, up?}` / `new_design` | `.sc` design (`.json` path = plain JSON). `open` takes .sc, STEP, 3MF/STL/OBJ/glTF (replaces the design) |
| `list_commands {filter}` / `describe_command {id}` | Look up commands. **Never unfiltered** (over 100 KB); grep the catalog instead |
| `skill_reference {skill, file?}` | SolidCraft's own agent skills (below) |
| `undo`, `redo`, `pending`, `running`, `crash_reports` | History; long calls in bridged mode; crash reports |

`undo` takes back one step (one feature: a sketch made in the same batch stays). Resources: `solidcraft://design`,
`solidcraft://commands`. Bad tool arguments are JSON-RPC `-32602`; a failed command is `isError` with the engine's
message, and the design is left unchanged.

**Bundled skills.** `skill_reference {skill:"solidcraft-modeling"}` returns SolidCraft's own command reference
(plane axes, id counting, hole/pattern/mirror shapes, error table); `file:"SKILL.md"` its workflow. Also
`solidcraft-editing` (SKILL.md: change an existing design via `dN` parameters, checkpoints),
`solidcraft-mechanisms` (assemblies, joints, motion; SKILL.md and reference.md) and `solidcraft-checking`
(parameter-range walks, STEP comparison; SKILL.md, `reference/porting.md`). Read the mechanisms one before any
assembly work: this skill does not cover joints.

## Procedure

1. `inspect_design {measure:false, sketches:false}`, even in a new session. If it has features (bridged), ask
   before `new_design`.
2. **Plan in numbers:** parameters, the part centred on the origin (or on a corner if that's simpler), each
   feature with the world point of every edge/face pick, and the expected volume and bbox after each stage.
3. **Build in 2–4 `batch` calls** with `verbose:false` and `expect`: (1) parameters + sketch + first solid,
   (2) fillets and shell, (3) holes, cuts, patterns. A risky step (a boolean between curved faces) goes alone.
4. **Check:** `expect` ok, `body_topology {faces:"cylinders"}` for hole positions, `inspect_design` errors null.
5. **Parametric test:** `check_parameters {set:{L:"120 mm"}}` or `set_parameter`, then measure against your number.
6. **Look:** `screenshot {view:"iso", width:800, height:560, axes:false}`; `view:"top"` for holes and inner features.
7. **Deliver** with absolute paths in an allowed folder: `save {path:"/abs/part.sc"}`, `export` `.step` for CAD,
   `.stl`/`.3mf` for printing.

### Recipe: parametric plate with 4 counterbored holes (tested)

```text
batch {verbose:false, expect:{volume_mm3:23335.2, tol:0.001, bodies:1, bbox:{min:[-40,-25,0], max:[40,25,6]}}, commands:[
  parameters.add {name:"L", expression:"80 mm"}   (+ W 50 mm, T 6 mm, inset 8 mm)
  sketch.create {plane:"XY", name:"PlateSketch"}
  sketch.draw.dimensioned {command:"sketch.rectangle.center", params:{center:[0,0], corner:[40,25]},
                           dimensions:{width:"L", height:"W"}}
  sketch.finish {}
  solid.extrude {distance:"T", name:"Plate"}
  solid.fillet {edges:[[40,25,3],[-40,25,3],[40,-25,3],[-40,-25,3]], radius:5, name:"Corners"}
  sketch.create {plane:"XY", offset:"T", name:"HolePts"}
  sketch.point {point:[32,17]}
  sketch.dimension {entities:["origin","p1"], type:"horizontal", value:"L/2 - inset"}
  sketch.dimension {entities:["origin","p1"], type:"vertical", value:"W/2 - inset"}
  sketch.finish {}
  solid.hole {sketch:"HolePts", diameter:3.4, type:"counterbore", cb_diameter:6.5, cb_depth:3.3, name:"Hole"}
  solid.pattern.rectangular {features:["Hole"], dir1:[-1,0,0], count1:2, spacing1:"L - 2*inset",
                             dir2:[0,-1,0], count2:2, spacing2:"W - 2*inset", name:"Holes"} ]}
     → expectation.ok, measured 23335.19 mm³, 22 faces
body_topology {body:"Body1", faces:"cylinders"}   → bores r 1.7 at (±32, ±17), corner rounds r 5
check_parameters {set:{L:"120 mm"}}                → holes at x ±52, restored: true
set_parameter {name:"L", value:"120 mm"}           → errors: [], measure → 35335.2 mm³, bbox x ±60
screenshot {view:"top", width:800, height:560}     → look: four counterbores in the corners
save {path:"/abs/plate.sc"} · export {path:"/abs/plate.step"} · .stl · .3mf
```

Volume check: `L*W*T − 4r²(1−π/4)T − 4(π·1.7²·(T−3.3) + π·3.25²·3.3)`.

### Recipe: L-bracket from a sketch profile, fillet, chamfer, holes (tested)

```text
batch {verbose:false, expect:{volume_mm3:14250, bodies:1, bbox:{min:[0,-15,0], max:[60,15,40]}}, commands:[
  parameters.add L 60 mm, H 40 mm, W 30 mm, T 5 mm
  sketch.create {plane:"XZ", name:"ProfileSketch"}          (sketch y = −Z: draw upward with negative y)
  sketch.line {points:[[0,0],["L",0],["L","-T"],["T","-T"],["T","-H"],[0,"-H"]], closed:true}   → dof 0
  sketch.finish {}
  solid.extrude {distance:"W", direction:"symmetric", name:"Bracket"} ]}
batch {verbose:false, expect:{volume_mm3:14029.41, bodies:1}, commands:[
  solid.fillet {edges:[[5,0,5]], radius:4, name:"InnerFillet"}         (inside corner, edge along Y)
  solid.chamfer {edges:[[0,0,40]], distance:1.5, name:"TopChamfer"}
  solid.hole {position:["L - 12",0,"T"], clearance:"M5", name:"BaseHole"}    (5.5 mm, through the base)
  solid.hole {position:[0,0,"H - 15"], clearance:"M6", name:"WallHole"} ]}   (6.6 mm, into the face at x=0)
set_parameter {name:"H", value:"50 mm"}   → measure 15529.5 mm³ (+1500), body_topology: WallHole moved to z 35
screenshot {view:"iso", axes:false} · screenshot {camera:{target:[30,0,20], yaw:-2.4, pitch:0.5, distance:150}}
```

`clearance:"M5"` uses ISO 273 normal fit (`fit: close|normal|loose`); `thread:"M6"` makes a tapped hole.

### Recipe: revolved flanged bushing with a bolt circle (tested)

```text
batch {verbose:false, expect:{volume_mm3:6672.74, bodies:1, bbox:{min:[-16,-16,0], max:[16,16,20]}}, commands:[
  parameters.add bore_r 5, hub_r 10, flange_r 16, flange_t 4, H 20 (mm)
  sketch.create {plane:"YZ", name:"Section"}                (sketch x = +Y, y = +Z: the half section)
  sketch.line {points:[["bore_r",0],["flange_r",0],["flange_r","flange_t"],["hub_r","flange_t"],
                       ["hub_r","H"],["bore_r","H"]], closed:true}
  sketch.finish {}
  solid.revolve {axis:"Z", name:"Bushing"} ]}                       → 6672.03 mm³ (0.01 %)
batch {verbose:false, expect:{volume_mm3:6497.10, bodies:1}, commands:[
  solid.chamfer {edges:[[0,10,20]], distance:1, name:"TopChamfer"}   (a point on the circular edge)
  parameters.add {name:"bcd", expression:"26 mm"} · parameters.add {name:"n", expression:"4", unit:""}
  solid.cylinder {diameter:3.4, height:"flange_t + 2", base:["bcd/2",0,-1], operation:"cut", name:"BoltHole"}
  solid.pattern.circular {features:["BoltHole"], axis:"Z", count:"n", name:"BoltHoles"} ]}
check_parameters {set:{n:"6"}, report:["measure","errors"]}   → 6424.3 mm³ (two more holes), restored
execute inspect.section {plane:"XZ", flip:true} · screenshot {view:"front", grid:false, axes:false}
```

Start a cutter 1 mm outside the faces it pierces (`base z −1`, height `+2`). `axis` also takes a sketch line, `x`/`y`
(sketch axes), `{origin, dir}` or `{edge|face:[x,y,z]}`.

### Recipe: shelled enclosure (tested)

```text
batch {verbose:false, expect:{volume_mm3:13274.2, bodies:1, bbox:{min:[-30,-20,0], max:[30,20,25]}}, commands:[
  parameters.add w 60, d 40, h 25, wall 2 (mm)
  solid.box {length:"w", width:"d", height:"h", center:[0,0,"h/2"], name:"Block", body_name:"Case"}
  solid.fillet {edges:[[30,20,12.5],[-30,20,12.5],[30,-20,12.5],[-30,-20,12.5]], radius:5, name:"Corners"}
  solid.shell {faces:[[0,0,25]], thickness:"wall", name:"Shell"} ]}          → 13273.1 mm³
execute material.assign {bodies:["Case"], material:"ABS Plastic"}   → execute inspect.measure: mass_g 14.07
```

Fillet outside edges **before** the shell so the walls follow them; round the rim of the open face after it.
`material.list`: Default 1.29 g/cm³, Steel, Stainless Steel, Aluminum, Brass, Copper, Titanium, Cast Iron, ABS
Plastic, PLA, Nylon, Polycarbonate, Oak, … `measure` reports `mass_g` from the body's material.

### Recipe: STEP in, measure, section, picture (tested)

```text
open {path:"/abs/bushing.step"}         → {bodies:["bushing"], component_name, errors:0, warnings:[]}  (`up:"y"` for Y-up files)
measure {summary:true}                  → same volume as the design that wrote it (plate: 23335.17 vs 23335.19 mm³)
compare_picture {reference:"/abs/ref.png", view:"front"}   → overlap 0.984, edges in mm, overlay PNG (red model, blue picture)
```

### Recipe: a 2D view for CADCraft (tested)

```text
execute file.export_view_dxf {camera:{target:[0,0,0], yaw:0, pitch:1.5707963, distance:200, fov:0},
                              path:"/abs/plate_top.dxf"}     → {visible: 609, projection: "orthographic"}
```

Headless, `camera` is required (`camera is required`; `view.apply` does not count). Pitch π/2 = top. The DXF is
plain LINE segments in mm (curves tessellated, `tolerance` 0.01): `cadcraft-cli info` read 609 lines spanning ±60 ×
±25. `hidden:"dashed"` adds hidden edges. For sheet metal use `sheet.flat_pattern` / its DXF export.

Also tested: `sketch.draw.dimensioned`, `solid.box` with `body_name`, `material.assign`, `inspect.measure`,
`view.apply`, `inspect.section`, `undo`, every error below.

## More building blocks

Grep `references/commands.md` for the params. Not tested here:

- **Sketch:** `sketch.rectangle.two_point|rounded`, `sketch.circle.center`, `sketch.arc.*`, `sketch.slot.overall`,
  `sketch.polygon.*`, `sketch.fillet`, `sketch.offset`, `sketch.project`, `sketch.constraint.*`, `sketch.text`,
  `sketch.insert_dxf` / `insert_svg`.
- **Solid:** `solid.sweep`, `solid.loft`, `solid.draft`, `solid.mirror {features|bodies, plane}`, `solid.coil`,
  `solid.thread`, `solid.rib`, `solid.combine`, `solid.split_body`, `solid.move`, `solid.offset_face`.
- **Other areas:** `sheet.*` (sheet metal, flat pattern), `plastic.*` (bosses, snap fits), `frame.*` (weldments),
  `surface.*`, `component.*` / `joint.*` / `motion.*` (assemblies: read `solidcraft-mechanisms`),
  `config.*` (configurations), `render.*` (ray-traced product images as jobs: `render.start`, `render.status`,
  `render.export`), `inspect.interference`, `inspect.clearance`, `inspect.parameter_sweep`, `inspect.draft`.
- **Editing an existing design:** `parameters.list {filter:"feature"}`, `timeline.inspect {feature}` /
  `timeline.edit {feature, set}`, `timeline.roll_to`, `timeline.dependents`, `edit.checkpoint` /
  `edit.restore_checkpoint` (read `solidcraft-editing`).
- **Printing:** `file.slicers`, `file.send_to_slicer`. `file.open_in_easyprint` uploads to Printables: only with
  the user's explicit consent.

## Formats

- **Open (`open` / `doc.open`):** `.sc` (and `.solidcraft`), `.step`/`.stp`, IGES, FreeCAD `.FCStd`, Rhino `.3dm`
  (B-rep: an Import base feature in a component), `.3mf`/`.stl`/`.obj`/`.ply`/`.glb`/`.gltf` (mesh bodies), `.dxf`/`.svg`
  (a new design with an XY sketch). `file.insert_step` / `file.insert_mesh` add to the current design.
- **Save:** `.sc` (container, default) or `.json` (plain JSON, diff-friendly). `file.save` refuses `.step`/`.stl`/`.dxf`
  names: export those.
- **Export (`export` / `file.export`):** STEP (an assembly when the design has components), binary STL, ASCII STL
  (`format:"stla"`), 3MF (`objects: body|component`, `3mf-tagged`), OBJ (+ `.mtl` colours), URDF (whole assembly, STL
  meshes in metres next to it), JSON. Meshes take `quality: standard|fine|finest`. `bodies:[…]` limits any export.
- **Pictures:** `screenshot` (PNG), `solidcraft-cli snapshot` / `render`, `render.export` (PNG/EXR).

## CLI (no MCP needed)

```bash
solidcraft-cli run build.json --out part.step --out part.stl --save part.sc   # {"commands":[...]} = batch steps; prints the measurement
solidcraft-cli run edit.json --in part.sc --save part-v2.sc                   # a script on top of a design
solidcraft-cli eval part.step                                                 # JSON: bodies, volume, mass, bbox, params, timeline
solidcraft-cli snapshot --in part.sc --out shot.png --view iso --width 640 --height 400 --no-axes
solidcraft-cli snapshot --in part.step --out cut.png --view front --section "y=0,flip" --no-grid
solidcraft-cli exec solid.box '{"length":20,"width":10,"height":5}'           # one command in an empty design
solidcraft-cli script part.sc --out build.json                                # a design's history as a replayable script
solidcraft-cli commands                                                       # the catalog as JSON (330 KB)
```

The CLI has no folder limits. `run` writes nothing when a timeline feature fails (`--allow-errors` writes anyway);
`--param-check warn|strict` works here too. `snapshot` takes `--view iso|front|…|<saved view>` or `--camera JSON`,
`--body NAME:opacity=0.3,color=#rrggbb`, `--section z=27|XY|XZ|YZ[,flip]`.

## Pitfalls

- **No writable folder by default.** See Setup: ask for `--allow-path`, use absolute paths.
- **"ok" is not proof.** A cut that misses reports success with `changed_bodies: []` and an unchanged volume
  (tested: a circle sketched at z 100). Always give `expect` or `measure` against your own number.
- **Misspelt keys are ignored** without `--param-check`: `operaton:"cut"` built a new body instead of cutting.
- **XZ sketches are upside down:** sketch y is world −Z. Draw a profile that rises in Z with negative y, or use YZ
  (y = +Z).
- **Edge picks:** a pick far from every edge is refused (`no edge at [0, 0, 60]: the nearest edge is 39.357 mm
  away`; the limit is 5 % of the body size, so on a big body a sloppy pick can snap to the wrong edge: compute exact
  midpoints). Expressions are refused: `an edge is a point [x,y,z], {point} or {body, index}`.
- **Sections keep the near side.** `inspect.section {plane:"XZ"}` seen from `front` shows the outside; add
  `flip:true` (CLI `--section "y=0,flip"`) to see the cut face.
- **`file.export_view_dxf` headless needs `camera`** (`invalid parameters for \`file.export_view_dxf\`: camera is required`).
- **Shell order:** fillet outer edges first; a fillet between two curved faces makes the shell fail
  (`offset: only bodies with planes, cylinders, cones, spheres and tori`): shell first then.
- `solid.extrude` with no sketch: `invalid parameters for \`solid.extrude\`: there is no sketch to use (create one first)`.
  Unknown commands suggest neighbours: `unknown command \`solid.bogus\`; closest: \`solid.torus\`, \`solid.box\`, \`solid.coil\``.
- `extrude` takes **every** region: two concentric circles give a ring; pass `profiles` to choose.
- A repeated `body_name` is renamed (`Body1`) without an error. `timeline.roll_to {feature}` finds the first match,
  which can be a sketch of the same name: keep names unique.
- A `Boolean retry: …` feature warning means faces coincided; trust it only if the volume still matches.
- Never call `list_commands {}` unfiltered (over 100 KB) or full `body_topology` unless needed (25–45 KB).

## Verification

- `expect` on every build batch (`expectation.ok`, `mismatch: []`), or `measure {summary:true}`: volume within
  ~0.01 % of your formula, bbox, face count, `closed: true`.
- `body_topology {faces:"cylinders"}`: each hole's centre, axis and radius where planned.
- `inspect_design {measure:false, sketches:false}`: every timeline `error`/`warning` null, every sketch `dof: 0`.
- Change a driving parameter (`check_parameters`) and confirm the volume and positions move as computed.
- `screenshot` iso and top, and look. For deliverables, `solidcraft-cli eval out.step` reopens the STEP with the same
  volume; check an STL's bbox, or open it in a slicer.

## References

- `references/commands.md`: all 570 commands with labels, toolbar place and params, grouped by id prefix (sketch,
  solid, surface, sheet, component, joint, timeline, parameters, inspect, file, render…). Grep it
  (`grep -n '^- \`solid[.]hole' ${HERMES_SKILL_DIR}/references/commands.md`).
- `skill_reference` (MCP) for SolidCraft's own `solidcraft-modeling`, `-editing`, `-mechanisms`, `-checking` skills.
- Upstream docs: https://github.com/tangency-labs/solidcraft/tree/main/docs (`mcp.md`, `control-protocol.md`,
  `urdf.md`, `render-jobs.md`). They track `main` and may list features newer than 0.30.1.
