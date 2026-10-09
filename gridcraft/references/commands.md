# GridCraft command catalog

Generated from `gridcraft-cli commands --json` (GridCraft 0.3.0, 313 commands). Run any of them with
`execute_command {command, params}` (MCP) or `gridcraft-cli run --cmd 'id={json}'`. Check one live with
`list_commands {search}`. `?` = optional, `a|b` = choices, `→ {...}` = what it returns. Most commands act on the
selection when `range` is omitted.

## file

- `file.new` — New Workbook (File) [Cmd+N]: {sample?: "budget"\|"sales"\|"grades"}
- `file.open` — Open… (File) [Cmd+O]: {path} \| {name, base64} (xlsx, xlsm, csv, tsv, txt, json)
- `file.save` — Save (File) [Cmd+S]: {path?} (xlsx by default; .csv/.tsv/.json/.html by extension)
- `file.saveAs` — Save As… (File) [Cmd+Shift+S]: {path}
- `file.saveBytes` — Encode Workbook: {format?: xlsx\|csv\|tsv\|json\|html} → {base64}
- `file.close` — Close (File) [Cmd+W]: {force?: bool}
- `file.exportCsv` — Export as CSV (File › Export): {path, sheet?}
- `file.exportHtml` — Save as Web Page (File › Export): {path}
- `file.properties` — Properties (File): {title?, subject?, author?, company?, keywords?, description?}
- `file.exportPdf` — Export as PDF (File › Export): {path?, sheets?: active\|all, range?: "A1:F40" (active sheet), fitToPage?: bool} → {pages, bytes, path} or {pages, bytes, base64} when no path. Honours each sheet's Page Setup.
- `file.print` — Print… (File) [Cmd+P]: {path?, sheets?: active\|all, range?, fitToPage?: bool} → {pages, bytes, base64} — the PDF the UI hands to the system print dialog
- `file.printPreview` — Print Preview (File): {page? (1-based), sheets?: active\|all, range?, fitToPage?} → {pages, pageList: [{page, sheet, range, rows, columns, scale, paper, orientation, width, height}]}

## window

- `window.activate` — Switch Window (Window): {index}

## cell

- `cell.set` — Enter Cell: {cell?: "B2", input: "text, number or =formula", sheet?, array?: bool}
- `cell.get` — Get Cell: {cell?, sheet?} → value, formula, display text, style, comment, link
- `cell.toggleCheckbox` — Toggle Checkbox [Space]: {cell?}

## range

- `range.setValues` — Set Values: {range?: "A1", values: [[...]] (rows of numbers/strings/bools/null; strings starting with = are formulas)}
- `range.fill` — Fill Range With Input [Ctrl+Enter]: {range?, input}: enters the same input in every selected cell (relative formulas adjust)

## selection

- `selection.set` — Select: {range: "A1:B2,D4" \| cell, active?: "A1", sheet?}
- `selection.move` — Move Selection: {dr, dc, extend?: bool, jump?: bool (Ctrl+arrow), page?: bool}
- `selection.next` — Next Cell in Selection: {forward?: true, byRow?: false} (Enter/Tab inside a selection)
- `selection.currentRegion` — Select Current Region [Ctrl+Shift+8]: {}
- `selection.row` — Select Entire Row [Shift+Space]: {}
- `selection.column` — Select Entire Column [Ctrl+Space]: {}
- `selection.stats` — Selection Statistics: {} → count, sum, average, min, max

## edit

- `edit.selectAll` — Select All (Edit) [Cmd+A]: {} (current region first, then the whole sheet)
- `edit.goTo` — Go To… (Home › Editing › Find & Select) [Ctrl+G]: {reference: "B5" \| "Sheet2!A1:C3" \| name}
- `edit.goToSpecial` — Go To Special… (Home › Editing › Find & Select): {kind: blanks\|constants\|formulas\|comments\|lastCell\|currentRegion\|visible\|conditionalFormats\|dataValidation\|errors\|numbers\|text}
- `edit.undo` — Undo (Edit) [Cmd+Z]: {steps?: 1}
- `edit.redo` — Redo (Edit) [Cmd+Y]: {steps?: 1}
- `edit.copy` — Copy (Home › Clipboard) [Cmd+C]: {range?}
- `edit.cut` — Cut (Home › Clipboard) [Cmd+X]: {range?}
- `edit.paste` — Paste (Home › Clipboard) [Cmd+V]: {at?: "C3", text?: "tab-separated text from the system clipboard"}
- `edit.pasteSpecial` — Paste Special… (Home › Clipboard) [Ctrl+Cmd+V]: {what: all\|formulas\|values\|formats\|comments\|validation\|allExceptBorders\|columnWidths\|formulasAndNumberFormats\|valuesAndNumberFormats, operation?: none\|add\|subtract\|multiply\|divide, skipBlanks?, transpose?, link?}
- `edit.clearClipboard` — Cancel Copy [Escape]: {}
- `edit.clearAll` — Clear All (Home › Editing › Clear): {range?}
- `edit.clearFormats` — Clear Formats (Home › Editing › Clear): {range?}
- `edit.clearContents` — Clear Contents (Home › Editing › Clear) [Delete]: {range?}
- `edit.clearComments` — Clear Comments and Notes (Home › Editing › Clear): {range?}
- `edit.clearHyperlinks` — Clear Hyperlinks (Home › Editing › Clear): {range?}
- `edit.fillDown` — Fill Down (Home › Editing › Fill) [Cmd+D]: {range?}
- `edit.fillRight` — Fill Right (Home › Editing › Fill) [Cmd+R]: {range?}
- `edit.fillUp` — Fill Up (Home › Editing › Fill): {range?}
- `edit.fillLeft` — Fill Left (Home › Editing › Fill): {range?}
- `edit.autoFill` — AutoFill: {source: "A1:A2", target: "A1:A10", mode?: series\|copy\|formats\|values}: the fill-handle drag
- `edit.fillSeries` — Series… (Home › Editing › Fill): {range?, direction?: columns\|rows, type?: linear\|growth\|date\|autofill, step?: 1, stop?, dateUnit?: day\|weekday\|month\|year}
- `edit.flashFill` — Flash Fill (Home › Editing › Fill) [Cmd+E]: {range?}
- `edit.find` — Find… (Home › Editing › Find & Select) [Cmd+F]: {what, matchCase?, wholeCell?, lookIn?: formulas\|values, byColumns?, all?: bool, within?: sheet\|workbook}
- `edit.replace` — Replace… (Home › Editing › Find & Select) [Ctrl+H]: {what, with, matchCase?, wholeCell?, all?: true, within?: sheet\|workbook}
- `edit.formatPainter` — Format Painter (Home › Clipboard): {sticky?: bool} — first call picks up the selection's formats; with {apply: "C3:D4"} pastes them
- `edit.beginEdit` — Edit Cell [F2]: {}

## home

- `home.bold` — Bold (Home › Font) [Cmd+B]: {range?, on?: bool}
- `home.italic` — Italic (Home › Font) [Cmd+I]: {range?, on?}
- `home.underline` — Underline (Home › Font) [Cmd+U]: {range?, on?, style?: single\|double\|singleAccounting\|doubleAccounting}
- `home.doubleUnderline` — Double Underline (Home › Font): {range?}
- `home.strikethrough` — Strikethrough (Home › Font) [Cmd+Shift+X]: {range?, on?}
- `home.superscript` — Superscript (Home › Font): {range?, on?}
- `home.subscript` — Subscript (Home › Font): {range?, on?}
- `home.fontName` — Font (Home › Font): {range?, name: "Calibri"}
- `home.fontSize` — Font Size (Home › Font): {range?, size: 11}
- `home.increaseFontSize` — Increase Font Size (Home › Font) [Cmd+Shift+>]: {range?}
- `home.decreaseFontSize` — Decrease Font Size (Home › Font) [Cmd+Shift+<]: {range?}
- `home.fontColor` — Font Color (Home › Font): {range?, color: "#C00000" \| "auto" \| {theme: 4, tint: -0.25}}
- `home.fillColor` — Fill Color (Home › Font): {range?, color: "#FFFF00" \| "none" \| {theme, tint}}
- `home.borders` — Borders (Home › Font): {range?, preset: bottom\|top\|left\|right\|none\|all\|outside\|thickOutside\|thickBottom\|doubleBottom\|topBottom\|topThickBottom\|topDoubleBottom\|insideHorizontal\|insideVertical\|inside\|diagonalDown\|diagonalUp, style?: thin\|medium\|thick\|dashed\|dotted\|double\|hair…, color?}
- `home.formatCells` — Format Cells… (Home › Cells › Format) [Cmd+1]: {range?, style: {font?, fill?, borders?, align?, numFmt?, protection?}} (partial Style JSON merged in)
- `home.alignLeft` — Align Left (Home › Alignment) [Cmd+L]: {range?}
- `home.alignCenter` — Center (Home › Alignment) [Cmd+E]: {range?}
- `home.alignRight` — Align Right (Home › Alignment) [Cmd+R]: {range?}
- `home.justify` — Justify (Home › Alignment): {range?}
- `home.alignTop` — Top Align (Home › Alignment): {range?}
- `home.alignMiddle` — Middle Align (Home › Alignment): {range?}
- `home.alignBottom` — Bottom Align (Home › Alignment): {range?}
- `home.wrapText` — Wrap Text (Home › Alignment): {range?, on?}
- `home.shrinkToFit` — Shrink to Fit: {range?, on?}
- `home.increaseIndent` — Increase Indent (Home › Alignment) [Ctrl+Alt+Tab]: {range?}
- `home.decreaseIndent` — Decrease Indent (Home › Alignment) [Ctrl+Alt+Shift+Tab]: {range?}
- `home.orientation` — Orientation (Home › Alignment): {range?, angle: -90..90 \| "vertical" \| "counterclockwise" \| "clockwise" \| "up" \| "down" \| 0}
- `home.mergeCenter` — Merge & Center (Home › Alignment): {range?}
- `home.mergeAcross` — Merge Across (Home › Alignment): {range?}
- `home.mergeCells` — Merge Cells (Home › Alignment): {range?}
- `home.unmergeCells` — Unmerge Cells (Home › Alignment): {range?}
- `home.numberFormat` — Number Format (Home › Number): {range?, format: "General"\|"Number"\|"Currency"\|"Accounting"\|"Short Date"\|"Long Date"\|"Time"\|"Percentage"\|"Fraction"\|"Scientific"\|"Text" \| code: "0.00"}
- `home.accounting` — Accounting Number Format (Home › Number): {range?, symbol?: "$"}
- `home.percent` — Percent Style (Home › Number) [Ctrl+Shift+%]: {range?}
- `home.comma` — Comma Style (Home › Number): {range?}
- `home.increaseDecimal` — Increase Decimal (Home › Number): {range?}
- `home.decreaseDecimal` — Decrease Decimal (Home › Number): {range?}
- `home.cellStyle` — Cell Styles (Home › Styles): {range?, name: "Good"\|"Bad"\|"Neutral"\|"Heading 1"\|"Title"\|"Total"\|"Accent1"…\|"Normal"}
- `home.rowHeight` — Row Height… (Home › Cells › Format): {rows?: "2:5", height: 20 (points on screen)}
- `home.columnWidth` — Column Width… (Home › Cells › Format): {cols?: "B:D", width: 64 (points) \| chars: 8.43}
- `home.autofitRowHeight` — AutoFit Row Height (Home › Cells › Format): {rows?}
- `home.autofitColumnWidth` — AutoFit Column Width (Home › Cells › Format): {cols?}
- `home.defaultWidth` — Default Width… (Home › Cells › Format): {width: 64}
- `home.hideRows` — Hide Rows (Home › Cells › Format › Hide & Unhide) [Cmd+9]: {rows?}
- `home.hideColumns` — Hide Columns (Home › Cells › Format › Hide & Unhide) [Cmd+0]: {cols?}
- `home.unhideRows` — Unhide Rows (Home › Cells › Format › Hide & Unhide) [Cmd+Shift+9]: {rows?}
- `home.unhideColumns` — Unhide Columns (Home › Cells › Format › Hide & Unhide) [Cmd+Shift+0]: {cols?}
- `home.lockCell` — Lock Cell (Home › Cells › Format): {range?, on?}
- `home.insertRows` — Insert Sheet Rows (Home › Cells › Insert) [Ctrl+Shift+=]: {rows?: "3:5", count?}
- `home.insertColumns` — Insert Sheet Columns (Home › Cells › Insert): {cols?: "B:C"}
- `home.deleteRows` — Delete Sheet Rows (Home › Cells › Delete) [Cmd+-]: {rows?}
- `home.deleteColumns` — Delete Sheet Columns (Home › Cells › Delete): {cols?}
- `home.insertCells` — Insert Cells… (Home › Cells › Insert): {range?, shift: right\|down\|row\|column}
- `home.deleteCells` — Delete Cells… (Home › Cells › Delete): {range?, shift: left\|up\|row\|column}
- `home.insertSheet` — Insert Sheet (Home › Cells › Insert) [Shift+F11]: {name?, before?: index}
- `home.deleteSheet` — Delete Sheet (Home › Cells › Delete): {sheet?}
- `home.formatAsTable` — Format as Table (Home › Styles): {range?, style: "TableStyleMedium2", header?}
- `home.conditionalFormat` — Conditional Formatting (Home › Styles): {range?, rule: {type: cellIs\|expression\|containsText\|beginsWith\|endsWith\|blanks\|noBlanks\|errors\|noErrors\|duplicate\|unique\|top10\|aboveAverage\|timePeriod\|colorScale\|dataBar\|iconSet, operator?, value?, value2?, formula?, text?, rank?, bottom?, percent?, below?, period?, colors?: [..], color?, set?, style?: {font..fill..}\|preset: lightRedFill\|redText\|yellowFill\|greenFill\|redBorder\|lightRedFillDarkRedText…}}
- `home.clearRules` — Clear Rules (Home › Styles › Conditional Formatting): {range?\|sheet: true}
- `home.manageRules` — Manage Rules… (Home › Styles › Conditional Formatting): {delete?: index, moveUp?: index, moveDown?: index}
- `home.drawBorder` — Draw Border (Home › Font): {range, edge: top\|bottom\|left\|right\|grid, style?, color?}
- `home.newCellStyle` — New Cell Style… (Home › Styles): {name, fromCell?: "A1" (default: active cell)}
- `home.addIns` — Add-ins (Home › Add-ins): {} → GridCraft extends through MCP and scripts instead of add-ins

## sheet

- `sheet.rename` — Rename Sheet (Home › Cells › Format): {sheet?, name}
- `sheet.move` — Move or Copy Sheet… (Home › Cells › Format): {sheet?, to: index, copy?: bool}
- `sheet.tabColor` — Tab Color (Home › Cells › Format): {sheet?, color: "#FF0000"\|"none"}
- `sheet.hide` — Hide Sheet (Home › Cells › Format › Hide & Unhide): {sheet?}
- `sheet.unhide` — Unhide Sheet… (Home › Cells › Format › Hide & Unhide): {sheet}
- `sheet.activate` — Activate Sheet: {sheet: index \| name}
- `sheet.next` — Next Sheet [Ctrl+PageDown]: {}
- `sheet.previous` — Previous Sheet [Ctrl+PageUp]: {}
- `sheet.read` — Read Range: {range?: "A1:D10" (default: used range), sheet?, formulas?: bool, formatted?: bool} → rows of values

## insert

- `insert.table` — Table (Insert › Tables) [Cmd+T]: {range?, header?: true, style?: "TableStyleMedium2", name?}
- `insert.chart` — Insert Chart (Insert › Charts): {range?, type?: column\|bar\|line\|pie\|doughnut\|area\|scatter\|bubble\|radar\|combo\|histogram\|waterfall\|funnel\|treemap\|sunburst\|boxWhisker\|stock, subtype?: clustered\|stacked\|stacked100\|markers, title?, at?: "H2", width?, height?}
- `insert.recommendedCharts` — Recommended Charts (Insert › Charts): {range?}
- `insert.sparkline` — Sparklines (Insert › Sparklines): {range: "B2:M2", location: "N2", type?: line\|column\|winLoss, markers?}
- `insert.picture` — Picture (Insert › Illustrations): {path? \| base64?: "...", mime?, at?: "B2", width?, height?, alt?}
- `insert.shape` — Shapes (Insert › Illustrations): {kind: rectangle\|roundedRectangle\|ellipse\|triangle\|line\|arrow\|textBox, at?, width?, height?, text?, fill?, line?}
- `insert.icons` — Icons (Insert › Illustrations): {name: chart\|table\|sum\|filter\|lock\|comment\|picture\|book\|folder\|search\|calc\|check\|… , at?, size?: 48, color?: hex}
- `insert.textBox` — Text Box (Insert › Text): {at?, width?, height?, text?}
- `insert.link` — Link (Insert › Links) [Cmd+K]: {cell?, target: "https://…" \| "Sheet2!A1" \| "mailto:…", text?, tooltip?, remove?: bool}
- `insert.symbol` — Symbol (Insert › Symbols): {char: "€"} (inserted at the end of the active cell's text)
- `insert.checkbox` — Checkbox (Insert › Cell Controls): {range?} (cells hold TRUE/FALSE and draw as checkboxes; Space toggles)
- `insert.pivotTable` — PivotTable (Insert › Tables): {source?: "Sheet1!$A$1:$E$200" \| table name (default: the table or current region of the selection), destination?: "new" (default: new sheet before the current one, report at A3) \| "Sheet1!H3", name?, rows?: [field \| {field, group?: years\|quarters\|months\|days}], columns?: [..], values?: [field \| {field, func?, name?}], filters?: [field], replace?: bool} → {id, name, sheet, anchor, fields}
- `insert.recommendedPivotTables` — Recommended PivotTables (Insert › Tables): {source?, apply?: index, destination?} → suggestions [{index, title, rows, columns, values}]; with apply, creates that one

## table

- `table.totalRow` — Total Row (Table › Table Style Options): {table?, on?: bool}
- `table.bandedRows` — Banded Rows (Table › Table Style Options): {table?, on?}
- `table.bandedColumns` — Banded Columns (Table › Table Style Options): {table?, on?}
- `table.headerRow` — Header Row (Table › Table Style Options): {table?, on?}
- `table.firstColumn` — First Column (Table › Table Style Options): {table?, on?}
- `table.lastColumn` — Last Column (Table › Table Style Options): {table?, on?}
- `table.style` — Table Styles (Table › Table Styles): {table?, style}
- `table.rename` — Table Name (Table › Properties): {table?, name}
- `table.convertToRange` — Convert to Range (Table › Tools): {table?}
- `table.totalFunction` — Totals Function: {table?, column: "Sales", function: sum\|average\|count\|countNums\|max\|min\|stdDev\|var\|none}
- `table.resize` — Resize Table (Table Design › Properties): {table?, range: "A1:F20"}
- `table.removeDuplicates` — Remove Duplicates (Table Design › Tools): {table?, columns?}
- `table.summarizePivot` — Summarize with PivotTable (Table Design › Tools): {table?, destination?} creates a PivotTable from the table

## chart

- `chart.set` — Chart Properties (Chart Design): {chart?: id, type?, title?, legend?: none\|bottom\|top\|left\|right, dataLabels?, gridlines?, style?, xTitle?, yTitle?, at?, width?, height?, dx?, dy?}
- `chart.switchRowColumn` — Switch Row/Column (Chart Design › Data): {chart?}
- `chart.delete` — Delete Chart: {chart?}
- `chart.addElement` — Add Chart Element (Chart Design › Chart Layouts): {chart?, element: title\|legend\|dataLabels\|gridlines\|axisTitles, on?: bool, position?: bottom\|top\|left\|right}
- `chart.quickLayout` — Quick Layout (Chart Design › Chart Layouts): {chart?, layout: 1..6}
- `chart.changeColors` — Change Colors (Chart Design › Chart Styles): {chart?, palette: colorful\|monochrome\|accent1..accent6 \| colors: [hex…]}
- `chart.selectData` — Select Data… (Chart Design › Data): {chart?, range: "Sheet1!A1:D7", byRows?: bool}
- `chart.changeType` — Change Chart Type… (Chart Design › Type): {chart?, type, subtype?}
- `chart.move` — Move Chart… (Chart Design › Location): {chart?, sheet?: name (moves to that sheet), at?: "B2"}
- `chart.formatSelection` — Format Selection (Format › Current Selection): {chart?, series?: index, color?: hex}
- `chart.shapeFill` — Shape Fill (Format › Shape Styles): {chart? \| kind: shape, id?, series?, color: hex}
- `chart.shapeOutline` — Shape Outline (Format › Shape Styles): {kind: shape, id?, color: hex}

## object

- `object.delete` — Delete Object: {kind: chart\|image\|shape, id}
- `object.move` — Move Object: {kind: chart\|image\|shape, id, at?: "C3", dx?, dy?, width?, height?}

## review

- `review.newNote` — New Note (Review › Notes): {cell?, text, author?}
- `review.newComment` — New Comment (Review › Comments): {cell?, text, author?}
- `review.replyComment` — Reply: {cell?, text, author?}
- `review.resolveComment` — Resolve Thread: {cell?, resolved?: true}
- `review.deleteComment` — Delete Comment (Review › Comments): {cell?}
- `review.showNote` — Show/Hide Note (Review › Notes): {cell?}
- `review.protectSheet` — Protect Sheet… (Review › Protect): {password?, formatCells?, formatColumns?, formatRows?, insertRows?, insertColumns?, deleteRows?, deleteColumns?, sort?, autofilter?}
- `review.unprotectSheet` — Unprotect Sheet (Review › Protect): {password?}
- `review.protectWorkbook` — Protect Workbook (Review › Protect): {on?: bool}
- `review.workbookStatistics` — Workbook Statistics (Review › Proofing): {}
- `review.checkAccessibility` — Check Accessibility (Review › Accessibility): {} → issues
- `review.spelling` — Spelling (Review › Proofing) [F7]: {range?, sheet?} → misspelled words with cells and suggestions
- `review.addToDictionary` — Add to Dictionary: {word}
- `review.changeSpelling` — Change: {cell, word, to, all?: bool}
- `review.thesaurus` — Thesaurus (Review › Proofing): {word} → related words (words sharing the stem in the dictionary)

## data

- `data.sortAscending` — Sort A to Z (Data › Sort & Filter): {range?, column?: "B"}
- `data.sortDescending` — Sort Z to A (Data › Sort & Filter): {range?, column?}
- `data.sort` — Sort… (Data › Sort & Filter): {range?, header?: bool, keys: [{column: "B", order: asc\|desc, by?: values\|cellColor\|fontColor, customList?: [..]}], orientation?: rows\|columns, matchCase?}
- `data.filter` — Filter (Data › Sort & Filter) [Cmd+Shift+F]: {range?} toggles AutoFilter on the current region
- `data.filterBy` — Filter Column: {column: "B" (or 0-based offset), values?: [..], blanks?: bool, custom?: {op: ">", value: "10", op2?, value2?, and?}, top?: {count, bottom?, percent?}, aboveAverage?: bool, clear?: bool}
- `data.clearFilter` — Clear (Data › Sort & Filter): {}
- `data.reapply` — Reapply (Data › Sort & Filter): {}
- `data.removeDuplicates` — Remove Duplicates (Data › Data Tools): {range?, columns?: ["A","C"], header?: bool}
- `data.textToColumns` — Text to Columns (Data › Data Tools): {range?, delimiters?: [",", "\t", " ", ";"], other?: "\|", fixedWidths?: [5, 10], treatConsecutive?: bool, textQualifier?: "\"", destination?: "B1"}
- `data.validation` — Data Validation… (Data › Data Tools): {range?, type: any\|whole\|decimal\|list\|date\|time\|textLength\|custom, operator?: between\|notBetween\|equal\|notEqual\|greater\|less\|greaterOrEqual\|lessOrEqual, formula1, formula2?, ignoreBlank?, dropdown?, inputTitle?, inputMessage?, errorStyle?: stop\|warning\|information, errorTitle?, errorMessage?, clear?: bool}
- `data.validate` — Check Value Against Validation: {cell?, input} → {ok, message?}
- `data.circleInvalid` — Circle Invalid Data (Data › Data Tools › Data Validation): {} → invalid cells
- `data.group` — Group (Data › Outline) [Cmd+Shift+K]: {rows?: "2:5" \| cols?: "B:C"}
- `data.ungroup` — Ungroup (Data › Outline) [Cmd+Shift+J]: {rows? \| cols?}
- `data.hideDetail` — Hide Detail (Data › Outline): {rows? \| cols?}
- `data.showDetail` — Show Detail (Data › Outline): {rows? \| cols?}
- `data.subtotal` — Subtotal (Data › Outline): {range?, groupBy: "A", function?: sum\|count\|average\|max\|min\|product, columns: ["C"], header?: true}
- `data.flashFill` — Flash Fill (Data › Data Tools): {range?}
- `data.fromTextCsv` — From Text/CSV (Data › Get & Transform Data): {path \| text, delimiter?: ",", sheet?: new sheet name} → imports into a new sheet as a table
- `data.getData` — Get Data (Data › Get & Transform Data): {path \| text} (CSV/TSV/JSON array of objects) → new sheet table
- `data.fromTableRange` — From Table/Range (Data › Get & Transform Data): {range?} → copies the table/range to a new sheet as a table
- `data.queriesConnections` — Queries & Connections (Data › Queries & Connections): {} → imported tables
- `data.refreshAll` — Refresh All (Data › Queries & Connections) [Cmd+Alt+F5]: {replace?} refreshes every PivotTable → {refreshed, errors}
- `data.goalSeek` — Goal Seek… (Data › Forecast › What-If Analysis): {set: "B5" (formula cell), to: number, changing: "B2" (constant cell)} → {value, result, iterations, converged}. Secant search with bisection once the answer is bracketed; stops within Maximum Change (0.001) or after Maximum Iterations (100) from File › Options › Formulas. Writes the found value into `changing`.
- `data.scenarioManager` — Scenario Manager… (Data › Forecast › What-If Analysis): {sheet?} → {scenarios: [{name, sheet, changing, values, comment}]} (scenarios of the active sheet; `sheet: "*"` lists all)
- `data.scenarioAdd` — Add Scenario: {name, changing: "B2:B4" or "B2,B4" (≤32 cells, active sheet), values?: [..] (default: the cells' current values), comment?, replace?: bool}
- `data.scenarioShow` — Show Scenario: {name} writes the scenario's values into its changing cells
- `data.scenarioDelete` — Delete Scenario: {name}
- `data.scenarioSummary` — Scenario Summary: {resultCells?: "B10" or "B10:B12,D4"} inserts a "Scenario Summary" sheet: changing cells and result cells for the current values and each scenario
- `data.dataTable` — Data Table… (Data › Forecast › What-If Analysis): {range: "D2:E10", rowInput?: "B1", columnInput?: "B2"} one-variable (values down the first column with columnInput, or across the top row with rowInput; formulas in the other edge) or two-variable (formula in the top-left corner). Computes every result by substitution and writes static values (a snapshot, not a live {=TABLE()}); ≤100,000 cells.
- `data.advancedFilter` — Advanced… (Data › Sort & Filter): {range? (list with headers; default current region), criteria: "H1:I3" (header row of field names; rows OR'ed, columns AND'ed; ">100", "=abc", "a*", "<>"; blank-headed formula cells are computed criteria for the first data row), copyTo?: "K1" (else filter in place by hiding rows), unique?: bool}
- `data.consolidate` — Consolidate… (Data › Data Tools): {sources: ["Sheet2!A1:C10", ..], destination?: "A1" (default active cell), function?: sum\|count\|countNums\|average\|max\|min\|product, topRow?: bool, leftColumn?: bool (consolidate by labels; else by position)}

## formulas

- `formulas.autoSum` — AutoSum (Formulas › Function Library) [Cmd+Shift+T]: {function?: SUM\|AVERAGE\|COUNT\|MAX\|MIN, range?}
- `formulas.insertFunction` — Insert Function… (Formulas › Function Library) [Shift+F3]: {name?: "VLOOKUP"} (UI opens the dialog; with a name, starts the formula in the active cell)
- `formulas.functions` — List Functions: {category?, search?} → [{name, category, signature, description}]
- `formulas.defineName` — Define Name… (Formulas › Defined Names): {name, refersTo?: "=Sheet1!$A$1:$A$10" (default: the selection), scope?: "Workbook"\|sheet name, comment?}
- `formulas.deleteName` — Delete Name: {name, scope?}
- `formulas.nameManager` — Name Manager (Formulas › Defined Names) [Cmd+F3]: {} → names with values
- `formulas.createFromSelection` — Create from Selection (Formulas › Defined Names) [Cmd+Shift+F3]: {range?, top?: true, left?: false, bottom?, right?}
- `formulas.tracePrecedents` — Trace Precedents (Formulas › Formula Auditing): {cell?} → ranges
- `formulas.traceDependents` — Trace Dependents (Formulas › Formula Auditing): {cell?} → cells
- `formulas.removeArrows` — Remove Arrows (Formulas › Formula Auditing): {}
- `formulas.showFormulas` — Show Formulas (Formulas › Formula Auditing) [Ctrl+`]: {on?}
- `formulas.errorChecking` — Error Checking (Formulas › Formula Auditing): {} → cells with errors
- `formulas.evaluateFormula` — Evaluate Formula (Formulas › Formula Auditing): {cell?, formula?} → steps
- `formulas.evaluate` — Evaluate: {formula: "=SUM(A1:A3)", cell?} → value without changing the sheet
- `formulas.calculateNow` — Calculate Now (Formulas › Calculation) [F9]: {}
- `formulas.calculateSheet` — Calculate Sheet (Formulas › Calculation) [Shift+F9]: {}
- `formulas.calculationOptions` — Calculation Options (Formulas › Calculation): {mode: automatic\|automaticExceptTables\|manual, iterative?, maxIterations?, maxChange?}
- `formulas.recentlyUsed` — Recently Used (Formulas › Function Library): {} → recently used functions in this workbook
- `formulas.financial` — Financial (Formulas › Function Library): {}
- `formulas.logical` — Logical (Formulas › Function Library): {}
- `formulas.text` — Text (Formulas › Function Library): {}
- `formulas.dateTime` — Date & Time (Formulas › Function Library): {}
- `formulas.lookupReference` — Lookup & Reference (Formulas › Function Library): {}
- `formulas.mathTrig` — Math & Trig (Formulas › Function Library): {}
- `formulas.moreFunctions` — More Functions (Formulas › Function Library): {category?: Statistical\|Engineering\|Information\|Database\|Compatibility\|Web\|Cube}
- `formulas.useInFormula` — Use in Formula (Formulas › Defined Names): {name} (inserts the name into the cell being edited)
- `formulas.watchWindow` — Watch Window (Formulas › Formula Auditing): {add?: "Sheet1!B5", remove?: "…"} → watched cells with current values

## view

- `view.freezePanes` — Freeze Panes (View › Window › Freeze Panes): {cell?: "B2" (rows above and columns left of it freeze)}
- `view.freezeTopRow` — Freeze Top Row (View › Window › Freeze Panes): {}
- `view.freezeFirstColumn` — Freeze First Column (View › Window › Freeze Panes): {}
- `view.unfreezePanes` — Unfreeze Panes (View › Window › Freeze Panes): {}
- `view.gridlines` — Gridlines (View › Show): {on?}
- `view.headings` — Headings (View › Show): {on?}
- `view.showZeros` — Show Zeros: {on?}
- `view.rightToLeft` — Sheet Right-to-Left (Page Layout › Sheet Options): {on?}
- `view.zoom` — Zoom (View › Zoom): {percent: 10..400}
- `view.zoomToSelection` — Zoom to Selection (View › Zoom): {viewWidth?, viewHeight?}
- `view.normal` — Normal (View › Workbook Views): {}
- `view.pageLayout` — Page Layout (View › Workbook Views): {}
- `view.pageBreakPreview` — Page Break Preview (View › Workbook Views): {}
- `view.customViews` — Custom Views… (View › Workbook Views): {save?: name, show?: name, delete?: name} → list
- `view.split` — Split (View › Window): {} (toggles a split at the active cell; shown as frozen panes in this version)
- `view.newWindow` — New Window (View › Window): {} opens a second window on the same workbook (a linked copy)
- `view.arrangeAll` — Arrange All (View › Window): {}
- `view.hideWindow` — Hide (View › Window): {}
- `view.unhideWindow` — Unhide… (View › Window): {index?}
- `view.switchWindows` — Switch Windows (View › Window): {} → open windows
- `view.ruler` — Ruler (View › Show): {on?}
- `view.macros` — Macros (View › Macros): {} → scripts

## pageLayout

- `pageLayout.orientation` — Orientation (Page Layout › Page Setup): {orientation: portrait\|landscape}
- `pageLayout.size` — Size (Page Layout › Page Setup): {paper: Letter\|Legal\|A4\|A3\|A5\|Tabloid\|Executive}
- `pageLayout.margins` — Margins (Page Layout › Page Setup): {preset?: normal\|wide\|narrow, left?, right?, top?, bottom?, header?, footer? (inches)}
- `pageLayout.printArea` — Set Print Area (Page Layout › Page Setup › Print Area): {range?, clear?: bool}
- `pageLayout.printTitles` — Print Titles (Page Layout › Page Setup): {rows?: "1:1", cols?: "A:A"}
- `pageLayout.scaleToFit` — Scale to Fit (Page Layout › Scale to Fit): {scale?: 100, width?: pages, height?: pages}
- `pageLayout.printGridlines` — Print Gridlines (Page Layout › Sheet Options): {on?}
- `pageLayout.printHeadings` — Print Headings (Page Layout › Sheet Options): {on?}
- `pageLayout.breaks` — Breaks (Page Layout › Page Setup): {insert?: bool, remove?: bool, reset?: bool, cell?}
- `pageLayout.headerFooter` — Header & Footer (Insert › Text): {header?: "&C&P", footer?: "&CPage &P of &N"}
- `pageLayout.theme` — Themes (Page Layout › Themes): {name: Craft\|Slate\|Meadow\|Ember\|Ocean\|Orchid\|Graphite, colors?: [12 hex], majorFont?, minorFont?}
- `pageLayout.themeColors` — Colors (Page Layout › Themes): {name: theme name \| colors: [12 hex]}
- `pageLayout.themeFonts` — Fonts (Page Layout › Themes): {major, minor}
- `pageLayout.themeEffects` — Effects (Page Layout › Themes): {name} (chart effects preset; stored with the theme name)
- `pageLayout.background` — Background (Page Layout › Page Setup): {path? \| clear?: bool} (sheet background picture)
- `pageLayout.pageSetup` — Page Setup… (Page Layout › Page Setup): {sheet?, orientation?: portrait\|landscape, paper?: Letter\|Legal\|A4\|A3\|A5\|Tabloid\|Executive\|Ledger\|B5, margins?: {left,right,top,bottom,header,footer} (inches; also accepted as top-level keys), scale?: 10..400, fitWidth?, fitHeight? (pages; 0 = automatic), fitToPage?: bool, centerH?, centerV?, gridlines?, headings?, header?: "&L&A&RPage &P of &N", footer?, printArea?: "A1:F50" ("" clears), titleRows?: "1:2", titleCols?: "A:A", rowBreaks?: [46, 91], colBreaks?: ["K"]} → the sheet's print settings

## document

- `document.inspect` — Inspect Workbook: {} → sheets, selection, names, tables, charts, dirty, history

## history

- `history.list` — Undo History: {} → undo/redo labels

## app

- `app.commands` — List Commands: {search?} → ids, labels, params

## arrange

- `arrange.bringForward` — Bring Forward (Page Layout › Arrange): {kind: chart\|image\|shape, id, toFront?: bool}
- `arrange.sendBackward` — Send Backward (Page Layout › Arrange): {kind: chart\|image\|shape, id, toBack?: bool}
- `arrange.selectionPane` — Selection Pane (Page Layout › Arrange): {} → objects on the sheet in stacking order
- `arrange.align` — Align (Page Layout › Arrange): {kind: chart\|image\|shape, ids: [..], align: left\|center\|right\|top\|middle\|bottom}
- `arrange.group` — Group (Page Layout › Arrange): {kind, ids} (moves objects together: aligns their anchors to the first)
- `arrange.rotate` — Rotate (Page Layout › Arrange): {kind: shape, id, flip?: horizontal\|vertical} (swaps width/height for 90° turns)

## automate

- `automate.recordActions` — Record Actions (Automate › Scripting Tools): {stop?: bool, name?: script name when stopping}
- `automate.newScript` — New Script (Automate › Scripting Tools): {name, commands: [{command, params}] }
- `automate.allScripts` — All Scripts (Automate › Scripting Tools): {} → saved scripts
- `automate.runScript` — Run Script: {name}
- `automate.deleteScript` — Delete Script: {name}

## draw

- `draw.pen` — Pen (Draw › Tools): {on?: bool, color?: hex, width?: 2}
- `draw.eraser` — Eraser (Draw › Tools): {on?: bool}
- `draw.lasso` — Lasso Select (Draw › Tools): {} (selects ink by dragging; same as Select Objects)
- `draw.stroke` — Ink Stroke: {points: [[x,y],…] in sheet points, color?: hex, width?: 2}
- `draw.inkToShape` — Ink to Shape (Draw › Convert): {id?} converts an ink stroke (default: the last) into a rectangle, ellipse, triangle or line

## pivot

- `pivot.fields` — PivotTable Fields: {pivot?} → source fields (name, numeric, date, samples, areas) and the current layout
- `pivot.fieldList` — Field List (PivotTable Analyze › Show): {pivot?} (same as pivot.fields)
- `pivot.list` — PivotTables: {} → every PivotTable in the workbook
- `pivot.addField` — Add Field: {pivot?, field, area: rows\|columns\|values\|filters, func?: sum\|count\|average\|max\|min\|product\|countNumbers\|stdDev\|stdDevP\|var\|varP, name?, position?: index, replace?}
- `pivot.removeField` — Remove Field: {pivot?, field (or value caption), area?: rows\|columns\|values\|filters, replace?}
- `pivot.moveField` — Move Field: {pivot?, field, from: rows\|columns\|values\|filters, to: rows\|columns\|values\|filters, position?: index, replace?}
- `pivot.valueSettings` — Value Field Settings (PivotTable Analyze › Active Field): {pivot?, field: caption or source field \| index: n, func?, name?, showAs?: normal\|percentOfGrandTotal\|percentOfColumnTotal\|percentOfRowTotal\|runningTotal\|rank, numberFormat?: "#,##0" \| null, replace?}
- `pivot.filter` — Filter Items: {pivot?, field, selected: ["East", ..] \| null (all), replace?}
- `pivot.sort` — Sort Field: {pivot?, field, order: asc\|desc\|none, replace?}
- `pivot.group` — Group Field (PivotTable Analyze › Group): {pivot?, field, by: years\|quarters\|months\|days\|none, replace?}
- `pivot.collapse` — Expand/Collapse Field (PivotTable Analyze › Active Field): {pivot?, field, items?: [labels] (default: all), collapse?: true, replace?}
- `pivot.layout` — PivotTable Layout (PivotTable Design › Layout): {pivot?, layout?: compact\|outline\|tabular, grandTotalsRows?: bool, grandTotalsCols?: bool, subtotals?: bool\|top\|bottom\|none, style?: "PivotStyleLight16", showHeaders?: bool, replace?}
- `pivot.grandTotals` — Grand Totals (PivotTable Design › Layout): {pivot?, mode?: off\|on\|rows\|columns, rows?: bool, cols?: bool}
- `pivot.subtotals` — Subtotals (PivotTable Design › Layout): {pivot?, mode: none\|top\|bottom}
- `pivot.reportLayout` — Report Layout (PivotTable Design › Layout): {pivot?, layout: compact\|outline\|tabular}
- `pivot.style` — PivotTable Styles (PivotTable Design › PivotTable Styles): {pivot?, style: "PivotStyleMedium9"}
- `pivot.refresh` — Refresh (PivotTable Analyze › Data) [Alt+F5]: {pivot?, replace?}
- `pivot.changeSource` — Change Data Source (PivotTable Analyze › Data): {pivot?, source: "Sheet1!$A$1:$E$300" \| table name, replace?} (fields missing from the new source are removed)
- `pivot.delete` — Delete PivotTable (PivotTable Analyze › Actions): {pivot?} clears the report and removes the PivotTable
