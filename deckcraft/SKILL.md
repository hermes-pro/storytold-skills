---
name: deckcraft
description: "Presentations with DeckCraft (PowerPoint-style): build and edit slide decks — pitch decks, reports, lectures, briefings. Slides from layouts, bullets, pictures, charts, tables, shapes and diagrams, themes and backgrounds, speaker notes, transitions and animations. Open and save .pptx, export PDF (slides, notes, handouts) and PNG."
version: 0.1.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Office, Presentation, Slides, PowerPoint, Pptx, Deck, Chart, PDF, MCP]
    related_skills: [storytold, storytold-install, wordcraft, gridcraft, vectorcraft, photocraft, designcraft]
---

# DeckCraft

DeckCraft is a free, open-source clean-room take on Microsoft PowerPoint (storytold Crafting Apps). An agent
drives it through an MCP server (`deckcraft-cli mcp`) or one-shot CLI commands. It opens and saves `.pptx`,
and exports PDF (slides, notes pages, handouts), PNG/JPEG and text outlines.

## When to Use

Use it for **slides**:

- pitch decks, quarterly reviews, lectures, training, status briefings, kickoff decks
- turning an outline or report into a deck, with charts, tables and speaker notes
- editing an existing `.pptx`: retheme, fix text, add notes/transitions, export PDF handouts or slide PNGs

Pick a different Crafting App when:

| The job is… | Use |
|---|---|
| A written document, report or letter (flowing text) | `wordcraft` |
| The numbers themselves: spreadsheets, models, data cleaning | `gridcraft` |
| A logo, icon or custom illustration to put on a slide | `vectorcraft` (export PNG/SVG, then insert it) |
| Retouching a photo before it goes on a slide | `photocraft` |
| Print layouts: brochures, posters, magazines | `designcraft` |

## Setup

1. If tools named `mcp_deckcraft_*` are available, use them. This is the preferred way.
2. Otherwise check for the CLI with `deckcraft-cli --version`. If it's missing, load the `storytold-install`
   skill and run its `setup deckcraft`. Then ask the user to start a new session or run `/reload-mcp`.
3. Until the MCP tools appear, use the CLI one-shots (see **CLI**).

The server is **headless** by default (in-process engine, no window). Everything works except `screenshot` and
`call_app`. For the user to watch live: `deckcraft --control 7990`, then `deckcraft-cli mcp --connect 7990`
(a bare port, not host:port).

## Mental Model

- **Slides are built from layouts** (`title`, `titleAndContent`, `sectionHeader`, `twoContent`, `comparison`,
  `titleOnly`, `blank`, `contentWithCaption`, `pictureWithCaption`). A layout gives **placeholders** (title, body
  `obj`, subtitle…) that inherit the theme's fonts and positions. Fill them with `set_text {id, text}`.
- **Coordinates are points, y down.** A 16:9 slide is **960 × 540**. Boxes are `[x, y, w, h]`. Title placeholders sit at
  about `[60, 29, 840, 104]`, the body at `[60, 144, 840, 343]`; keep free-placed content inside `y ≥ 140`.
- **Shape ids are numbers.** Every creating tool returns `{id}`; `inspect_slide` lists every shape's id, kind,
  placeholder type, box and text. Formatting commands act on the **selection** (`select {ids}`) or on `ids`.
- **There's a current slide.** `add_slide` inserts after it and makes the new slide current; `go_to_slide {index}`
  switches. Shape tools (`add_shape`, `insert_chart`…) act on the current slide. Slide indexes are 0-based.
- **Theme colours** (`accent1`..`accent6`, `tx1`, `bg1`) work anywhere a colour does, so a retheme recolours them.
- Every action is a command (222). `run_command {command, params}` runs one, `batch` runs several.

## Tools (Hermes names them `mcp_deckcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `new_presentation {theme?, blank?}` | New deck with one empty title slide (in a fresh session its title/subtitle are ids 258/259; confirm with `inspect_slide`), or none with `blank: true` |
| `open_presentation {path}` / `save_presentation {path}` | `.pptx` or `.deckcraft` (native), picked by extension |
| `add_slide {layout, title?, body?}` | New slide after the current one. `body`: one paragraph per line |
| `set_text {id, text}` | Replace a shape's text. **Leading tabs set bullet levels** |
| `add_shape {preset, x, y, w, h, fill?, line?, text?}` | Preset shapes (`references/catalogs.md`); `fill` `#RRGGBB` or `accent1..6` |
| `add_text_box {x, y, w, text, size?, color?, align?}` | Free text; height grows to fit |
| `insert_picture {path, x?, y?, w?, h?}` | Image from file (or `data` base64) |
| `insert_table {rows, cols, data?, x?, y?, w?, h?}` | Table, first row styled as header |
| `insert_chart {type, categories, series:[{name, values}], title?}` | Native chart. **No position params**: see Pitfalls |
| `inspect_document` / `inspect_slide {index?}` | Deck structure / one slide's shapes, notes, transition, animations |
| `render_slide {slide?, scale?}` | PNG of a slide so you can **look** at it (`scale: 0.6` is enough to check) |
| `export {path, format, all?, slide?, scale?}` | `png`/`jpeg` (one or all slides), `pptx`, `outline`. PDF: `run_command file.export` |
| `select {ids}`, `go_to_slide {index}` | Selection and current slide |
| `list_commands {filter}` / `run_command` / `batch` | Everything else |
| `pointer`, `select_tool`, `key`, `type_text` | Mouse/keyboard emulation (rarely needed) |
| `screenshot`, `call_app` | Desktop app only (`--connect`) |

## Commands you'll use most

- **Slides:** `slide.notes {text, index?}`, `slide.layout {layout}`, `slide.duplicate`, `slide.move {from, to}`,
  `slide.delete {index}`, `slide.hide`, `slide.fromOutline {text}`, `section.add {name, at}`.
- **Design:** `design.theme {name}`, `design.colors {name | colors}`, `design.fonts {name | major, minor}`,
  `design.background {color | gradient | style, index?, all?}`, `design.headerFooter {slideNumber, footer, footerText, hideOnTitle}`,
  `design.slideSize {preset | w, h}`.
- **Text (on selection):** `format.size {size}`, `format.bold`, `format.color {color}`, `format.font {family}`,
  `format.align {align}`, `format.bullets {on, char?}`, `format.numbering {on, scheme?}`, `format.paragraph {spaceAfter…}`, `format.autofit {mode}`.
- **Shapes:** `shape.fill {color | gradient | transparency}`, `shape.line {color, width, dash, tail}`, `shape.effects {shadow: "outer"}`,
  `shape.setBounds {x, y, w, h, ids}`, `shape.connect {from, to, preset?}`, `arrange.align {edge, to?}`, `arrange.distribute`, `arrange.group`.
- **Charts & tables:** `chart.options {title, legend, dataLabels, gridlines}`, `chart.data`, `chart.type`,
  `table.style {style: "medium2-accent1"…}`, `table.options {headerRow, bandedRows…}`, `table.cellFill {color, cells}`, `table.merge`.
- **Motion:** `transition.set {kind, option?, duration?}`, `transition.applyAll`, `animation.add {effect, ids, start?}`,
  `animation.options {textBuild: "byParagraph", index}`.
- **Files:** `file.export {path, format: "pdf", layout?: slides|notes|handouts, perPage?}`, `file.properties {title, author…}`.

## Procedure

1. **Plan** one message per slide, the layout for each, and where charts/tables/pictures go. Pick a theme
   (`DeckCraft`, `Harbor`, `Ember`, `Meadow`, `Nocturne`, `Paper`, `Coral Reef`, `Slate`).
2. **Build** slide by slide: `add_slide {layout, title}` → `inspect_slide` for the placeholder ids → `set_text` /
   `insert_*` → `slide.notes`.
3. **Style** with theme colours, then transitions (`transition.set` + `transition.applyAll`) and a few animations.
4. **Look:** `render_slide` every slide. Check overlap with the title, overflow, contrast, empty placeholders.
5. **Save** `.pptx`, then export PDF/PNGs. Absolute paths; the PNG output folder must exist.

### Recipe: 5-slide review deck (tested)

```text
new_presentation {theme:"Harbor"}
set_text {id:258, text:"Northwind Q3 Review"} · set_text {id:259, text:"Leadership update - October 2026"}
run_command design.background {color:"#12384D", index:0}
select {ids:[258,259]} → run_command format.color {color:"#FFFFFF"}
run_command slide.notes {text:"Welcome. Twenty minutes, questions at the end.", index:0}

add_slide {layout:"titleAndContent", title:"Highlights"}  → inspect_slide → body placeholder id (here 262)
set_text {id:262, text:"Revenue up 12% quarter on quarter\nTwo new markets\n\tPorto\n\tWarsaw\nChurn down to 2.1%"}
run_command animation.add {effect:"fade", ids:[262]} → run_command animation.options {textBuild:"byParagraph", index:0}

add_slide {layout:"titleOnly", title:"Revenue by region"}
run_command insert.chart {type:"column", rect:[80,140,800,370], categories:["North","South","East"],
                          series:[{name:"Q2", values:[420,310,280]}, {name:"Q3", values:[470,355,300]}]}
run_command chart.options {title:null, dataLabels:true, legend:"b"}

add_slide {layout:"titleOnly", title:"Team"}
insert_table {rows:3, cols:2, x:80, y:150, w:800, h:150, data:[["Name","Role"],["Ana","Lead"],["Raj","QA"]]}
run_command table.style {style:"medium2-accent2"}

add_slide {layout:"twoContent", title:"Product snapshot"}       → placeholders 271 (left), 272 (right)
set_text {id:271, text:"Faster sync engine\nOffline mode\n\tiOS and Android"}
insert_picture {path:"/abs/chart.png", x:488, y:170, w:412, h:206} → run_command edit.delete {ids:[272]}

run_command design.headerFooter {slideNumber:true, footer:true, footerText:"Northwind - Confidential", hideOnTitle:true}
run_command transition.set {kind:"fade", duration:600} → run_command transition.applyAll
render_slide {slide:i, scale:0.6} for each slide  → look, fix
save_presentation {path:"/abs/deck.pptx"}
run_command file.export {path:"/abs/deck.pdf", format:"pdf"}
run_command file.export {path:"/abs/deck-notes.pdf", format:"pdf", layout:"notes"}       (or handouts, perPage:6)
export {path:"/abs/png/slide.png", format:"png", all:true, scale:1}   → png/slide1.png … (folder must exist)
```

### Recipe: diagram slide with shapes (tested)

```text
add_slide {layout:"blank"}
add_shape {preset:"roundRect", x:60,  y:60, w:260, h:140, fill:"accent1", line:"none", text:"Plan"}
add_shape {preset:"roundRect", x:350, y:60, w:260, h:140, fill:"accent2", line:"none", text:"Build"}
add_shape {preset:"roundRect", x:640, y:60, w:260, h:140, fill:"#F78154", line:"none", text:"Ship"}
add_text_box {x:60, y:300, w:840, text:"Three phases, one team.", size:40, align:"center", color:"#12384D"}
select {ids:[<the three ids>]} → run_command format.size {size:28} → run_command format.bold
run_command shape.connect {from:<id A>, to:<id B>, preset:"straightConnector1"}   ← glued connector
select {ids:[…]} → run_command shape.effects {shadow:"outer"}
```

### Recipe: edit an existing deck (tested)

```text
open_presentation {path:"/abs/deck.pptx"} → inspect_document          (slide titles, notes, transitions)
run_command slide.notes {text:"…", index:0} · go_to_slide {index:1} → inspect_slide → set_text {id, text}
run_command design.theme {name:"Slate"}                                (accent fills and fonts follow; hex colours stay)
save_presentation {path:"/abs/deck-v2.pptx"}                           (notes, animations, transitions survive)
```

## Formats

- **Open:** .pptx .deckcraft. **Save:** .pptx .deckcraft. **Export:** PDF (`slides`, `notes`, `handouts` with `perPage`
  1/2/3/4/6/9), PNG/JPEG (one slide or all), outline text (`format: "outline"`).
- PDF has selectable text; `deckcraft-cli convert deck.pptx deck.pdf` does it without MCP.

## CLI (no MCP needed)

```bash
deckcraft-cli info deck.pptx                          # JSON: slides, layouts, theme, notes
deckcraft-cli render deck.pptx /abs/outdir --all --scale 0.5   # outdir/slide-01.png … (OUT is a folder with --all)
deckcraft-cli render deck.pptx slide3.png --slide 2
deckcraft-cli convert deck.pptx deck.pdf
deckcraft-cli run --cmd 'file.new={"theme":"Ember"}' \
  --cmd 'slide.fromOutline={"text":"Agenda\n\tWhy now\n\tPlan\nRisks\n\tBudget"}' --save /abs/o.pptx --export /abs/o.pdf
deckcraft-cli commands [FILTER]  ·  deckcraft-cli describe shape.fill     # one command's params
```

## Pitfalls

- **`insert_chart` has no position** and lands over the title. Use `run_command insert.chart {…, rect:[80,140,800,370]}`,
  or move it with `shape.setBounds {x, y, w, h, ids}`.
- **`add_slide {body}` doesn't indent:** a leading tab becomes a literal tab after the bullet. Put nested bullets in with
  `set_text {id, text}` on the body placeholder (tabs there set levels correctly).
- **Placeholders you don't fill stay on the slide.** Delete unused ones (`edit.delete {ids}`) after putting a picture or
  chart in their place, or use `titleOnly`/`blank` layouts.
- `animation.options` without `index` fails: `no animation to change (select an animated object or give index)`.
  Use `index` (0-based on the current slide) or select the shape.
- `export {all:true}` writes `<stem>1.png`, `<stem>2.png`… and fails with `os error 3` if the folder doesn't exist.
  `export` has no `pdf` format; use `run_command file.export {format:"pdf"}`.
- `shape.connect` with a wrong id says `both shapes need connection sites` rather than "not found". Check ids with `inspect_slide`.
- `deckcraft-cli run --cmd file.new` makes a *second* document (the run starts with one); the active (new) one is saved.
  `slide.fromOutline` appends after the existing empty title slide.
- Text inside `add_shape` shapes comes out small; size it with `select` + `format.size`.
- **Use theme colours (`accent1`..`accent6`) for anything that should follow a retheme.** Hex fills and text colours stay put
  when you run `design.theme` (and `inspect_slide` reports both as resolved hex, so you can't tell them apart later).
- Errors are explicit, e.g. ``unknown command `shape.fil` `` or ``invalid parameters for `slide.layout`: no layout "bogus" ``. Look ids up with
  `list_commands {filter}` or `deckcraft-cli describe ID`; don't invent them.
- UI-only tools fail headless: `screenshot: it needs the desktop app: start deckcraft --control 7979 …`. Use `render_slide`.

## Verification

- `inspect_document`: slide count, titles, layouts, `notes`, `transition`, `animations` per slide.
- `render_slide` every slide and look before reporting done.
- `deckcraft-cli info out.pptx` reopens the saved file; `export {format:"outline"}` gives a quick text check.

## References

- `references/commands.md`: all 222 commands with params, menu place and shortcut. Grep it (`grep -n 'chart[.]' …`).
- `references/catalogs.md`: themes, colour/font schemes, 145 shape presets, 49 transitions, 64 animation effects.
- Upstream docs: https://github.com/storytold/deckcraft/tree/main/docs (`mcp.md`, `control-protocol.md`).
