---
name: gridcraft
description: "Spreadsheets with GridCraft (Excel-style): budgets, sales reports, financial models, data analysis, pivot tables, charts and dashboards. Enter data and formulas (SUM, XLOOKUP, SUMIFS, dynamic arrays), format numbers, sort, filter, and open / save XLSX, CSV, TSV, JSON, HTML or export PDF."
version: 0.1.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Office, Spreadsheet, Excel, XLSX, CSV, Data, Formulas, Charts, Finance, MCP]
    related_skills: [storytold, storytold-install, deckcraft, wordcraft, vectorcraft, pdfcraft]
---

# GridCraft

GridCraft is a free, open-source clean-room take on Microsoft Excel (storytold Crafting Apps). An agent
drives it through an MCP server (`gridcraft-cli mcp`) or one-shot CLI commands. XLSX is the native format,
so formulas, styles, conditional formats, tables, charts, validation and PivotTables round-trip to Excel.

## When to Use

Use it for **tabular data and anything that calculates**:

- budgets, invoices, price lists, timesheets, gradebooks, trackers
- financial models: loans (`PMT`), NPV/IRR, what-if (`data.goalSeek`, scenarios, data tables)
- analysing a CSV/XLSX: totals by group (`SUMIFS`, PivotTables), lookups, dedupe, sort, filter
- charts from table data (column, bar, line, pie, scatter, waterfall, …) and PDF reports of a sheet
- converting between XLSX, CSV, TSV, JSON and HTML

Pick a different Crafting App when:

| The job is… | Use |
|---|---|
| A report or letter where prose matters more than the numbers | `wordcraft` |
| Slides presenting the numbers | `deckcraft` |
| A designed infographic / poster chart | `vectorcraft` |
| Editing pages or forms of an existing PDF | `pdfcraft` |
| Technical drawings, floor plans | `cadcraft` |

## Setup

1. If tools named `mcp_gridcraft_*` are available, use them. This is the preferred way.
2. Otherwise check for the CLI with `gridcraft-cli version`. If it's missing, load the `storytold-install`
   skill and run its `setup gridcraft`. Then ask the user to start a new session or run `/reload-mcp`.
3. Until the MCP tools appear, use the CLI one-shots (see **CLI**), which take the same command ids.

Without a running desktop app the server is **headless** (in-process engine, no window). Everything works
except `screenshot`. For the user to watch live, they run `gridcraft --control 7979` and the server is
started as `gridcraft-cli mcp --connect 7979`.

## Mental Model

- A **workbook** has **sheets**; cells are addressed A1-style: `"B2"`, `"A1:D10"`, `"B:B"`, `"Sheet2!A1:C3"`.
  Several workbooks can be open; `new_workbook` / `open_workbook` make the new one active.
- **Input is parsed like typing**: `"=…"` is a formula, `"12%"`, `"$5"`, `"1/2/2024"` become numbers with a
  format, `"'0012"` forces text. Formulas recalculate automatically (dependency graph, dynamic arrays spill).
- **Every action is a command** (313 of them: `home.*`, `data.*`, `insert.*`, `chart.*`, `pivot.*`, …). The
  dedicated tools cover the common flow; `execute_command {command, params}` runs anything else. Find ids with
  `list_commands {search}` or grep `references/commands.md`.
- Commands without `range` act on the **selection** (`select`). Programmatic calls never open dialogs: a
  missing required param is an error that names it.
- Every change is one undo step (`undo` / `redo`); `inspect_workbook` lists the history.

## Tools (Hermes names them `mcp_gridcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `inspect_workbook` | Sheets, used ranges, tables, charts (ids), merges, filters, freeze, names, selection, history |
| `write_range {range, values}` | A 2-D block of values/formulas from a top-left cell. One undo step. The fastest way to build a sheet |
| `set_cell {cell, input}` | One cell, as typed. Returns the computed value |
| `read_range {range?, sheet?, formulas?, formatted?}` | Values back (default: used range). `formulas: true` shows the formula text, `formatted: true` the display text |
| `get_cell {cell}` | Value, type, formula, display text, spill range, full style, merge, comment |
| `evaluate_formula {formula, cell?}` | Try a formula without touching the sheet (great for checking answers) |
| `format_range` | `bold`, `italic`, `underline`, `fontName`, `fontSize`, `fontColor`, `fillColor`, `numberFormat`, `horizontalAlign`, `wrapText`, `borders` in one call |
| `insert_chart {range, type, title?, subtype?, at?}` | Chart from a block with headers; returns the chart id |
| `create_table {range, name?, style?, header?}` | Excel table: banding, filter buttons, structured refs `Name[Column]` |
| `sort_range {keys, range?, header?}` | `keys: [{"column":"G","order":"desc"}]` or `["B"]` |
| `filter {column, values?\|custom?\|top?\|clear?, range?}` | AutoFilter one column (hides rows). Not on table ranges, see Pitfalls |
| `select {range, active?}` | Set the selection; `"Sheet2!A1"` switches sheet |
| `open_workbook` / `save_workbook` / `new_workbook {sample?}` | Files; samples `budget`, `sales`, `grades` |
| `list_functions {search?, category?}` | The 501 worksheet functions with signatures |
| `list_commands` / `execute_command` | Everything else |
| `undo` / `redo` | History |
| `screenshot {path}` | Desktop app only (`--connect`) |

Resources: `gridcraft://workbook`, `gridcraft://commands`, `gridcraft://functions`. There are no prompts.

## Formatting and structure

- **Number formats:** `format_range {numberFormat}` takes a name (`Currency`, `Accounting`, `Percentage`,
  `Short Date`, `Comma`, `Text`, …) or a code (`"#,##0.00"`, `"0.0%"`, `"yyyy-mm-dd"`, `"$#,##0;[Red]-$#,##0"`).
- **Borders:** `borders: "all" | "outside" | "thickBottom" | "topDoubleBottom" | …` or `{preset, style, color}`.
- **Columns:** `home.autofitColumnWidth {cols:"A:H"}`, `home.columnWidth {cols:"B:D", chars: 14}`.
- **Freeze headers:** `view.freezeTopRow`, or `view.freezePanes {cell:"B2"}`.
- **Merge a title:** `home.mergeCenter {range:"A1:F1"}`. Cell styles: `home.cellStyle {name:"Title"|"Total"|"Good"…}`.
- **Conditional formatting:** `home.conditionalFormat {range, rule}` — e.g.
  `{type:"cellIs", operator:"greaterThan", value:"50000", preset:"greenFill"}`, `{type:"colorScale"}`,
  `{type:"dataBar"}`, `{type:"iconSet"}`, `{type:"expression", formula:"=$D2<0", preset:"lightRedFill"}`.
- **Validation:** `data.validation {range, type:"list", formula1:"Yes,No"}` or `type:"decimal", operator:"greaterOrEqual", formula1:"0"`.
- **Sheets:** `home.insertSheet {name}` (becomes active), `sheet.rename`, `sheet.activate {sheet}`, `sheet.tabColor`.
- **Names:** `formulas.defineName {name, refersTo:"=Sheet1!$C$2:$C$4"}`, then `=SUM(Actuals)`.
- **Charts after insert:** `chart.set {chart, title, legend:"bottom", dataLabels:true, xTitle, yTitle}`,
  `chart.changeColors {chart, colors:["#1F4E78","#ED7D31"]}`, `chart.changeType`, `chart.move`.
- **Sparklines:** `insert.sparkline {range:"B2:M2", location:"N2", type:"line"|"column"|"winLoss"}`.
- **PivotTable:** `insert.pivotTable {source:"Orders", rows:["Region"], columns:["Product"], values:[{field:"Revenue", func:"sum"}]}`.

## Procedure

1. **Plan the layout:** header row, one record per row, inputs separate from calculations, totals at the bottom.
2. **Enter data + formulas** with one `write_range` per block. Use relative formulas row by row, or write the
   first one and `edit.fillDown {range:"G2:G41"}`.
3. **Read back** with `read_range` and check the numbers (spot-check with `evaluate_formula`). Look for
   `{"error":"#NAME?"}` etc. in the values.
4. **Format:** headers, number formats, borders, column widths, freeze panes, conditional rules.
5. **Chart / pivot** if asked, then `chart.set` for legend, labels and axis titles.
6. **Save** `.xlsx` (the editable master), then export what was asked: `.csv`, `file.exportPdf`, `.html`.
7. **Verify** (below) before reporting.

### Recipe: quarterly sales report with chart and PDF (tested)

```text
write_range {range:"A1", values:[["Region","Q1","Q2","Q3","Q4","Total","Avg","Flag"],
  ["North",12000,13500,14100,15800,"=SUM(B2:E2)","=AVERAGE(B2:E2)","=IF(F2>50000,\"High\",\"Low\")"],
  …3 more regions…, ["Total","=SUM(B2:B5)","=SUM(C2:C5)","=SUM(D2:D5)","=SUM(E2:E5)","=SUM(F2:F5)",null,null]]}
format_range {range:"A1:H1", bold:true, fillColor:"#1F4E78", fontColor:"#FFFFFF", horizontalAlign:"center"}
format_range {range:"B2:G6", numberFormat:"Currency"}
format_range {range:"A6:G6", bold:true, borders:"topDoubleBottom"}
execute_command {command:"home.conditionalFormat", params:{range:"F2:F5",
                 rule:{type:"cellIs", operator:"greaterThan", value:"50000", preset:"greenFill"}}}
execute_command {command:"home.conditionalFormat", params:{range:"B2:E5", rule:{type:"colorScale"}}}
insert_chart {range:"A1:E5", type:"column", title:"Sales by Quarter", at:"J2"}   → {chart: 1}
execute_command {command:"home.autofitColumnWidth", params:{cols:"A:H"}}
execute_command {command:"view.freezeTopRow"}
read_range {range:"A1:H6", formatted:true}                                       → check
save_workbook {path:"/abs/sales.xlsx"}  ·  save_workbook {path:"/abs/sales.csv"}
execute_command {command:"file.exportPdf", params:{path:"/abs/sales.pdf", fitToPage:true}}
```

The PDF contains the table, the colour scale and the chart on one page.

### Recipe: analyse a CSV (tested)

```text
open_workbook {path:"/abs/orders.csv"}                    → sheet named after the file ("orders")
read_range {range:"A1:F3"}                                → see the columns
set_cell {cell:"G1", input:"Revenue"} · set_cell {cell:"G2", input:"=E2*F2"}
execute_command {command:"edit.fillDown", params:{range:"G2:G41"}}
create_table {range:"A1:G41", name:"Orders"}
evaluate_formula {formula:"=SUMIFS(Orders[Revenue],Orders[Region],\"North\")"}
set_cell {cell:"I1", input:"=SORT(UNIQUE(Orders[Rep]))"}  → spills I1:I4
sort_range {range:"A1:G41", keys:[{column:"G", order:"desc"}], header:true}
execute_command {command:"insert.pivotTable", params:{source:"Orders", rows:["Region"],
                 columns:["Product"], values:[{field:"Revenue", func:"sum"}]}}   → new sheet, report at A3
save_workbook {path:"/abs/orders.xlsx"}
```

Other tested formulas: `VLOOKUP`, `XLOOKUP`, `IF`, `LET`, `FILTER`, `TEXT(DATE(…),"yyyy-mm-dd")`, `PMT`,
cross-sheet `=Data!A2*10`, named ranges. Grep `references/functions.md` before using a rarer function.

## Formats

- **Open:** .xlsx .xlsm .csv .tsv .txt .json
- **Save** (`save_workbook`, by extension): .xlsx (default, everything round-trips), .csv / .tsv (**active sheet
  only**, computed values), .json, .html. `file.exportCsv {path, sheet}` picks the sheet.
- **PDF:** `file.exportPdf {path, sheets?: "active"|"all", range?, fitToPage?}` → `{pages, bytes, path}`; it honours
  Page Setup (`pageLayout.orientation`, `pageLayout.scaleToFit`, `pageLayout.printArea`, `pageLayout.printTitles`).

## CLI (no MCP needed)

```bash
gridcraft-cli eval '=PMT(5%/12,360,-300000)'                 # 1610.46…   (--in book.xlsx for sheet refs)
gridcraft-cli info book.xlsx [--json]                         # sheets, used ranges, tables, charts, names
gridcraft-cli cat book.xlsx [--range A1:F20] [--sheet S] [--formulas] [--csv]
gridcraft-cli convert book.xlsx data.csv [--sheet Sales]      # xlsx/csv/tsv/json/html by extension
gridcraft-cli run [--in FILE | --sample budget] --cmd 'home.bold={"range":"A1:D1"}' \
                  [--script steps.jsonl] --out book.xlsx --print A1:F5 [--formulas]
gridcraft-cli commands --search chart  ·  gridcraft-cli functions --search lookup
```

A `--script` file has one command per line, `id {json}`, `id={json}` or `{"command":…, "params":…}`; `#` lines
are comments. The first failing step stops the run with a non-zero exit. Tested: a 13-step budget script
(values, number format code, validation, sparkline, named range, merge, bar chart, `chart.set`, PDF).

## Pitfalls

- **Use absolute paths** for `open_workbook`, `save_workbook` and `file.exportPdf`: the server's cwd isn't yours.
- **`filter` fails on a table** (`create_table` range) with `filter: no filter`. Filter before making it a
  table, run `table.convertToRange` first, or use a `=FILTER(...)` formula instead.
- **Spill references `A1#` are not supported**: `There's a problem with this formula: unknown error literal`.
  Reference the spill range explicitly (`I1:I4`, see `get_cell` → `spill`) or nest the formulas.
- **`list_functions {category}` needs the internal names** (`MathTrig`, `Lookup`, `Statistical`, `Text`,
  `DateTime`, …). The schema's example `"Math & Trig"` returns `[]`. Usually just use `search`.
- **CSV dates arrive as serial numbers** (`46170`) with no format. Apply `numberFormat:"yyyy-mm-dd"` to the column.
- **The pivot sheet becomes active** (inserted before the current sheet, report at A3), and so does a new
  sheet from `home.insertSheet`. Later unqualified ranges then hit that sheet; use `Sheet!A1` or `sheet.activate`.
- **CSV / TSV save only the active sheet.** Activate the right one or use `file.exportCsv {sheet}`.
- **A typo'd function doesn't error**: `set_cell` stores it and the value is `#NAME?`. Read values back.
- **Bar charts are horizontal**: `chart.set {yTitle}` labels the vertical (category) axis there.
- **`file.exportPdf` without `fitToPage: true` splits a wide sheet across pages** and can cut a chart in half.
- **Autofit after styling**: a bigger font (`home.cellStyle "Heading 1"`) clips headers until `home.autofitColumnWidth`.
- Icon-set conditional formats (`type:"iconSet"`) are stored but don't show in the PDF export; data bars, colour
  scales and fills do.
- `filter` only hides rows; `read_range` still returns hidden rows.
- Unknown ids give `unknown command \`x\``; missing params give e.g.
  `invalid parameters for \`home.numberFormat\`: missing \`format\` or \`code\``. Check with `list_commands {search}`.
- `screenshot` in headless mode errors (`no UI in headless mode`). Export a PDF to look at the sheet instead.

## Verification

- `read_range` (values) and `read_range {formatted:true}` (what a reader sees) match the intent; no `{"error":…}`.
- `inspect_workbook` shows the expected sheets, tables, charts, conditional formats, freeze and names.
- To **look** at layout, charts and colours: `file.exportPdf`, render the page to PNG (e.g.
  `vectorcraft-cli convert out.pdf page.png --artboard 0`) and check the image.
- `gridcraft-cli info out.xlsx` and `gridcraft-cli cat out.xlsx --formulas` confirm the saved file reopens.

## References

- `references/commands.md`: all 313 commands with params, grouped by area. Grep it rather than reading it whole.
- `references/functions.md`: all 501 worksheet functions with signatures, grouped by category. Grep it.
- Upstream docs: https://github.com/storytold/gridcraft/tree/main/docs (`mcp.md`, `cli.md`, `control-protocol.md`).
