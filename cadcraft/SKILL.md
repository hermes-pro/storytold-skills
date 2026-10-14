---
name: cadcraft
description: "Technical drawing and drafting with CADCraft (AutoCAD-style): floor plans, site plans, mechanical part drawings, brackets, layouts with title blocks, dimensioned 2D drawings to scale. Draw lines, polylines, circles and arcs at exact coordinates, offset / trim / fillet, layers, dimensions, hatches, blocks, tables, then save DXF / DWG or export PDF, SVG, PNG."
version: 0.2.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [CAD, Drafting, AutoCAD, DXF, DWG, Floor Plan, Engineering, Architecture, MCP]
    related_skills: [storytold, storytold-install, vectorcraft, pdfcraft, gridcraft]
---

# CADCraft

CADCraft is a free, open-source clean-room take on AutoCAD (storytold Crafting Apps). An agent drives it
through an MCP server (`cadcraft-cli mcp`) or one-shot CLI commands. It reads DXF (R12–2018), DWG (R13–2018)
and SVG, writes DXF / DWG (versions 2000–2018, DXF also binary), and plots PDF; SVG and PNG are exports.
This skill is tested against CADCraft 0.6.2.

## When to Use

Use it for **drawings where exact dimensions and scale matter**:

- floor plans, room layouts, site plans, furniture layouts, wall/door/window plans
- mechanical part drawings: plates, brackets, flanges, hole patterns, section hatches, GD&T frames
- dimensioned sketches for fabrication, laser/CNC outlines (DXF), title-blocked sheets (PDF)
- opening, inspecting, measuring, comparing or converting DXF / DWG files

Pick a different Crafting App when:

| The job is… | Use |
|---|---|
| A logo, icon, poster or illustration (looks matter, not measurements) | `vectorcraft` |
| Marking up or editing pages of an existing PDF | `pdfcraft` |
| A bill of materials or cost sheet | `gridcraft` |
| Photo editing | `photocraft` |

## Setup

1. If tools named `mcp_cadcraft_*` are available, use them. This is the preferred way.
2. Otherwise check for the CLI with `cadcraft-cli --version`. If it's missing, load the `storytold-install`
   skill and run its `setup cadcraft`. Then ask the user to start a new session or run `/reload-mcp`.
3. Until the MCP tools appear, use the CLI one-shots (see **CLI**).

Without a running desktop app the server is **headless** (in-process session with a CPU renderer). For the
user to watch live, they run `cadcraft --control 7979` and the server is
`cadcraft-cli mcp --connect 127.0.0.1:7979` (add `--lazy` to start before the app, `--launch` to open it).
Only that bridged mode adds `screenshot`, `ui_inspect` and `ui_click`.

## Mental Model

- **Drawing units, y up.** One unit is whatever you decide: `new_drawing {metric: true}` = millimetres
  (ISO-25 dim style, A-size limits); the default is inches (decimal display). Draw **full size** (an 8 m wall
  is `8000` in a metric drawing); scale happens at annotation (DIMSCALE, text height) and plot time.
- **Model space** holds the geometry. **Layouts** (paper space, mm) hold sheets with viewports onto model
  space at a scale (`1:50`) plus title-block text. `layout.set {name: "Model"|"<layout>"}` switches.
- **Entities** have a **handle** (hex string such as `"10A"`), a layer, and geometry. Every create command
  returns the handle(s); modify commands take `handle`/`handles`. Keep the handles.
- **Layers** carry colour, linetype and lineweight (`ByLayer`). Set the current layer before drawing.
- **Two ways to run commands** (404 commands):
  - `command_line {text}` types AutoCAD syntax: `line 0,0 @100,0 @0,50 c`, `circle 50,25 10`, `rectang 0,0 @80,40`.
    Coordinates: absolute `x,y`, relative `@dx,dy`, polar `@dist<angle`. Spaces act as Enter, and a trailing
    space ends an open-ended command.
  - `execute {command, params}` runs the same command with JSON and no prompts. Best for agents: exact,
    returns handles, errors name the missing param. It takes command **ids** only, not aliases
    (`rec` → `unknown command \`rec\``). Grep `references/commands.md` for ids/params.

## Tools (Hermes names them `mcp_cadcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `execute {command, params}` | Any command with JSON params (`line`, `circle`, `offset`, `dimlinear`, `layer.new`, …) |
| `command_line {text}` | Type at the prompt; returns `prompt`, `keywords`, `running`, `output` (and `error`) |
| `script {text}` | Several command lines at once (like a `.scr` file); a blank line = Enter |
| `inspect_drawing {entities?, limit?}` | Counts by type, extents, layers, styles, blocks, layouts, undo history, entities |
| `query_entities {type?, layer?, window?, crossing?, limit?, offset?}` | Entities with handles and geometry, e.g. `{type:"Circle"}`, `{window:[[0,0],[100,100]], crossing:false}`. `count` = all matches; pages of 500 |
| `render {width?, height?, fit?, path?}` | PNG of the active space, fitted to extents (`path` also writes it). **Look at it** |
| `new_drawing {metric?}` / `open {path}` / `save {path?}` | `open` takes .dxf/.dwg/.svg; `save` writes .dxf/.dwg by extension, or exports .svg/.png/.pdf |
| `list_commands {filter?}` | The catalog with aliases and params |
| `cancel` | Escape: abort a running prompt |

Resources: `cadcraft://drawing` (inspect JSON) and `cadcraft://commands`. There are no prompts. Bad tool
arguments (missing `text`, wrong type) are JSON-RPC errors `-32602`; a command that fails returns `isError`.

## Drafting essentials (JSON params)

- **Draw:** `line {points:[[x,y],…], closed?}` · `pline {vertices, closed?, width?}` (bulge for arcs) ·
  `rectang {p1, p2, fillet?, chamfer?}` · `circle {center, radius}` · `arc {center, radius, start, end}` (degrees,
  CCW) · `polygon {sides, center, radius}` · `ellipse` · `spline {fit}` · `point` · `table {at, rows, cols, cells}`.
- **Modify:** `offset {handle, distance, side:[x,y]}` · `trim {handle, pick, edges?}` · `extend` ·
  `fillet {h1, p1, h2, p2, radius}` · `chamfer {h1, p1, h2, p2, d1, d2}` · `break {handle, p1, p2}` ·
  `move {handles, delta}` · `copy {handles, delta, count?}` · `rotate {handles, base, angle}` · `mirror` · `scale` ·
  `arrayrect {handles, rows, cols, rowSpacing, colSpacing}` · `arraypolar {handles, center, count, rotate?}` ·
  `erase {handles}` · `join` · `explode`. `p1`/`pick` are points **on** the object, near the end to keep/cut.
  Arrays are associative by default (one block reference); `associative:false` gives loose copies.
- **Layers:** `layer.new {name, color, linetype?, lineweight? (mm), current?}` · `layer.current {name}` ·
  `layer.set {name, on?, frozen?, locked?, color?, lineweight?}` · `linetype {load:"*"}` for DASHED/CENTER.
- **Text:** `text {at, text, height, justify?: "MC"|"BL"…, rotation?}` · `mtext {at, text, height, width}` (`\P` = new
  line; also `columns`, `list`, `align`). For TrueType: `style {name:"Notes", font:"Arial", current:true}`.
- **Dimensions:** `dimlinear {p1, p2, at}` · `dimaligned` · `dimradius {handle, at}` · `dimdiameter` ·
  `dimangular` · `dimcontinue {points}` / `dimbaseline` (chain from the last linear dim) · `qdim` ·
  `tolerance` (GD&T). Size them for the drawing: `dimstyle {name:"ISO-25", DIMSCALE: 50, DIMDEC: 0}` (any DIM*
  variable works; `setvar {name:"DIMSCALE", value:50}` also works, as an override for new dimensions).
- **Hatch:** `hatch {handles:[outer, inner], pattern:"ANSI31", scale}` or `{points:[[x,y]], style:"outer"}`; `pattern:"SOLID"`.
- **Blocks:** `block {name, base, handles, keep:"delete"}` → `insert {name, at, rotation?, scale?, attribs?}`;
  attributes via `attdef {tag, prompt, default, at, height}` inside the block, filled with `attribs:{TAG: value}`.
  `block`'s default `keep` is `"convert"` (the originals become an insert).
- **Measure:** `dist {p1, p2}`, `area {handle}` (numeric `area`, `perimeter`), `list`, `properties {handles}`,
  `massprop`, `count` / `countlist` (blocks), `compare {path}` (diff against another drawing).

## Procedure

1. **Plan** units (mm vs inches), sheet size and plot scale (e.g. A3 at 1:50), and layers (WALLS, DOORS, FURN,
   DIMS, TEXT, HATCH, CENTER).
2. `new_drawing {metric:true}`, set DIMSCALE (= plot scale denominator, e.g. 50) and a TrueType text style.
3. **Geometry first**, layer by layer, with `execute` and exact coordinates; chain the returned handles into
   offset/trim/fillet. Use `command_line` for quick AutoCAD-style input.
4. **Annotate:** dimensions on DIMS, text (height = paper mm × scale, e.g. 2.5 mm × 50 = 125), hatches.
5. **Check:** `inspect_drawing` counts and extents, `query_entities` geometry, then `render` and look.
6. **Save** `save {path:"/abs/x.dxf"}` or `.dwg`; export `.pdf` (`exportpdf` or `save` to .pdf), `.svg`, `.png`.

### Recipe: dimensioned floor plan (tested)

```text
new_drawing {metric:true}
execute dimstyle {name:"ISO-25", DIMSCALE:50, DIMDEC:0}
execute style {name:"Notes", font:"Arial", current:true}
execute layer.new {name:"WALLS", color:"7", lineweight:0.5}   (+ DIMS blue, TEXT 7, FURN green, HATCH 8)
execute layer.current {name:"WALLS"}
execute rectang {p1:[0,0], p2:[8000,6000]}                 → {handle:"100"}
execute offset {handle:"100", distance:200, side:[4000,3000]} → {handle:"101"}   (inner wall face)
execute line {points:[[5000,200],[5000,5800]]}             → {handles:["102"]}  (partition)
execute offset {handle:"102", distance:100, side:[5100,3000]} → {handle:"103"}
execute break {handle:"102", p1:[5000,1000], p2:[5000,1900]}  → {handles:["104","105"]}  (900 door opening;
        same for "103")
execute layer.current {name:"HATCH"}
execute hatch {handles:["100","101"], pattern:"ANSI31", scale:40}   (walls only)
execute layer.current {name:"FURN"}
execute line {points:[[0,0],[0,900]]} · execute arc {center:[0,0], radius:900, start:0, end:90}
execute block {name:"DOOR900", base:[0,0], handles:[line, arc], keep:"delete"}
execute insert {name:"DOOR900", at:[5100,1000]}
execute circle {center:[2500,3000], radius:600}  · rectang chair · arraypolar {handles:[chair], center:[2500,3000], count:4, rotate:true}
execute layer.current {name:"TEXT"} · text {at:[2500,5000], text:"LIVING ROOM", height:250, justify:"MC"}
execute mtext {at:[5400,5500], text:"Floor plan\\Pscale 1:50", height:200, width:2400}
execute layer.current {name:"DIMS"}
execute dimlinear {p1:[0,0], p2:[8000,0], at:[4000,-500]} · dimlinear {p1:[0,0], p2:[0,6000], at:[-500,3000]}
execute dimradius {handle:<table>, at:[3000,2500]}
render {width:1000, height:800}                             → look
save {path:"/abs/plan.dxf"} · save {path:"/abs/plan.dwg"}
execute exportpdf {path:"/abs/plan.pdf", fit:true}          (A4 landscape, real text in Arial)
```

### Recipe: plotted A3 sheet from a layout (tested)

`layout.new` sizes its viewport for the default paper, so a later `pagesetup` to A3 leaves it in one corner.
Make the layout without a viewport, set the page, then draw the viewport:

```text
execute layout.new {name:"Sheet", viewport:false}
execute pagesetup {layout:"Sheet", paper:"A3", landscape:true, plotStyleTable:"monochrome.ctb"}
execute layout.set {name:"Sheet"}
execute mview {p1:[15,40], p2:[405,282]}                     → {viewports:["1182"]}   (paper mm)
execute viewport.set {handle:"1182", scale:"1:50", center:[4000,3000]}
execute rectang {p1:[10,10], p2:[410,287]} · line {points:[[10,35],[410,35]]}   (border, title strip)
execute text {at:[20,20], text:"Ground floor plan   1:50", height:5}
execute exportpdf {path:"/abs/sheet.pdf", layout:"Sheet"}
execute layout.set {name:"Model"}
```

### Recipe: one PDF per sheet (tested)

```text
execute publish {path:"/abs/set.pdf", layouts:["Model","Sheet"]}   → set-Model.pdf, set-Sheet.pdf
```

Without `layouts` it publishes Model plus **every** layout, including the empty Layout1/Layout2.

Also tested: `trim` (→ `{handles}`), `fillet` (→ `{arc}`), `script` with `pline … c` / `circle` / polar
`line 300,0 @50<30`, `command_line` `rectang 0,300 @80,40`, `circle 2p …`, `offset 5 <pick> <side>`,
attribute blocks, `open` of a DWG and an SVG, `import` of a DWG into the current drawing, `compare`.

## Formats

- **Open:** .dxf (ASCII/binary R12–2018), .dwg (R13–2018), .svg/.svgz (1 px = 0.2646 mm; SVG y-down
  becomes negative y). `import {path, at?, scale?}` merges a DXF/DWG/SVG into the current drawing.
- **Save:** `save {path}` → .dxf/.dwg by extension (2018 by default). `saveas {path, version?: 2000…2018,
  binary?}` for an older version or binary DXF; the format comes from the extension. `save {}` with no path
  fails on a new drawing (`drawing has no file name yet; use saveas {path}`).
- **Export:** `save` or `export {path}` to .svg/.png/.pdf exports without renaming the drawing.
- **PDF:** `exportpdf {path, layout?, paper?, landscape?, fit?, scale?, plotArea?, window?}` or `plot {…}`; uses
  the layout's page setup. Layers become PDF layers; TrueType text stays real text.
  `plotStyleTable:"monochrome.ctb"` (or `grayscale.ctb`) prints all colours black/grey.
- PNG exports and `render` use the dark model-space background; SVG and PDF are on white.

## CLI (no MCP needed)

```bash
cadcraft-cli info plan.dwg                               # JSON: counts, extents, layers, blocks, layouts
cadcraft-cli convert plan.dxf plan.svg                   # also .png, .pdf, .dxf, .dwg
cadcraft-cli convert plan.dxf room.png --window 0,0,5000,3000   # frame a rectangle (drawing units)
cadcraft-cli run --metric --script 'rectang 0,0 100,50
circle 50,25 10
' --cmd 'dimlinear {"p1":[0,0],"p2":[100,0],"at":[50,-10]}' --save part.dxf --export part.png
cadcraft-cli run plan.dxf --script-file edits.scr --save plan2.dxf
cadcraft-cli sample bracket|floorplan out.dxf            # reference drawings to study (.dxf/.dwg/.svg/.png)
cadcraft-cli commands dimlin                             # catalog as JSON, filtered
```

Image exports are 2400×1600 and always model space. `--view extents|current` picks the framing; `run --export`
uses the current view if the commands zoomed or panned. `run` exits 1 on the first error
(`unknown command \`bogus\``) and on unknown options (`unknown option --bogusflag`).

## Pitfalls

- **Dimensions vanish at real-world scale.** ISO-25 text and arrows are 2.5 units: invisible on an 8000 mm
  plan. Set `dimstyle {name:"ISO-25", DIMSCALE:<plot scale>}` (or `setvar DIMSCALE`) **before** dimensioning.
- **Modify commands replace handles.** `trim` and `break` return new handles and the old one is gone. `break`,
  `trim` on it fail with `no such object`, `offset` with `invalid parameters for \`offset\`: no such object`, but
  `erase`, `move`, `list`, `properties` quietly do nothing (`{erased: 0}`, `{moved: 0}`). Always continue
  with the handles from the latest reply.
- Return shapes differ: `line`/`break`/`trim` → `{handles:[…]}`, most single creates → `{handle}`, `hatch` →
  both, `fillet` → `{arc}`, `mview` → `{viewports:[…]}`, `layer.*` → `null`. `"LAST"` is not a handle
  (`"LAST" is not an object handle (a hex string such as "1A2")`).
- **Hatch by internal point** uses the normal island style: an island inside an island is hatched again (a table
  inside a room gets hatched when you hatch the walls). Pass `style:"outer"`, or hatch with explicit boundary
  `handles`.
- **`command_line` leaves open-ended commands running** (`line …`, `pline …`) unless the text ends with a space
  or you send `command_line {text:""}`. The next line is then fed to the old prompt: `circle 10,10 5` becomes
  `Point or option keyword required.` plus an extra line segment. Check `running` is `null`.
- **In `script`, a blank line repeats the last command** if it already finished (`circle x,y r` + blank → a new
  CIRCLE prompt eats the next line). Only put a blank line after open-ended commands (and to end MTEXT).
- Command-line picks must land **on** the object (on a circle's edge, not its centre); a miss selects nothing,
  silently.
- PDF plots keep layer colours: yellow/cyan on white are unreadable. Use dark colours or `monochrome.ctb`.
- Layout1/Layout2 in a new drawing are empty (no viewport). `publish` without `layouts` still prints them.
- Use absolute paths for `open`/`save`/`exportpdf`: relative paths resolve against the server's working
  directory, not yours.

## Verification

- `inspect_drawing`: expected counts per type, layers, blocks, and sensible `extents`.
- `query_entities {type:"Dimension"}` / `{layer:"WALLS"}` to confirm geometry and layer assignment.
- `render`, then look: walls closed, openings where planned, dims readable, nothing hatched by mistake.
- For the deliverable, render the PDF to PNG (e.g. `pdftoppm -png -r 60 plan.pdf page`, or
  `vectorcraft-cli convert plan.svg page.png --artboard 0`) and check it; `cadcraft-cli info out.dwg` confirms
  the file reopens.

## References

- `references/commands.md`: all 404 commands with aliases and JSON params, grouped by menu. Grep it rather than
  reading it whole (e.g. `grep -n "^- \`dim" ${HERMES_SKILL_DIR}/references/commands.md`).
- Upstream docs: https://github.com/storytold/cadcraft/tree/main/docs (`mcp.md`, `control-protocol.md`). They
  track `main` and may list tools newer than 0.6.2 (`find_text`, `render {window}` are not in 0.6.2).
