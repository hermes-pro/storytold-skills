# WordCraft command catalog

Generated from `wordcraft-cli commands` (WordCraft 0.3.0): 389 commands. Run one with `execute {command, params}`, or several with `batch`.
Grep this file for a verb (`grep -n 'table[.]' commands.md`) rather than reading it whole.
`?` = optional, `a|b` = choices, `→` = what it returns. Unknown param keys are ignored silently, so copy names exactly.
`(Tab › Group)` is where the command sits in the desktop UI; `[keys]` is its shortcut.

Groups: `text` (14), `caret` (15), `select` (11), `edit` (17), `format` (34), `para` (43), `styles` (7), `view` (26), `insert` (33), `layout` (14), `table` (34), `review` (32), `file` (23), `document` (6), `design` (11), `references` (23), `mailings` (17), `picture` (13), `arrange` (7), `shape` (3), `tools` (3), `hf` (3)

## text

- `text.insert` (Editing): Type Text {"text": string}
- `text.newParagraph` (Editing): New Paragraph {} [Enter]
- `text.lineBreak` (Editing): Line Break {} [Shift+Enter]
- `text.pageBreak` (Insert › Pages): Page Break {} [Mod+Enter]
- `text.columnBreak` (Layout › Breaks): Column Break {} [Mod+Shift+Enter]
- `text.tab` (Editing): Tab {} [Tab]
- `text.backTab` (Editing): Shift+Tab {} [Shift+Tab]
- `text.backspace` (Editing): Backspace {} [Backspace]
- `text.delete` (Editing): Delete {} [Delete]
- `text.deleteWordBack` (Editing): Delete Previous Word {} [Mod+Backspace / Alt+Backspace]
- `text.deleteWordForward` (Editing): Delete Next Word {} [Mod+Delete / Alt+Delete]
- `text.nbsp` (Insert › Symbols): Nonbreaking Space {} [Mod+Shift+Space]
- `text.nbHyphen` (Insert › Symbols): Nonbreaking Hyphen {} [Mod+Shift+-]
- `text.optionalHyphen` (Insert › Symbols): Optional Hyphen {} [Mod+-]

## caret

- `caret.left` (Navigation): Left {"extend"?: bool} [Left]
- `caret.right` (Navigation): Right {"extend"?: bool} [Right]
- `caret.up` (Navigation): Up {"extend"?: bool} [Up]
- `caret.down` (Navigation): Down {"extend"?: bool} [Down]
- `caret.wordLeft` (Navigation): Word Left {"extend"?: bool} [Mod+Left / Alt+Left]
- `caret.wordRight` (Navigation): Word Right {"extend"?: bool} [Mod+Right / Alt+Right]
- `caret.home` (Navigation): Line Start {"extend"?: bool} [Home]
- `caret.end` (Navigation): Line End {"extend"?: bool} [End]
- `caret.paraUp` (Navigation): Paragraph Up {"extend"?: bool} [Mod+Up / Alt+Up]
- `caret.paraDown` (Navigation): Paragraph Down {"extend"?: bool} [Mod+Down / Alt+Down]
- `caret.docStart` (Navigation): Document Start {"extend"?: bool} [Mod+Home]
- `caret.docEnd` (Navigation): Document End {"extend"?: bool} [Mod+End]
- `caret.pageUp` (Navigation): Page Up {"extend"?: bool} [PageUp]
- `caret.pageDown` (Navigation): Page Down {"extend"?: bool} [PageDown]
- `caret.set` (Navigation): Set Caret {"pos": Pos, "extend"?: bool} | {"page": n, "x": pt, "y": pt}

## select

- `select.all` (Home › Editing › Select): Select All {} [Mod+A]
- `select.range` (Navigation): Select Range {"anchor": Pos, "focus": Pos}
- `select.word` (Navigation): Select Word {}
- `select.sentence` (Navigation): Select Sentence {}
- `select.paragraph` (Navigation): Select Paragraph {}
- `select.line` (Navigation): Select Line {}
- `select.text` (Navigation): Select Text {"text": string, "occurrence"?: n}
- `select.collapse` (Navigation): Collapse Selection {} [Escape]
- `select.objects` (Home › Editing › Select): Select Objects {"index"?: n}
- `select.similar` (Home › Editing › Select): Select Text with Similar Formatting {}
- `select.extend` (Editing › Selection): Extend Selection {} [F8]

## edit

- `edit.undo` (Quick Access Toolbar): Undo {} [Mod+Z]
- `edit.redo` (Quick Access Toolbar): Redo {} [Mod+Y / Mod+Shift+Z]
- `edit.cut` (Home › Clipboard): Cut {} [Mod+X]
- `edit.copy` (Home › Clipboard): Copy {} [Mod+C]
- `edit.paste` (Home › Clipboard): Paste {"text"?: string} [Mod+V]
- `edit.pasteText` (Home › Clipboard › Paste): Paste: Keep Text Only {"text"?: string} [Mod+Shift+Alt+V]
- `edit.pasteMerge` (Home › Clipboard › Paste): Paste: Merge Formatting {"text"?: string}
- `edit.find` (Home › Editing): Find {"text": string, "matchCase"?: bool, "wholeWord"?: bool, "regex"?: bool} [Mod+F]
- `edit.findNext` (Home › Editing › Find): Find Next {} [Mod+G / F3]
- `edit.findPrevious` (Home › Editing › Find): Find Previous {} [Mod+Shift+G / Shift+F3]
- `edit.replace` (Home › Editing): Replace {"text": string, "with": string} [Mod+H]
- `edit.replaceAll` (Home › Editing › Replace): Replace All {"text": string, "with": string, "matchCase"?: bool, "wholeWord"?: bool, "regex"?: bool}
- `edit.goto` (Home › Editing › Find): Go To {"page"?: n, "bookmark"?: string, "paragraph"?: n} [Mod+Alt+G / F5]
- `edit.formatPainter` (Home › Clipboard): Format Painter {"sticky"?: bool}
- `edit.copyFormat` (Home › Clipboard): Copy Formatting {} [Mod+Shift+C]
- `edit.pasteFormat` (Home › Clipboard): Paste Formatting {} [Mod+Shift+V]
- `edit.repeat` (Quick Access Toolbar): Repeat {} [F4]

## format

- `format.bold` (Home › Font): Bold {"value"?: bool} [Mod+B]
- `format.italic` (Home › Font): Italic {"value"?: bool} [Mod+I]
- `format.underline` (Home › Font): Underline {"value"?: bool, "style"?: "single|double|thick|dotted|dash|dotDash|dotDotDash|wave|words"} [Mod+U]
- `format.doubleUnderline` (Home › Font › Underline): Double Underline {} [Mod+Shift+D]
- `format.wordUnderline` (Home › Font › Underline): Underline Words Only {} [Mod+Shift+W]
- `format.strikethrough` (Home › Font): Strikethrough {"value"?: bool}
- `format.doubleStrikethrough` (Home › Font › Font): Double Strikethrough {}
- `format.subscript` (Home › Font): Subscript {} [Mod+=]
- `format.superscript` (Home › Font): Superscript {} [Mod+Shift+=]
- `format.allCaps` (Home › Font › Font): All Caps {} [Mod+Shift+A]
- `format.smallCaps` (Home › Font › Font): Small Caps {} [Mod+Shift+K]
- `format.hidden` (Home › Font › Font): Hidden {} [Mod+Shift+H]
- `format.outline` (Home › Font › Text Effects): Outline {}
- `format.shadow` (Home › Font › Text Effects): Shadow {}
- `format.emboss` (Home › Font › Font): Emboss {}
- `format.engrave` (Home › Font › Font): Engrave {}
- `format.font` (Home › Font): Font {"name": string} [Mod+Shift+F]
- `format.size` (Home › Font): Font Size {"size": number} [Mod+Shift+P]
- `format.growFont` (Home › Font): Increase Font Size {} [Mod+Shift+. / Mod+Shift+>]
- `format.shrinkFont` (Home › Font): Decrease Font Size {} [Mod+Shift+, / Mod+Shift+<]
- `format.growFont1` (Home › Font): Grow Font 1 Point {} [Mod+]]
- `format.shrinkFont1` (Home › Font): Shrink Font 1 Point {} [Mod+[]
- `format.color` (Home › Font): Font Color {"color": "RRGGBB" | "auto"}
- `format.highlight` (Home › Font): Text Highlight Color {"color": "yellow|brightGreen|turquoise|pink|blue|red|darkBlue|teal|green|violet|darkRed|darkYellow|gray50|gray25|black|none"}
- `format.shading` (Home › Font): Character Shading {"color": "RRGGBB" | null}
- `format.changeCase` (Home › Font): Change Case {"mode"?: "sentence|lower|upper|title|toggle"} [Shift+F3]
- `format.clear` (Home › Font): Clear All Formatting {} [Mod+Space]
- `format.spacing` (Home › Font › Font › Advanced): Character Spacing {"points": number}
- `format.scale` (Home › Font › Font › Advanced): Character Scale {"percent": number}
- `format.position` (Home › Font › Font › Advanced): Character Position {"points": number}
- `format.charStyle` (Home › Styles): Apply Character Style {"style": string}
- `format.set` (Home › Font › Font): Set Character Formatting {"props": CharProps}
- `format.fontDialog` (Home › Font): Font Dialog {} [Mod+D]
- `format.state` (Home › Font): Formatting at Selection {}

## para

- `para.alignLeft` (Home › Paragraph): Align Left {} [Mod+L]
- `para.alignCenter` (Home › Paragraph): Center {} [Mod+E]
- `para.alignRight` (Home › Paragraph): Align Right {} [Mod+R]
- `para.justify` (Home › Paragraph): Justify {} [Mod+J]
- `para.distribute` (Home › Paragraph): Distributed {} [Mod+Shift+J]
- `para.align` (Home › Paragraph): Alignment {"value": "left|center|right|justify|distribute"}
- `para.indent` (Home › Paragraph): Increase Indent {} [Mod+M]
- `para.outdent` (Home › Paragraph): Decrease Indent {} [Mod+Shift+M]
- `para.hangingIndent` (Home › Paragraph › Paragraph): Hanging Indent {} [Mod+T]
- `para.removeHanging` (Home › Paragraph › Paragraph): Reduce Hanging Indent {} [Mod+Shift+T]
- `para.indents` (Layout › Paragraph): Indents {"left"?: pt, "right"?: pt, "firstLine"?: pt (negative = hanging)}
- `para.lineSpacing` (Home › Paragraph): Line and Paragraph Spacing {"value": number (multiple) } | {"atLeast": pt} | {"exactly": pt}
- `para.single` (Home › Paragraph › Line Spacing): Single Spacing {} [Mod+1]
- `para.double` (Home › Paragraph › Line Spacing): Double Spacing {} [Mod+2]
- `para.oneAndHalf` (Home › Paragraph › Line Spacing): 1.5 Line Spacing {} [Mod+5]
- `para.spacing` (Layout › Paragraph): Paragraph Spacing {"before"?: pt, "after"?: pt}
- `para.addSpaceBefore` (Home › Paragraph › Line Spacing): Add Space Before Paragraph {} [Mod+0]
- `para.removeSpaceAfter` (Home › Paragraph › Line Spacing): Remove Space After Paragraph {}
- `para.style` (Home › Styles): Apply Style {"style": string (name or id)} [Mod+Shift+S]
- `para.normal` (Home › Styles): Normal Style {} [Mod+Shift+N]
- `para.heading1` (Home › Styles): Heading 1 {} [Mod+Alt+1]
- `para.heading2` (Home › Styles): Heading 2 {} [Mod+Alt+2]
- `para.heading3` (Home › Styles): Heading 3 {} [Mod+Alt+3]
- `para.bullets` (Home › Paragraph): Bullets {"kind"?: "bullet" | single char, "off"?: bool} [Mod+Shift+L]
- `para.numbering` (Home › Paragraph): Numbering {"kind"?: "numbered|numberedParen|upperLetter|lowerLetter|lowerRoman|outline", "off"?: bool}
- `para.multilevel` (Home › Paragraph): Multilevel List {"kind"?: "legal|outline"}
- `para.listLevel` (Home › Paragraph › Bullets): Change List Level {"level": 0-8}
- `para.restartNumbering` (Home › Paragraph › Numbering): Restart at 1 {}
- `para.shading` (Home › Paragraph): Shading {"color": "RRGGBB" | null}
- `para.borders` (Home › Paragraph): Borders {"kind": "bottom|top|left|right|none|all|outside|inside|horizontalLine", "width"?: pt, "color"?: "RRGGBB", "style"?: "single|double|dotted|dashed|thick"}
- `para.sort` (Home › Paragraph): Sort {"descending"?: bool}
- `para.keepNext` (Home › Paragraph › Line and Page Breaks): Keep with Next {}
- `para.keepLines` (Home › Paragraph › Line and Page Breaks): Keep Lines Together {}
- `para.pageBreakBefore` (Home › Paragraph › Line and Page Breaks): Page Break Before {}
- `para.widowControl` (Home › Paragraph › Line and Page Breaks): Widow/Orphan Control {}
- `para.tabs` (Home › Paragraph › Paragraph): Tabs {"tabs": [{"pos": pt, "align": "left|center|right|decimal|bar", "leader": "none|dot|hyphen|underscore"}]}
- `para.outlineLevel` (Home › Paragraph › Paragraph): Outline Level {}
- `para.set` (Home › Paragraph › Paragraph): Set Paragraph Formatting {"props": ParaProps}
- `para.dialog` (Home › Paragraph): Paragraph Settings {}
- `para.setNumberingValue` (Home › Paragraph › Numbering): Set Numbering Value {"value": n}
- `para.defineBullet` (Home › Paragraph › Bullets): Define New Bullet {"char": string}
- `para.defineNumber` (Home › Paragraph › Numbering): Define New Number Format {"format": "decimal|upperRoman|lowerLetter…", "text"?: "%1.", "start"?: n}
- `para.rtl` (Home › Paragraph): Right-to-Left Text Direction {}

## styles

- `styles.create` (Home › Styles): Create a Style {"name": string, "basedOn"?: string, "fromSelection"?: bool}
- `styles.modify` (Home › Styles): Modify Style {"style": string, "chr"?: CharProps, "para"?: ParaProps, "name"?: string, "next"?: string}
- `styles.updateToMatch` (Home › Styles): Update Style to Match Selection {"style"?: string}
- `styles.delete` (Home › Styles): Delete Style {}
- `styles.list` (Home › Styles): Styles {}
- `styles.pane` (Home › Styles): Styles Pane {} [Mod+Alt+Shift+S]
- `styles.addToGallery` (Home › Styles): Add to Style Gallery {}

## view

- `view.marks` (Home › Paragraph): Show/Hide ¶ {} [Mod+Shift+8 / Mod+8]
- `view.printLayout` (View › Views): Print Layout {}
- `view.webLayout` (View › Views): Web Layout {}
- `view.draft` (View › Views): Draft {}
- `view.outline` (View › Views): Outline {}
- `view.readMode` (View › Views): Read Mode {}
- `view.focus` (View › Immersive): Focus {}
- `view.ruler` (View › Show): Ruler {}
- `view.gridlines` (View › Show): Gridlines {}
- `view.navigationPane` (View › Show): Navigation Pane {}
- `view.zoom` (View › Zoom): Zoom {"value": percent (10-500) | "pageWidth" | "onePage" | "multiplePages"}
- `view.zoom100` (View › Zoom): 100% {}
- `view.zoomIn` (Status Bar): Zoom In {}
- `view.zoomOut` (Status Bar): Zoom Out {}
- `view.onePage` (View › Zoom): One Page {}
- `view.multiplePages` (View › Zoom): Multiple Pages {}
- `view.pageWidth` (View › Zoom): Page Width {}
- `view.darkMode` (View › Dark Mode): Switch Modes {}
- `view.stylesPane` (Home › Styles): Styles Pane {}
- `view.commentsPane` (Review › Comments): Comments Pane {}
- `view.newWindow` (View › Window): New Window {}
- `view.split` (View › Window): Split {}
- `view.state` (View): View State {}
- `view.immersive` (View › Immersive): Immersive Reader {}
- `view.vertical` (View › Page Movement): Vertical {}
- `view.sideToSide` (View › Page Movement): Side to Side {}

## insert

- `insert.pageBreak` (Insert › Pages): Page Break {}
- `insert.blankPage` (Insert › Pages): Blank Page {}
- `insert.coverPage` (Insert › Pages): Cover Page {"title"?: string, "subtitle"?: string, "author"?: string}
- `insert.table` (Insert › Tables): Table {"rows": n, "cols": n, "style"?: string}
- `insert.picture` (Insert › Illustrations): Pictures {"path"?: string, "data"?: base64, "width"?: pt, "alt"?: string}
- `insert.shape` (Insert › Illustrations): Shapes {"kind": "rectangle|roundedRectangle|ellipse|triangle|diamond|line|arrow|star|heart", "width"?: pt, "height"?: pt, "fill"?: "RRGGBB", "stroke"?: "RRGGBB"}
- `insert.textBox` (Insert › Text): Text Box {"text"?: string, "width"?: pt, "height"?: pt}
- `insert.link` (Insert › Links): Link {"url": string, "text"?: string} [Mod+K]
- `insert.removeLink` (Insert › Links): Remove Hyperlink {}
- `insert.bookmark` (Insert › Links): Bookmark {"name": string}
- `insert.header` (Insert › Header & Footer): Header {"text"?: string, "preset"?: "blank|blankThree|title"}
- `insert.footer` (Insert › Header & Footer): Footer {"text"?: string, "preset"?: "blank|blankThree|pageNumber"}
- `insert.pageNumber` (Insert › Header & Footer): Page Number {"position"?: "top|bottom|current", "align"?: "left|center|right", "format"?: "x of y"}
- `insert.editHeader` (Insert › Header & Footer › Header): Edit Header {}
- `insert.editFooter` (Insert › Header & Footer › Footer): Edit Footer {}
- `insert.closeHeader` (Header & Footer): Close Header and Footer {}
- `insert.removeHeader` (Insert › Header & Footer › Header): Remove Header {}
- `insert.removeFooter` (Insert › Header & Footer › Footer): Remove Footer {}
- `insert.dateTime` (Insert › Text): Date & Time {"format"?: "M/d/yyyy", "update"?: bool}
- `insert.symbol` (Insert › Symbols): Symbol {"char": string}
- `insert.equation` (Insert › Symbols): Equation {"linear"?: string} [Alt+=]
- `insert.field` (Insert › Text › Quick Parts): Field {"instr": string, "result"?: string} [Mod+F9]
- `insert.dropCap` (Insert › Text): Drop Cap {"lines"?: n (0 = none)}
- `insert.horizontalLine` (Home › Paragraph › Borders): Horizontal Line {}
- `insert.wordArt` (Insert › Text): WordArt {}
- `insert.textFromFile` (Insert › Text › Object): Text from File {"path": string}
- `insert.crossReference` (Insert › Links): Cross-reference {"to": "heading|bookmark|figure|table", "target": string (text / name / number), "show"?: "text|page|number|aboveBelow"} or {} to list targets
- `insert.quickParts` (Insert › Text): Quick Parts {"save"?: name (from the selection), "insert"?: name, "delete"?: name} → list
- `insert.autoText` (Insert › Text › Quick Parts): AutoText {"save"?: name, "insert"?: name}
- `insert.docProperty` (Insert › Text › Quick Parts): Document Property {"name": "Title|Author|Subject|Keywords|Comments|Category"}
- `insert.signatureLine` (Insert › Text): Signature Line {"signer"?: string, "title"?: string}
- `insert.object` (Insert › Text): Object {"path": string}
- `insert.spreadsheet` (Insert › Tables): Spreadsheet Table {"csv"?: string}

## layout

- `layout.margins` (Layout › Page Setup): Margins {"preset"?: "normal|narrow|moderate|wide|mirrored|office2003", "top"?: pt, "bottom"?: pt, "left"?: pt, "right"?: pt, "gutter"?: pt}
- `layout.orientation` (Layout › Page Setup): Orientation {"value": "portrait|landscape"}
- `layout.size` (Layout › Page Setup): Size {"name"?: "Letter|Legal|A4|…", "width"?: pt, "height"?: pt}
- `layout.columns` (Layout › Page Setup): Columns {"count": 1-12, "space"?: pt, "separator"?: bool, "preset"?: "left|right"}
- `layout.break` (Layout › Page Setup): Breaks {"kind": "page|column|textWrapping|nextPage|continuous|evenPage|oddPage"}
- `layout.lineNumbers` (Layout › Page Setup): Line Numbers {"value": "none|continuous|restartPage|restartSection"}
- `layout.hyphenation` (Layout › Page Setup): Hyphenation {}
- `layout.pageSetup` (Layout › Page Setup): Page Setup {"section"?: SectionProps}
- `layout.verticalAlign` (Layout › Page Setup › Layout): Vertical Alignment {}
- `layout.differentFirstPage` (Header & Footer › Options): Different First Page {}
- `layout.differentOddEven` (Header & Footer › Options): Different Odd & Even Pages {}
- `layout.pageNumberFormat` (Insert › Header & Footer › Page Number): Format Page Numbers {"format"?: "decimal|lowerRoman|upperRoman|lowerLetter|upperLetter", "start"?: n}
- `layout.section` (Layout › Page Setup): Section Properties {}
- `layout.linkToPrevious` (Header & Footer › Navigation): Link to Previous {"footer"?: bool}

## table

- `table.insertRowAbove` (Table Layout › Rows & Columns): Insert Above {}
- `table.insertRowBelow` (Table Layout › Rows & Columns): Insert Below {}
- `table.insertColumnLeft` (Table Layout › Rows & Columns): Insert Left {}
- `table.insertColumnRight` (Table Layout › Rows & Columns): Insert Right {}
- `table.deleteRow` (Table Layout › Rows & Columns › Delete): Delete Rows {}
- `table.deleteColumn` (Table Layout › Rows & Columns › Delete): Delete Columns {}
- `table.deleteTable` (Table Layout › Rows & Columns › Delete): Delete Table {}
- `table.deleteCells` (Table Layout › Rows & Columns › Delete): Delete Cells {}
- `table.merge` (Table Layout › Merge): Merge Cells {}
- `table.split` (Table Layout › Merge): Split Cells {"columns"?: n}
- `table.splitTable` (Table Layout › Merge): Split Table {}
- `table.style` (Table Design › Table Styles): Table Styles {"style": string}
- `table.look` (Table Design › Table Style Options): Table Style Options {"headerRow"?: bool, "totalRow"?: bool, "bandedRows"?: bool, "firstColumn"?: bool, "lastColumn"?: bool, "bandedColumns"?: bool}
- `table.shading` (Table Design › Table Styles): Shading {"color": "RRGGBB" | null}
- `table.borders` (Table Design › Borders): Borders {"kind": "all|outside|inside|none|top|bottom|left|right", "width"?: pt, "color"?: "RRGGBB"}
- `table.cellAlign` (Table Layout › Alignment): Alignment {"value": "topLeft|topCenter|…|bottomRight"}
- `table.autofit` (Table Layout › Cell Size): AutoFit {"mode": "contents|window|fixed"}
- `table.distributeColumns` (Table Layout › Cell Size): Distribute Columns {}
- `table.distributeRows` (Table Layout › Cell Size): Distribute Rows {}
- `table.columnWidth` (Table Layout › Cell Size): Table Column Width {"width": pt}
- `table.rowHeight` (Table Layout › Cell Size): Table Row Height {"height": pt}
- `table.repeatHeader` (Table Layout › Data): Repeat Header Rows {}
- `table.sort` (Table Layout › Data): Sort {"column"?: n, "descending"?: bool, "header"?: bool}
- `table.toText` (Table Layout › Data): Convert to Text {"separator"?: "tab|comma|paragraph"}
- `table.formula` (Table Layout › Data): Formula {"formula"?: "=SUM(ABOVE)"}
- `table.selectTable` (Table Layout › Table › Select): Select Table {}
- `table.selectRow` (Table Layout › Table › Select): Select Row {}
- `table.selectCell` (Table Layout › Table › Select): Select Cell {}
- `table.properties` (Table Layout › Table): Properties {"align"?: "left|center|right"}
- `table.fromText` (Insert › Tables): Convert Text to Table {"separator"?: "tab|comma"}
- `table.quick` (Insert › Tables): Quick Tables {"kind"?: "calendar|tabular|matrix"}
- `table.textDirection` (Table Layout › Alignment): Text Direction {}
- `table.cellMargins` (Table Layout › Alignment): Cell Margins {"top"?, "left"?, "bottom"?, "right"? (pt)}
- `table.borderPainter` (Table Design › Borders): Border Painter {}

## review

- `review.newComment` (Review › Comments): New Comment {"text": string} [Mod+Alt+M]
- `review.reply` (Review › Comments): Reply {"id": n, "text": string}
- `review.deleteComment` (Review › Comments): Delete {"id"?: n, "all"?: bool}
- `review.resolveComment` (Review › Comments): Resolve {}
- `review.nextComment` (Review › Comments): Next {}
- `review.previousComment` (Review › Comments): Previous {}
- `review.comments` (Review › Comments): Show Comments {}
- `review.trackChanges` (Review › Tracking): Track Changes {} [Mod+Shift+E]
- `review.acceptAll` (Review › Changes): Accept All Changes {}
- `review.rejectAll` (Review › Changes): Reject All Changes {}
- `review.accept` (Review › Changes): Accept {}
- `review.reject` (Review › Changes): Reject {}
- `review.nextChange` (Review › Changes): Next Change {}
- `review.previousChange` (Review › Changes): Previous Change {}
- `review.markup` (Review › Tracking): Display for Review {}
- `review.wordCount` (Review › Proofing): Word Count {}
- `review.changes` (Review › Tracking): Reviewing Pane {}
- `review.spelling` (Review › Proofing): Spelling & Grammar {} [F7]
- `review.issues` (Review › Proofing): Proofing Issues {}
- `review.suggestions` (Review › Proofing): Spelling Suggestions {"pos"?: Pos}
- `review.addToDictionary` (Review › Proofing): Add to Dictionary {"word"?: string}
- `review.ignoreAll` (Review › Proofing): Ignore All {}
- `review.applySuggestion` (Review › Proofing): Change {"text": string}
- `review.proofing` (File › Options › Proofing): Check Spelling as You Type {}
- `review.thesaurus` (Review › Proofing): Thesaurus {} [Shift+F7]
- `review.compare` (Review › Compare): Compare {"path"?: string, "text"?: string (revised version)}
- `review.combine` (Review › Compare): Combine {"path"?: string}
- `review.restrict` (Review › Protect): Restrict Editing {"mode": "none|readOnly|comments|trackedChanges|forms"}
- `review.language` (Review › Language): Language {"lang": "en-US|en-GB|fr-FR|…", "noProof"?: bool}
- `review.showMarkup` (Review › Tracking): Show Markup {}
- `review.editor` (Home › Editor): Editor {}
- `review.readAloud` (Review › Speech): Read Aloud {}

## file

- `file.new` (File): New {"template"?: "blank|sample|letter|resume|report"} [Mod+N]
- `file.open` (File): Open {"path": string} [Mod+O]
- `file.save` (File): Save {"path"?: string} [Mod+S]
- `file.saveAs` (File): Save As {"path": string} [F12]
- `file.exportPdf` (File › Export): Export PDF {"path": string}
- `file.exportPng` (File › Export): Export Page as PNG {"path": string, "page"?: n (1-based), "scale"?: px per pt}
- `file.print` (File): Print {} [Mod+P]
- `file.close` (File): Close {} [Mod+W]
- `file.properties` (File › Info): Properties {"title"?, "subject"?, "author"?, "keywords"?, "comments"?, "category"?}
- `file.info` (File): Info {}
- `file.options` (File): Options {}
- `file.setAuthor` (File › Options › General): User Name {}
- `file.accessibility` (Review › Accessibility): Check Accessibility {}
- `file.inspect` (File › Info): Inspect Document {"remove"?: ["comments", "revisions", "properties", "hidden", "headers"]}
- `file.protect` (File › Info): Protect Document {"mode": "none|readOnly|comments|trackedChanges"}
- `file.versions` (File › Info): Version History {"save"?: label, "restore"?: index}
- `file.recover` (File › Info): Recover Unsaved Documents {}
- `file.newFromTemplate` (File › New): New from Template {"path": string}
- `file.saveTemplate` (File › Save As): Save as Template {"path": string}
- `file.autosave` (Quick Access Toolbar): AutoSave {}
- `file.compatibility` (File › Info): Check Compatibility {}
- `file.share` (File): Share {}
- `file.encrypt` (File › Info › Protect Document): Encrypt with Password {}

## document

- `document.inspect` (Agents): Inspect Document {"text"?: bool}
- `document.text` (Agents): Document Text {}
- `document.paragraph` (Agents): Paragraph Details {"path": [n], "story"?: Story}
- `document.selection` (Agents): Selection {}
- `document.layout` (Agents): Layout Summary {}
- `document.setText` (Agents): Replace Document Text {"text": string}

## design

- `design.theme` (Design › Document Formatting): Themes {"name": string}
- `design.themeFonts` (Design › Document Formatting): Fonts {"heading": string, "body"?: string}
- `design.themeColors` (Design › Document Formatting): Colors {}
- `design.styleSet` (Design › Document Formatting): Style Set {"name": "default|basic|lines|shaded|casual|centered|minimalist|title"}
- `design.paragraphSpacing` (Design › Document Formatting): Paragraph Spacing {"value": "default|none|compact|tight|open|relaxed|double"}
- `design.watermark` (Design › Page Background): Watermark {"text"?: string, "remove"?: bool, "diagonal"?: bool, "color"?: "RRGGBB"}
- `design.pageColor` (Design › Page Background): Page Color {"color": "RRGGBB" | null}
- `design.pageBorders` (Design › Page Background): Page Borders {"kind": "box|none", "width"?: pt, "color"?: "RRGGBB"}
- `design.setDefault` (Design › Document Formatting): Set as Default {}
- `design.themes` (Design › Document Formatting): Theme List {}
- `design.effects` (Design › Document Formatting): Effects {}

## references

- `references.toc` (References › Table of Contents): Table of Contents {"levels"?: 1-9, "title"?: string}
- `references.updateToc` (References › Table of Contents): Update Table {}
- `references.removeToc` (References › Table of Contents): Remove Table of Contents {}
- `references.addText` (References › Table of Contents): Add Text {"level": 0 (do not show) | 1-9}
- `references.footnote` (References › Footnotes): Insert Footnote {"text"?: string} [Mod+Alt+F]
- `references.endnote` (References › Footnotes): Insert Endnote {"text"?: string} [Mod+Alt+D]
- `references.nextFootnote` (References › Footnotes): Next Footnote {}
- `references.notes` (References › Footnotes): Show Notes {}
- `references.caption` (References › Captions): Insert Caption {"label"?: "Figure|Table|Equation", "text"?: string}
- `references.updateFields` (References): Update Field {} [F9]
- `references.sources` (References › Citations & Bibliography): Manage Sources {"add"?: Source, "remove"?: tag} → list
- `references.citation` (References › Citations & Bibliography): Insert Citation {"tag"?: string, "source"?: Source (added if new), "pages"?: string}
- `references.citationStyle` (References › Citations & Bibliography): Style {"style": "APA|MLA|Chicago|IEEE"}
- `references.bibliography` (References › Citations & Bibliography): Bibliography {"title"?: string}
- `references.tableOfFigures` (References › Captions): Insert Table of Figures {"label"?: "Figure|Table|Equation"}
- `references.updateFigures` (References › Captions): Update Table {}
- `references.markEntry` (References › Index): Mark Entry {"entry"?: string}
- `references.index` (References › Index): Insert Index {}
- `references.updateIndex` (References › Index): Update Index {}
- `references.markCitation` (References › Table of Authorities): Mark Citation {"entry"?: string}
- `references.tableOfAuthorities` (References › Table of Authorities): Insert Table of Authorities {}
- `references.noteOptions` (References › Footnotes): Footnote and Endnote {"footnoteFormat"?: "decimal|lowerRoman|upperRoman|lowerLetter|upperLetter", "endnoteFormat"?: …}
- `references.researcher` (References › Research): Researcher {}

## mailings

- `mailings.start` (Mailings › Start Mail Merge): Start Mail Merge {"kind": "letters|emails|envelopes|labels|directory"}
- `mailings.recipients` (Mailings › Start Mail Merge): Select Recipients {"csv"?: string, "path"?: string, "rows"?: [{field: value}]}
- `mailings.editRecipients` (Mailings › Start Mail Merge): Edit Recipient List {"rows"?: [{field: value}]}
- `mailings.insertField` (Mailings › Write & Insert Fields): Insert Merge Field {"field": string}
- `mailings.addressBlock` (Mailings › Write & Insert Fields): Address Block {}
- `mailings.greetingLine` (Mailings › Write & Insert Fields): Greeting Line {}
- `mailings.rules` (Mailings › Write & Insert Fields): Rules {"rule": "IF|SKIPIF|NEXT|MERGEREC", "field"?, "value"?, "then"?, "else"?}
- `mailings.matchFields` (Mailings › Write & Insert Fields): Match Fields {}
- `mailings.highlightFields` (Mailings › Write & Insert Fields): Highlight Merge Fields {}
- `mailings.preview` (Mailings › Preview Results): Preview Results {}
- `mailings.next` (Mailings › Preview Results): Next Record {}
- `mailings.previous` (Mailings › Preview Results): Previous Record {}
- `mailings.findRecipient` (Mailings › Preview Results): Find Recipient {}
- `mailings.checkErrors` (Mailings › Finish): Check for Errors {}
- `mailings.finish` (Mailings › Finish): Finish & Merge {"path"?: string (save the merged document), "from"?: n, "to"?: n}
- `mailings.envelopes` (Mailings › Create): Envelopes {"delivery": string, "return"?: string, "size"?: "Envelope #10|Envelope DL"}
- `mailings.labels` (Mailings › Create): Labels {"text"?: string, "rows"?: n, "cols"?: n, "fromRecipients"?: bool}

## picture

- `picture.size` (Picture Format › Size): Size {"width"?: pt, "height"?: pt, "lockAspect"?: bool, "scale"?: percent}
- `picture.crop` (Picture Format › Size): Crop {"left"?, "top"?, "right"?, "bottom"? (fractions 0–0.45)}
- `picture.altText` (Picture Format › Accessibility): Alt Text {"text": string}
- `picture.corrections` (Picture Format › Adjust): Corrections {"brightness"?: -100..100, "contrast"?: -100..100, "sharpen"?: -100..100}
- `picture.color` (Picture Format › Adjust): Color {"mode": "grayscale|sepia|washout|blackAndWhite|saturation|tint", "saturation"?: 0..400}
- `picture.effects` (Picture Format › Adjust): Artistic Effects {"effect": "blur|sharpen|invert|posterize|pixelate"}
- `picture.transparency` (Picture Format › Adjust): Transparency {"percent": 0..100}
- `picture.removeBackground` (Picture Format › Adjust): Remove Background {"tolerance"?: 0..255}
- `picture.compress` (Picture Format › Adjust): Compress Pictures {"maxPixels"?: n}
- `picture.reset` (Picture Format › Adjust): Reset Picture {}
- `picture.change` (Picture Format › Adjust): Change Picture {"path"?: string, "data"?: base64}
- `picture.style` (Picture Format › Picture Styles): Picture Styles {"style": "simpleFrame|thickFrame|rounded|softEdge|shadow"}
- `picture.border` (Picture Format › Picture Styles): Picture Border {"color"?: "RRGGBB", "width"?: px}

## arrange

- `arrange.rotate` (Layout › Arrange): Rotate {"direction": "right|left|flipH|flipV"}
- `arrange.wrap` (Layout › Arrange): Wrap Text {"wrap": "inline|square|tight|through|topAndBottom|behindText|inFrontOfText"}
- `arrange.position` (Layout › Arrange): Position {"preset"?: "topLeft|topCenter|topRight|middleLeft|middleCenter|middleRight|bottomLeft|bottomCenter|bottomRight", "x"?: pt, "y"?: pt}
- `arrange.bringForward` (Layout › Arrange): Bring Forward {}
- `arrange.sendBackward` (Layout › Arrange): Send Backward {}
- `arrange.align` (Layout › Arrange): Align {"value": "left|center|right"}
- `arrange.selectionPane` (Layout › Arrange): Selection Pane {}

## shape

- `shape.fill` (Shape Format › Shape Styles): Shape Fill {"color": "RRGGBB" | null}
- `shape.outline` (Shape Format › Shape Styles): Shape Outline {"color": "RRGGBB" | null, "width"?: pt}
- `shape.change` (Shape Format › Insert Shapes): Change Shape {"kind": string}

## tools

- `tools.recordMacro` (View › Macros): Record Macro {"name"?: string} (call again to stop)
- `tools.macros` (View › Macros): Macros {"run"?: name, "define"?: {"name": string, "steps": [{"command", "params"}]}, "delete"?: name}
- `tools.autocorrect` (File › Options › Proofing): AutoCorrect Options {"enabled"?: bool, "add"?: {"from": string, "to": string}}

## hf

- `hf.next` (Header & Footer › Navigation): Next Section {}
- `hf.previous` (Header & Footer › Navigation): Previous Section {}
- `hf.position` (Header & Footer › Position): Header/Footer Position {"header"?: pt, "footer"?: pt}
