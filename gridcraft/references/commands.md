# GridCraft command catalog

Generated from `gridcraft-cli commands --json` (GridCraft 0.16.1, 377 commands). Run any of them with
`execute_command {command, params}` (MCP) or `gridcraft-cli run --cmd 'id={json}'`. Check one live with
`list_commands {search}`. `?` = optional, `a|b` = choices, `→ {...}` = what it returns. Most commands act on the
selection when `range` is omitted.

## file

- `file.new` — New Workbook (File) [Cmd+N]: {sample?: "budget"\|"sales"\|"grades"}
- `file.open` — Open… (File) [Cmd+O]: {path} \| {name, base64}, plus {password} for a password-protected workbook and {csvAsText?: bool} to keep every csv/tsv/txt field as text, with no number or date conversion (xlsx, xlsm, xls import, xlsb and ods data import, csv, tsv, txt, json)
- `file.save` — Save (File) [Cmd+S]: {path?} (xlsx by default; .csv/.tsv/.json/.html/.pdf by extension)
- `file.saveAs` — Save As… (File) [Cmd+Shift+S]: {path} (.xlsx, .csv, .tsv, .json, .html, or .pdf: a PDF of the active sheet)
- `file.saveBytes` — Encode Workbook: {format?: xlsx\|csv\|tsv\|json\|html} → {base64}
- `file.close` — Close (File) [Cmd+W]: {force?: bool, document?: bool} (closes the active window, or with `document` the workbook and all its windows; the workbook closes with its last window)
- `file.exportCsv` — Export as CSV (File › Export): {path, sheet?, values?: bool} → {path, bytes}: writes the cells as displayed, like Excel's Save As CSV; `values: true` writes raw values instead (full-precision numbers, ISO 8601 dates and times, TRUE/FALSE)
- `file.exportHtml` — Save as Web Page (File › Export): {path}
- `file.properties` — Properties (File): {title?, subject?, author?, company?, keywords?, description?}
- `file.options` — Options (File): {} → {calculation: {mode, iterative, maxIterations, maxChange}} for the active workbook (the interface opens File › Options; change settings with their own commands, e.g. formulas.calculationOptions, view.theme, app.language.set)
- `file.exportPdf` — Export as PDF (File › Export): {path?, sheets?: active\|all, range?: "A1:F40" (active sheet), fitToPage?: bool} → {pages, bytes, path} or {pages, bytes, base64} when no path. Honours each sheet's Page Setup.
- `file.print` — Print… (File) [Cmd+P]: {path?, sheets?: active\|all, range?, fitToPage?: bool} → {pages, bytes, base64} — the PDF the UI hands to the system print dialog
- `file.printPreview` — Print Preview (File): {page? (1-based), sheets?: active\|all, range?, fitToPage?} → {pages, pageList: [{page, sheet, range, rows, columns, scale, paper, orientation, pageOrder, width, height}]} in print order

## window

- `window.activate` — Switch Window (Window): {window} \| {doc} \| {index} (a window id, a workbook id, or the workbook's position in the list)
- `window.close` — Close Window (Window): {window?, doc?, force?: bool} → {closed, document}: closes a window (the active one by default); its workbook closes with its last window, asking first when it has unsaved changes unless `force`
- `window.list` — Windows (Window): {} → [{window, doc, index, title, dirty, active, hidden}]

## cell

- `cell.set` — Enter Cell: {cell?: "B2", input: "text, number or =formula", sheet?, array?: bool}
- `cell.get` — Get Cell: {cell?, sheet?} → value, formula, display text, style, comment, link, python {code, output, typeName, preview, stale}
- `cell.toggleCheckbox` — Toggle Checkbox [Space]: {cell?}

## range

- `range.setValues` — Set Values: {range?: "A1", values: [[...]] (rows of numbers/strings/bools/null; strings starting with = are formulas), parse?: bool (default true: a string goes through typed input, so "05.04.2026" becomes a date and "2.500" a number, by en-US rules; false stores every other string as the text it is, so a dd.mm.yyyy date or a thousands separator survives, a leading ' is kept and an empty string clears the cell)} → {cells, convertedCount, converted: [{cell, input, stored}] (up to 20 of the strings typed input read as a number, date, time, boolean or error, so a script can notice)}
- `range.fill` — Fill Range With Input [Ctrl+Enter]: {range?, input}: enters the same input in every selected cell (relative formulas adjust)
- `range.move` — Drag and Drop: {range?, to: "C3", overwrite?: bool} (drag the selection's border: a cut and paste that asks before replacing data unless overwrite)

## selection

- `selection.set` — Select: {range: "A1:B2,D4" \| cell, active?: "A1", sheet?}
- `selection.move` — Move Selection: {dr, dc, extend?: bool, jump?: bool (Ctrl+arrow), page?: bool}
- `selection.next` — Next Cell in Selection: {forward?: true, byRow?: false} (Enter/Tab inside a selection)
- `selection.nextCorner` — Next Corner of Selection [Ctrl+.]: {} (the active cell moves clockwise to the next corner of the selected area, which stays selected)
- `selection.currentRegion` — Select Current Region [Ctrl+Shift+8]: {}
- `selection.row` — Select Entire Row [Shift+Space]: {}
- `selection.column` — Select Entire Column [Ctrl+Space]: {}
- `selection.stats` — Selection Statistics: {} → count, sum, average, min, max

## edit

- `edit.selectAll` — Select All (Edit) [Cmd+A]: {} (current region first, then the whole sheet)
- `edit.goTo` — Go To… (Home › Editing › Find & Select) [Ctrl+G]: {reference: "B5" \| "Sheet2!A1:C3" \| name \| "Sheet2!Name" \| "B14:C22,F19:G30" \| "Price, Type", record?: bool} (record: keep a reference without names among the recent ones) or {list: true} → {names, recent}
- `edit.goToSpecial` — Go To Special… (Home › Editing › Find & Select): {kind: blanks\|constants\|formulas\|comments\|lastCell\|currentRegion\|visible\|conditionalFormats\|dataValidation\|errors\|numbers\|text}
- `edit.undo` — Undo (Edit) [Cmd+Z]: {steps?: 1}
- `edit.redo` — Redo (Edit) [Cmd+Y]: {steps?: 1}
- `edit.copy` — Copy (Home › Clipboard) [Cmd+C]: {range?, html?: bool} → {range, text, html?} (html: a styled HTML table, only when requested and small enough)
- `edit.cut` — Cut (Home › Clipboard) [Cmd+X]: {range?, html?: bool} → {range, text, html?} (html: a styled HTML table, only when requested and small enough)
- `edit.paste` — Paste (Home › Clipboard) [Cmd+V]: {at?: "C3", text?: "tab-separated text from the system clipboard", html?: "the clipboard's HTML flavour; cells the source recorded as numbers (x:num, sdval) stay numbers"}
- `edit.pasteSpecial` — Paste Special… (Home › Clipboard) [Ctrl+Alt+V]: {what: all\|formulas\|values\|formats\|comments\|validation\|allExceptBorders\|columnWidths\|formulasAndNumberFormats\|valuesAndNumberFormats, operation?: none\|add\|subtract\|multiply\|divide, skipBlanks?, transpose?, link?}
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
- `edit.autoFill` — AutoFill: {source: "A1:A2", target: "A1:A10", mode?: series\|alternate\|copy\|formats\|values\|extend\|days\|weekdays\|months\|years}: the fill-handle drag (alternate = Ctrl+drag: a lone number counts up, any other series copies; values = Fill Without Formatting: the series, targets keep their formats; extend = Fill Series: the series, and a lone number counts up; days, weekdays, months, years = Fill Days, Fill Weekdays, Fill Months, Fill Years: dates step by one unit, or by the difference between the first two dates in that unit, and weekdays skip Saturday and Sunday)
- `edit.fillSeries` — Series… (Home › Editing › Fill): {range?, direction?: columns\|rows, type?: linear\|growth\|date\|autofill, step?: 1, stop?, dateUnit?: day\|weekday\|month\|year}
- `edit.flashFill` — Flash Fill (Home › Editing › Fill) [Ctrl+E]: {range?}
- `edit.find` — Find… (Home › Editing › Find & Select) [Cmd+F]: {what, matchCase?, wholeCell?, lookIn?: formulas\|values, byColumns?, all?: bool, within?: sheet\|workbook\|selection} (selection: only the selected cells; Find Next keeps them selected and moves the active cell)
- `edit.replace` — Replace… (Home › Editing › Find & Select) [Ctrl+H]: {what, with, matchCase?, wholeCell?, all?: true, within?: sheet\|workbook\|selection} → {replaced, skipped?} (in a Python cell the code is edited; skipped counts Python cells whose code would no longer fit)
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
- `home.alignRight` — Align Right (Home › Alignment): {range?}
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
- `home.rowHeight` — Row Height… (Home › Cells › Format): {sheet?, rows?: "2:5" \| "2:2,4:5" \| "Sheet2!2:5", height: 20 (pixels) \| points: 15}
- `home.columnWidth` — Column Width… (Home › Cells › Format): {sheet?, cols?: "B:D" \| "B:B,D:F" \| "Sheet2!B:D", width: 64 (pixels) \| chars: 8.43}
- `home.autofitRowHeight` — AutoFit Row Height (Home › Cells › Format): {sheet?, rows?}
- `home.autofitColumnWidth` — AutoFit Column Width (Home › Cells › Format): {sheet?, cols?}
- `home.defaultWidth` — Default Width… (Home › Cells › Format): {sheet?, width: 64 (pixels)}
- `home.hideRows` — Hide Rows (Home › Cells › Format › Hide & Unhide) [Cmd+9]: {sheet?, rows?}
- `home.hideColumns` — Hide Columns (Home › Cells › Format › Hide & Unhide) [Cmd+0]: {sheet?, cols?}
- `home.unhideRows` — Unhide Rows (Home › Cells › Format › Hide & Unhide) [Cmd+Shift+9]: {sheet?, rows?}
- `home.unhideColumns` — Unhide Columns (Home › Cells › Format › Hide & Unhide) [Cmd+Shift+0]: {sheet?, cols?}
- `home.lockCell` — Lock Cell (Home › Cells › Format): {range?, on?}
- `home.insertRows` — Insert Sheet Rows (Home › Cells › Insert) [Ctrl+Shift+=]: {rows?: "3:5", count?}
- `home.insertColumns` — Insert Sheet Columns (Home › Cells › Insert): {cols?: "B:C"}
- `home.deleteRows` — Delete Sheet Rows (Home › Cells › Delete) [Cmd+-]: {rows?}
- `home.deleteColumns` — Delete Sheet Columns (Home › Cells › Delete): {cols?}
- `home.insertCells` — Insert Cells… (Home › Cells › Insert): {range?, shift: right\|down\|row\|column}
- `home.insertCopiedCells` — Insert Copied Cells (Home › Cells › Insert): {at?: "B3", shift?: down\|right}: inserts the copied cells at `at` (the active cell) and pastes them there. Whole copied rows or columns insert whole rows or columns; other blocks shift the cells at `at` down (default) or right. A cut of whole rows or columns moves them (Insert Cut Cells)
- `home.deleteCells` — Delete Cells… (Home › Cells › Delete): {range?, shift: left\|up\|row\|column}
- `home.insertSheet` — Insert Sheet (Home › Cells › Insert) [Shift+F11]: {name?, before?: index}
- `home.deleteSheet` — Delete Sheet (Home › Cells › Delete): {sheet?}
- `home.formatAsTable` — Format as Table (Home › Styles): {range?, style: "TableStyleMedium2", header?} (inside a table: restyles it)
- `home.conditionalFormat` — Conditional Formatting (Home › Styles): {range?, rule: {type: cellIs\|expression\|containsText\|beginsWith\|endsWith\|blanks\|noBlanks\|errors\|noErrors\|duplicate\|unique\|top10\|aboveAverage\|timePeriod\|colorScale\|dataBar\|iconSet, operator?, value?, value2?, formula?, text?, rank?, bottom?, percent?, below?, period?, colors?: [..], color?, set?, style?: {font?: {bold?, italic?, color?}, fill?: "#FFC7CE" \| {pattern?, fg?, bg?}, borders?, num_fmt?} (colours "#RRGGBB") \| preset?: lightRedFill\|redText\|yellowFill\|greenFill\|redBorder\|lightRedFillDarkRedText…}; a text `value` is matched as text, or kept when already a quoted literal}
- `home.clearRules` — Clear Rules (Home › Styles › Conditional Formatting): {range?\|sheet: true}
- `home.manageRules` — Manage Rules… (Home › Styles › Conditional Formatting): {delete?: index, moveUp?: index, moveDown?: index}
- `home.drawBorder` — Draw Border (Home › Font): {range, edge: top\|bottom\|left\|right\|grid, style?, color?}
- `home.newCellStyle` — New Cell Style… (Home › Styles): {name, fromCell?: "A1" (default: active cell)}
- `home.addIns` — Add-ins (Home › Add-ins): {} → GridCraft extends through MCP and scripts instead of add-ins

## sheet

- `sheet.moveColumns` — Move Columns: {cols?: "B:C", before: zero-based column index}
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
- `insert.recommendedCharts` — Recommended Charts (Insert › Charts): {range?, type?, subtype?} (no type: the first of insert.chartRecommendations; the ribbon button opens the dialog)
- `insert.chartRecommendations` — Chart Recommendations: {range?} → [{type, subtype, label}] chart types that suit the data's shape, best first
- `insert.sparkline` — Sparklines (Insert › Sparklines): {range: "B2:M2", location: "N2", type?: line\|column\|winLoss, markers?}
- `insert.picture` — Picture (Insert › Illustrations): {path? \| base64?: "...", mime?, at?: "B2", width?, height?, alt?, mode?: moveOnly\|moveAndSize\|absolute, placement?: cell\|overCells}
- `insert.shape` — Shapes (Insert › Illustrations): {kind: rectangle\|roundedRectangle\|ellipse\|triangle\|line\|arrow\|textBox, at?, width?, height?, text?, fill?, line?}
- `insert.icons` — Icons (Insert › Illustrations): {name: chart\|table\|sum\|filter\|lock\|comment\|picture\|book\|folder\|search\|calc\|check\|… , at?, size?: 48, color?: hex}
- `insert.textBox` — Text Box (Insert › Text): {at?, width?, height?, text?}
- `insert.link` — Link (Insert › Links) [Cmd+K]: {cell?, target: "https://…" \| "Book.xlsx" \| "Sheet2!A1" \| "mailto:…", text?, tooltip?, remove?: bool}
- `insert.symbol` — Symbol (Insert › Symbols): {char: "€"} (inserted at the end of the active cell's text)
- `insert.equation` — Equation (Insert › Symbols): {latex: "x^2", cell?\|at?: "B2", size?: 11 (points), color?: hex\|"auto"}
- `insert.checkbox` — Checkbox (Insert › Cell Controls): {range?} (TRUE/FALSE and empty cells draw as checkboxes, empty ones become FALSE, other values show as they are; click or Space toggles; Delete unchecks, then removes; Clear Formats removes and keeps the values)
- `insert.pivotTable` — PivotTable (Insert › Tables): {source?: "Sheet1!$A$1:$E$200" \| table name (default: the table or current region of the selection), destination?: "new" (default: new sheet before the current one, report at A3) \| "Sheet1!H3", name?, rows?: [field \| {field, group?: years\|quarters\|months\|days}], columns?: [..], values?: [field \| {field, func?, name?}], filters?: [field], replace?: bool} → {id, name, sheet, anchor, fields}
- `insert.recommendedPivotTables` — Recommended PivotTables (Insert › Tables): {source?, apply?: index, destination?} → suggestions [{index, title, rows, columns, values}]; with apply, creates that one
- `insert.pivotChart` — PivotChart (Insert › Charts): {pivot?: name \| id \| a cell of the report ("Sheet2!B5"; default: the PivotTable at the active cell), type?: column\|bar\|line\|pie\|area\|… (default column), subtype?, title?, at?: "H2", width?, height?} adds a chart bound to the PivotTable's report: categories are the innermost row items, series the column items × value fields; it follows refreshes and layout changes → {chart, pivot, series}
- `insert.slicer` — Slicer (Insert › Filters): {table?, column?: "Region", columns?: 1, at?: "H2", width?, height?}

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
- `table.insertSlicer` — Insert Slicer (Table › Tools): {table?, column?: "Region", columns?: 1, at?, width?, height?}

## chart

- `chart.set` — Chart Properties (Chart Design): {chart?: id, type?, subtype?, title?, legend?: none\|bottom\|top\|left\|right, dataLabels?, gridlines?, dataTable?: bool, dataTableKeys?: bool, dataTableHorizontalBorder?: bool, dataTableVerticalBorder?: bool, dataTableOutline?: bool (data tables: column/bar/line/area and compatible combo charts), quartiles?: exclusive\|inclusive, style?, xTitle?, yTitle?, at?, width?, height?, dx?, dy?}
- `chart.switchRowColumn` — Switch Row/Column (Chart Design › Data): {chart?}
- `chart.delete` — Delete Chart: {chart?}
- `chart.addElement` — Add Chart Element (Chart Design › Chart Layouts): {chart?, element: title\|legend\|dataLabels\|dataTable\|gridlines\|axisTitles\|smooth\|trendline, on?: bool, position?: bottom\|top\|left\|right; dataTable: dataTableKeys?: bool, dataTableHorizontalBorder?: bool, dataTableVerticalBorder?: bool, dataTableOutline?: bool; trendline: series?: index (default all), type?: linear\|exponential\|linearForecast\|movingAverage\|logarithmic\|power\|polynomial, order?: 2..6, period?: 2..255, forward?, backward?, displayEquation?, displayRSquared?}
- `chart.quickLayout` — Quick Layout (Chart Design › Chart Layouts): {chart?, layout: 1..6}
- `chart.changeColors` — Change Colors (Chart Design › Chart Styles): {chart?, palette: colorful\|monochrome\|accent1..accent6 \| colors: [hex…]}
- `chart.selectData` — Select Data… (Chart Design › Data): {chart?, range?: "Sheet1!A1:D7", byRows?: bool, categories?: "Sheet1!A2:A7" (Horizontal (Category) Axis Labels for every series; "" clears), removeSeries?: [index…]}
- `chart.changeType` — Change Chart Type… (Chart Design › Type): {chart?, type, subtype?}
- `chart.move` — Move Chart… (Chart Design › Location): {chart?, sheet?: name (moves to that sheet), at?: "B2"}
- `chart.formatSelection` — Format Selection (Format › Current Selection): {chart?, series?: index, color?: hex}
- `chart.shapeFill` — Shape Fill (Format › Shape Styles): {chart? \| kind: shape, id?, series?, color: hex}
- `chart.shapeOutline` — Shape Outline (Format › Shape Styles): {kind: shape, id?, color: hex}

## shape

- `shape.setText` — Edit Text Box: {id: textBox id, text: string}

## object

- `object.delete` — Delete Object: {kind: chart\|image\|shape\|slicer\|equation, id}
- `object.move` — Move Object: {kind: chart\|image\|shape\|slicer\|equation, id, at?: "C3", dx?, dy?, width?, height? (each at most 10,000 points, or the object's current size when a file made it larger)}
- `object.setAnchorMode` — Object Properties: {kind: chart\|image\|shape\|slicer\|equation, id, mode: moveAndSize\|moveOnly\|absolute}

## link

- `link.open` — Open Hyperlink: {url?: "https://…" \| "mailto:…" \| "Sheet2!A1", cell?} (default: the cell's link); a reference selects; a web or e-mail address is an error unless the host allows it: the user opens those by clicking the link and confirming; any scheme but http, https and mailto is always an error

## review

- `review.newNote` — New Note (Review › Notes) [Shift+F2]: {cell?, text, author?}
- `review.newComment` — New Comment (Review › Comments) [Cmd+Shift+F2]: {cell?, text, author?}
- `review.replyComment` — Reply: {cell?, text, author?}
- `review.resolveComment` — Resolve Thread: {cell?, resolved?: true}
- `review.deleteComment` — Delete Comment (Review › Comments): {cell?}
- `review.showNote` — Show/Hide Note (Review › Notes): {cell?}
- `review.protectSheet` — Protect Sheet… (Review › Protect): {password?, formatCells?, formatColumns?, formatRows?, insertRows?, insertColumns?, deleteRows?, deleteColumns?, sort?, autofilter?}
- `review.unprotectSheet` — Unprotect Sheet (Review › Protect): {password?}
- `review.protectWorkbook` — Protect Workbook (Review › Protect): {on?: bool (default: toggle), password?} (structure protection; unprotecting needs the password when one was set)
- `review.workbookStatistics` — Workbook Statistics (Review › Proofing): {}
- `review.allowEditRanges` — Allow Edit Ranges… (Review › Protect): {action?: list (default) \| add \| modify \| delete \| unlock, title?, range?, password?, newTitle?, sheet?} → ranges
- `review.checkAccessibility` — Check Accessibility (Review › Accessibility): {} → issues
- `review.previousComment` — Previous Comment (Review › Comments): {} → {sheet, cell}
- `review.nextComment` — Next Comment (Review › Comments): {} → {sheet, cell}
- `review.showComments` — Show Comments (Review › Comments): {on?: bool} (toggles the Comments pane)
- `review.showAllNotes` — Show All Notes (Review › Notes): {on?: bool}
- `review.convertToComments` — Convert to Comments (Review › Notes): {} (every note in the workbook) → {converted}
- `review.spelling` — Spelling (Review › Proofing) [F7]: {range?, sheet?} → misspelled words with cells and suggestions
- `review.addToDictionary` — Add to Dictionary: {word}
- `review.changeSpelling` — Change: {cell, word, to, all?: bool}
- `review.thesaurus` — Thesaurus (Review › Proofing): {word} → related words (words sharing the stem in the dictionary)

## equation

- `equation.edit` — Edit Equation: {id, latex}

## data

- `data.sortAscending` — Sort A to Z (Data › Sort & Filter): {range?, column?: "B"}
- `data.sortDescending` — Sort Z to A (Data › Sort & Filter): {range?, column?}
- `data.sort` — Sort… (Data › Sort & Filter): {range?, header?: bool, keys: [{column: "B", order: asc\|desc, by?: values\|cellColor\|fontColor, customList?: [..]}], orientation?: rows\|columns, matchCase?}
- `data.filter` — Filter (Data › Sort & Filter) [Ctrl+Shift+L]: {range?} toggles AutoFilter on the current region
- `data.filterBy` — Filter Column: {column: "B" (or 0-based offset), values?: [..], blanks?: bool, custom?: {op: ">", value: "10", op2?, value2?, and?}, top?: {count, bottom?, percent?}, aboveAverage?: bool, clear?: bool}
- `data.clearFilter` — Clear (Data › Sort & Filter): {}
- `data.reapply` — Reapply (Data › Sort & Filter): {}
- `data.removeDuplicates` — Remove Duplicates (Data › Data Tools): {range?, columns?: ["A","C"], header?: bool}
- `data.textToColumns` — Text to Columns (Data › Data Tools): {range?, delimiters?: [",", "\t", " ", ";"], other?: "\|", fixedWidths?: [5, 10], treatConsecutive?: bool, textQualifier?: "\"", destination?: "B1"}
- `data.validation` — Data Validation… (Data › Data Tools): {range?, type: any\|whole\|decimal\|list\|date\|time\|textLength\|custom, operator?: between\|notBetween\|equal\|notEqual\|greater\|less\|greaterOrEqual\|lessOrEqual, formula1, formula2?, ignoreBlank?, dropdown?, inputTitle?, inputMessage?, errorStyle?: stop\|warning\|information, errorTitle?, errorMessage?, clear?: bool}
- `data.validate` — Check Value Against Validation: {cell?, input} → {ok, message?}
- `data.circleInvalid` — Circle Invalid Data (Data › Data Tools › Data Validation): {} → invalid cells
- `data.group` — Group (Data › Outline) [Alt+Shift+Right]: {rows?: "2:5" \| cols?: "B:C" \| by?: rows\|cols (the selection's rows or columns; a block of cells groups rows by default), sheet?}
- `data.ungroup` — Ungroup (Data › Outline) [Alt+Shift+Left]: {rows? \| cols? \| by?: rows\|cols, sheet?}
- `data.hideDetail` — Hide Detail (Data › Outline): {rows? \| cols? \| by?, level?: 1-7} (the innermost group, or the one at `level`, holding the lines or summarised by them)
- `data.showDetail` — Show Detail (Data › Outline): {rows? \| cols? \| by?, level?: 1-7}
- `data.showLevels` — Show Outline Levels: {rows?: 1-8, cols?: 1-8} (1 shows only the top-level summaries, as the outline's level buttons)
- `data.outlineSettings` — Outline Settings (Data › Outline): {sheet?, summaryBelow?: bool, summaryRight?: bool} (summary rows below their detail, summary columns right of it; off puts them above / left) → {summaryBelow, summaryRight}
- `data.subtotal` — Subtotal (Data › Outline): {range?, groupBy: "A", function?: sum\|count\|average\|max\|min\|product, columns: ["C"], header?: true}
- `data.flashFill` — Flash Fill (Data › Data Tools): {range?}
- `data.fromTextCsv` — From Text/CSV (Data › Get & Transform Data): {path \| text, delimiter?: ",", sheet?: new sheet name} → imports into a new sheet as a table
- `data.getData` — Get Data (Data › Get & Transform Data): {path \| text} (CSV/TSV/JSON array of objects) → new sheet table
- `data.fromTableRange` — From Table/Range (Data › Get & Transform Data): {range?} → copies the table/range to a new sheet as a table
- `data.queriesConnections` — Queries & Connections (Data › Queries & Connections): {} → imported tables
- `data.solver` — Solver… (Data › Analysis): {objective: "B10" (formula cell), goal?: max\|min\|value (default max), value?: number (for goal value), variables: "B2:B4,D1" (≤200 constant cells, same sheet), constraints?: ["B5 <= 10", "B2:B4 >= C2:C4", "B2 int", "B3 bin", {lhs: "B6", op: "=", rhs: 3 \| "C6"}], nonNegative?: bool (default true: variables without a lower bound get 0), method?: grg\|simplex\|evolutionary (default grg), populationSize?: 100, mutationRate?: 0.075, randomSeed?: 0 (a fixed seed, so runs repeat), convergence?: 0.0001, generationsWithoutImprovement?: 50, requireBounds?: bool (default true: every variable needs both bounds; false searches within ±100 of the start) (Evolutionary options), keep?: bool (default true; false restores the original values), saveModel?: bool (default true: hidden names, solver_* as Excel names them, with the options; the evaluation limit and generations without improvement, which Excel lacks, as gridcraft_solver_evals and gridcraft_solver_stall), maxEvaluations?: 20000 (at most 200000), integerOptimality?: percent (default 0), saved?: bool (solve the sheet's saved model; other params override), reports?: [answer\|sensitivity\|limits] (written on new sheets when a solution is found)} → {status: optimal\|converged\|cannotImprove\|iterationLimit\|infeasible\|unbounded\|notLinear, message, objective, values: {cell: value}, original: {cell: value}, model: the model as params, evaluations, changed, reports?: [sheet names], skippedReports?: [{report: "sensitivity", reason}] (a Sensitivity report left out because the run did not reach an optimum or the values are not one; the solve and the other reports still apply)}. No `objective` → {model: the saved model} (the menu opens the dialog).
- `data.solverReport` — Solver Reports: {reports: [answer\|sensitivity\|limits], values?: {cell: number} (the solution; default the variable cells' current values), original?: {cell: number} (the values before solving; default `values`), message?: text (the result line), skipNotOptimal?: bool (default false: a Sensitivity report for values that are not optimal refuses the call; true leaves it out and writes the others), model?: data.solver params (default the sheet's saved model, with any data.solver params given here over it)} → {sheets: [names], skippedReports?: [{report, reason}]}. Writes Answer, Sensitivity and Limits reports on new sheets before the model's sheet; Sensitivity and Limits need Simplex LP or GRG Nonlinear and no integer constraints, and Sensitivity a Max or Min objective. data.solver's result can be passed as is.
- `data.solverSaveModel` — Save Model: {to: "H1" (the first cell, on the model's sheet), model?: data.solver params (default the sheet's saved model), overwrite?: false} → {range}. Writes the model down a column as formulas: =MAX(objective), =MIN(objective) or =objective=value; =COUNT(variables); one =AND(relation) per constraint (=AND(x=INT(x)) for integer, =AND((x=0)+(x=1)) for binary), which shows TRUE while it holds; and the options as an array constant {method (1 GRG Nonlinear, 2 Simplex LP, 3 Evolutionary), non-negative (1 yes, 2 no), population size, mutation rate, random seed, require bounds (1 yes, 2 no), convergence, generations without improvement, maximum evaluations, integer optimality %}, which spills into the cells to its right. Refused, with the sheet unchanged, when the model's cells, content, another formula's spilled values, merged cells or a table are in the way of the options' spill, or it would run off the sheet, and when the column would cover another formula's spilled values. A column that holds a value or a formula (a model saved there before included) is replaced only with overwrite: true; without it the command is refused ("already holds data"), as Excel asks first. One undo step.
- `data.solverLoadModel` — Load Model: {from: "H1:H6" (a range on the active sheet; one cell reads down to the first cell without a formula; a range needs a formula in every cell up to its last formula, and may end in empty cells)} → {model}. Reads a model written by Save Model and makes it the sheet's Solver model. The model must end with its options row ({…}), which Save Model writes last; a model cut short (a cell before the options row without a formula, or the options row cleared) is refused and the sheet's model stays as it was.
- `data.solverReset` — Reset All: {} → {removed, masked}. Removes the active sheet's Solver model. A model read from workbook-level names stays for the other sheets and is masked on this one by an empty sheet-level solver_opt (masked: true).
- `data.refreshAll` — Refresh All (Data › Queries & Connections) [Cmd+Alt+F5]: {replace?} refreshes every PivotTable → {refreshed, errors}
- `data.goalSeek` — Goal Seek… (Data › Forecast › What-If Analysis): {set: "B5" (formula cell), to: number, changing: "B2" (constant cell)} → {value, result, iterations, converged}. Secant search with bisection once the answer is bracketed; stops within Maximum Change (0.001) or after Maximum Iterations (100) from File › Options › Formulas. Writes the found value into `changing`.
- `data.scenarioManager` — Scenario Manager… (Data › Forecast › What-If Analysis): {sheet?} → {scenarios: [{name, sheet, changing, values, comment}]} (scenarios of the active sheet; `sheet: "*"` lists all)
- `data.scenarioAdd` — Add Scenario: {name, changing: "B2:B4" or "B2,B4" (≤32 cells, active sheet), values?: [..] (default: the cells' current values), comment?, replace?: bool}
- `data.scenarioShow` — Show Scenario: {name} writes the scenario's values into its changing cells
- `data.scenarioDelete` — Delete Scenario: {name}
- `data.scenarioSummary` — Scenario Summary: {resultCells?: "B10" or "B10:B12,D4"} inserts a "Scenario Summary" sheet: changing cells and result cells for the current values and each scenario
- `data.dataTable` — Data Table… (Data › Forecast › What-If Analysis): {range: "D2:E10", rowInput?: "B1", columnInput?: "B2"} one-variable (values down the first column with columnInput, or across the top row with rowInput; formulas in the other edge) or two-variable (formula in the top-left corner). Computes every result by substitution and writes static values (a snapshot, not a live {=TABLE()}); ≤100,000 cells.
- `data.advancedFilter` — Advanced… (Data › Sort & Filter): {range? (list with headers; default current region), criteria?: "H1:I3" (omitted/blank matches all rows; header row of field names; rows OR'ed, columns AND'ed; ">100", "=abc", "a*", "<>"; blank-headed formula cells are computed criteria for the first data row), copyTo?: "K1" (else filter in place by hiding rows), unique?: bool}
- `data.consolidate` — Consolidate… (Data › Data Tools): {sources: ["Sheet2!A1:C10", ..], destination?: "A1" (default active cell), function?: sum\|count\|countNums\|average\|max\|min\|product, topRow?: bool, leftColumn?: bool (consolidate by labels; else by position)}
- `data.forecastSheet` — Forecast Sheet (Data › Forecast): {timeline?: "A2:A25", values?: "B2:B25" (default: the first two columns of `range`, the selection or the current region; a text first cell is the header), end?: timeline value or date text \| periods?: n (default: a third of the history, at least 1; ≤10,000 and history × periods ≤ 500,000; history ≤ 10,000 rows), forecastStart?: a timeline value or date text on the history, before its last point (hindcast: the model is fit to the points before it, the forecast columns start there and run over the actuals; default and the last point: forecast after the history), confidenceInterval?: bool (default true), confidence?: 0.95 or 95, seasonality?: "auto" \| 0 (none) \| 2–8,760, fillMissing?: interpolate\|zeros, aggregate?: average\|count\|counta\|max\|median\|min\|sum, statistics?: bool, chart?: line\|column} → {sheet, table, chart, history, periods}. Inserts a sheet before the active one: timeline, values, Forecast (FORECAST.ETS), Lower/Upper Confidence Bound (FORECAST.ETS.CONFINT), optional FORECAST.ETS.STAT table, and a chart.
- `data.analysisToolPak` — Data Analysis… (Data › Analysis): {tool: anovaSingle\|anovaTwoFactorWith\|anovaTwoFactorWithout\|correlation\|covariance\|descriptive\|exponentialSmoothing\|fTest\|fourierAnalysis\|histogram\|movingAverage\|randomNumberGeneration\|rankPercentile\|regression\|sampling\|tTestPaired\|tTestEqual\|tTestUnequal\|zTest (or the tool's label), output?: "E1" (top-left of the report; default a new sheet), newSheet?: name, outputTo?: range\|newSheet (picks between the two), overwrite?: bool (else non-empty output cells are refused), labels?: bool (first row/column holds names), groupedBy?: columns\|rows, …tool params} — range tools take `range`; descriptive: summary? (default true), confidence?: 95, kthLargest?, kthSmallest?; histogram: bins?: range (default evenly spaced), pareto?, cumulative?; regression: inputY, inputX, constantZero?, confidence?: 95, residuals?, standardizedResiduals?, normalProbability?; movingAverage: interval? (3), standardErrors?; exponentialSmoothing: damping? (0.3), standardErrors?; t-tests and fTest: range1, range2, alpha? (0.05), hypothesizedDifference? (0); anovaSingle: alpha?; anovaTwoFactorWithout: range, labels? (the first row holds column names and the first column row names), alpha?; anovaTwoFactorWith: range (first row and column hold labels), rowsPerSample, alpha?; zTest: range1, range2, variance1, variance2 (known variances), alpha?, hypothesizedDifference?; fourierAnalysis: range (one row or column of 2^k numbers or complex text, at most 4096), inverse?; randomNumberGeneration: variables? (1), count (per variable; not for patterned), distribution: uniform{from, to} \| normal{mean, standardDeviation} \| bernoulli{p} \| binomial{p, trials} \| poisson{lambda} \| patterned{from, to, step, repeatEach, repeatSequence} \| discrete{valueRange: two columns of value and probability}, seed? (whole number, not for patterned; the same seed repeats the numbers; the result reports the seed used), at most 1,000,000 numbers; sampling: range, method?: periodic\|random, period (periodic), samples (random, with replacement), seed?. Writes static values. No `tool` → {tools} (the menu opens the dialog).

## formulas

- `formulas.autoSum` — AutoSum (Formulas › Function Library) [Cmd+Shift+T]: {function?: SUM\|AVERAGE\|COUNT\|MAX\|MIN, range?}
- `formulas.insertFunction` — Insert Function… (Formulas › Function Library) [Shift+F3]: {name?: "VLOOKUP"} (UI opens the dialog; with a name, starts the formula in the active cell)
- `formulas.functions` — List Functions: {category?, search?} → [{name, category, signature, description}]
- `formulas.defineName` — Define Name… (Formulas › Defined Names): {name, refersTo?: "=Sheet1!$A$1:$A$10" (default: the selection), scope?: "Workbook"\|sheet name, comment?, oldName?, oldScope?, force?: bool} (oldName: edit that name (Name Manager › Edit); a new name also renames it in formulas; a hidden name GridCraft keeps its own data in, `_gc_<key>_<n>` or `_sc_<key>`, is refused unless force is true)
- `formulas.deleteName` — Delete Name: {name, scope?: "Workbook"\|sheet name (default: every scope), force?: bool} (a hidden name GridCraft keeps its own data in, `_gc_<key>_<n>` or `_sc_<key>`, is refused unless force is true)
- `formulas.nameManager` — Name Manager (Formulas › Defined Names) [Cmd+F3]: {} → names with values
- `formulas.createFromSelection` — Create from Selection (Formulas › Defined Names) [Cmd+Shift+F3]: {range?, top?: true, left?: false, bottom?: false, right?: false, replace?: false (existing names are kept and listed in `skipped`), force?: false (labels of the shape GridCraft keeps its own data in, `_gc_<key>_<n>` and `_sc_<key>`, are listed in `skipped` unless force is true)}
- `formulas.pasteName` — Paste Names… (Formulas › Defined Names) [F3]: {name?: "Sales" (one of the names listed; OK: puts the name at the caret of the cell being edited, or starts `=Sales` in the active cell), list?: true (Paste List: writes each name and what it refers to in two columns, from `at`), at?: cell (default the active cell)} → {names: [{name, refersTo}]}: the names the Paste Name dialog lists (workbook names and the active sheet's own, hidden names left out, in alphabetical order). With neither nothing changes; the menu opens the dialog.
- `formulas.tracePrecedents` — Trace Precedents (Formulas › Formula Auditing): {cell?} → ranges
- `formulas.traceDependents` — Trace Dependents (Formulas › Formula Auditing): {cell?} → cells
- `formulas.traceError` — Trace Error (Formulas › Formula Auditing): {cell?} → {sheet, cell, error, source: {sheet, cell}, arrows: [{from: {sheet, range}, to: {sheet, cell}, kind: "error"\|"precedent"}], truncated}: from the cell, follows the first reference that shows the same error (in a range, its first cell showing it) back to the cell the error starts in, `source`. `error` arrows link the cells on the way; `precedent` arrows lead from the source's own references into it. A cell without an error gives `error` and `source` null and no arrows. A chain longer than 10,000 links stops there with `truncated` true and `source` null.
- `formulas.selectPrecedents` — Select Precedents (Formulas › Formula Auditing) [Ctrl+[]: {cell?, all?: true = every level (Ctrl+Shift+[)} → selects the precedent cells
- `formulas.selectDependents` — Select Dependents (Formulas › Formula Auditing) [Ctrl+]]: {cell?, all?: true = every level (Ctrl+Shift+])}
- `formulas.removeArrows` — Remove Arrows (Formulas › Formula Auditing): {}
- `formulas.showFormulas` — Show Formulas (Formulas › Formula Auditing) [Ctrl+`]: {on?}
- `formulas.convertToNumber` — Convert to Number: {range?} → {converted} (numbers stored as text in the range or selection become numbers)
- `formulas.errorChecking` — Error Checking (Formulas › Formula Auditing): {} → cells with errors
- `formulas.evaluateFormula` — Evaluate Formula (Formulas › Formula Auditing): {cell?, formula?} → steps
- `formulas.evaluate` — Evaluate: {formula: "=SUM(A1:A3)", cell?} → value without changing the sheet; a formula that couldn't be entered in a cell is an error
- `formulas.calculateNow` — Calculate Now (Formulas › Calculation) [F9]: {}
- `formulas.calculateSheet` — Calculate Sheet (Formulas › Calculation) [Shift+F9]: {}
- `formulas.calculationOptions` — Calculation Options (Formulas › Calculation): {mode?: automatic\|automaticExceptTables\|manual, iterative?: bool (Enable iterative calculation), maxIterations?: 1–32767 (100), maxChange?: number (0.001)} → the settings. File › Options › Formulas › Calculation options; stored in the workbook.
- `formulas.recentlyUsed` — Recently Used (Formulas › Function Library): {} → the functions most recently entered in formulas, newest first
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

- `view.freezePanes` — Freeze Panes (View › Window › Freeze Panes): {sheet?, cell?: "B2" (rows above and columns left of it freeze); without `cell`, unfreezes a frozen sheet}
- `view.freezeTopRow` — Freeze Top Row (View › Window › Freeze Panes): {sheet?}
- `view.freezeFirstColumn` — Freeze First Column (View › Window › Freeze Panes): {sheet?}
- `view.unfreezePanes` — Unfreeze Panes (View › Window › Freeze Panes): {sheet?}
- `view.gridlines` — Gridlines (View › Show): {on?}
- `view.headings` — Headings (View › Show): {on?}
- `view.showZeros` — Show Zeros: {on?}
- `view.showOutlineSymbols` — Show Outline Symbols [Ctrl+8]: {on?}
- `view.showObjects` — Show Objects [Ctrl+6]: {on?}
- `view.showSheetTabs` — Show Sheet Tabs: {on?} (File › Options › Advanced, this workbook; toggles without `on`)
- `view.showHorizontalScrollBar` — Show Horizontal Scroll Bar: {on?} (this workbook; toggles without `on`)
- `view.showVerticalScrollBar` — Show Vertical Scroll Bar: {on?} (this workbook; toggles without `on`)
- `view.rightToLeft` — Sheet Right-to-Left (Page Layout › Sheet Options): {on?}
- `view.zoom` — Zoom (View › Zoom): {percent: 10..400}
- `view.zoom100` — 100% (View › Zoom): {}
- `view.formulaBar` — Formula Bar (View › Show): {on?: bool}
- `view.statusBar` — Customize Status Bar: {average?, count?, numericalCount?, minimum?, maximum?, sum?: bool (the statistics shown for a selection; returns all six)}
- `view.zoomToSelection` — Zoom to Selection (View › Zoom): {viewWidth?, viewHeight?}
- `view.normal` — Normal (View › Workbook Views): {sheet?} → {view} (per sheet, saved with the file)
- `view.pageLayout` — Page Layout (View › Workbook Views): {sheet?} → {view}: pages on paper with rulers; headers and footers are edited in place (per sheet, saved with the file)
- `view.pageBreakPreview` — Page Break Preview (View › Workbook Views): {sheet?} → {view} (per sheet, saved with the file)
- `view.customViews` — Custom Views… (View › Workbook Views): {save?: name, show?: name, delete?: name} → list
- `view.split` — Split (View › Window): {} (toggles a split at the active cell; shown as frozen panes in this version)
- `view.newWindow` — New Window (View › Window): {} → {window, doc, title}: opens another window on the active workbook (the same workbook: saving from either window saves it)
- `view.arrangeAll` — Arrange All (View › Window): {arrange?: tiled\|horizontal\|vertical\|cascade, activeWorkbook?: bool} → {arrange, windows}: lays out the visible windows (tiled by default; `activeWorkbook` only the active workbook's), the active window first
- `view.hideWindow` — Hide (View › Window): {window?, doc?} (the active window by default)
- `view.unhideWindow` — Unhide… (View › Window): {window?, doc?, index?} (the most recently hidden window by default)
- `view.switchWindows` — Switch Windows (View › Window): {window?, doc?} → open windows [{window, doc, index, title, dirty, active, hidden}]; with `window` (an id from the list), or `doc` (a workbook id: its most recent window), shows and activates that window first
- `view.ruler` — Ruler (View › Show): {on?} → {on}: rulers in Page Layout view (an application option)
- `view.macros` — Macros (View › Macros): {} → scripts

## pageLayout

- `pageLayout.orientation` — Orientation (Page Layout › Page Setup): {orientation: portrait\|landscape}
- `pageLayout.size` — Size (Page Layout › Page Setup): {paper: Letter\|Legal\|A4\|A3\|A5\|A6\|Tabloid\|Executive\|Ledger\|B4\|B5\|B6\|B4 (ISO)\|B5 (ISO)\|B6 (ISO)\|Japanese Postcard\|Japanese Double Postcard\|Japanese Envelope #3\|Japanese Envelope #4\|Japanese Envelope Kaku #2\|Japanese Envelope Kaku #3 (B4/B5/B6 are the JIS sizes)}
- `pageLayout.margins` — Margins (Page Layout › Page Setup): {preset?: normal\|wide\|narrow, left?, right?, top?, bottom?, header?, footer? (inches)}
- `pageLayout.printArea` — Set Print Area (Page Layout › Page Setup › Print Area): {range?, clear?: bool}
- `pageLayout.printTitles` — Print Titles (Page Layout › Page Setup): {rows?: "1:1", cols?: "A:A"}
- `pageLayout.scaleToFit` — Scale to Fit (Page Layout › Scale to Fit): {scale?: 100, width?: pages, height?: pages}
- `pageLayout.printGridlines` — Print Gridlines (Page Layout › Sheet Options): {on?}
- `pageLayout.printHeadings` — Print Headings (Page Layout › Sheet Options): {on?}
- `pageLayout.breaks` — Breaks (Page Layout › Page Setup): {insert?: bool, remove?: bool, reset?: bool, cell?}
- `pageLayout.headerFooter` — Header & Footer (Insert › Text): {sheet?, header?: "&C&P", footer?: "&CPage &P of &N", differentFirst?: bool, differentOddEven?: bool, scaleWithDoc?: bool, alignWithMargins?: bool, firstHeader?, firstFooter?, evenHeader?, evenFooter?} or one section: {sheet?, page?: odd\|even\|first, part: header\|footer, section: left\|center\|right, text: "Page &[Page] of &[Pages]"} (field names or codes) → {header, footer, differentFirst, differentOddEven, scaleWithDoc, alignWithMargins, firstHeader, firstFooter, evenHeader, evenFooter}
- `pageLayout.theme` — Themes (Page Layout › Themes): {name: Craft\|Slate\|Meadow\|Ember\|Ocean\|Orchid\|Graphite, colors?: [12 hex], majorFont?, minorFont?}
- `pageLayout.themeColors` — Colors (Page Layout › Themes): {name: theme name \| colors: [12 hex]}
- `pageLayout.themeFonts` — Fonts (Page Layout › Themes): {major, minor}
- `pageLayout.themeEffects` — Effects (Page Layout › Themes): {name} (chart effects preset; stored with the theme name)
- `pageLayout.background` — Background (Page Layout › Page Setup): {path? \| clear?: bool} (sheet background picture)
- `pageLayout.pageSetup` — Page Setup… (Page Layout › Page Setup): {sheet?, orientation?: portrait\|landscape, paper?: Letter\|Legal\|A4\|A3\|A5\|A6\|Tabloid\|Executive\|Ledger\|B4\|B5\|B6\|B4 (ISO)\|B5 (ISO)\|B6 (ISO)\|Japanese Postcard\|Japanese Double Postcard\|Japanese Envelope #3\|Japanese Envelope #4\|Japanese Envelope Kaku #2\|Japanese Envelope Kaku #3 (B4/B5/B6 are the JIS sizes), margins?: {left,right,top,bottom,header,footer} (inches; also accepted as top-level keys), scale?: 10..400, fitWidth?, fitHeight? (pages; 0 = automatic), fitToPage?: bool, centerH?, centerV?, gridlines?, headings?, header?: "&L&A&RPage &P of &N", footer?, printArea?: "A1:F50" ("" clears), titleRows?: "1:2", titleCols?: "A:A", rowBreaks?: [46, 91], colBreaks?: ["K"], pageOrder?: downThenOver\|overThenDown} → the sheet's print settings

## document

- `document.inspect` — Inspect Workbook: {} → sheets, selection, names, tables, charts, dirty, trust (local\|fromFile), history

## history

- `history.list` — Undo History: {} → undo/redo labels, grouping (an undo group is open)

## app

- `app.commands` — List Commands: {search?} → ids, labels, params

## arrange

- `arrange.bringForward` — Bring Forward (Page Layout › Arrange): {kind: chart\|image\|shape\|slicer\|equation, id, toFront?: bool}
- `arrange.sendBackward` — Send Backward (Page Layout › Arrange): {kind: chart\|image\|shape\|slicer\|equation, id, toBack?: bool}
- `arrange.selectionPane` — Selection Pane (Page Layout › Arrange): {} → objects on the sheet in stacking order
- `arrange.align` — Align (Page Layout › Arrange): {kind: chart\|image\|shape\|slicer\|equation, ids: [..], align: left\|center\|right\|top\|middle\|bottom}
- `arrange.group` — Group (Page Layout › Arrange): {kind, ids} (moves objects together: aligns their anchors to the first)
- `arrange.rotate` — Rotate (Page Layout › Arrange): {kind: shape, id} (swaps width/height for a 90° turn; `flip` is rejected: shapes have no flip state)

## automate

- `automate.recordActions` — Record Actions (Automate › Scripting Tools): {stop?: bool, name?: script name when stopping}
- `automate.newScript` — New Script (Automate › Scripting Tools): {name, commands: [{command, params}] }
- `automate.allScripts` — All Scripts (Automate › Scripting Tools): {} → saved scripts
- `automate.runScript` — Run Script: {name, trusted?: bool (runs a script from an untrusted workbook this once)} — refuses scripts in a workbook opened from a file until it is trusted, and steps that reach outside the workbook (file.*, link.*, any `path` param)
- `automate.trustScripts` — Trust Scripts (Automate › Scripting Tools): {trusted?: bool (default true)} → {trusted}: lets this workbook's scripts run for the rest of the session
- `automate.deleteScript` — Delete Script: {name}
- `automate.stopAction` — Stop Action: {} → {stopped: bool}: stops an action left running on the active workbook (an open undo group, such as a debugger's) and puts back the workbook and its undo history as they were when it began

## macro

- `macro.list` — List Macros: {} → [{name, description, shortcut?, steps, inputs: [names], onConflict, permissions}]
- `macro.get` — Get Macro: {name} → the macro: {v, name, description, shortcut?, inputs, steps, output, permissions}
- `macro.save` — Save Macro: {macro: {name, description?, shortcut?, inputs?: [{name, kind: cell\|range, rows: [min, max], cols: [min, max], header, colTypes: [number\|text\|date\|bool\|any], nonEmpty, defaultRef?}], steps: [{type: command, id, params, enabled?, breakpoint?, note?} \| {type: repeat, over, of: rows\|columns, max, body} \| {type: if, cell, op: eq\|ne\|gt\|ge\|lt\|le\|empty\|notEmpty\|contains, value, then, else} \| {type: stop, message, rollback?}], output?: {anchor?, onConflict: ask\|fail\|overwrite\|shiftDown\|shiftRight}, permissions?: [command ids]} (or those fields at the top level), replace?: bool (default false: saving over a macro with the name is refused)} → {name, steps}
- `macro.delete` — Delete Macro: {name}
- `macro.rename` — Rename Macro: {name, to}
- `macro.run` — Run Macro: {name, inputs?: {Input: "B2:D9"} \| "B2:D9", onConflict?: ask\|fail\|overwrite\|shiftDown\|shiftRight, overwrite?: bool, approve?: bool, timeLimit?: seconds} runs as one undo step; any error rolls it all back → {macro, ran, inputs, stopped?, shifted?}
- `macro.check` — Check Macro: {name, inputs?, onConflict?, overwrite?, timeLimit?: seconds} validates the inputs and dry-runs the macro on the workbook (then puts everything back) → {ok (macro.run with these parameters would go ahead without a question), errors?, needsApproval?, onConflict, inputs, output?, conflicts, footprint}
- `macro.record` — Record Macro (View › Macros): {stop?: bool, cancel?: bool (ends a recording without saving it), relative?: bool (default true; when starting), name?, shortcut?: "Ctrl+Shift+M" \| "M", description?} toggles recording; when starting, the name (new and valid) and the shortcut (free) are checked and kept for the save, and without a name the macro gets the next MacroN; when stopping, a name or description given then wins (a taken name gets a suffix); with relative references the selection when it starts is the example input → {recording, name?, relative?, input?} or {recording: false, saved, steps, dropped, skipped, inputs, shortcutDropped? (the shortcut another macro took while recording)}
- `macro.debug` — Step Into: {action: start\|step\|continue\|runTo\|stop\|state, name, inputs?, onConflict?, overwrite?, approve?, timeLimit?: seconds per action (start, as macro.run), step: path (runTo), keep?: bool (stop), breakpoints?: ["3", "2.1"] (steps of the macro), breakpointsOnly?: bool (the list replaces the steps' own breakpoints)} debugs a macro one step at a time; stop keeps the changes as one undo step or rolls them back. Runs on its own, never as a step of a script or macro. Until it finishes or stops, its workbook runs only macro.debug, queries, selection and sheet changes, Go To, Find, Copy, zoom, Switch Window, Close and Stop Action (other workbooks stay editable) → {state: paused\|finished\|stopped\|failed, current: {step, kind, command?, params?, iteration?}, lastParams, executed, changed (at most 500), changedCells, atBreakpoint?, shifted?, wroteFiles?, message?, error?}

## draw

- `draw.pen` — Pen (Draw › Tools): {on?: bool, color?: hex, width?: 2}
- `draw.eraser` — Eraser (Draw › Tools): {on?: bool}
- `draw.lasso` — Lasso Select (Draw › Tools): {} (selects ink by dragging; same as Select Objects)
- `draw.stroke` — Ink Stroke: {points: [[x,y],…] in sheet points, color?: hex, width?: 2}
- `draw.inkToShape` — Ink to Shape (Draw › Convert): {id?} converts an ink stroke (default: the last) into a rectangle, ellipse, triangle or line

## pivot

- `pivot.calculatedField` — Calculated Field (PivotTable Analyze › Calculations): {pivot?, name, formula?: "=Sales*0.1" (fields bare or 'quoted'; evaluated on each cell's sums), delete?: bool, values?: bool (add a new field to Values, default true)} adds, changes or deletes a calculated field; without `name` opens the dialog → {name, formula, calculatedFields}
- `pivot.fields` — PivotTable Fields: {pivot?} → source fields (name, numeric, date, samples, areas) and the current layout
- `pivot.fieldList` — Field List (PivotTable Analyze › Show): {pivot?} (same as pivot.fields)
- `pivot.list` — PivotTables: {} → every PivotTable in the workbook
- `pivot.addField` — Add Field: {pivot?, field, area: rows\|columns\|values\|filters, func?: sum\|count\|average\|max\|min\|product\|countNumbers\|stdDev\|stdDevP\|var\|varP, name?, position?: index, replace?}
- `pivot.removeField` — Remove Field: {pivot?, field (or value caption), area?: rows\|columns\|values\|filters, replace?}
- `pivot.moveField` — Move Field: {pivot?, field ("Σ Values" moves the value fields between rows and columns; in columns it stays after the last field), from: rows\|columns\|values\|filters, to: rows\|columns\|values\|filters, position?: index, replace?}
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
- `pivot.showDetails` — Show Details: {cell?: "B5" (a value, subtotal or grand total cell of a PivotTable on the active sheet; default: the active cell)} puts the source records behind that value on a new sheet before the current one → {sheet, records}. An error when the PivotTable's Enable show details option is off (`pivot.options` `{enableShowDetails: true}` turns it on).
- `pivot.options` — PivotTable Options (PivotTable Analyze › PivotTable): {pivot?, enableShowDetails?: bool (Data › Enable show details: off, Show Details and double-clicking a value cell list no records)} → {enableShowDetails}
- `pivot.delete` — Delete PivotTable (PivotTable Analyze › Actions): {pivot?} clears the report and removes the PivotTable

## python

- `python.set` — Set Python Code: {cell?, code, output?: object\|value} makes the cell (default: the active cell) a Python cell with this code; the code must fit in Excel's 8,192-character formula once written as PY(…). `output` is the return type: `value` (an Excel value, the default) or `object` (a Python object)
- `python.output` — Python Output [Ctrl+Alt+Shift+M]: {cell?, mode?: object\|value} sets the return type of a Python cell (default: the active cell): `object` (a Python object) or `value` (an Excel value). Without `mode` it switches to the other one. The cell keeps its code; a cached result of the old return type goes, as with `python.set`, so the cell shows #BLOCKED! until it runs

## slicer

- `slicer.toggle` — Toggle Slicer Value: {slicer?: id, value: "East", multi?: false}
- `slicer.selectAll` — Clear Slicer Filter: {slicer?: id}
- `slicer.clear` — Clear Slicer Filter: {slicer?: id}
- `slicer.delete` — Delete Slicer: {slicer?: id}
