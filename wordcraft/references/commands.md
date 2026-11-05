# WordCraft command catalog

Generated from `wordcraft-cli commands --json` (WordCraft 0.15.2): 655 commands. Run one with `execute {command, params}`, or several with `batch`.
Grep this file for a verb (`grep -n 'table[.]' commands.md`) rather than reading it whole.
`?` = optional, `a|b` = choices, `→` = what it returns. Unknown param keys are ignored silently, so copy names exactly.
`(Tab › Group)` is where the command sits in the desktop UI; `[keys]` is its shortcut.

Groups: `text` (23), `caret` (16), `select` (14), `edit` (31), `format` (41), `font` (5), `para` (50), `styles` (16), `list` (3), `view` (41), `table` (48), `outline` (26), `insert` (44), `link` (1), `equation` (21), `layout` (18), `review` (36), `file` (30), `document` (6), `proof` (3), `design` (12), `references` (25), `fields` (8), `mailings` (23), `picture` (14), `object` (1), `arrange` (15), `shape` (9), `smartArt` (9), `chart` (5), `draw` (16), `canvas` (4), `wordArt` (4), `tools` (11), `hf` (3), `readAloud` (7), `developer` (16)

## text

- `text.insert` (Editing): Type Text {"text": string, "raw"?: bool, "paragraphs"?: bool} (paragraphs: each line a paragraph, one undo step, at most 10000 lines)
- `text.newParagraph` (Editing): New Paragraph {} [Enter]
- `text.lineBreak` (Editing): Line Break {} [Shift+Enter]
- `text.pageBreak` (Insert › Pages): Page Break {} [Mod+Enter]
- `text.columnBreak` (Layout › Breaks): Column Break {} [Mod+Shift+Enter]
- `text.tab` (Editing): Tab {} [Tab]
- `text.backTab` (Editing): Shift+Tab {} [Shift+Tab]
- `text.insertTab` (Editing): Tab Character {} [Alt+Tab]
- `text.backspace` (Editing): Backspace {} [Backspace]
- `text.delete` (Editing): Delete {} [Delete]
- `text.deleteWordBack` (Editing): Delete Previous Word {} [Mod+Backspace / Alt+Backspace]
- `text.deleteWordForward` (Editing): Delete Next Word {} [Mod+Delete / Alt+Delete]
- `text.nbsp` (Insert › Symbols): Nonbreaking Space {} [Mod+Shift+Space]
- `text.nbHyphen` (Insert › Symbols): Nonbreaking Hyphen {} [Mod+Shift+-]
- `text.optionalHyphen` (Insert › Symbols): Optional Hyphen {} [Mod+-]
- `text.toggleUnicode` (Editing): Toggle Unicode Character {}
- `text.typeCode` (Editing): Type Character Code {"code": string (decimal digits as typed on the keypad, e.g. "0233"), "ansi"?: 874 | 1250–1258 (the leading-0 code page, default 1252), "oem"?: 437 | 737 | 850 | 852 | 857 | 866 (default from the locale)}
- `text.emDash` (Insert › Symbols): Em Dash {} [Mod+Alt+-]
- `text.copyright` (Insert › Symbols): Copyright Sign {}
- `text.registered` (Insert › Symbols): Registered Sign {}
- `text.trademark` (Insert › Symbols): Trademark Sign {}
- `text.ellipsis` (Insert › Symbols): Ellipsis {}
- `text.overtype` (File › Options › Advanced): Overtype {"value"?: bool (default: toggle)}

## caret

- `caret.left` (Navigation): Left {"extend"?: bool} [Left]
- `caret.right` (Navigation): Right {"extend"?: bool} [Right]
- `caret.up` (Navigation): Up {"extend"?: bool} [Up]
- `caret.down` (Navigation): Down {"extend"?: bool} [Down]
- `caret.wordLeft` (Navigation): Word Left {"extend"?: bool} [Alt+Left]
- `caret.wordRight` (Navigation): Word Right {"extend"?: bool} [Alt+Right]
- `caret.home` (Navigation): Line Start {"extend"?: bool} [Home / Mod+Left]
- `caret.end` (Navigation): Line End {"extend"?: bool} [End / Mod+Right]
- `caret.paraUp` (Navigation): Paragraph Up {"extend"?: bool} [Mod+Up / Alt+Up]
- `caret.paraDown` (Navigation): Paragraph Down {"extend"?: bool} [Mod+Down / Alt+Down]
- `caret.docStart` (Navigation): Document Start {"extend"?: bool} [Mod+Home]
- `caret.docEnd` (Navigation): Document End {"extend"?: bool} [Mod+End]
- `caret.pageUp` (Navigation): Page Up {"extend"?: bool} [PageUp]
- `caret.pageDown` (Navigation): Page Down {"extend"?: bool} [PageDown]
- `caret.set` (Navigation): Set Caret {"pos": Pos, "extend"?: bool} | {"page": n, "x": pt, "y": pt}
- `caret.pastCitation` (Zotero › Citations): Move Past Citation {}

## select

- `select.all` (Home › Editing › Select): Select All {} [Mod+A]
- `select.range` (Navigation): Select Range {"anchor": Pos, "focus": Pos}
- `select.word` (Navigation): Select Word {}
- `select.sentence` (Navigation): Select Sentence {}
- `select.paragraph` (Navigation): Select Paragraph {}
- `select.dragUnit` (Navigation): Extend Selection by Units {"unit": "word|sentence|line|paragraph|document", "start": Pos, "end": Pos, "pos": Pos}
- `select.line` (Navigation): Select Line {"pos"?: Pos}
- `select.text` (Navigation): Select Text {"text": string, "occurrence"?: n}
- `select.collapse` (Navigation): Collapse Selection {} [Escape]
- `select.column` (Editing › Selection): Column Selection {"anchor": Pos, "focus": Pos} | {"from": {"page": n, "x": pt, "y": pt}, "to": {"page": n, "x": pt, "y": pt}, "story"?: StoryRef} | {"on"?: bool} (no corners: toggle column selection mode, where the arrow keys extend the block) [Mod+Shift+F8]
- `select.addObject` (Home › Editing › Select): Add Object to Selection {"pos"?: Pos, "index"?: n, "objects"?: [Pos | n]}  (n: its Selection Pane index; with no object selected yet, the first one becomes the selection)
- `select.objects` (Home › Editing › Select): Select Objects {"index"?: n}
- `select.similar` (Home › Editing › Select): Select Text with Similar Formatting {}
- `select.extend` (Editing › Selection): Extend Selection {} [F8]

## edit

- `edit.undo` (Quick Access Toolbar): Undo {} [Mod+Z]
- `edit.undoTo` (Quick Access Toolbar): Undo Actions {"count": n (1 = the newest step, like edit.undo; n undoes the newest n steps at once; at most the undo depth)}
- `edit.undoHistory` (Quick Access Toolbar): Undo History {}
- `edit.redo` (Quick Access Toolbar): Redo {} [Mod+Y / Mod+Shift+Z]
- `edit.cut` (Home › Clipboard): Cut {} [Mod+X]
- `edit.copy` (Home › Clipboard): Copy {} [Mod+C / Mod+Insert]
- `edit.spike` (Editing): Spike {} [Mod+F3]
- `edit.insertSpike` (Editing): Insert Spike {} [Mod+Shift+F3]
- `edit.paste` (Home › Clipboard): Paste {"text"?: string, "html"?: string, "rtf"?: string} [Mod+V / Shift+Insert]
- `edit.pasteText` (Home › Clipboard › Paste): Paste: Keep Text Only {"text"?: string} [Mod+Shift+Alt+V]
- `edit.pasteMerge` (Home › Clipboard › Paste): Paste: Merge Formatting {"text"?: string, "html"?: string, "rtf"?: string}
- `edit.clipboardPane` (Home › Clipboard): Clipboard Pane {"value"?: bool}
- `edit.clipboardItems` (Home › Clipboard › Clipboard Pane): Clipboard Items {}
- `edit.pasteClipboardItem` (Home › Clipboard › Clipboard Pane): Paste Clipboard Item {"index": n (0 = newest)}
- `edit.pasteAllClipboard` (Home › Clipboard › Clipboard Pane): Paste All {}
- `edit.deleteClipboardItem` (Home › Clipboard › Clipboard Pane): Delete Clipboard Item {"index": n (0 = newest)}
- `edit.clearClipboard` (Home › Clipboard › Clipboard Pane): Clear All {}
- `edit.find` (Home › Editing): Find {"text": string, "matchCase"?: bool, "wholeWord"?: bool, "matchPrefix"?: bool, "matchSuffix"?: bool, "ignorePunct"?: bool, "ignoreSpace"?: bool, "wildcards"?: bool, "special"?: bool (^p ^t ^# … codes, default true), "regex"?: bool} [Mod+F]
- `edit.advancedFind` (Home › Editing › Find): Advanced Find {"text"?: string, …options of edit.find, "in"?: "main|selection", "highlight"?: bool}
- `edit.findNext` (Home › Editing › Find): Find Next {"text"?: string, "matchCase"?: bool, "wholeWord"?: bool, "regex"?: bool} [Mod+G / F3 / Shift+F4 / Mod+PageDown]
- `edit.findPrevious` (Home › Editing › Find): Find Previous {"text"?: string, "matchCase"?: bool, "wholeWord"?: bool, "regex"?: bool} [Mod+Shift+G / Mod+PageUp]
- `edit.replace` (Home › Editing): Replace {"text": string, "with": string, …options of edit.replaceAll}
- `edit.findReplace` (Home › Editing): Find and Replace {"tab"?: "find|replace|goto" (default replace)} [Mod+H / Ctrl+H]
- `edit.replaceAll` (Home › Editing › Replace): Replace All {"text": string, "with": string (^p ^t ^& ^c …; \\1 with wildcards; with regex also $1 ${n} ${name} $0 $$ \\1 \\n (paragraph mark) \\t), …options of edit.find}
- `edit.goto` (Home › Editing › Find): Go To {"page"?: n, "pageBy"?: int (pages forward, negative back, from the caret's page), "bookmark"?: string (selects its text), "paragraph"?: n}; none opens Find and Replace on its Go To tab [Mod+Alt+G / F5]
- `edit.goBack` (Navigation): Go Back {} [Shift+F5 / Mod+Alt+Z]
- `edit.formatPainter` (Home › Clipboard): Format Painter {"sticky"?: bool}
- `edit.copyFormat` (Home › Clipboard): Copy Formatting {} [Mod+Shift+C]
- `edit.pasteFormat` (Home › Clipboard): Paste Formatting {} [Mod+Shift+V]
- `edit.pasteSpecial` (Home › Clipboard › Paste): Paste Special {"as"?: "formatted"|"rtf"|"html"|"picture"|"text", "text"?: string, "html"?: string, "rtf"?: string, "picture"?: base64} [Mod+Alt+V]
- `edit.repeat` (Quick Access Toolbar): Repeat {} [F4]

## format

- `format.bold` (Home › Font): Bold {"value"?: bool} [Mod+B]
- `format.italic` (Home › Font): Italic {"value"?: bool} [Mod+I]
- `format.underline` (Home › Font): Underline {"value"?: bool, "style"?: "single|double|thick|dotted|dash|dotDash|dotDotDash|wave|words"} [Mod+U]
- `format.doubleUnderline` (Home › Font › Underline): Double Underline {} [Mod+Shift+D]
- `format.wordUnderline` (Home › Font › Underline): Underline Words Only {} [Mod+Shift+W]
- `format.strikethrough` (Home › Font): Strikethrough {"value"?: bool} [Mod+Shift+X]
- `format.border` (Home › Font): Character Border {"value"?: bool}
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
- `format.font` (Home › Font): Font {"name"?: string, "eastAsia"?: string} [Mod+Shift+F]
- `format.size` (Home › Font): Font Size {"size": number} [Mod+Shift+P]
- `format.growFont` (Home › Font): Increase Font Size {} [Mod+Shift+. / Mod+Shift+>]
- `format.shrinkFont` (Home › Font): Decrease Font Size {} [Mod+Shift+, / Mod+Shift+<]
- `format.growFont1` (Home › Font): Grow Font 1 Point {} [Mod+]]
- `format.shrinkFont1` (Home › Font): Shrink Font 1 Point {} [Mod+[]
- `format.color` (Home › Font): Font Color {"color": "RRGGBB" | "auto"}
- `format.underlineColor` (Home › Font › Underline): Underline Color {"color": "RRGGBB" | "auto"} (the underline's own colour; "auto" follows the text colour)
- `format.highlight` (Home › Font): Text Highlight Color {"color"?: "yellow|brightGreen|turquoise|pink|blue|red|darkBlue|teal|green|violet|darkRed|darkYellow|gray50|gray25|black|none"} (explicit colour sets it; omitted toggles the last chosen colour, initially yellow)
- `format.shading` (Home › Font): Character Shading {"color": "RRGGBB" | null}
- `format.changeCase` (Home › Font): Change Case {"mode"?: "sentence|lower|upper|title|toggle"} [Shift+F3]
- `format.clear` (Home › Font): Clear All Formatting {}
- `format.resetChar` (Home › Font): Reset Character Formatting {} [Ctrl+Space]
- `format.spacing` (Home › Font › Font › Advanced): Character Spacing {"points": number}
- `format.scale` (Home › Font › Font › Advanced): Character Scale {"percent": number}
- `format.position` (Home › Font › Font › Advanced): Character Position {"points": number}
- `format.emphasisMark` (Home › Font › Font): Emphasis Mark {"mark"?: "none" | "dot" | "comma" | "circle" | "underDot"}
- `format.charStyle` (Home › Styles): Apply Character Style {"style": string}
- `format.set` (Home › Font › Font): Set Character Formatting {"props": CharProps}
- `format.fontDialog` (Home › Font): Font Dialog {} [Mod+D]
- `format.enclose` (Home › Font): Enclose Characters {"shape": "circle|square|triangle|diamond" | null, "style"?: "shrink|enlarge", "text"?: string}
- `format.state` (Home › Font): Formatting at Selection {}
- `format.phonetic` (Home › Font): Phonetic Guide {"ruby"?: string | null, "align"?: "center|distributeLetter|distributeSpace|left|right|rightVertical", "size"?: number, "offset"?: number}
- `format.textEffects` (Home › Font): Text Effects {"style"?: "solid"|"outlined"|"hollow"|"gradient"|"shadowed"|"glowing"|"reflected"|"sunset", "clear"?: bool, "fill"?: "RRGGBB"|"none" (hollow)|{"color": "RRGGBB", "transparency"?: %}|{"gradient": ["RRGGBB", …], "angle"?: deg}|null (the run's colour), "outline"?: "RRGGBB"|"none"|{"color"?: "RRGGBB"|null, "width"?: pt, "transparency"?: %}|null, "shadow"?: preset|{"color"?, "transparency"?, "blur"?, "distance"?, "angle"?}|null, "glow"?: pt|{"color"?, "size"?, "transparency"?}|null, "reflection"?: bool|"none"|{"transparency"?: %, "size"?: %, "distance"?: pt}|null}  (an omitted key is left as it is; with a shape selected or the caret in a text box, the box's whole text)

## font

- `font.add` (Home › Font): Add Font… {"path"?: string, "data"?: base64, "name"?: string (file name for "data")} — a TTF, OTF, TTC, WOFF or WOFF2 file; none: pick a file
- `font.list` (Home › Font): Added Fonts {"all"?: bool (also every available family)}
- `font.remove` (Home › Font): Remove Added Font {"family": string}
- `font.loadSystem` (Home › Font): Load System Installed Fonts… {}
- `font.missing` (Status Bar): Missing Fonts {} → {"missing": [{"font": string, "shownAs": [string] (the families drawn instead), "metricCompatible": bool (its substitute measures like the font)}]} — the text the current view shows

## para

- `para.alignLeft` (Home › Paragraph): Align Left {} [Mod+L]
- `para.alignCenter` (Home › Paragraph): Center {} [Mod+E]
- `para.alignRight` (Home › Paragraph): Align Right {} [Mod+R]
- `para.justify` (Home › Paragraph): Justify {} [Mod+J]
- `para.distribute` (Home › Paragraph): Distributed {} [Mod+Shift+J]
- `para.align` (Home › Paragraph): Alignment {"value": "left|center|right|justify|distribute (as seen on the page) | start|end (reading direction)"}
- `para.rtl` (Home › Paragraph): Right-to-Left Text Direction {"value"?: bool (false = left to right)}
- `para.ltr` (Home › Paragraph): Left-to-Right Text Direction {"value"?: bool (false = right to left)}
- `para.indent` (Home › Paragraph): Increase Indent {} [Mod+M]
- `para.outdent` (Home › Paragraph): Decrease Indent {} [Mod+Shift+M]
- `para.hangingIndent` (Home › Paragraph › Paragraph): Hanging Indent {} [Mod+T]
- `para.removeHanging` (Home › Paragraph › Paragraph): Reduce Hanging Indent {} [Mod+Shift+T]
- `para.indents` (Layout › Paragraph): Indents {"left"?: pt, "right"?: pt, "firstLine"?: pt (negative = hanging)}
- `para.lineSpacing` (Home › Paragraph): Line and Paragraph Spacing {"value": number (multiple) } | {"atLeast": pt} | {"exactly": pt}
- `para.single` (Home › Paragraph › Line Spacing): Single Spacing {} [Mod+1]
- `para.double` (Home › Paragraph › Line Spacing): Double Spacing {} [Mod+2]
- `para.oneAndHalf` (Home › Paragraph › Line Spacing): 1.5 Line Spacing {} [Mod+5]
- `para.spacing` (Layout › Paragraph): Paragraph Spacing {"before"?: pt, "after"?: pt, "beforeAuto"?: bool, "afterAuto"?: bool (automatic, HTML-style spacing: 14 pt)}
- `para.addSpaceBefore` (Home › Paragraph › Line Spacing): Add Space Before Paragraph {} [Mod+0]
- `para.removeSpaceAfter` (Home › Paragraph › Line Spacing): Remove Space After Paragraph {}
- `para.reset` (Home › Paragraph): Reset Paragraph Formatting {} [Ctrl+Q]
- `para.style` (Home › Styles): Apply Style {"style": string (name or id)}
- `para.normal` (Home › Styles): Normal Style {} [Mod+Shift+N]
- `para.heading1` (Home › Styles): Heading 1 {} [Mod+Alt+1]
- `para.heading2` (Home › Styles): Heading 2 {} [Mod+Alt+2]
- `para.heading3` (Home › Styles): Heading 3 {} [Mod+Alt+3]
- `para.bullets` (Home › Paragraph): Bullets {"kind"?: "bullet" | single char, "off"?: bool} [Mod+Shift+L]
- `para.numbering` (Home › Paragraph): Numbering {"kind"?: "numbered|numberedParen|upperLetter|lowerLetter|lowerRoman|outline", "off"?: bool}
- `para.multilevel` (Home › Paragraph): Multilevel List {"kind"?: "legal|outline"}
- `para.listLevel` (Home › Paragraph › Bullets): Change List Level {"level": 0-8}
- `para.restartNumbering` (Home › Paragraph › Numbering): Restart at 1 {}
- `para.moveUp` (Home › Paragraph): Move Paragraph Up {} [Ctrl+Shift+Up]
- `para.moveDown` (Home › Paragraph): Move Paragraph Down {} [Ctrl+Shift+Down]
- `para.promote` (Home › Paragraph): Promote {} [Ctrl+Shift+Left]
- `para.demote` (Home › Paragraph): Demote {} [Ctrl+Shift+Right]
- `para.shading` (Home › Paragraph): Shading {"color": "RRGGBB" | null}
- `para.borders` (Home › Paragraph): Borders {"kind": "bottom|top|left|right|none|all|outside|inside|horizontalLine", "width"?: pt, "color"?: "RRGGBB", "style"?: "single|double|dotted|dashed|thick|triple|dotDash|wave", "sides"?: Sides} where Sides = {"top"|"left"|"bottom"|"right"|"between": {"style"?, "width"?: pt, "color"?: "RRGGBB"} | null}: exactly these sides (others off), instead of `kind`
- `para.sort` (Home › Paragraph): Sort {"descending"?: bool}
- `para.keepNext` (Home › Paragraph › Line and Page Breaks): Keep with Next {"value"?: bool}
- `para.keepLines` (Home › Paragraph › Line and Page Breaks): Keep Lines Together {"value"?: bool}
- `para.pageBreakBefore` (Home › Paragraph › Line and Page Breaks): Page Break Before {"value"?: bool}
- `para.widowControl` (Home › Paragraph › Line and Page Breaks): Widow/Orphan Control {"value"?: bool}
- `para.asianTypography` (Home › Paragraph › Asian Typography): Asian Typography {"kinsoku"?: bool (East Asian line-breaking rules), "wordWrap"?: bool (false: Latin words may break at any character), "overflowPunct"?: bool (hanging punctuation), "topLinePunct"?: bool (compress punctuation at the start of a line), "autoSpaceDE"?: bool (space between Asian and Latin text), "autoSpaceDN"?: bool (space between Asian text and numbers)} — flags left out stay as they are; returns the flags at the caret
- `para.tabs` (Home › Paragraph › Paragraph): Tabs {"tabs"?: [TabStop] (replace the direct stops), "set"?: [TabStop], "clear"?: [pt], "clearAll"?: bool, "default"?: pt} where TabStop = {"pos": pt, "align"?: "left|center|right|decimal|bar", "leader"?: "none|dot|hyphen|underscore|middleDot"}
- `para.outlineLevel` (Home › Paragraph › Paragraph): Outline Level {}
- `para.set` (Home › Paragraph › Paragraph): Set Paragraph Formatting {"props": ParaProps, "onPage"?: {"align"?: "left|center|right|justify|distribute", "left"?: pt, "right"?: pt} (alignment and indents as seen on the page: each paragraph's own direction, after `props`, says which edge is its start)}
- `para.dialog` (Home › Paragraph): Paragraph Settings {}
- `para.setNumberingValue` (Home › Paragraph › Numbering): Set Numbering Value {"value": n}
- `para.defineBullet` (Home › Paragraph › Bullets): Define New Bullet {"char": string}
- `para.defineNumber` (Home › Paragraph › Numbering): Define New Number Format {"format": "decimal|upperRoman|lowerLetter…", "text"?: "%1.", "start"?: n}

## styles

- `styles.create` (Home › Styles): Create a Style {"name": string, "basedOn"?: string, "fromSelection"?: bool}
- `styles.modify` (Home › Styles): Modify Style {"style": string, "chr"?: CharProps, "para"?: ParaProps, "name"?: string, "next"?: string}
- `styles.updateToMatch` (Home › Styles): Update Style to Match Selection {"style"?: string}
- `styles.delete` (Home › Styles): Delete Style {"style": string (name or id; custom styles only)}
- `styles.manage` (Home › Styles): Manage Styles {"sort"?: "recommended|alphabetical"} → [{id, name, type: "paragraph|character|linked|table", builtIn, inGallery, hidden, basedOn, priority, format}]
- `styles.setVisibility` (Home › Styles): Show or Hide Style {"style": string, "gallery"?: bool (Styles gallery, w:qFormat), "hidden"?: bool (hidden from style lists, w:semiHidden)}
- `styles.list` (Home › Styles): Styles {}
- `styles.pane` (Home › Styles): Styles Pane {} [Mod+Alt+Shift+S]
- `styles.apply` (Home › Styles): Apply Styles {"style"?: string (name or id)}
- `styles.addToGallery` (Home › Styles): Add to Style Gallery {}
- `styles.inspector` (Home › Styles): Style Inspector {"value"?: bool (show/hide the pane)} [Shift+F1]
- `styles.inspect` (Home › Styles › Style Inspector): Inspect Styles at Selection {}
- `styles.inspectorClear` (Home › Styles › Style Inspector): Clear Formatting Level {"level": "paragraphStyle|paragraphFormatting|characterStyle|characterFormatting"}
- `styles.organizer` (View › Templates › Organizer): Organizer {"path"?: string, "data"?: base64} → {"document": [style], "file"?: {"path", "styles": [style]}}
- `styles.copyFrom` (View › Templates › Organizer): Copy Styles {"path": string, "data"?: base64, "styles": [name or id]} → {"added", "replaced", "skipped"}
- `styles.rename` (View › Templates › Organizer): Rename Style {"style": string (name or id; custom styles only), "name": string}

## list

- `list.define` (Home › Paragraph › Multilevel List): Define New Multilevel List {"levels": [{"format"?: "decimal|lowerLetter|upperLetter|lowerRoman|upperRoman|decimalZero|ordinal|bullet|none", "text"?: "%1.%2." (%n = level n's number; the bullet character for bullet), "start"?: n, "restartAfter"?: 0-8 (0 = never; omit = the level above), "style"?: paragraph style linked to the level | null, "align"?: "left|center|right", "alignedAt"?: pt, "indentAt"?: pt, "follow"?: "tab|space|nothing", "tabAt"?: pt | null, "font"?: string | null, "bold"?: bool, "italic"?: bool, "color"?: "RRGGBB" | null, "legal"?: bool}, …] (index = level, up to 9; fields left out keep the base list's), "num"?: list id to change in place (default: a new list), "apply"?: bool (default true: number the selected paragraphs), "name"?: string}
- `list.get` (Home › Paragraph › Multilevel List): List Definition {"num"?: list id (default: the caret's list)} → {"num", "levels": [as list.define]}
- `list.multilevelPreset` (Home › Paragraph › Multilevel List): Multilevel List Library {"preset": "headings" (1 / 1.1 / 1.1.1) | "article" (Article I. / Section 1.01 / (a)) | "outlineHeadings" (I. / A. / 1.) | "chapter" (Chapter 1, lower levels unnumbered)} — a new list whose nine levels are linked to Heading 1–9: every paragraph in those styles is numbered, selected paragraphs already in a Heading style keep it, and any other selected paragraph becomes Heading 1 (the first level)

## view

- `view.marks` (Home › Paragraph): Show/Hide ¶ {} [Mod+Shift+8 / Mod+8]
- `view.printLayout` (View › Views): Print Layout {} [Mod+Alt+P]
- `view.webLayout` (View › Views): Web Layout {}
- `view.draft` (View › Views): Draft {} [Mod+Alt+N]
- `view.outline` (View › Views): Outline {} [Mod+Alt+O]
- `view.readMode` (View › Views): Read Mode {}
- `view.readColumnWidth` (Reading › Layout): Reading Column Width {"value": "auto" | "narrow" | "medium" | "wide" | "page"}
- `view.readTextSize` (Reading › Layout): Reading Text Size {"value": percent (75–150)}
- `view.readLineSpacing` (Reading › Layout): Reading Line Spacing {"value": "document" | 1.0 | 1.25 | 1.5 | 2.0}
- `view.readPageColor` (Reading › Layout): Reading Page Color {"value": "none" | "sepia" | "inverse"}
- `view.hideWhiteSpace` (View › Show): Hide White Space {"value"?: bool}
- `view.focus` (View › Immersive): Focus {"value"?: bool}
- `view.fullScreenView` (View › Immersive): Full Screen View {"value"?: bool}
- `view.ruler` (View › Show): Ruler {}
- `view.gridlines` (View › Show): Gridlines {"value"?: bool}
- `view.navigationPane` (View › Show): Navigation Pane {}
- `view.zoom` (View › Zoom): Zoom {"value": percent (10-500) | "pageWidth" | "onePage" | "multiplePages"}
- `view.zoom100` (View › Zoom): 100% {}
- `view.zoomIn` (View › Zoom): Zoom In {}
- `view.zoomOut` (View › Zoom): Zoom Out {}
- `view.onePage` (View › Zoom): One Page {}
- `view.multiplePages` (View › Zoom): Multiple Pages {}
- `view.pageWidth` (View › Zoom): Page Width {}
- `view.darkMode` (View › Dark Mode): Switch Modes {}
- `view.interfaceTheme` (View › Dark Mode): Interface Theme {"value"?: "light" | "dark" | "system"; without it, toggles light and dark}
- `view.stylesPane` (Home › Styles): Styles Pane {}
- `view.stylesPaneDock` (Home › Styles): Styles Pane Position {"dock"?: "left" | "right" | "float"}
- `view.commentsPane` (Review › Comments): Comments Pane {}
- `view.accessibilityPane` (Review › Accessibility): Accessibility Pane {"value"?: bool}
- `view.altTextPane` (Review › Accessibility): Alt Text Pane {"value"?: bool}
- `view.formatShapePane` (Shape Format › Shape Styles): Format Shape Pane {"value"?: bool}
- `view.newWindow` (View › Window): New Window {}
- `view.switchWindows` (View › Window): Switch Windows {"id"?: n (make this open document the active one)} → {"documents": [{"id", "title", "path", "dirty", "active"}]} in the order they were opened
- `view.split` (View › Window): Split {} [Mod+Alt+S]
- `view.fullScreen` (View › Window): Full Screen {"value"?: bool} [Mod+Ctrl+F / F11]
- `view.state` (View): View State {}
- `view.numeral` (File › Options › Advanced): Numerals {"value"?: "arabic|hindi|context|system"}
- `view.fieldCodes` (View › Show): Field Codes {"value"?: bool} [Alt+F9]
- `view.immersive` (View › Immersive): Immersive Reader {}
- `view.vertical` (View › Page Movement): Vertical {}
- `view.sideToSide` (View › Page Movement): Side to Side {}

## table

- `table.viewGridlines` (Table Layout › Table): View Gridlines {"value"?: bool}
- `table.insertRowAbove` (Table Layout › Rows & Columns): Insert Above {}
- `table.insertRowBelow` (Table Layout › Rows & Columns): Insert Below {}
- `table.insertColumnLeft` (Table Layout › Rows & Columns): Insert Left {}
- `table.insertColumnRight` (Table Layout › Rows & Columns): Insert Right {}
- `table.deleteRow` (Table Layout › Rows & Columns › Delete): Delete Rows {}
- `table.deleteColumn` (Table Layout › Rows & Columns › Delete): Delete Columns {}
- `table.deleteTable` (Table Layout › Rows & Columns › Delete): Delete Table {}
- `table.deleteCells` (Table Layout › Rows & Columns › Delete): Delete Cells {}
- `table.merge` (Table Layout › Merge): Merge Cells {}
- `table.split` (Table Layout › Merge): Split Cells {"columns"?: n (2), "rows"?: n (1), "mergeFirst"?: bool (true: several selected cells are merged first)}
- `table.splitTable` (Table Layout › Merge): Split Table {}
- `table.style` (Table Design › Table Styles): Table Styles {"style": string}
- `table.look` (Table Design › Table Style Options): Table Style Options {"headerRow"?: bool, "totalRow"?: bool, "bandedRows"?: bool, "firstColumn"?: bool, "lastColumn"?: bool, "bandedColumns"?: bool}
- `table.shading` (Table Design › Table Styles): Shading {"color": "RRGGBB" | null}
- `table.borders` (Table Design › Borders): Borders {"kind": "all|outside|inside|none|top|bottom|left|right", "width"?: pt, "color"?: "RRGGBB"}
- `table.cellAlign` (Table Layout › Alignment): Alignment {"value": "topLeft|topCenter|…|bottomRight"}
- `table.textDirection` (Table Layout › Alignment): Text Direction {"value"?: "horizontal|down|up"} (default: the next direction after the caret cell's, like Word's button)
- `table.autofit` (Table Layout › Cell Size): AutoFit {"mode": "contents|window|fixed"}
- `table.distributeColumns` (Table Layout › Cell Size): Distribute Columns {}
- `table.distributeRows` (Table Layout › Cell Size): Distribute Rows {}
- `table.columnWidth` (Table Layout › Cell Size): Table Column Width {"width": pt} (every column the selection covers, the caret cell's without one; the table's preferred width is cleared so the columns get exactly this)
- `table.rowHeight` (Table Layout › Cell Size): Table Row Height {"height": pt, "rule"?: "atLeast|exact"} (every row the selection covers, the caret's without one)
- `table.repeatHeader` (Table Layout › Data): Repeat Header Rows {}
- `table.altText` (Table Layout › Table › Properties): Alt Text {"text"?: string, "title"?: string} (empty clears)
- `table.sort` (Table Layout › Data): Sort {"column"?: n, "descending"?: bool, "header"?: bool}
- `table.toText` (Table Layout › Data): Convert to Text {"separator"?: "tab|comma|paragraph|other", "char"?: string (with other)} (the selected rows, or the whole table)
- `table.formula` (Table Layout › Data): Formula {"formula"?: "=SUM(ABOVE)"}
- `table.selectTable` (Table Layout › Table › Select): Select Table {}
- `table.selectRow` (Table Layout › Table › Select): Select Row {}
- `table.selectColumn` (Table Layout › Table › Select): Select Column {}
- `table.selectCell` (Table Layout › Table › Select): Select Cell {}
- `table.rtl` (Table Layout › Table): Right-to-Left Table {"value"?: bool} (true: the first column stands at the right; without a value it toggles)
- `table.properties` (Table Layout › Table): Properties {"align"?: "left|center|right", "rtl"?: bool, "width"?: pt|null, "widthPct"?: percent, "indent"?: pt, "rowHeight"?: pt|null, "rowHeightRule"?: "atLeast|exact", "allowBreak"?: bool, "headerRow"?: bool, "columnWidth"?: pt, "cellWidth"?: pt|null, "valign"?: "top|center|bottom"} (row, column and cell settings apply to the selected rows, columns and cells, or the caret's; without settings it returns the caret's current ones)
- `table.fromText` (Insert › Tables): Convert Text to Table {"separator"?: "tab|comma|paragraph|other", "char"?: string (with other), "columns"?: n, "autofit"?: "initial|fixed|contents|window", "width"?: pt (initial column width, 0 = Auto, at most 1584)}
- `table.quick` (Insert › Tables): Quick Tables {"kind"?: "calendar|tabular|matrix"}
- `table.newStyle` (Table Design › Table Styles): New Table Style {"name": string, "basedOn"?: string, "<part>"?: Part for each part name (wholeTable, headerRow|firstRow, lastRow|totalRow, firstColumn|firstCol, lastColumn|lastCol, bandedRows|band1Horz, band2Horz, bandedColumns|band1Vert, band2Vert, nwCell, neCell, swCell, seCell), "part"?: part name (the Part fields then sit at the top level), "parts"?: [Part & {"part": name}], "bandSize"?: n (rows per band), "para"?: ParaProps, "apply"?: bool} where Part = {"fill"?: "RRGGBB" | null, "font"?: string | null (null or "": inherited), "size"?: pt, "bold"?: bool, "italic"?: bool, "underline"?: bool | "single" | "double" | "thick" | "words" | "dotted" | "dash" | "wave" | "none", "color"?: "RRGGBB" | null, "align"?: "left" | "center" | "right" | "justify" | null, "vAlign"?: "top" | "center" | "bottom" | null, "cellAlign"?: "topLeft" | "topCenter" | "topRight" | "centerLeft" | "center" | "centerRight" | "bottomLeft" | "bottomCenter" | "bottomRight" | null (both alignments), "borders"?: bool | null (true: single lines on every edge, false: none, null: inherit) | Edges | [Edges], "borderColor"?: "RRGGBB", "borderWidth"?: pt} and Edges = {"edges"?: "all" | "none" | "outside" | "inside" | "top" | "bottom" | "left" | "right" | "insideH" | "insideV" (default all), "style"?: "single" | "double" | "dotted" | "dashed" | "dotDash" | "thick" | "triple" | "wave" | "none", "width"?: pt, "color"?: "RRGGBB" | null}
- `table.modifyStyle` (Table Design › Table Styles): Modify Table Style {"style"?: string (default: the current table's), "name"?: string, "basedOn"?: string, "<part>"?: Part for each part name (wholeTable, headerRow|firstRow, lastRow|totalRow, firstColumn|firstCol, lastColumn|lastCol, bandedRows|band1Horz, band2Horz, bandedColumns|band1Vert, band2Vert, nwCell, neCell, swCell, seCell), "part"?: part name (the Part fields then sit at the top level), "parts"?: [Part & {"part": name}], "bandSize"?: n (rows per band), "para"?: ParaProps, "apply"?: bool} where Part = {"fill"?: "RRGGBB" | null, "font"?: string | null (null or "": inherited), "size"?: pt, "bold"?: bool, "italic"?: bool, "underline"?: bool | "single" | "double" | "thick" | "words" | "dotted" | "dash" | "wave" | "none", "color"?: "RRGGBB" | null, "align"?: "left" | "center" | "right" | "justify" | null, "vAlign"?: "top" | "center" | "bottom" | null, "cellAlign"?: "topLeft" | "topCenter" | "topRight" | "centerLeft" | "center" | "centerRight" | "bottomLeft" | "bottomCenter" | "bottomRight" | null (both alignments), "borders"?: bool | null (true: single lines on every edge, false: none, null: inherit) | Edges | [Edges], "borderColor"?: "RRGGBB", "borderWidth"?: pt} and Edges = {"edges"?: "all" | "none" | "outside" | "inside" | "top" | "bottom" | "left" | "right" | "insideH" | "insideV" (default all), "style"?: "single" | "double" | "dotted" | "dashed" | "dotDash" | "thick" | "triple" | "wave" | "none", "width"?: pt, "color"?: "RRGGBB" | null}
- `table.deleteStyle` (Table Design › Table Styles): Delete Table Style {"style"?: string (default: the current table's)}
- `table.draw` (Insert › Tables): Draw Table {"page": n, "x0": pt, "y0": pt, "x1": pt, "y1": pt, "story"?: StoryRef} (a pen stroke in page points, 0-based page: a rectangle at least 12 pt each way outside any table inserts a one-cell table of that size at the paragraph under its start; a straight vertical or horizontal line inside a table splits the cells it crosses there. In the app the button turns the pen on.)
- `table.eraser` (Table Layout › Draw): Eraser {"page": n, "x": pt, "y": pt} (removes the border between two cells within 4 pt of the point: cells that make one rectangle merge, including cells merged down the same rows; otherwise the border is hidden along the whole edge. In the app the button turns the eraser on.)
- `table.resizeDrag` (Table Layout › Cell Size): Resize Table by Dragging {"page": n, "x": pt, "y": pt, "toX": pt, "toY": pt, "shift"?: bool, "ctrl"?: bool, "reach"?: pt} (a mouse drag in page points, 0-based page, starting on a table border or the resize handle: a column border moves (the column to its right gives or takes the difference, so the table keeps its width; with ctrl the columns right of it share it in proportion; with shift, or on the table's right edge, only the column left of it changes); the table's left edge moves a left-aligned table's indent, the first column making up the difference (a centred or right-aligned table keeps its alignment: only the first column changes); with cells of the table selected, a border of theirs moves only in their rows; a row's bottom border sets that row's height; the handle just outside the bottom-right corner scales every column and the rows on that page. `reach` (default 3) is how near the start has to be.)
- `table.selectAt` (Table Layout › Table › Select): Select Table Cells by Clicking {"page": n, "x": pt, "y": pt, "toX"?: pt, "toY"?: pt, "reach"?: pt, "extend"?: bool, "anchorRow"?: n} (a click in page points, 0-based page, on a selection area of a table in the caret's story: just above a column selects the column, left of a row the row, along a cell's left edge inside it the cell, the move handle past the top-left corner the table; with toX/toY (a drag) every column, row or cell from there to that point; the page margin beside a table (its leading side: right for a right-to-left table) is a row area too, and `extend` (Shift+click) on one takes the rows from the selected ones' anchor, or from row `anchorRow` (0-based) when given, so a drag keeps its press's anchor. `reach` (default 3) is the column borders' resize reach, which the cell areas keep clear of.)
- `table.insertAt` (Table Layout › Rows & Columns): Insert Row or Column by Clicking {"page": n, "x": pt, "y": pt, "reach"?: pt} (a click on a table's insert button: left of a row border adds a row there, above a column border a column; the new row or column is selected, as in Word)
- `table.moveDrag` (Table Layout › Table): Move Table by Dragging {"page": n, "x": pt, "y": pt, "toX": pt, "toY": pt, "reach"?: pt} (a drag from the move handle past a table's top-left corner: the table floats where it's dropped, the text wrapping around it; tables in the main text only)
- `table.fitColumn` (Table Layout › Cell Size): AutoFit Column by Double-Clicking {"page": n, "x": pt, "y": pt, "reach"?: pt} (a double-click on a column border: the column left of it fits its contents and the columns right of it keep their widths, moving with the border, so the table narrows or widens (up to the right margin), as in Word)
- `table.cellMargins` (Table Layout › Alignment): Cell Margins {"top"?, "left"?, "bottom"?, "right"? (pt)}
- `table.borderPainter` (Table Design › Borders): Border Painter {}

## outline

- `outline.promoteToHeading1` (Outlining › Outline Tools): Promote to Heading 1 {}
- `outline.promote` (Outlining › Outline Tools): Promote {}
- `outline.demote` (Outlining › Outline Tools): Demote {}
- `outline.demoteToBody` (Outlining › Outline Tools): Demote to Body Text {}
- `outline.level` (Outlining › Outline Tools): Outline Level {"level": 1-9 | "body"}
- `outline.moveUp` (Outlining › Outline Tools): Move Up {}
- `outline.moveDown` (Outlining › Outline Tools): Move Down {}
- `outline.expand` (Outlining › Outline Tools): Expand {"block"?: body paragraph index (default: the selection)} [Alt+Shift+=]
- `outline.collapse` (Outlining › Outline Tools): Collapse {"block"?: body paragraph index (default: the selection)} [Alt+Shift+-]
- `outline.toggle` (Outlining › Outline Tools): Expand or Collapse Heading {"block"?: body paragraph index (default: the selection)}
- `outline.selectSubtree` (Outlining › Outline Tools): Select Heading and Content {"block"?: body paragraph index (default: the selection)}
- `outline.showLevel` (Outlining › Outline Tools): Show Level {"level": 1-9 | "all"}
- `outline.showLevel1` (Outlining › Outline Tools): Show Level 1 {} [Alt+Shift+1]
- `outline.showLevel2` (Outlining › Outline Tools): Show Level 2 {} [Alt+Shift+2]
- `outline.showLevel3` (Outlining › Outline Tools): Show Level 3 {} [Alt+Shift+3]
- `outline.showLevel4` (Outlining › Outline Tools): Show Level 4 {} [Alt+Shift+4]
- `outline.showLevel5` (Outlining › Outline Tools): Show Level 5 {} [Alt+Shift+5]
- `outline.showLevel6` (Outlining › Outline Tools): Show Level 6 {} [Alt+Shift+6]
- `outline.showLevel7` (Outlining › Outline Tools): Show Level 7 {} [Alt+Shift+7]
- `outline.showLevel8` (Outlining › Outline Tools): Show Level 8 {} [Alt+Shift+8]
- `outline.showLevel9` (Outlining › Outline Tools): Show Level 9 {} [Alt+Shift+9]
- `outline.showAll` (Outlining › Outline Tools): Show All Levels {} [Alt+Shift+A]
- `outline.firstLineOnly` (Outlining › Outline Tools): Show First Line Only {"value"?: bool}
- `outline.showFormatting` (Outlining › Outline Tools): Show Text Formatting {"value"?: bool}
- `outline.close` (Outlining › Close): Close Outline View {}
- `outline.state` (Outlining): Outline State {}

## insert

- `insert.pageBreak` (Insert › Pages): Page Break {}
- `insert.blankPage` (Insert › Pages): Blank Page {}
- `insert.coverPage` (Insert › Pages): Cover Page {"title"?: string, "subtitle"?: string, "author"?: string}
- `insert.table` (Insert › Tables): Table {"rows": n, "cols": n, "style"?: string}
- `insert.picture` (Insert › Illustrations): Pictures {"path"?: string, "data"?: base64, "width"?: pt, "alt"?: string}
- `insert.icon` (Insert › Illustrations): Icons {"id"?: string (omit to list the library), "color"?: "RRGGBB", "size"?: pt, "query"?: string, "category"?: string}
- `insert.shape` (Insert › Illustrations): Shapes {"kind": "rectangle|roundedRectangle|ellipse|triangle|diamond|line|arrow|star|heart|straightConnector|elbowConnector|curvedConnector", "width"?: pt, "height"?: pt, "fill"?: "RRGGBB", "stroke"?: "RRGGBB", "arrow"?: "none"|"start"|"end"|"both" (lines and connectors; glue a connector's ends with shape.connect)}
- `insert.textBox` (Insert › Text): Text Box {"text"?: string, "width"?: pt, "height"?: pt}
- `insert.link` (Insert › Links): Link {"url": string} | {"bookmark": name} | {"heading": block (see link.targets)} | {"top": true}, "text"?: string (Place in This Document: a bookmark, a heading or the top of the document) [Mod+K]
- `insert.removeLink` (Insert › Links): Remove Hyperlink {}
- `insert.bookmark` (Insert › Links): Bookmark {"name": string} [Mod+Shift+F5]
- `insert.deleteBookmark` (Insert › Links): Delete Bookmark {"name": string}
- `insert.header` (Insert › Header & Footer): Header {"text"?: string, "preset"?: "blank|blankThree|title"}
- `insert.footer` (Insert › Header & Footer): Footer {"text"?: string, "preset"?: "blank|blankThree|pageNumber"}
- `insert.pageNumber` (Insert › Header & Footer): Page Number {"position"?: "top|bottom|current", "align"?: "left|center|right", "format"?: "x of y"}
- `insert.editHeader` (Insert › Header & Footer › Header): Edit Header {"page"?: number (0-based: the header that page shows, created if it has none)}
- `insert.editFooter` (Insert › Header & Footer › Footer): Edit Footer {"page"?: number (0-based: the footer that page shows, created if it has none)}
- `insert.createHeader` (Insert › Header & Footer): Header {"page"?: number (0-based; default: the caret's section)} — the header that page shows, created if it has none, with the caret in it
- `insert.createFooter` (Insert › Header & Footer): Footer {"page"?: number (0-based; default: the caret's section)} — the footer that page shows, created if it has none, with the caret in it
- `insert.closeHeader` (Header & Footer): Close Header and Footer {}
- `insert.removeEmptyHeaders` (Header & Footer): Close Header and Footer {}
- `insert.removeHeader` (Insert › Header & Footer › Header): Remove Header {}
- `insert.removeFooter` (Insert › Header & Footer › Footer): Remove Footer {}
- `insert.dateTime` (Insert › Text): Date & Time {"format"?: "M/d/yyyy", "update"?: bool}
- `insert.symbol` (Insert › Symbols): Symbol {"char": string, "font"?: family (the symbol's own font)}
- `insert.field` (Insert › Text › Quick Parts): Field {"instr": string, "result"?: string} [Mod+F9]
- `insert.dateField` (Insert › Text › Quick Parts): Insert Date Field {} [Ctrl+Shift+D]
- `insert.timeField` (Insert › Text › Quick Parts): Insert Time Field {} [Ctrl+Shift+T]
- `insert.pageField` (Insert › Text › Quick Parts): Insert Page Field {} [Ctrl+Shift+P]
- `insert.dropCap` (Insert › Text): Drop Cap {"position"?: "none"|"dropped"|"margin" (default dropped), "lines"?: 1..10 (default 3; 0 = none), "distance"?: pt from the text (0..1584, default 0), "font"?: family (omit for the text's font), "keep"?: bool (true: each selected paragraph that has a drop cap keeps its own lines, distance and font unless given here)}
- `insert.horizontalLine` (Home › Paragraph › Borders): Horizontal Line {}
- `insert.textFromFile` (Insert › Text › Object): Text from File {"path": string}
- `insert.equation` (Insert › Symbols): Equation {"linear"?: string, "latex"?: string, "builtin"?: "pythagoras|area|quadratic|binomial|expansion|euler|derivative|taylor|gaussian|fourier|trig1|trig2|normal|bayes", "display"?: bool, "edit"?: bool (default true)} [Alt+=]
- `insert.crossReference` (Insert › Links): Cross-reference {"to": "heading|bookmark|figure|table|equation|label:<Name> (a caption label of your own)", "target": string (text / name / number), "show"?: "text|page|number|aboveBelow"} or {} to list targets
- `insert.smartArt` (Insert › Illustrations): SmartArt {"layout"?: "basicList|process|cycle|hierarchy|pyramid|radial|matrix|venn", "items"?: [string | {"text": string, "level"?: 0-7, "color"?: RRGGBB}], "colors"?: "accent1…accent6|colorful", "width"?: pt, "height"?: pt} (no items: sample items for the layout)
- `insert.chart` (Insert › Illustrations): Chart {"type"?: "column|columnStacked|bar|barStacked|line|area|pie|doughnut|scatter", "data"?: {"categories": [string], "series": [{"name": string, "values": [number|null]}]}, "title"?: string, "legend"?: "right|left|top|bottom|none", "dataLabels"?: bool, "width"?: pt, "height"?: pt} (no params: the chart type picker)
- `insert.canvas` (Insert › Illustrations): Drawing Canvas {"width"?: pt (default 432 = 6"), "height"?: pt (default 216 = 3"), "fill"?: "RRGGBB", "outline"?: "RRGGBB"}  (in line with text at the caret; it stays selected, so the next Pictures, Shapes or Text Box goes inside it)
- `insert.wordArt` (Insert › Text): WordArt {"text"?: string, "style"?: WordArt style id (see format.textEffects), "transform"?: "textArchUp"|"textArchDown"|"textCircle"|"textWave1"|… (a DrawingML preset text warp)}
- `insert.quickParts` (Insert › Text): Quick Parts {"save"?: name (from the selection), "in"?: "document" (save into the document's own building blocks, kept in its file; else this session's), "insert"?: name, "delete"?: name} → {"parts": names (this session's, then the document's Quick Parts), "document": the document's Quick Parts}
- `insert.autoText` (Insert › Text › Quick Parts): AutoText {"save"?: name, "in"?: "document", "insert"?: name, "delete"?: name} → {"parts": names, "document": the document's AutoText}
- `insert.docProperty` (Insert › Text › Quick Parts): Document Property {"name": "Title|Author|Subject|Keywords|Comments|Category"}
- `insert.signatureLine` (Insert › Text): Signature Line {"signer"?: string, "title"?: string}
- `insert.object` (Insert › Text): Object {"path": string}
- `insert.spreadsheet` (Insert › Tables): Spreadsheet Table {"csv"?: string}

## link

- `link.targets` (Insert › Links): Link {}

## equation

- `equation.edit` (Equation): Edit Equation {"pos"?: {"path": [[node, child]…], "off": n}}
- `equation.exit` (Equation): Leave Equation {"before"?: bool}
- `equation.type` (Equation): Type in Equation {"text": string}
- `equation.insertStructure` (Equation › Structures): Insert Structure {"id"?: string (see equation.gallery), "linear"?: string, "latex"?: string}
- `equation.insertSymbol` (Equation › Symbols): Insert Symbol {"char": string}
- `equation.move` (Equation): Move in Equation {"dir": "left|right|up|down|home|end|next|prev"}
- `equation.backspace` (Equation): Delete Back in Equation {}
- `equation.delete` (Equation): Delete in Equation {}
- `equation.deleteSurrounding` (Equation): Delete Around Caret in Equation {"before": n, "after": n}
- `equation.enter` (Equation): Enter in Equation {}
- `equation.convert` (Equation › Conversions): Convert {"to": "professional|linear", "all"?: bool}
- `equation.inputFormat` (Equation › Conversions): Input Format {"format": "unicode|latex"}
- `equation.normalText` (Equation › Tools): Normal Text {"value"?: bool}
- `equation.display` (Equation): Change to Display {"value"?: bool}
- `equation.justify` (Equation): Justification {"jc": "centerGroup|center|left|right"}
- `equation.number` (Equation): Equation Number {"value"?: bool}
- `equation.set` (Equation): Set Equation {"linear"?: string, "latex"?: string}
- `equation.get` (Equation): Equation Info {}
- `equation.gallery` (Equation › Structures): Equation Gallery {}
- `equation.structureActions` (Equation): Structure Actions {}
- `equation.structure` (Equation): Change Structure {"action": string (see equation.structureActions), "level"?: n}

## layout

- `layout.margins` (Layout › Page Setup): Margins {"preset"?: "normal|narrow|moderate|wide|mirrored|office2003", "top"?: pt, "bottom"?: pt, "left"?: pt, "right"?: pt, "gutter"?: pt, "mirror"?: bool}
- `layout.orientation` (Layout › Page Setup): Orientation {"value": "portrait|landscape"}
- `layout.size` (Layout › Page Setup): Size {"name"?: "Letter|Legal|A4|…", "width"?: pt, "height"?: pt} (each side clamped to 7.2–1584 pt, 0.1–22 in; the section keeps its orientation)
- `layout.columns` (Layout › Page Setup): Columns {"count": 1-12, "space"?: pt, "separator"?: bool, "preset"?: "left|right", "widths"?: [[width pt, space after pt], …] (unequal columns; sets the count), "apply"?: "section|document|forward|selection"} (default: selection when text is selected in the main text — section breaks around it — else section)
- `layout.break` (Layout › Page Setup): Breaks {"kind": "page|column|textWrapping|nextPage|continuous|evenPage|oddPage"}
- `layout.lineNumbers` (Layout › Page Setup): Line Numbers {"value"?: "none|continuous|restartPage|restartSection", "start"?: 1-32767, "countBy"?: 1-100, "distance"?: pt (0 = auto)}
- `layout.hyphenation` (Layout › Page Setup): Hyphenation {"value"?: bool (automatic; toggles when nothing is given), "zone"?: pt, "caps"?: bool (hyphenate words in capitals), "limit"?: n (consecutive hyphens, 0 = no limit)}
- `layout.manualHyphenation` (Layout › Page Setup › Hyphenation): Manual Hyphenation {"from"?: Pos (default: the caret)} → the next word at a line end that could be hyphenated: {"word", "pos", "points": [char index], "suggest": char index} or {"done": true}
- `layout.pageSetup` (Layout › Page Setup): Page Setup {"section"?: SectionProps} (replaces the whole section, headers and footers included; checked like Size, Margins, Columns, Line Numbers, Footnotes and Page Borders: non-finite numbers and margins that leave no room for text are refused; page sides 7.2–1584 pt, 1–12 columns with 0–300 pt gaps, header/footer/gutter 0–1584 pt, page border width 0.25–6 pt and distance 0–31 pt, note start 1–32767, line numbers start 1–32767, countBy 1–100, distance 0–1584 pt are clamped)
- `layout.verticalAlign` (Layout › Page Setup › Layout): Vertical Alignment {"value": "top|center|justify|bottom"} (also both|justified; anything else is top). Justified shares each page's spare room between its paragraphs and tables
- `layout.sectionRtl` (Layout › Page Setup): Right-to-Left Section {"value"?: bool} (true: the section's columns run right to left; without a value it toggles)
- `layout.textDirection` (Layout › Page Setup): Text Direction {"value"?: "horizontal|down|up"} (also lrTb|tbRl|btLr; down: rotate all text 90°, lines top to bottom stacking right to left; up: 270°; default: the next after the current). In a table cell it turns the selected cells, in a text box the box; anywhere else the section(s) of the selection
- `layout.differentFirstPage` (Header & Footer › Options): Different First Page {}
- `layout.differentOddEven` (Header & Footer › Options): Different Odd & Even Pages {}
- `layout.pageNumberFormat` (Insert › Header & Footer › Page Number): Format Page Numbers {"format"?: "decimal|lowerRoman|upperRoman|lowerLetter|upperLetter", "start"?: n | null} ("start" left out: the numbering keeps its start; null: the pages number on from the section before; a number: numbering starts there)
- `layout.documentGrid` (Layout › Page Setup › Document Grid): Document Grid {"type"?: "none|lines|linesAndChars|snapToChars", "linesPerPage"?: n (sets the line pitch from the text height), "charsPerLine"?: n (sets the character pitch from the text width), "linePitch"?: pt, "charSpace"?: n (4096ths of a point added to the default font size: the character pitch)} — left out stays as it is; returns the grid with its lines per page and characters per line
- `layout.section` (Layout › Page Setup): Section Properties {}
- `layout.linkToPrevious` (Header & Footer › Navigation): Link to Previous {"footer"?: bool}

## review

- `review.newComment` (Review › Comments): New Comment {"text": string} [Mod+Alt+A / Mod+Alt+M]
- `review.reply` (Review › Comments): Reply {"id": non-negative JSON integer, "text": string}
- `review.editComment` (Review › Comments): Edit Comment {"id": non-negative JSON integer, "text": string}
- `review.deleteComment` (Review › Comments): Delete {"id"?: non-negative JSON integer (omit to use the caret), "all"?: bool}
- `review.resolveComment` (Review › Comments): Resolve {"id"?: non-negative JSON integer (omit to use the caret), "value"?: bool (omit to toggle)}
- `review.nextComment` (Review › Comments): Next {}
- `review.previousComment` (Review › Comments): Previous {}
- `review.comments` (Review › Comments): Show Comments {}
- `review.trackChanges` (Review › Tracking): Track Changes {"value"?: bool (omit to toggle)} [Mod+Shift+E]
- `review.acceptAll` (Review › Changes): Accept All Changes {"stopTracking"?: bool (also turn Track Changes off)}
- `review.rejectAll` (Review › Changes): Reject All Changes {"stopTracking"?: bool (also turn Track Changes off)}
- `review.accept` (Review › Changes): Accept {"next"?: bool (then select the next change)}
- `review.reject` (Review › Changes): Reject {"next"?: bool (then select the next change)}
- `review.nextChange` (Review › Changes): Next Change {}
- `review.previousChange` (Review › Changes): Previous Change {}
- `review.markup` (Review › Tracking): Display for Review {}
- `review.trackingOptions` (Review › Tracking): Track Changes Options {"comments"?: bool, "ink"?: bool, "insertionsDeletions"?: bool, "formatting"?: bool, "balloons"?: "revisions|inline|commentsAndFormatting", "commentDisplay"?: "margin|selected", "insertMark"?: "underline|doubleUnderline|bold|italic|strikethrough|colorOnly|none", "insertColor"?: "byAuthor" | "RRGGBB", "deleteMark"?: "strikethrough|doubleStrikethrough|hidden|caret|hash|underline|doubleUnderline|bold|italic|colorOnly|none", "deleteColor"?: "byAuthor" | "RRGGBB", "changedLines"?: "outside|left|right|none", "changedLinesColor"?: "auto" | "RRGGBB", "trackFormatting"?: bool, "moveFromMark"?: (as deleteMark; none = plain text, no colour), "moveFromColor"?: "byAuthor" | "RRGGBB", "moveToMark"?: (as insertMark; none = plain text, no colour), "moveToColor"?: "byAuthor" | "RRGGBB", "trackMoves"?: bool (the document's setting; off = a cut and paste is a deletion and an insertion, not a move)} → the options (omit all to read them)
- `review.wordCount` (Review › Proofing): Word Count {"includeTextBoxes"?: bool}
- `review.changes` (Review › Tracking): Reviewing Pane {}
- `review.spelling` (Review › Proofing): Spelling & Grammar {"wrap"?: bool (default true; false stops at the end of the current story)} [F7 / Alt+F7 / Mod+Alt+L]
- `review.issues` (Review › Proofing): Proofing Issues {}
- `review.suggestions` (Review › Proofing): Spelling Suggestions {"pos"?: Pos}
- `review.addToDictionary` (Review › Proofing): Add to Dictionary {"word"?: string}
- `review.ignoreAll` (Review › Proofing): Ignore All {}
- `review.applySuggestion` (Review › Proofing): Change {"text": string}
- `review.proofing` (File › Options › Proofing): Check Spelling as You Type {}
- `review.thesaurus` (Review › Proofing): Thesaurus {} [Shift+F7]
- `review.hideInk` (Review › Ink): Hide Ink {"value"?: bool}
- `review.compare` (Review › Compare): Compare {"path"?: string (revised document), "text"?: string (revised text), "original"?: string (original document; default: this one), "author"?: string (label changes with), "caseChanges"?: bool, "whiteSpace"?: bool, "formatting"?: bool (default true: differences count), "level"?: "word|character", "showIn"?: "original|revised|new" (revised/new: an untitled document), "moves"|"comments"|"tables"|"headersFooters"|"footnotes"|"textBoxes"|"fields"?: bool (accepted; not honoured yet except tables, always compared)}
- `review.combine` (Review › Compare): Combine {"path"?: string (revised document), "text"?: string (revised text), "original"?: string (original document; default: this one), "author"?: string (label changes with), "caseChanges"?: bool, "whiteSpace"?: bool, "formatting"?: bool (default true: differences count), "level"?: "word|character", "showIn"?: "original|revised|new" (revised/new: an untitled document), "moves"|"comments"|"tables"|"headersFooters"|"footnotes"|"textBoxes"|"fields"?: bool (accepted; not honoured yet except tables, always compared)}
- `review.language` (Review › Language): Language {"lang"?: "en-US|en-GB|pl-PL|fr-FR|…" (BCP 47; default en-US), "noProof"?: bool, "detect"?: bool (detect language automatically, a preference), "default"?: bool (also the document's default and the saved language for future blank documents)}
- `review.language.preferred` (File › Options › Language): Set as Default Language {"lang": "en-US|en-GB|pl-PL|nl-NL|…" (BCP 47)} — only the saved default proofing language, what future blank documents are written in, as Options › Language › Set as default does; the open document, the selection and the undo history don't change. Returns {"preferred": tag}.
- `review.showMarkup` (Review › Tracking): Show Markup {}
- `review.editor` (Home › Editor): Editor {}
- `review.restrict` (Review › Protect): Restrict Editing {"mode"?: "none|readOnly|comments|trackedChanges|forms" (start enforcing; "none" stops), "formatting"?: bool (limit formatting to unlocked styles), "lockedStyles"?: [style id or name] (the styles that can't be applied; every other style is unlocked), "password"?: string (set when enforcing; required to stop a password-protected document), "stop"?: bool, "exception"?: "add" (the selection stays editable for everyone) | "remove" (exceptions touching the selection) | "removeAll"} → state
- `review.readAloud` (Review › Speech): Read Aloud {"skipCitations"?: bool} [Mod+Alt+Space]

## file

- `file.rename` (File › Info): Rename Document {"name": string (document name; its extension is kept, so the name may be given with or without it)}
- `file.new` (File): New {"template"?: "blank|sample|letter|resume|report"} [Mod+N]
- `file.open` (File): Open {"path": string, "data"?: base64 (the file's bytes; `path` then only names it), "password"?: string (for a password-protected Word document)} [Mod+O / Mod+F12 / Mod+Alt+F2]
- `file.save` (File): Save {"path"?: string, "password"?: string (encrypt this and later saves with it, as file.encrypt does), "markup"?: bool (Print Markup for a PDF, PNG, HTML, Markdown or text copy: comments shown; default file.printMarkup), "format"?: "wordml2003" (an .xml file as a Word 2003 XML Document) | "flatopc" (as a Word XML Document, the default; saving over a Word 2003 XML file keeps that format)} [Mod+S / Shift+F12 / Alt+Shift+F2]
- `file.saveAs` (File): Save As {"path": string, "password"?: string, "markup"?: bool, "format"?: string (as file.save)} [F12 / Mod+Shift+S]
- `file.encrypt` (File › Info › Protect Document): Encrypt with Password {"password": string (Word documents are saved encrypted with it) | null or "" (saved unencrypted)}
- `file.exportPdf` (File › Export): Export PDF {"path": string, "markup"?: bool (Print Markup: tracked changes marked up and each page scaled down beside the comments in balloons; default file.printMarkup)}
- `file.exportPng` (File › Export): Export Page as PNG {"path": string, "page"?: n (1-based), "scale"?: px per pt, "markup"?: bool (the page with its comments in balloons beside it; default file.printMarkup)}
- `file.printMarkup` (File › Print): Print Markup {"value"?: bool (omit to toggle)} — PDFs, prints and copies show comments (balloons beside each page; a list at the end of HTML, Markdown and text) and tracked changes
- `file.printPdf` (File › Print): Print to PDF {"path": string, "pagesPerSheet"?: 1 | 2 | 4 | 6 | 9 | 16 | "booklet" | "bookletReverse", "range"?: "all" | "current" | "selection" (the pages the selection touches) | "custom", "pages"?: "1-3,5" (implies custom), "parity"?: "all" | "odd" | "even", "copies"?: 1-999, "collate"?: bool (default true), "paper"?: "none" | "Letter" | "Legal" | "A4" | … (a Layout › Size name: scale every page to this paper, centred; the document keeps its size)}
- `file.print` (File): Print {} [Mod+P / Mod+Shift+F12 / Mod+F2 / Mod+Alt+I]
- `file.close` (File): Close {"force"?: bool (desktop app's control channel and MCP bridge only: without it a document with unsaved changes is an error and stays open; with it the changes are discarded. Headless sessions never ask; file.closeDocument closes a document there)} [Mod+W / Mod+F4]
- `file.closeDocument` (Agents): Close Document {"id"?: n (an open document, see view.switchWindows; default the active one), "force"?: bool (discard unsaved changes; without it a document with unsaved changes is an error and stays open)} → {"closed": id, "active": id, "documents": [{"id", "title", "path", "dirty", "active"}]}; closing the last document leaves a new blank one
- `file.properties` (File › Info): Properties {"title"?, "subject"?, "author"?, "keywords"?, "comments"?, "category"?, "custom"?: {name: string | {"value": string, "linkTarget"?: string | null} | null (removes)}}; text values and bookmark targets are at most 1 MiB; a string keeps an existing target, an object replaces it (omitted/null target unlinks)
- `file.info` (File): Info {}
- `file.setAuthor` (File › Options › General): User Name {"name": string (author of new tracked changes and comments)}
- `file.privacyOptions` (File › Options › Save): Privacy Options {"removePersonalInfo"?: bool (save comment and revision authors as "Author", no creator or last-modified-by), "removeDateTime"?: bool (save comments and tracked changes without dates)} — at least one; the open document keeps its real names and dates
- `file.privacy` (File › Options › Save): Privacy Settings {} → {"removePersonalInfo": bool, "removeDateTime": bool} (file.privacyOptions changes them)
- `file.options` (File): Options {"pane"?: "general|display|proofing|save|language|accessibility|advanced|agents", "author"?: string, "initials"?: string, "units"?: "inches|centimeters|millimeters|points|picas|auto" (auto: the region's), "region"?: string (a locale tag like pl-PL, saved: the paper File › New starts on, the default units and the decimal separator; auto: the system's), "typingReplacesSelection"?: bool, "insertKeyOvertype"?: bool, "overtype"?: bool, "marks"?: {"tabs"?: bool, "spaces"?: bool, "paragraphs"?: bool, "hidden"?: bool}, "checkSpelling"?: bool, "markGrammar"?: bool, "ignoreUppercase"?: bool, "ignoreNumbers"?: bool, "ignoreInternet"?: bool, "dictionariesFolder"?: string (a folder of Hunspell .aff/.dic files searched first, saved; auto: the system locations only), "userTemplatesFolder"?: string (the folder File › New lists personal templates from, saved; auto: the app's own Templates folder; not a network folder), "addWords"?: [string], "removeWords"?: [string]} — with any setting it changes them and opens nothing; without, it opens File › Options (at `pane`). Returns the settings.
- `file.accessibility` (Review › Accessibility): Check Accessibility {}
- `file.inspect` (File › Info): Inspect Document {"remove"?: ["comments", "revisions", "properties", "hidden", "headers"]} → {found: {comments, revisions, properties, hiddenText, hiddenCount, hidden: [{story: "body|header|footer|footnote|endnote|comment|textBox", part?, text}] (at most 1000), truncated, unsupported: [{story, object: "table|opaque", ..}] (hidden text not inspected: table styles, verbatim objects), headers}, removed, residual: [..] (hidden text a removal couldn't reach), removedNotes: [{kind, part, text}] (notes whose hidden reference was removed)}; whole hidden paragraphs go with their marks; the removals are refused while the document tracks changes
- `file.protect` (File › Info): Protect Document {"mode": "none|readOnly|comments|trackedChanges"} (starting enforcement; "none" doesn't stop a protected document — use review.restrict {"stop": true})
- `file.versions` (File › Info): Version History {"save"?: label, "restore"?: index}
- `file.recover` (File › Info): Recover Unsaved Documents {"restore"?: recoveryId, "discard"?: recoveryId, "refresh"?: true}; desktop only; returns {enabled,busy,documents,error}; restore loads asynchronously without a file path
- `file.newFromTemplate` (File › New): New from Template {"path": string} → a new, untitled document from the template, attached to it
- `file.saveTemplate` (File › Save As): Save as Template {"path": string}
- `file.autosave` (Quick Access Toolbar): AutoSave {}
- `file.compatibility` (File › Info): Check Compatibility {}
- `file.share` (File): Share {}
- `file.listTemplates` (File › New): Personal Templates {"dir"?: string (the user templates folder; default: the one saved in File › Options)} → {"dir", "templates": [{"label" (the file name without its extension), "title": string|null (dc:title), "path", "category" ("" at the top level, else the subfolder's name), "modified": ISO-8601|null}] (.dotx and .dotm, at most 500, by category then label), "truncated": bool}; a network folder is refused

## document

- `document.inspect` (Agents): Inspect Document {"text"?: bool}
- `document.text` (Agents): Document Text {}
- `document.paragraph` (Agents): Paragraph Details {"path": [n], "story"?: Story}
- `document.selection` (Agents): Selection {}
- `document.layout` (Agents): Layout Summary {}
- `document.setText` (Agents): Replace Document Text {"text": string}

## proof

- `proof.packs` (File › Options › Language): Language Packs {"refresh"?: bool (fetch the pinned index again; only while downloading is on; in the app it runs in the background: see "refreshing")} — opens nothing. Returns {"packs": [{"locale", "name", "size" (bytes), "licence" (SPDX), "class", "source" (where the data comes from), "archive" (the download), "spelling", "hyphenation", "installed"}], "languages": [{"tags", "pack", "installed", "size", "proofing" (built_in, installed, own_dictionary, system_dictionary, install, grammar_built_in, not_available), "default"}] (Options › Language › Your languages), "installed": [{"locale", "name", "licence"}], "installing": [{"locale", "done", "total"} (bytes)], "refreshing": bool, "errors": {locale or "" (the list): message} (the last failure of each), "index_override": string|null (a test index in use instead of the pinned one), "network": bool (downloading on), "available": bool (a font store to install into)}
- `proof.installPack` (File › Options › Language): Install Language Pack {"locale": string (a pack's locale from proof.packs, like nl or pt-pt)} — downloads, verifies (sha256) and installs it; spelling and hyphenation in that language use it at once. Needs downloading on (only the person in the app can turn it on). Opens nothing. In the app it runs in the background and returns {"started": true}: follow it with proof.packs ("installing", then "installed" or "errors"); elsewhere it returns when installed.
- `proof.removePack` (File › Options › Language): Remove Language Pack {"locale": string} — removes the installed pack. Opens nothing.

## design

- `design.theme` (Design › Document Formatting): Themes {"name": string}
- `design.themeFonts` (Design › Document Formatting): Fonts {"heading": string, "body"?: string}
- `design.themeColors` (Design › Document Formatting): Colors {}
- `design.styleSet` (Design › Document Formatting): Style Set {"name": "default|basic|lines|shaded|casual|centered|minimalist|title"}
- `design.paragraphSpacing` (Design › Document Formatting): Paragraph Spacing {"value": "default|none|compact|tight|open|relaxed|double"}
- `design.scaleFontSizes` (Design › Document Formatting): Scale Font Sizes {"delta": pt (-1638..1638, not 0) | "percent": number (-99..1000, not 0; 10 = +10%)} (exactly one)
- `design.watermark` (Design › Page Background): Watermark {"text"?: string, "remove"?: bool, "diagonal"?: bool, "color"?: "RRGGBB"}
- `design.pageColor` (Design › Page Background): Page Color {"color": "RRGGBB" | null}
- `design.pageBorders` (Design › Page Background): Page Borders {"kind"?: "box|none", "width"?: pt, "color"?: "RRGGBB", "style"?: "single|double|dotted|dashed|thick|triple|dotDash|wave", "sides"?: {"top"|"left"|"bottom"|"right": {"style"?, "width"?: pt, "color"?: "RRGGBB"} | null} (exactly these sides, instead of `kind`), "applyTo"?: "section|document"}
- `design.setDefault` (Design › Document Formatting): Set as Default {}
- `design.themes` (Design › Document Formatting): Theme List {}
- `design.effects` (Design › Document Formatting): Effects {}

## references

- `references.toc` (References › Table of Contents): Table of Contents {"levels"?: 1-9, "title"?: string, "pageNumbers"?: bool, "rightAlign"?: bool, "tabLeader"?: "dot|hyphen|underscore|none", "hyperlinks"?: bool, "headingStyles"?: bool, "outlineLevels"?: bool, "tcFields"?: bool, "styleLevels"?: {style name: 1-9}} (replaces an existing table; {} updates it)
- `references.updateToc` (References › Table of Contents): Update Table {}
- `references.removeToc` (References › Table of Contents): Remove Table of Contents {}
- `references.addText` (References › Table of Contents): Add Text {"level": 0 (do not show) | 1-9}
- `references.footnote` (References › Footnotes): Insert Footnote {"text"?: string, "mark"?: string (a custom mark instead of the number)} [Mod+Alt+F]
- `references.endnote` (References › Footnotes): Insert Endnote {"text"?: string, "mark"?: string (a custom mark instead of the number)} [Mod+Alt+E]
- `references.convertNotes` (References › Footnotes): Convert Notes {"to": "endnote" (footnotes become endnotes) | "footnote" (endnotes become footnotes) | "swap"}
- `references.nextFootnote` (References › Footnotes): Next Footnote {}
- `references.notes` (References › Footnotes): Show Notes {}
- `references.caption` (References › Captions): Insert Caption {"label"?: "Figure|Table|Equation|any label", "text"?: string, "position"?: "below|above", "excludeLabel"?: bool, "format"?: "ARABIC|alphabetic|ALPHABETIC|roman|ROMAN", "chapter"?: heading level 1-9, "separator"?: "-|.|:|—|–"}
- `references.updateFields` (References): Update Field {"all"?: bool (the body and every header, footer, note and text box, wherever the caret is; default: the story the caret is in)} [F9]
- `references.sources` (References › Citations & Bibliography): Manage Sources {"add"?: Source, "remove"?: tag, "import"?: path (a Word bibliography file, `b:Sources` / `Sources.xml`)} → list
- `references.citation` (References › Citations & Bibliography): Insert Citation {"tag"?: string, "source"?: Source (added if new), "pages"?: string}
- `references.citationStyle` (References › Citations & Bibliography): Style {"style": "APA|Chicago|GB/T 7714|GOST (name sort)|GOST (title sort)|Harvard (Anglia)|IEEE|ISO 690 (author-date)|ISO 690 (numerical)|MLA|SIST02|Turabian" (Word's style names work too)}
- `references.bibliography` (References › Citations & Bibliography): Bibliography {"title"?: string}
- `references.tableOfFigures` (References › Captions): Insert Table of Figures {"label"?: "Figure|Table|Equation" or a caption label of your own, "includeLabel"?: bool, "pageNumbers"?: bool, "rightAlign"?: bool, "tabLeader"?: "dot|hyphen|underscore|none"}
- `references.updateFigures` (References › Captions): Update Table {}
- `references.markCitation` (References › Table of Authorities): Mark Citation {"entry"?: string}
- `references.tableOfAuthorities` (References › Table of Authorities): Insert Table of Authorities {}
- `references.updateAuthorities` (References › Table of Authorities): Update Table {}
- `references.noteOptions` (References › Footnotes): Footnote and Endnote {"kind"?: "footnote|endnote", "pos"?: "pageBottom|beneathText" (footnotes) | "sectEnd|docEnd" (endnotes), "numFmt"?: "decimal|lowerRoman|upperRoman|lowerLetter|upperLetter|…", "numStart"?: 1-32767, "numRestart"?: "continuous|eachSect|eachPage" (each page: footnotes only), "scope"?: "document|section", "footnoteFormat"?: …, "endnoteFormat"?: …} — no settings: the options in effect at the caret
- `references.researcher` (References › Research): Researcher {}
- `references.markEntry` (References › Index): Mark Entry {"entry"?: string (the selection), "subentry"?: string, "crossReference"?: "See …", "bookmark"?: page-range bookmark, "bold"?: bool, "italic"?: bool, "all"?: bool (Mark All: every paragraph's first match of "text" or the selection)}
- `references.index` (References › Index): Insert Index {"type"?: "indented|runIn", "columns"?: 1-4, "rightAlign"?: bool, "tabLeader"?: "dot|hyphen|underscore|none", "headings"?: bool (letter headings)} (replaces an existing index's settings)
- `references.updateIndex` (References › Index): Update Index {}

## fields

- `fields.toggleCode` (Insert › Text › Quick Parts): Toggle Field Codes {} [Shift+F9]
- `fields.setCode` (Insert › Text › Quick Parts): Edit Field Code {"code": string}
- `fields.unlink` (Insert › Text › Quick Parts): Unlink Fields {} [Mod+Shift+F9]
- `fields.lock` (Insert › Text › Quick Parts): Lock Fields {} [Mod+F11]
- `fields.unlock` (Insert › Text › Quick Parts): Unlock Fields {} [Mod+Shift+F11]
- `fields.next` (Insert › Text › Quick Parts): Next Field {} [Alt+F1]
- `fields.previous` (Insert › Text › Quick Parts): Previous Field {} [Shift+F11 / Alt+Shift+F1]
- `fields.selected` (Insert › Text › Quick Parts): Selected Fields {}

## mailings

- `mailings.start` (Mailings › Start Mail Merge): Start Mail Merge {"kind": "letters|emails|envelopes|labels|directory|normal"}
- `mailings.recipients` (Mailings › Start Mail Merge): Select Recipients {"csv"?: string, "path"?: string (.csv/.tsv/.txt, or a .xlsx/.xlsm/.xls/.ods workbook), "data"?: base64 (a file's bytes, as for path), "encoding"?: string (a text list's encoding, e.g. "gbk", "big5", "shift_jis", "utf-16le"; default: detected), "sheet"?: name | number (1 = first; a workbook with several sheets and no sheet answers {"sheets": [...], "chooseSheet": true} and loads nothing), "headers"?: bool (default true: the first non-blank row names the fields; false: fields are Column 1…N), "rows"?: [{field: value}] | [[value]], "fields"?: [string] (column order; required with array rows)}
- `mailings.editRecipients` (Mailings › Start Mail Merge): Edit Recipient List {"rows"?: [{field: value}] | [[value]], "fields"?: [string]} (no params: the list as {headers, rows (every record), records (how many merge), rules, sort})
- `mailings.filterRecipients` (Mailings › Start Mail Merge › Edit Recipient List): Filter Recipients {"rules"?: [{"field": string, "op": "equal|notEqual|less|greater|lessOrEqual|greaterOrEqual|blank|notBlank|contains|notContains", "value"?: string, "join"?: "and|or" (with the rule before; And binds tighter)}], "sort"?: [{"field": string, "descending"?: bool}]} (replaces the filter; `sort` too when given; {} clears both). Preview, Finish & Merge and labels use only the matching records, in sort order
- `mailings.sortRecipients` (Mailings › Start Mail Merge › Edit Recipient List): Sort Recipients {"sort"?: [{"field": string, "descending"?: bool}]} | {"field": string, "descending"?: bool} (no params: the list's own order)
- `mailings.insertField` (Mailings › Write & Insert Fields): Insert Merge Field {"field": string}
- `mailings.addressBlock` (Mailings › Write & Insert Fields): Address Block {}
- `mailings.greetingLine` (Mailings › Write & Insert Fields): Greeting Line {}
- `mailings.rules` (Mailings › Write & Insert Fields): Rules {"rule": "IF|SKIPIF|NEXTIF|NEXT|MERGEREC", "field"?, "value"?, "then"?, "else"?}
- `mailings.matchFields` (Mailings › Write & Insert Fields): Match Fields {}
- `mailings.highlightFields` (Mailings › Write & Insert Fields): Highlight Merge Fields {}
- `mailings.preview` (Mailings › Preview Results): Preview Results {}
- `mailings.next` (Mailings › Preview Results): Next Record {}
- `mailings.previous` (Mailings › Preview Results): Previous Record {}
- `mailings.first` (Mailings › Preview Results): First Record {}
- `mailings.last` (Mailings › Preview Results): Last Record {}
- `mailings.goToRecord` (Mailings › Preview Results): Go to Record {"record": n (1 = the first; past either end goes to the first or last record)}
- `mailings.findRecipient` (Mailings › Preview Results): Find Recipient {}
- `mailings.checkErrors` (Mailings › Finish): Check for Errors {}
- `mailings.finish` (Mailings › Finish): Finish & Merge {"path"?: string (save the merged document), "records"?: "all|current" (current: the previewed record; default all, or from/to), "from"?: n, "to"?: n (record numbers, 1 = the first)}
- `mailings.printDocuments` (Mailings › Finish › Finish & Merge): Print Documents {"records"?: "all|current", "from"?: n, "to"?: n} (merges into a new document, as Finish & Merge does, and opens Print for it)
- `mailings.envelopes` (Mailings › Create): Envelopes {"delivery": string, "return"?: string, "size"?: "Envelope #10|#9|Monarch|DL|C4|C5|C6|B5", "width"?: pt, "height"?: pt, "add"?: bool (add to this document instead of a new one)}
- `mailings.labels` (Mailings › Create): Labels {"text"?: string, "product"?: "letter-3x10|letter-2x10|letter-2x7|letter-2x5|letter-4x20|a4-3x7|a4-2x7|a4-3x8|a4-2x4", "rows"?: n, "cols"?: n, "fromRecipients"?: bool (one label per selected recipient, continuing across sheets), "single"?: {"row": n, "col": n}}

## picture

- `picture.size` (Picture Format › Size): Size {"width"?: pt, "height"?: pt, "lockAspect"?: bool, "scale"?: percent, "original"?: bool} (scale: of the current size, or with original of the picture's original size, its pixels at 96 ppi less what is cropped; original alone restores that size; one side alone keeps the proportions unless lockAspect is false; 1–4000 pt: when the proportions are kept, a side past 4000 pt shrinks the other with it)
- `picture.crop` (Picture Format › Size): Crop {"left"?, "top"?, "right"?, "bottom"? (fractions of the source 0–0.95; the two sides of an axis keep at least 5% between them; a side left out is uncropped), "width"?: pt, "height"?: pt (the new display size, in the same undo step; a floating picture also moves by what a left/top crop trims, so the visible part stays put)}
- `picture.altText` (Picture Format › Accessibility): Alt Text {"text": string, "title"?: string, "decorative"?: bool}
- `picture.corrections` (Picture Format › Adjust): Corrections {"brightness"?: -100..100, "contrast"?: -100..100, "sharpen"?: -100..100}
- `picture.color` (Picture Format › Adjust): Color {"mode": "grayscale|sepia|washout|blackAndWhite|saturation|tint", "saturation"?: 0..400}
- `picture.iconColor` (Picture Format › Adjust): Icon Color {"color": "RRGGBB"}
- `picture.effects` (Picture Format › Adjust): Artistic Effects {"effect": "blur|sharpen|invert|posterize|pixelate|none"} (replaces the picture's effect)
- `picture.transparency` (Picture Format › Adjust): Transparency {"percent": 0..100}
- `picture.removeBackground` (Picture Format › Adjust): Remove Background {"tolerance"?: 0..255}
- `picture.compress` (Picture Format › Adjust): Compress Pictures {"maxPixels"?: n}
- `picture.reset` (Picture Format › Adjust): Reset Picture {}
- `picture.change` (Picture Format › Adjust): Change Picture {"path"?: string, "data"?: base64}
- `picture.style` (Picture Format › Picture Styles): Picture Styles {"style": "simpleFrame|thickFrame|rounded|softEdge|shadow"} (replaces the picture's style and border)
- `picture.border` (Picture Format › Picture Styles): Picture Border {"color"?: "RRGGBB", "width"?: px} (replaces the picture's border)

## object

- `object.altText` (Shape Format › Accessibility): Alt Text {"text"?: string, "title"?: string, "decorative"?: bool} (the selected picture, shape, text box, group or chart)

## arrange

- `arrange.rotate` (Layout › Arrange): Rotate {"direction": "right|left|flipVertical|flipHorizontal"}  (turns 90° or mirrors the selected picture, shape or text box; its pixels are kept)
- `arrange.rotation` (Layout › Arrange): Rotation {"degrees": number, "flipH"?: bool, "flipV"?: bool}  (the exact angle, clockwise, of the selected picture, shape or text box; normalised to 0–360)
- `arrange.wrap` (Layout › Arrange): Wrap Text {"wrap": "inline|square|tight|through|topAndBottom|behindText|inFrontOfText"}
- `arrange.wrapText` (Layout › Arrange): Wrap Text Sides {"side": "bothSides|left|right|largest"}  (the sides of the selected Square, Tight or Through object text flows on; largest: the wider side, line by line)
- `arrange.moveWithText` (Layout › Arrange › Wrap Text): Move with Text {"value": bool}  (true: Move with Text, the floating object's vertical position follows its paragraph; false: Fix Position on Page. It stays where it is)
- `arrange.position` (Layout › Arrange): Position {"preset"?: "topLeft|topCenter|topRight|middleLeft|middleCenter|middleRight|bottomLeft|bottomCenter|bottomRight", "x"?: pt, "y"?: pt}
- `arrange.bringForward` (Layout › Arrange): Bring Forward {}
- `arrange.sendBackward` (Layout › Arrange): Send Backward {}
- `arrange.align` (Layout › Arrange): Align {"value": "left|center|right"}
- `arrange.selectionPane` (Layout › Arrange): Selection Pane {}
- `arrange.bounds` (Layout › Arrange): Move or Resize {"width"?: pt, "height"?: pt, "x"?: pt, "y"?: pt, "page"?: n, "to"?: Pos}  (x/y: the top-left on page `page` (0-based, default its page); moving an inline object by x/y floats it. to: an In Line with Text object moves to that text position and stays inline, as a drag does)
- `arrange.copyTo` (Layout › Arrange): Copy to {"x": pt, "y": pt, "page"?: n} | {"to": Pos}  (Ctrl+drag: a copy of the selected object lands with its top-left there, or an In Line with Text one at the text position `to`, and is selected; the original and the clipboard stay as they were)
- `arrange.nudge` (Layout › Arrange): Nudge {"dx"?: pt, "dy"?: pt}
- `arrange.group` (Layout › Arrange): Group {}  (groups the selected pictures, shapes and text boxes: the selected one plus those added with select.addObject)
- `arrange.ungroup` (Layout › Arrange): Ungroup {}

## shape

- `shape.outline` (Shape Format › Shape Styles): Shape Outline {"color": "RRGGBB" | null, "width"?: pt}  (a selected drawing canvas: its border)
- `shape.effects` (Shape Format › Shape Styles): Shape Effects {"shadow"?: preset|{"preset"?, "color"?: "RRGGBB", "transparency"?: %, "blur"?: pt, "distance"?: pt, "angle"?: deg}|null, "glow"?: pt|{"color"?: "RRGGBB", "size"?: pt, "transparency"?: %}|null, "softEdge"?: pt|null}  (shadow presets: offsetBottomRight, offsetBottom, offsetBottomLeft, offsetRight, offsetCenter, offsetLeft, offsetTopRight, offsetTop, offsetTopLeft; an omitted key is left as it is; applies to every shape in the selection)
- `shape.change` (Shape Format › Insert Shapes): Change Shape {"kind": string}
- `shape.textDirection` (Shape Format › Text): Text Direction {"dir": "horz|vert|vert270|wordArtVert"}  (horizontal, rotate all text 90°, 270°, stacked; the selected text box or the one the caret is in)
- `shape.alignText` (Shape Format › Text): Align Text {"anchor": "t|ctr|b"}  (top, middle, bottom of the box: for turned text, from the side its lines start on)
- `shape.link` (Shape Format › Text): Create Link {"target": Pos | n}  (the empty text box the selected box's text continues in: its position, or its Selection Pane index)
- `shape.breakLink` (Shape Format › Text): Break Link {}  (the text stops at the end of the selected box; the boxes after it go back to their own text)
- `shape.fill` (Shape Format › Shape Styles): Shape Fill {"color": "RRGGBB" | null, "transparency"?: %} | {"gradient": {"stops": [{"pos": %, "color": "RRGGBB", "transparency"?: %}], "type"?: "linear|radial|rectangular|path", "angle"?: deg, "focus"?: [l, t, r, b], "tile"?: [l, t, r, b], "scaled"?: bool, "rotateWithShape"?: bool}}  (tile: percent insets of the gradient's area; scaled: a linear angle scaled with the shape; a colour alone keeps the shape's transparency; angle: linear only, 0 = left to right, 90 = top to bottom; focus: percent insets of where a radial, rectangular or path gradient starts; applies to every selected shape, text box and canvas background)
- `shape.connect` (Shape Format › Insert Shapes): Connect Shapes {"start"?: end, "end"?: end}  end: {"path": [..], "off": n, "site"?: n} (glue to that body shape's connection site; nearest one when omitted) | {"x": pt, "y": pt, "page"?: n} (drag the end there: it glues to a shape's site within 12 pt, else stays free there) | null (unglue)

## smartArt

- `smartArt.items` (SmartArt Design › Create Graphic): Edit Items {"items": [string | {"text": string, "level"?: 0-7, "color"?: RRGGBB}]} (replaces the outline)
- `smartArt.textPane` (SmartArt Design › Create Graphic): Text Pane {"value"?: bool} (no value: show or hide the Text Pane)
- `smartArt.addShape` (SmartArt Design › Create Graphic): Add Shape {"after"?: item index (default: the last), "text"?: string, "below"?: bool (a sub-item instead of the next item)}
- `smartArt.promote` (SmartArt Design › Create Graphic): Promote {"index"?: item index (default: the last)} (the item and the items under it move up a level)
- `smartArt.demote` (SmartArt Design › Create Graphic): Demote {"index"?: item index (default: the last)} (the item and the items under it move down a level)
- `smartArt.layout` (SmartArt Design › Layouts): Change Layout {"layout": "basicList|process|cycle|hierarchy|pyramid|radial|matrix|venn"}
- `smartArt.colors` (SmartArt Design › SmartArt Styles): Change Colors {"variant": "accent1|accent2|accent3|accent4|accent5|accent6|colorful"} (the items' own colours are dropped)
- `smartArt.itemColor` (SmartArt Design › SmartArt Styles): Item Color {"index"?: item index (default: the last), "color"?: "RRGGBB" (none: the style's colour)}
- `smartArt.reset` (SmartArt Design › Reset): Reset Graphic {} (back to the default colours; the items and layout stay)

## chart

- `chart.type` (Chart Design › Type): Change Chart Type {"type": "column|columnStacked|bar|barStacked|line|area|pie|doughnut|scatter"}
- `chart.editData` (Chart Design › Data): Edit Data {"data": {"categories"?: [string], "series"?: [{"name": string, "values": [number|null]}]}}
- `chart.title` (Chart Design › Chart Layouts › Add Chart Element): Chart Title {"text"?: string|null} (no text: switch the title on or off)
- `chart.legend` (Chart Design › Chart Layouts › Add Chart Element): Legend {"pos"?: "right|left|top|bottom|none"} (no pos: switch the legend on or off)
- `chart.dataLabels` (Chart Design › Chart Layouts › Add Chart Element): Data Labels {"on"?: bool} (no value: switch the data labels on or off)

## draw

- `draw.select` (Draw › Tools): Select {}
- `draw.lasso` (Draw › Tools): Lasso Select {"page"?: n, "points"?: [[x, y], …], "clear"?: bool}  (no points: use the lasso; points: select the ink inside that loop; clear: drop the selection)
- `draw.lassoMove` (Draw › Tools): Move Selected Ink {"dx": pt, "dy": pt}
- `draw.lassoDelete` (Draw › Tools): Delete Selected Ink {}
- `draw.lassoColor` (Draw › Tools): Recolor Selected Ink {"color": "RRGGBB"}
- `draw.eraser` (Draw › Tools): Eraser {"page"?: n, "x"?: pt, "y"?: pt}  (no point: use the eraser; a point: delete the ink stroke there)
- `draw.pen` (Draw › Pens): Pen {"color"?: "RRGGBB", "width"?: pt}
- `draw.pencil` (Draw › Pens): Pencil {"color"?: "RRGGBB", "width"?: pt}
- `draw.highlighter` (Draw › Pens): Highlighter {"color"?: "RRGGBB", "width"?: pt}
- `draw.addPen` (Draw › Pens): Add Pen {"kind"?: "pen|pencil|highlighter", "color"?: "RRGGBB", "width"?: pt}  (adds the pen to the gallery and picks it up)
- `draw.removePen` (Draw › Pens): Remove Pen {"index": n}
- `draw.stroke` (Draw › Pens): Draw Ink {"page": n, "points": [[x, y], …] (page points, at most 5000), "tool"?: "pen|pencil|highlighter", "color"?: "RRGGBB", "width"?: pt}
- `draw.erase` (Draw › Tools): Erase Ink {"page": n, "x": pt, "y": pt}
- `draw.inkToShape` (Draw › Convert): Ink to Shape {"value"?: bool}  (no value: convert the lasso-selected strokes, or turn Ink to Shape on or off)
- `draw.convertInk` (Draw › Convert): Convert to Shapes {}
- `draw.replay` (Draw › Replay): Ink Replay {"value"?: bool}  (starts or stops Ink Replay; returns the strokes in the order they were drawn)

## canvas

- `canvas.fit` (Shape Format › Drawing Canvas): Fit {}  (shrinks the selected canvas's frame to its drawing: the members move to its top-left corner)
- `canvas.expand` (Shape Format › Drawing Canvas): Expand {"by"?: pt (default 36)}  (grows the frame right and down; at least enough to show every member)
- `canvas.scale` (Shape Format › Drawing Canvas): Scale Drawing {"factor": number (0.1–10)}  (scales the frame and every member together)
- `canvas.member` (Shape Format › Drawing Canvas): Canvas Member {"index": n, "x"?: pt, "y"?: pt, "width"?: pt, "height"?: pt, "delete"?: bool}  (moves, resizes or removes member `index` of the selected canvas; x/y from the canvas's top-left; with no change, returns the members)

## wordArt

- `wordArt.style` (Shape Format › WordArt Styles): WordArt Styles {"style": "solid"|"outlined"|"hollow"|"gradient"|"shadowed"|"glowing"|"reflected"|"sunset"}
- `wordArt.textFill` (Shape Format › WordArt Styles): Text Fill {"fill": "RRGGBB"|"none"|{"gradient": ["RRGGBB", …], "angle"?: deg}|null}
- `wordArt.textOutline` (Shape Format › WordArt Styles): Text Outline {"color"?: "RRGGBB"|null, "width"?: pt} or {"outline": "none"|null}
- `wordArt.transform` (Shape Format › WordArt Styles): Transform {"preset": "textArchUp"|"textArchDown"|"textCircle"|"textWave1"|"textSlantUp"|"textSlantDown"|"textInflate"|"textDeflate"|"textChevron"|"textChevronInverted"|"textTriangle"|"textTriangleInverted"|… (any DrawingML preset text warp)|"none", "adj"?: n (the preset's adjust value)}

## tools

- `tools.recordMacro` (View › Macros): Record Macro {"name"?: string} (call again to stop)
- `tools.macros` (View › Macros): Macros {"run"?: name, "define"?: {"name": string, "steps": [{"command", "params"}]}, "delete"?: name} [Alt+F8]
- `tools.autocorrect` (File › Options › Proofing): AutoCorrect Options {"enabled"?: bool (all of AutoCorrect), "replaceText"|"twoInitialCaps"|"capSentences"|"capCells"|"capDays"|"capsLock"|"smartQuotes"|"fractions"|"ordinals"|"dashes"|"links"|"bullets"|"numbering"|"borderLines"?: bool, "boldItalic"?: bool (*bold* and _italic_ with real formatting; default false), "tabIndent"?: bool (Set left- and first-indent with tabs and backspaces; default false), "headingStyles"?: bool (Built-in Heading styles; default false), "doubleSpacePeriod"?: bool (Add a period with double-space; default false), "autoAddFirstLetter"|"autoAddInitialCaps"?: bool (Automatically add words to the exception lists when an automatic capital is undone; default true), "add"?: {"from": string, "to": string} (adds or replaces an entry), "delete"?: string (an entry's "from", built in or added), "addException"?: string, "deleteException"?: string, "addInitialCapsException"?: string (keeps TWo INitial CApitals, like "IDs"), "deleteInitialCapsException"?: string} → options, entries and exceptions
- `tools.customizeKeyboard` (File › Options): Customize Keyboard {"command"?: id (its keys), "key"?: "Mod+Shift+K" (the command it runs), "assign"?: {"command": id, "key": string}, "remove"?: {"command": id, "key": string}, "reset"?: true (built-in keys only)} → {custom: {assigned: {key: id}, removed: [key]}, …}; no params opens the dialog
- `tools.customizeRibbon` (File › Options): Customize Ribbon {"hide"?: tab, "show"?: tab, "newTab"?: {"name"?, "after"?: tab}, "newGroup"?: {"tab", "name"?}, "add"?: {"tab", "group", "command", "after"?: id}, "remove"?: {"tab", "group"?, "command"?}, "rename"?: {"tab", "group"?, "to"}, "move"?: {"tab", "group"?, "command"?, "by": int}, "qatAdd"?: id, "qatRemove"?: id, "qatMove"?: {"command", "by": int}, "reset"?: true | "ribbon" | "qat", "layout"?: object} → {tabs: [{name, custom?, hidden?, groups?: [{name, commands}]}], qat: [id]}; only custom tabs and groups can be renamed or removed (built-in tabs can be hidden and moved); no params opens the dialog
- `tools.search` (Title Bar): Search {"query"?: string} → {matches: [{id, label, location, shortcut}]} (every word of the query in the label, location or id; at most 50); no query opens the Search box
- `tools.templates` (View › Templates): Templates and Add-ins {} → {"template": path|null, "linkStyles": bool} (from the ribbon, the app shows the dialog)
- `tools.attachTemplate` (View › Templates › Templates and Add-ins): Attach Template {"path": string, "linkStyles"?: bool, "update"?: bool (update the styles from it now), "data"?: base64 (the template's bytes, for "update")}
- `tools.detachTemplate` (View › Templates › Templates and Add-ins): Detach Template {}
- `tools.linkStyles` (View › Templates › Templates and Add-ins): Automatically Update Document Styles {"value"?: bool (default: toggle)}
- `tools.updateStyles` (View › Templates › Templates and Add-ins): Update Styles from Template {"path"?: string (default: the attached template), "data"?: base64 (the file's bytes; `path` then only names it)} → {"added", "replaced"}

## hf

- `hf.next` (Header & Footer › Navigation): Next Section {}
- `hf.previous` (Header & Footer › Navigation): Previous Section {}
- `hf.position` (Header & Footer › Position): Header/Footer Position {"header"?: pt, "footer"?: pt}

## readAloud

- `readAloud.playPause` (Review › Speech): Play/Pause {}
- `readAloud.next` (Review › Speech): Next Sentence {}
- `readAloud.previous` (Review › Speech): Previous Sentence {}
- `readAloud.stop` (Review › Speech): Stop Reading {}
- `readAloud.speed` (Review › Speech): Reading Speed {"value": number (0.5…3, 1 = normal)}
- `readAloud.skipCitations` (Review › Speech): Skip Citations and Bibliography {"value"?: bool}
- `readAloud.status` (Review › Speech): Read Aloud Status {}

## developer

- `developer.richText` (Developer › Controls): Rich Text Content Control {"title"?: string, "tag"?: string}
- `developer.plainText` (Developer › Controls): Plain Text Content Control {"title"?: string, "tag"?: string}
- `developer.picture` (Developer › Controls): Picture Content Control {"title"?: string, "tag"?: string}
- `developer.buildingBlock` (Developer › Controls): Building Block Gallery Content Control {"title"?: string, "tag"?: string}
- `developer.checkBox` (Developer › Controls): Check Box Content Control {"title"?: string, "tag"?: string, "checked"?: bool}
- `developer.comboBox` (Developer › Controls): Combo Box Content Control {"title"?: string, "tag"?: string, "items"?: [string | {"display": string, "value"?: string}]}
- `developer.dropDown` (Developer › Controls): Drop-Down List Content Control {"title"?: string, "tag"?: string, "items"?: [string | {"display": string, "value"?: string}]}
- `developer.datePicker` (Developer › Controls): Date Picker Content Control {"title"?: string, "tag"?: string, "format"?: "M/d/yyyy", "date"?: "YYYY-MM-DD"}
- `developer.repeatingSection` (Developer › Controls): Repeating Section Content Control {"title"?: string, "tag"?: string}
- `developer.designMode` (Developer › Controls): Design Mode {"value"?: bool}
- `developer.properties` (Developer › Controls): Properties {"control"?: tag or title, "title"?: string, "tag"?: string, "lockDelete"?: bool, "lockEdit"?: bool, "temporary"?: bool, "multiLine"?: bool, "placeholder"?: string, "items"?: [string | {"display", "value"}], "format"?: "M/d/yyyy", "checkedSymbol"?: char, "uncheckedSymbol"?: char}
- `developer.control` (Developer › Controls): Content Control at Selection {"control"?: tag or title, "at"?: pos}
- `developer.toggleCheckBox` (Developer › Controls): Toggle Check Box {"control"?: tag or title, "at"?: pos, "value"?: bool}
- `developer.chooseItem` (Developer › Controls): Choose List Item {"control"?: tag or title, "at"?: pos, "index"?: number, "value"?: string, "text"?: string}
- `developer.setDate` (Developer › Controls): Set Date {"control"?: tag or title, "at"?: pos, "date": "YYYY-MM-DD"}
- `developer.removeControl` (Developer › Controls): Remove Content Control {"control"?: tag or title, "at"?: pos}
