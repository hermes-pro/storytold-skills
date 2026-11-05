---
name: gridcraft
description: "Spreadsheets with GridCraft (Excel-style): budgets, sales reports, financial models, data analysis, pivot tables, charts and dashboards. Enter data and formulas (SUM, XLOOKUP, SUMIFS, dynamic arrays), format numbers, sort, filter, Solver and forecasts, and open / save XLSX, XLS, ODS, CSV, TSV, JSON, HTML or export PDF."
version: 0.5.0
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
This skill is tested against GridCraft 0.16.1.

## When to Use

Use it for **tabular data and anything that calculates**:

- budgets, invoices, price lists, timesheets, gradebooks, trackers
- financial models: loans (`PMT`), NPV/IRR, what-if (`data.goalSeek`, scenarios, data tables, `data.solver`)
- analysing a CSV/XLSX: totals by group (`SUMIFS`, PivotTables), lookups, dedupe, sort, filter
- statistics and forecasting: regression, descriptive stats, histograms (`data.analysisToolPak`),
  `data.forecastSheet` (FORECAST.ETS with confidence bounds and a chart)
- charts from table data (column, bar, line, pie, scatter, waterfall, …) and PDF reports of a sheet
- converting between XLSX, CSV, TSV, JSON, HTML and PDF; importing old .xls, .xlsb and .ods files
- repeatable jobs as **macros** saved in the workbook (typed command lists with checked inputs, not VBA)

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
2. Otherwise check for the CLI with `gridcraft-cli --version`. If it's missing, load the `storytold-install`
   skill and run its `setup gridcraft`. Then ask the user to start a new session or run `/reload-mcp`.
3. Until the MCP tools appear, use the CLI one-shots (see **CLI**), which take the same command ids.

Without a running desktop app the server is **headless** (in-process engine, no window). Everything works
except `screenshot`. For the user to watch live, they run `gridcraft --control 7979` and the server is
started as `gridcraft-cli mcp --connect 7979`. `gridcraft-cli mcp --in book.xlsx` (or `--sample budget`) starts
with a workbook already open. Those are the only MCP flags.

## Mental Model

- A **workbook** has **sheets**; cells are addressed A1-style: `"B2"`, `"A1:D10"`, `"B:B"`, `"Sheet2!A1:C3"`.
  Several workbooks can be open; `new_workbook` / `open_workbook` make the new one active. `list_windows`
  gives each window a `window` id and each workbook a `doc` id; pass either to a tool to act there without
  switching (default: the active window).
- **Input is parsed like typing**: `"=…"` is a formula, `"12%"`, `"$5"`, `"1/2/2024"` become numbers with a
  format, `"'0012"` forces text. Formulas recalculate automatically (dependency graph, dynamic arrays spill).
  `I1#` refers to a whole spill range; `A1:.F1000` trims blank outer rows/columns (trim-range operator).
- **Every action is a command** (377 of them: `home.*`, `data.*`, `insert.*`, `chart.*`, `pivot.*`, …). The
  dedicated tools cover the common flow; `execute_command {command, params}` runs anything else. Find ids with
  `list_commands {search}` or grep `references/commands.md`.
- Commands without `range` act on the **selection** (`select`). Programmatic calls never open dialogs: a
  missing required param is an error that names it.
- Every change is one undo step (`undo` / `redo`); `inspect_workbook` lists the history.

## Tools (Hermes names them `mcp_gridcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `inspect_workbook` | Sheets, used ranges, tables, charts (ids), merges, filters, freeze, names, selection, history |
| `list_windows` | Open windows: `window` id, workbook `doc` id, title, `dirty`, `active`, `hidden` |
| `write_range {range, values, parse?}` | A 2-D block of values/formulas from a top-left cell. One undo step. The fastest way to build a sheet. `parse:false` stores strings as text (`"0012"`, `"05.04.2026"`); `converted` lists the strings read as numbers or dates |
| `set_cell {cell, input}` | One cell, as typed (`input` may also be a JSON number or boolean). Returns the value as display text (`"171"`) |
| `read_range {range?, sheet?, formulas?, formatted?}` | Values back (default: used range). `formulas: true` shows the formula text, `formatted: true` the display text |
| `get_cell {cell}` | Value, type, formula, display text, spill range, full style, merge, comment |
| `evaluate_formula {formula, cell?}` | Try a formula without touching the sheet (great for checking answers) |
| `format_range` | `bold`, `italic`, `underline`, `fontName`, `fontSize`, `fontColor`, `fillColor`, `numberFormat`, `horizontalAlign`, `wrapText`, `borders` in one call |
| `insert_chart {range, type, title?, subtype?, at?}` | Chart from a block with headers; returns the chart id |
| `create_table {range, name?, style?, header?}` | Excel table: banding, filter buttons, structured refs `Name[Column]` |
| `sort_range {keys, range?, header?}` | `keys: [{"column":"G","order":"desc"}]` or `["B"]` |
| `filter {column, values?\|custom?\|top?\|clear?, range?}` | AutoFilter one column (hides rows). Works on a plain range and inside a table |
| `select {range, active?}` | Set the selection; `"Sheet2!A1"` switches sheet |
| `open_workbook` / `save_workbook` / `new_workbook {sample?}` | Files (see Formats); samples `budget`, `sales`, `grades` |
| `list_functions {search?, category?}` | The 515 worksheet functions with signatures |
| `list_commands` / `execute_command` | Everything else |
| `undo` / `redo` | History |
| `screenshot {path}` | Desktop app only (`--connect`) |

Every tool that acts on a workbook also takes `window` or `doc` (ids from `list_windows`).

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
- **Trendline:** `chart.addElement {chart, element:"trendline", type:"linear", displayEquation:true}` (also
  `exponential`, `linearForecast`, `movingAverage`, `logarithmic`, `power`, `polynomial`; `forward` periods).
- **PivotTable:** `insert.pivotTable {source:"Orders", rows:["Region"], columns:["Product"], values:[{field:"Revenue", func:"sum"}]}`.
  Then `pivot.calculatedField {name:"AvgPrice", formula:"=Revenue/Units"}` (works on the field sums) and
  `insert.pivotChart {type:"column", title, at:"F3"}` (the pivot at the active cell, or `pivot:"PivotTable1"`).
  Several value fields stacked under each row label: `pivot.moveField {field:"Σ Values", from:"columns", to:"rows"}`.
  `pivot.showDetails {cell:"B5"}` lists the source records behind a value on a new sheet.
- **Slicer on a table:** `insert.slicer {table:"Orders", column:"Region", at:"I2"}` → `{slicer}`, then
  `slicer.toggle {value:"East"}` filters the table, `slicer.clear` shows all. `SUBTOTAL(109, …)` sums only visible rows.
- **Equations:** `insert.equation {latex:"x^2+\\frac{a}{b}", cell:"B2"}` → `{equation}`; `equation.edit {id, latex}`.
- **Python cells** (`python.set {cell, code}`) are stored and saved as Excel's `PY` formula, but no code runs.

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
execute_command {command:"file.exportCsv", params:{path:"/abs/sales_raw.csv", values:true}}
execute_command {command:"file.exportPdf", params:{path:"/abs/sales.pdf", fitToPage:true}}
```

The PDF contains the table, the colour scale and the chart on one page. `sales.csv` holds the displayed text
(`"$12,000.00"`); `sales_raw.csv` with `values:true` holds the numbers (`12000`), see Formats.

### Recipe: analyse a CSV (tested)

```text
open_workbook {path:"/abs/orders.csv"}                    → sheet named after the file ("orders")
read_range {range:"A1:F3"}                                → see the columns
set_cell {cell:"G1", input:"Revenue"} · set_cell {cell:"G2", input:"=E2*F2"}
execute_command {command:"edit.fillDown", params:{range:"G2:G41"}}
create_table {range:"A1:G41", name:"Orders"}
evaluate_formula {formula:"=SUMIFS(Orders[Revenue],Orders[Region],\"North\")"}
set_cell {cell:"I1", input:"=SORT(UNIQUE(Orders[Rep]))"}  → spills I1:I4
set_cell {cell:"J1", input:"=COUNTA(I1#)"}                → 4 (I1# = the whole spill)
sort_range {range:"A1:G41", keys:[{column:"G", order:"desc"}], header:true}
filter {column:"B", values:["North"]}                     → {hiddenRows: 34}; SUBTOTAL(109,Orders[Revenue]) = North only
filter {column:"B", clear:true}
execute_command {command:"insert.pivotTable", params:{source:"Orders", rows:["Region"],
                 columns:["Product"], values:[{field:"Revenue", func:"sum"}]}}   → new sheet, report at A3
save_workbook {path:"/abs/orders.xlsx"}
```

To keep every CSV field as text (ids with leading zeros, no date guessing), open it with
`execute_command {command:"file.open", params:{path, csvAsText:true}}`.

Other tested formulas: `VLOOKUP`, `XLOOKUP`, `IF`, `LET`, `FILTER`, `TEXT(DATE(…),"yyyy-mm-dd")`, `PMT`,
cross-sheet `=Data!A2*10`, named ranges, `SUBTOTAL(109,…)` (skips filtered rows), `ROWS(A1:.F1000)`,
functions passed by name (`=GROUPBY(B2:B41,E2:E41,SUM)`, `=BYROW(E2:F4,SUM)`) or as a `LAMBDA`
(`=GROUPBY(B2:B41,G2:G41,LAMBDA(x,MAX(x)))`).
Grep `references/functions.md` before using a rarer function.

### Recipe: optimise with Solver, then what-if (tested)

```text
write_range {range:"A1", values:[["Product","Qty","Profit/unit","Hours/unit","Material/unit"],
  ["Chairs",0,45,2,3],["Tables",0,80,5,2],["Desks",0,110,6,5],
  ["Profit","=SUMPRODUCT(B2:B4,C2:C4)"],["Hours","=SUMPRODUCT(B2:B4,D2:D4)",null,"Limit",400],
  ["Material","=SUMPRODUCT(B2:B4,E2:E4)",null,"Limit",300]]}
execute_command {command:"data.solver", params:{objective:"B5", goal:"max", variables:"B2:B4",
                 constraints:["B6 <= E6","B7 <= E7","B2:B4 int"], method:"simplex"}}
  → {status:"optimal", objective:7220, values:{B2:62, B3:54, B4:1}}   (writes the values into B2:B4)
execute_command {command:"data.goalSeek", params:{set:"B5", to:10000, changing:"B2"}}  → {value, converged}
```

`method:"grg"` (default) handles nonlinear models; `keep:false` restores the original values. The model is
saved as hidden `solver_*` names. `reports:["answer","sensitivity","limits"]` writes the report sheets before the
model's sheet (the model sheet stays active) and returns their names; Sensitivity and Limits need `simplex` or
`grg` and no `int`/`bin` constraints. A refused report refuses the whole solve: the sheet stays unchanged.
`data.solverSaveModel {to:"H1"}` / `data.solverLoadModel {from:"H1"}` keep several models on a sheet;
`data.solverReset` removes it.
`method:"evolutionary"` (non-smooth models) needs both bounds on every variable (`"B2:B4 <= 200"`) or
`requireBounds:false`; set `randomSeed` for repeatable runs. It is slow and approximate (it hit the 20,000
evaluation limit at 7196 where simplex found 7227), so prefer `simplex` / `grg` when they apply.
Scenarios: `data.scenarioAdd`, `data.scenarioSummary`; tables: `data.dataTable`.

### Recipe: forecast and regression (tested)

```text
write_range {range:"A1", values:[["Month","Sales","Ads"],["2025-01-01",120,10], …12 months…]}
execute_command {command:"data.analysisToolPak", params:{tool:"regression", inputY:"B1:B13",
                 inputX:"C1:C13", labels:true, output:"E1"}}     → SUMMARY OUTPUT at E1:M18 (static values)
execute_command {command:"data.forecastSheet", params:{range:"A1:B13", periods:6}}
  → {sheet, table, chart, history, periods, fitted}: a new sheet before the current one with Forecast /
    Lower / Upper Confidence Bound columns (FORECAST.ETS formulas) and a line chart
```

The forecast columns come unformatted (`232.3090909`); apply `numberFormat:"0.0"`. Other ToolPak tools:
`descriptive`, `correlation`, `histogram`, `movingAverage`, `exponentialSmoothing`, t-tests, `fTest`, `anovaSingle`.

### Recipe: a macro saved in the workbook (tested)

```text
write_range {range:"A1", values:[["Item","Cost"],["Rent",1200],["Food",40],["Fuel",300]]}
execute_command {command:"macro.save", params:{macro:{name:"Totals", description:"Adds a total",
  inputs:[{name:"Input", header:true, cols:[2,2], colTypes:["text","number"]}],
  output:{anchor:"Input.right(2).cell(1,2)", onConflict:"ask"},
  steps:[{type:"command", id:"cell.set", params:{cell:"Output", input:"Total"}},
         {type:"command", id:"cell.set", params:{cell:"Output.offset(1,0)", input:"=SUM({{Input.data.col(2)}})"}},
         {type:"repeat", over:"Input.data", of:"rows", max:1000, body:[
           {type:"if", cell:"Row.cell(1,2)", op:"gt", value:100,
            then:[{type:"command", id:"home.bold", params:{range:"Row"}}]}]}]}}}
execute_command {command:"macro.check", params:{name:"Totals", inputs:"A1:B4"}}   → {ok:true, footprint, output:"D1"}
execute_command {command:"macro.run", params:{name:"Totals", inputs:"A1:B4"}}     → D1 "Total", D2 =SUM(B2:B4), rows over 100 bold
save_workbook {path:"/abs/book.xlsx"}                                             → the macro is saved in the file
```

A macro runs as one undo step and rolls back on any error. Bad inputs are refused with the cell named
(`Macro 'Totals' can't run on these inputs. Input column 2 (Cost) must hold numbers; G2 holds text.`). A macro from
a workbook opened from a file needs `approve:true` (``approve: Run macro 'Totals'? It came with a workbook you
opened. (run again with `approve: true`)``); so does one that reads or writes files (and the command must be in its
`permissions`). Tokens, steps and limits: https://github.com/storytold/gridcraft/blob/main/docs/macros.md.

## Formats

- **Open:** .xlsx .xlsm .csv .tsv .txt .json; .xls (values, formulas, number formats); .xlsb and .ods (data and
  cached formula values only, check `warnings` in the result). `file.open {path, password}` opens an encrypted file.
- **Save** (`save_workbook`, by extension): .xlsx (default, everything round-trips, unknown parts and macros are
  kept), .csv / .tsv (**active sheet only**, the **displayed text**: `"$12,000.00"`, `2026-01-05`), .json, .html, .pdf
  (active sheet, no fit-to-page). `file.exportCsv {path, sheet?, values?}` picks the sheet; `values:true` writes raw
  values (full-precision numbers, ISO dates, TRUE/FALSE). Any other extension is refused
  (`x.foo: unknown file format. Save as .xlsx, .csv, .tsv, .json or .html.`, though .pdf works).
- **PDF:** `file.exportPdf {path, sheets?: "active"|"all", range?, fitToPage?}` → `{pages, bytes, path}`; it honours
  Page Setup (`pageLayout.orientation`, `pageLayout.scaleToFit`, `pageLayout.printArea`, `pageLayout.printTitles`).

## CLI (no MCP needed)

```bash
gridcraft-cli eval '=PMT(5%/12,360,-300000)'                 # 1610.46…   (--in book.xlsx [--sheet S] [--cell A1] for refs)
gridcraft-cli info book.xlsx [--json]                         # sheets, used ranges, tables, charts, names
gridcraft-cli cat book.xlsx [--range A1:F20] [--sheet S] [--formulas] [--csv]
gridcraft-cli convert book.xlsx data.csv [--sheet Sales]      # xlsx/csv/tsv/json/html/pdf by extension
gridcraft-cli run [--in FILE | --sample budget] --cmd 'home.bold={"range":"A1:D1"}' \
                  [--script steps.jsonl] --out book.xlsx --print A1:F5 [--formulas] [--quiet]
gridcraft-cli check book.xlsx|DIR... [--json] [--tolerance 1e-9]   # recalc vs cached values + XLSX round trip
gridcraft-cli commands --search chart  ·  gridcraft-cli functions --search lookup [--category Lookup]
```

`check` recalculates every formula against the values Excel cached and re-saves the file; exit 1 on any
difference. Use it on an Excel file before trusting GridCraft's numbers for it.

A `--script` file has one command per line, `id {json}`, `id={json}` or `{"command":…, "params":…}`; `#` and `//`
lines are comments. The first failing step stops the run with exit 1 (`step 2 (steps.jsonl:2, bogus.cmd): unknown
command \`bogus.cmd\``). Tested on 0.16.1: a 13-step budget script (values, number format code, validation, two
sparklines, named range, merge, bar chart, `chart.set`, PDF), then `info`, `cat --formulas`, `eval --in`,
`convert` to CSV and PDF (`convert` has no fit-to-page: the sheet with its chart took 2 pages) and `check`.

## Pitfalls

- **Use absolute paths** for `open_workbook`, `save_workbook` and `file.exportPdf`: the server's cwd isn't yours.
- **A failed `filter` still adds a "Filter Column" undo step** (e.g. ``filter: invalid parameters for
  `data.filterBy`: column outside the filter range``) and leaves an AutoFilter behind (on A1 of a blank sheet, on
  the first column of a given `range`). The next `undo` removes that step, not your last real change. Check
  `inspect_workbook` → `undo` first.
- **Opening a file that is already open does nothing else**: `open_workbook` / `file.open` returns
  `{alreadyOpen: true, index}` and ignores new options such as `csvAsText`. Close it first (`file.close`).
- **`list_functions {category}` needs the internal names** (`MathTrig`, `Lookup`, `Statistical`, `Text`,
  `DateTime`, …). The schema's example `"Math & Trig"` returns `[]`. Usually just use `search`.
- **CSV dates become date serials** (`read_range` gives `46027`, `formatted:true` gives `2026-01-05`). Compare
  them with `DATE(…)` in formulas, not with text.
- **CSV / TSV export writes displayed text**, not raw numbers: a `Currency` cell becomes `"$12,000.00"`
  (`save_workbook`, `convert` and `cat --csv` too). For machine-readable numbers use
  `file.exportCsv {path, values:true}`. The .json save is GridCraft's internal model, not a table.
- **The pivot sheet becomes active** (inserted before the current sheet, report at A3), and so does the sheet
  from `data.forecastSheet`, `data.analysisToolPak` without `output`, or `home.insertSheet`. Later
  unqualified ranges then hit that sheet; use `Sheet!A1` or `sheet.activate`.
- **CSV / TSV save only the active sheet.** Activate the right one or use `file.exportCsv {sheet}`.
- **A typo'd function doesn't error**: `set_cell` stores `=SUMM(1,2)` and the value is `#NAME?`. Read values back.
  A wrong argument count is refused on entry: `ROUND has too few arguments. Use ROUND(number, num_digits)`.
- **Formulas over 8,192 characters are refused** like Excel (`There's a problem with this formula: formula is
  longer than 8192 characters`), and so is very deep nesting (`… formula is nested too deeply`). Split long
  formulas into helper cells or use `LET`.
- **Bar charts are horizontal**: `chart.set {yTitle}` labels the vertical (category) axis there.
- **`file.exportPdf` without `fitToPage: true` splits a wide sheet across pages** (the chart beside the table
  lands on page 2). `save_workbook {path:"x.pdf"}` has no fit option, so use `file.exportPdf` for reports.
- **Autofit after styling**: a bigger font (`home.cellStyle "Heading 1"`) clips headers until `home.autofitColumnWidth`.
  Dates from a CSV print as `#######` in the PDF until the column is autofit too.
- Icon-set conditional formats (`type:"iconSet"`) are stored but don't show in the PDF export; data bars, colour
  scales and fills do. Slicers don't print either.
- **`insert.pivotChart` charts every value field** as a series, so `Sum of Units` next to `Sum of Revenue` is a
  flat line. Give the pivot one value field (or two of the same scale) before charting it.
- `filter` only hides rows; `read_range` still returns hidden rows.
- Unknown ids give `unknown command \`x\``; missing params give e.g.
  `invalid parameters for \`home.numberFormat\`: missing \`format\` or \`code\``. Check with `list_commands {search}`.
- `screenshot` in headless mode errors (`screenshot: no UI in headless mode: start the app with \`gridcraft
  --control 7979\` …`). Export a PDF to look at the sheet instead.

## Verification

- `read_range` (values) and `read_range {formatted:true}` (what a reader sees) match the intent; no `{"error":…}`.
- `inspect_workbook` shows the expected sheets, tables, charts, conditional formats, freeze and names.
- To **look** at layout, charts and colours: `file.exportPdf`, render the page to PNG (e.g.
  `pdftoppm -r 90 -png out.pdf page` or `vectorcraft-cli convert out.pdf page.png --artboard 0`) and check the image.
- `gridcraft-cli info out.xlsx` and `gridcraft-cli cat out.xlsx --formulas` confirm the saved file reopens;
  `gridcraft-cli check out.xlsx` confirms formulas and round trip.

## References

- `${HERMES_SKILL_DIR}/references/commands.md`: all 377 commands with params, grouped by area. Grep it
  (`grep -n "data.solver" …`) rather than reading it whole.
- `${HERMES_SKILL_DIR}/references/functions.md`: all 515 worksheet functions with signatures, grouped by
  category. Grep it.
- Upstream docs: https://github.com/storytold/gridcraft/tree/main/docs (`mcp.md`, `cli.md`, `macros.md`, `control-protocol.md`).
