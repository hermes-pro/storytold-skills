---
name: cadcraft
description: "Technical drawing and drafting with CADCraft (AutoCAD-style): floor plans, site plans, mechanical part drawings, brackets, layouts with title blocks, dimensioned 2D drawings to scale. Draw lines, polylines, circles and arcs at exact coordinates, offset / trim / fillet, layers, dimensions, hatches, blocks, then save DXF / DWG or export PDF, SVG, PNG."
version: 0.1.0
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
through an MCP server (`cadcraft-cli mcp`) or one-shot CLI commands. It reads and writes DXF (R12–2018) and
DWG (R13–2018), and plots PDF; SVG and PNG are exports.

## When to Use

Use it for **drawings where exact dimensions and scale matter**:

- floor plans, room layouts, site plans, furniture layouts, wall/door/window plans
- mechanical part drawings: plates, brackets, flanges, hole patterns, section hatches
- dimensioned sketches for fabrication, laser/CNC outlines (DXF), title-blocked sheets (PDF)
- opening, inspecting, measuring or converting DXF / DWG files

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

Without a running desktop app the server is **headless** (in-process session with a CPU renderer).
Everything works except `screenshot`, `ui_inspect`, `ui_click`. For the user to watch live, they run
`cadcraft --control 7979` and the server is `cadcraft-cli mcp --connect 127.0.0.1:7979`.

## Mental Model

- **Drawing units, y up.** One unit is whatever you decide: `new_drawing {metric: true}` = millimetres
  (ISO-25 dim style, A-size limits); the default is imperial (inches). Draw **full size** (a 8 m wall is
  `8000` in a metric drawing); scale happens at annotation (DIMSCALE, text height) and plot time.
- **Model space** holds the geometry. **Layouts** (paper space) hold sheets with viewports onto model space
  at a scale (`1:50`) plus title-block text. `layout.set {name: "Model"|"<layout>"}` switches.
- **Entities** have a **handle** (hex string such as `"10A"`), a layer, and geometry. Every create command returns
  the handle(s); modify commands take `handle`/`handles`. Keep the handles.
- **Layers** carry colour, linetype and lineweight (`ByLayer`). Set the current layer before drawing.
- **Two ways to run commands** (295 commands):
  - `command_line {text}` types AutoCAD syntax: `line 0,0 @100,0 @0,50 c`, `circle 50,25 10`, `rectang 0,0 @80,40`.
    Coordinates: absolute `x,y`, relative `@dx,dy`, polar `@dist<angle`. Spaces act as Enter.
  - `execute {command, params}` runs the same command with JSON and no prompts. Best for agents: exact,
    returns handles, errors name the missing param. Grep `references/commands.md` for ids/params.

## Tools (Hermes names them `mcp_cadcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `execute {command, params}` | Any command with JSON params (`line`, `circle`, `offset`, `dimlinear`, `layer.new`, …) |
| `command_line {text}` | Type at the prompt; returns `prompt`, `keywords`, `running`, `output` (and `error`) |
| `script {text}` | Several command lines at once (like a `.scr` file); a blank line = Enter |
| `inspect_drawing {entities?, limit?}` | Counts by type, extents, layers, styles, blocks, layouts, undo history, entities |
| `query_entities {type?, layer?, window?, limit?}` | Entities with handles and geometry, e.g. `{type:"Circle"}`, `{window:[[0,0],[100,100]]}` |
| `render {width?, height?, fit?, path?}` | PNG of the active space, fitted to extents. **Look at it** |
| `new_drawing {metric?}` / `open {path}` / `save {path}` | Files: `open` takes .dxf/.dwg; `save` writes .dxf, or .svg/.png by extension |
| `list_commands {filter?}` | The catalog with aliases and params |
| `cancel` | Escape: abort a running prompt |

Resources: `cadcraft://drawing` (inspect JSON) and `cadcraft://commands`. There are no prompts.

## Drafting essentials (JSON params)

- **Draw:** `line {points:[[x,y],…], closed?}` · `pline {vertices, closed?, width?}` (bulge for arcs) ·
  `rectang {p1, p2, fillet?, chamfer?}` · `circle {center, radius}` · `arc {center, radius, start, end}` (degrees,
  CCW) · `polygon {sides, center, radius}` · `ellipse` · `spline {fit}` · `point`.
- **Modify:** `offset {handle, distance, side:[x,y]}` · `trim {handle, pick, edges?}` · `extend` ·
  `fillet {h1, p1, h2, p2, radius}` · `chamfer {h1, p1, h2, p2, d1, d2}` · `break {handle, p1, p2}` ·
  `move {handles, delta}` · `copy {handles, delta, count?}` · `rotate {handles, base, angle}` · `mirror` · `scale` ·
  `arrayrect {handles, rows, cols, rowSpacing, colSpacing}` · `arraypolar {handles, center, count, rotate?}` ·
  `erase {handles}` · `join` · `explode`. `p1`/`pick` are points **on** the object, near the end to keep/cut.
- **Layers:** `layer.new {name, color, linetype?, lineweight? (mm), current?}` · `layer.current {name}` ·
  `layer.set {name, on?, frozen?, locked?, color?, lineweight?}` · `linetype {load:"*"}` for DASHED/CENTER.
- **Text:** `text {at, text, height, justify?: "MC"|"BL"…, rotation?}` · `mtext {at, text, height, width}` (`\P` = new
  line). Make a TrueType style first: `style {name:"Notes", font:"Arial", current:true}`.
- **Dimensions:** `dimlinear {p1, p2, at}` · `dimaligned` · `dimradius {handle, at}` · `dimdiameter` ·
  `dimangular` · `dimcontinue {points}` / `dimbaseline` (chain from the last linear dim) · `qdim`. Size them for the
  drawing: `dimstyle {name:"ISO-25", DIMSCALE: 50, DIMDEC: 0}` (any DIM* variable works).
- **Hatch:** `hatch {handles:[outer, inner], pattern:"ANSI31", scale}` or `{points:[[x,y]]}`; `pattern:"SOLID"`.
- **Blocks:** `block {name, base, handles, keep:"delete"}` → `insert {name, at, rotation?, scale?, attribs?}`;
  attributes via `attdef {tag, prompt, default, at, height}` inside the block, filled with `attribs:{TAG: value}`.
- **Measure:** `dist {p1, p2}`, `area {handle}` (use the numeric `area`), `list`, `properties {handles}`, `massprop`.

## Procedure

1. **Plan** units (mm vs inches), sheet size and plot scale (e.g. A3 at 1:50), and layers (WALLS, DOORS, FURN,
   DIMS, TEXT, HATCH, CENTER).
2. `new_drawing {metric:true}`, set DIMSCALE (= plot scale denominator, e.g. 50) and a TrueType text style.
3. **Geometry first**, layer by layer, with `execute` and exact coordinates; chain the returned handles into
   offset/trim/fillet. Use `command_line` for quick AutoCAD-style input.
4. **Annotate:** dimensions on DIMS, text (height = paper mm × scale, e.g. 2.5 mm × 50 = 125), hatches.
5. **Check:** `inspect_drawing` counts and extents, `query_entities` geometry, then `render` and look.
6. **Save** `.dxf` (or `saveas {path, format:"dwg"}`); export `.pdf` (`exportpdf`), `.svg`, `.png` as asked.

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
execute offset {handle:"102", distance:100, side:[5100,3000]}
execute break {handle:"102", p1:[5000,1000], p2:[5000,1900]}  (900 door opening; same for the other face)
execute layer.current {name:"HATCH"}
execute hatch {handles:["100","101"], pattern:"ANSI31", scale:40}   (walls only)
execute layer.current {name:"FURN"}
execute line {points:[[0,0],[0,900]]} · execute arc {center:[0,0], radius:900, start:0, end:90}
execute block {name:"DOOR900", base:[0,0], handles:[line, arc], keep:"delete"}
execute insert {name:"DOOR900", at:[5100,1000]}
execute circle {center:[2500,3000], radius:600}  · rectang chair · arraypolar {handles:[chair], center:[2500,3000], count:4, rotate:true}
execute layer.current {name:"TEXT"} · text {at:[2500,5000], text:"LIVING ROOM", height:250, justify:"MC"}
execute layer.current {name:"DIMS"}
execute dimlinear {p1:[0,0], p2:[8000,0], at:[4000,-500]} · dimlinear {p1:[0,0], p2:[0,6000], at:[-500,3000]}
execute dimradius {handle:<table>, at:[3000,2500]}
render {width:1000, height:800}                             → look
save {path:"/abs/plan.dxf"} · execute saveas {path:"/abs/plan.dwg", format:"dwg"}
execute exportpdf {path:"/abs/plan.pdf", fit:true}
```

### Recipe: plotted sheet from a layout (tested)

```text
execute layout.new {name:"Sheet"}                           → {name, viewport:"10A"}
execute pagesetup {layout:"Sheet", paper:"A3", landscape:true, plotStyleTable:"monochrome.ctb"}
execute viewport.set {handle:"10A", scale:"1:50", center:[4000,3000]}
execute layout.set {name:"Sheet"} · execute text {at:[20,20], text:"TITLE", height:5}   (paper mm)
execute exportpdf {path:"/abs/sheet.pdf", layout:"Sheet"}
execute layout.set {name:"Model"}
```

Also tested: `trim`, `fillet` (→ `{arc}`), `script` with `pline … c` / `circle` / polar `line 300,0 @50<30`,
`command_line` `rectang 0,100 @80,40`, `circle 2p …`, `offset` with picks, attribute blocks, `open` of a DWG.

## Formats

- **Open:** .dxf (ASCII/binary R12–2018), .dwg (R13–2018).
- **Save:** `save {path}` → .dxf, .svg, .png (by extension); `saveas {path, format:"dwg"}` → DWG.
- **PDF:** `exportpdf {path, layout?, paper?, landscape?, fit?}` or `plot {…}`; uses the layout's page setup.
  `plotStyleTable:"monochrome.ctb"` prints all colours black.
- PNG exports use the dark model-space background; SVG and PDF are on white.

## CLI (no MCP needed)

```bash
cadcraft-cli info plan.dwg                               # JSON: counts, extents, layers, blocks, layouts
cadcraft-cli convert plan.dxf plan.svg                   # also .png, .pdf, .dxf
cadcraft-cli run --metric --script 'rectang 0,0 100,50
circle 50,25 10
' --cmd 'dimlinear {"p1":[0,0],"p2":[100,0],"at":[50,-10]}' --save part.dxf --export part.png
cadcraft-cli run plan.dxf --script-file edits.scr --save plan2.dxf
cadcraft-cli sample bracket|floorplan out.dxf            # reference drawings to study
cadcraft-cli commands dimlin                             # catalog, filtered
```

`run` exits 1 on the first error (e.g. `unknown command \`bogus\``).

## Pitfalls

- **Dimensions vanish at real-world scale.** ISO-25 text and arrows are 2.5 units: invisible on an 8000 mm
  plan. Set `dimstyle {name:"ISO-25", DIMSCALE:<plot scale>}` **before** dimensioning.
- **MTEXT in the default stroke font loses its spaces** ("Floor plan" renders as "Floorplan"). Use a TrueType
  style (`style {font:"Arial", current:true}`) or single-line `text`.
- **Modify commands replace handles.** `trim` and `break` return new handles and the old one is gone
  (`no such object`). Always continue with the handles from the latest reply.
- Return shapes differ: `line`/`break`/`trim` → `{handles:[…]}`, most single creates → `{handle}`, `fillet` →
  `{arc}`, `layer.*` → `null`. `"LAST"` is not a handle.
- **Hatch by internal point** treats everything inside as islands with alternating fill (furniture gets
  hatched). Hatch with explicit boundary `handles`, or before drawing contents.
- **`command_line` needs an explicit Enter** for open-ended commands: after `line …` / `pline …` send
  `command_line {text:""}` (a trailing space is not enough); `running` shows the active command.
- **In `script`, a blank line repeats the last command** if it already finished (`circle x,y r` + blank → a new
  CIRCLE prompt eats the next line). Only put a blank line after open-ended commands.
- Command-line picks must land **on** the object (on a circle's edge, not its centre), else `*Invalid selection*`.
- PDF plots keep layer colours: yellow/cyan on white are unreadable. Use dark colours or `monochrome.ctb`.
- `area`'s `message` mislabels imperial areas as lengths (`Area = 7200'-0"` for 86 400 sq in); use the numeric `area`.
- Layout1/Layout2 in a new drawing are empty (no viewport); `layout.new` creates one with a viewport.
- Use absolute paths for `open`/`save`/`exportpdf`: the server's working directory isn't yours.

## Verification

- `inspect_drawing`: expected counts per type, layers, blocks, and sensible `extents`.
- `query_entities {type:"Dimension"}` / `{layer:"WALLS"}` to confirm geometry and layer assignment.
- `render`, then look: walls closed, openings where planned, dims readable, nothing hatched by mistake.
- For the deliverable, render the PDF/SVG to PNG (e.g. `vectorcraft-cli convert plan.pdf page.png --artboard 0`)
  and check it; `cadcraft-cli info out.dwg` confirms the file reopens.

## References

- `references/commands.md`: all 295 commands with aliases and JSON params, grouped by menu. Grep it rather than
  reading it whole (e.g. `grep -n "^- \`dim" references/commands.md`).
- Upstream docs: https://github.com/storytold/cadcraft/tree/main/docs (`mcp.md`, `control-protocol.md`).
