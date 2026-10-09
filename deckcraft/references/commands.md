# DeckCraft command catalog

Generated from `deckcraft-cli commands` (DeckCraft 0.3.0): 222 commands. Run one with `run_command {command, params}`, or several with `batch`.
Grep this file for a verb (`grep -n 'table[.]' commands.md`) rather than reading it whole.
`?` = optional, `a|b` = choices, `→` = what it returns. Unknown param keys are ignored silently, so copy names exactly.
`(Tab › Group)` is where the command sits in the desktop UI; `[keys]` is its shortcut.

Groups: `file` (16), `window` (1), `edit` (11), `slide` (17), `section` (5), `shape` (23), `insert` (13), `chart` (3), `picture` (4), `media` (8), `arrange` (15), `text` (11), `format` (38), `design` (8), `view` (2), `master` (4), `transition` (5), `animation` (9), `table` (16), `comment` (5), `review` (2), `show` (4), `document` (1), `commands` (1)

## file

- `file.new` (File): New Presentation {theme?: name, size?: [w,h] pt, blank?: bool} [Cmd+N]
- `file.open` (File): Open… {path} [Cmd+O]
- `file.openBytes`: Open Data {name, data: base64}
- `file.save` (File): Save {path?, format?: deckcraft|pptx} [Cmd+S]
- `file.saveAs` (File): Save As… {path, format?} [Cmd+Shift+S]
- `file.saveTemplate` (File): Save as Template… {path}
- `file.saveBytes`: Save to Data {format?: deckcraft|pptx} → {data: base64}
- `file.export` (File): Export… {path, format: png|jpeg|pptx|deckcraft|outline|pdf, slide?: index, all?: bool, scale?: px per pt; pdf: layout?: slides|notes|handouts, perPage?: 1|2|3|4|6|9, dpi?, slides?: [index], includeHidden?, textLayer?, frame?}
- `file.render`: Render Slide {slide?: index, scale?, edit?: bool} → {png: base64, width, height}
- `file.close` (File): Close {} [Cmd+W]
- `file.properties` (File): Properties {title?, subject?, author?, keywords?, comments?, category?, company?} → properties
- `file.recovery.save`: Save AutoRecover Information {} → {written}
- `file.recovery.list`: Recovered Presentations {} → [{uid, path, title, saved}]
- `file.recovery.open`: Open Recovered Presentations {} → {opened: [document index]}
- `file.recovery.discard`: Discard Recovered Presentations {uid?: one entry, else all}
- `file.revert`: Revert {}

## window

- `window.next` (Window): Next Window {index?} [Cmd+`]

## edit

- `edit.undo` (Edit): Undo {} [Cmd+Z]
- `edit.redo` (Edit): Redo {} [Cmd+Y]
- `edit.cut` (Home › Clipboard): Cut {scope?: slides} [Cmd+X]
- `edit.copy` (Home › Clipboard): Copy {scope?: slides} → {text} [Cmd+C]
- `edit.paste` (Home › Clipboard): Paste {text?: plain text to paste, scope?: slides} [Cmd+V]
- `edit.pasteText` (Edit): Paste and Match Formatting {text?} [Cmd+Shift+V]
- `edit.duplicate` (Edit): Duplicate {ids?} [Cmd+D]
- `edit.delete` (Edit): Delete {ids?, scope?: slides} [Delete]
- `edit.selectAll` (Edit): Select All {} [Cmd+A]
- `edit.deselect`: Deselect {} [Escape]
- `edit.select`: Select Objects {ids: [id], add?: bool, toggle?: bool}

## slide

- `slide.new` (Home › Slides): New Slide {layout?: layout name or kind (title, titleAndContent, sectionHeader, twoContent, comparison, titleOnly, blank, contentWithCaption, pictureWithCaption), at?: index, title?: text, body?: text} [Cmd+Shift+N]
- `slide.duplicate` (Insert): Duplicate Slide {index?}
- `slide.delete` (Edit): Delete Slide {index?, ids?: [slide id]}
- `slide.move`: Move Slide {from?: index, to: index}
- `slide.go`: Go to Slide {index} | {id}
- `slide.next`: Next Slide {} [PageDown]
- `slide.previous`: Previous Slide {} [PageUp]
- `slide.first`: First Slide {} [Home]
- `slide.last`: Last Slide {} [End]
- `slide.selectSlides`: Select Slides {ids?: [slide id], indices?: [index], add?: bool}
- `slide.hide` (Slide Show › Set Up): Hide Slide {index?, hidden?: bool}
- `slide.layout` (Home › Slides): Layout {layout: name or kind, index?}
- `slide.reset` (Home › Slides): Reset {index?}
- `slide.notes` (View): Notes {text, index?}
- `slide.rename`: Rename Slide {name, index?}
- `slide.fromOutline` (Insert › Slides From): Slides from Outline… {text}
- `slide.inspect`: Inspect Slide {index?} → the slide's shapes with ids, kinds, boxes, text, fills, animations, transition, notes

## section

- `section.add` (Home › Slides › Section): Add Section {name?, at?: slide index}
- `section.rename` (Home › Slides › Section): Rename Section {index, name}
- `section.remove` (Home › Slides › Section): Remove Section {index, slides?: bool (also delete its slides)}
- `section.removeAll` (Home › Slides › Section): Remove All Sections {}
- `section.move`: Move Section {index, to}

## shape

- `shape.insert` (Insert › Illustrations): Shapes {preset: rect|roundRect|ellipse|triangle|rightArrow|star5|… (see shape.presets), rect: [x,y,w,h] pt, text?: string}
- `shape.presets`: Shape Gallery {} → [{name, label, category}]
- `shape.connect`: Connect Shapes {from: shape id, to: shape id, fromSite?, toSite?: site index (default: the closest pair), id?: existing line to glue (else a new connector), preset?: straightConnector1|bentConnector3|curvedConnector3} → {id}
- `shape.freeform` (Insert › Shapes): Freeform {points: [[x, y], …] slide pt (≥ 2), closed?: bool (filled shape), smooth?: bool (curve through the points)} → {id}
- `shape.sites`: Connection Sites {id} → [[x, y]] connection sites in slide points
- `shape.move`: Move {dx?, dy?: pt (relative) | x?, y?: pt (absolute), ids?}
- `shape.resize` (Shape Format › Size): Size {w?, h?: pt, lockAspect?: bool, ids?}
- `shape.setBounds`: Position and Size {x, y, w, h, ids?}
- `shape.rotate` (Shape Format › Arrange › Rotate): Rotation {deg?: absolute, by?: relative, ids?}
- `shape.flip` (Shape Format › Arrange › Rotate): Flip {axis: horizontal|vertical, ids?}
- `shape.adjust`: Adjust Shape {index, value (file units), ids?}
- `shape.change` (Shape Format › Insert Shapes › Edit Shape): Change Shape {preset, ids?}
- `shape.fill` (Shape Format › Shape Styles): Shape Fill {color? | none?: true | gradient?: {stops: [[pos, color]], angle?, kind?: linear|radial} | picture?: base64 | pattern?: {preset, fg, bg} | transparency?: 0..1 | reset?: true, ids?}
- `shape.line` (Shape Format › Shape Styles): Shape Outline {color?, none?, width?: pt, dash?: solid|dot|dash|lgDash|dashDot|sysDot|sysDash, cap?, join?, head?: none|triangle|stealth|diamond|oval|arrow, tail?, reset?, ids?}
- `shape.effects` (Shape Format › Shape Styles): Shape Effects {shadow?: none|outer|inner|perspective|{color, blur, dist, dir}, glow?: none|{color, radius}, softEdges?: pt, reflection?: none|tight|half|full, bevel?: none|circle|…, reset?, ids?}
- `shape.quickStyle` (Home › Drawing): Quick Styles {index: 0..41 (theme style row×accent), ids?}
- `shape.rename` (Selection Pane): Rename {name, id?}
- `shape.altText` (Shape Format › Accessibility): Alt Text {text, decorative?: bool, ids?}
- `shape.visible` (Selection Pane): Show/Hide {visible?: bool, ids?}
- `shape.lock`: Lock {locked?: bool, ids?}
- `shape.setDefault`: Set as Default Shape {}
- `shape.merge` (Shape Format › Insert Shapes › Merge Shapes): Merge Shapes {op: union|combine|fragment|intersect|subtract, ids?: shapes in selection order (the first one's formatting is kept)} → {ids}
- `shape.inspect`: Inspect Shape {id} → full shape JSON plus its effective box

## insert

- `insert.textBox` (Insert › Text): Text Box {rect?: [x,y,w,h], text?: string}
- `insert.picture` (Insert › Images › Pictures): Picture from File… {path? | data: base64, name?, rect?: [x,y,w,h]}
- `insert.table` (Insert › Tables): Table… {rows, cols, rect?}
- `insert.chart` (Insert › Illustrations): Chart… {type?: column|bar|line|pie|doughnut|area|scatter|stackedColumn|…, rect?, categories?: [..], series?: [{name, values}]}
- `insert.audio` (Insert › Media › Audio): Audio from File… {path? | data: base64, name?, rect?}
- `insert.video` (Insert › Media › Video): Video from File… {path? | data: base64, name?, rect?}
- `insert.wordArt` (Insert › Text): WordArt {text?, style?: 0..}
- `insert.slideNumber` (Insert › Text): Slide Number {}
- `insert.dateTime` (Insert › Text): Date & Time {format?: datetime1..}
- `insert.symbol` (Insert › Symbols): Symbol {text: character(s)}
- `insert.hyperlink` (Insert › Links): Link {url? | slide?: index, tooltip?, ids?} [Cmd+K]
- `insert.smartArt` (Insert › Illustrations): SmartArt {kind: list|process|cycle|hierarchy|pyramid|matrix, items: [text]}
- `insert.actionButton` (Insert › Illustrations): Action Buttons {kind: back|forward|beginning|end|home|information|return|movie|document|sound|help|custom, rect?}

## chart

- `chart.type` (Chart Design › Type): Change Chart Type {type, id?}
- `chart.data` (Chart Design › Data): Edit Data {categories?: [..], series?: [{name, values}], id?}
- `chart.options` (Chart Design › Chart Layouts): Chart Elements {title?: string|null, legend?: b|t|l|r|null, dataLabels?: bool, gridlines?: bool, palette?, id?}

## picture

- `picture.crop` (Picture Format › Size): Crop {left?, top?, right?, bottom?: fraction 0..1, ids?}
- `picture.adjust` (Picture Format › Adjust): Corrections {brightness?: -1..1, contrast?: -1..1, saturation?: 0..4, grayscale?: bool, transparency?: 0..1, reset?: bool, ids?}
- `picture.reset` (Picture Format › Adjust): Reset Picture {ids?}
- `picture.change` (Picture Format › Adjust): Change Picture {path? | data: base64, name?, ids?}

## media

- `media.options` (Playback): Playback {autoplay?, loop?, rewind?, acrossSlides?, hide?, fullScreen?, volume?: 0..1, trimStart?: ms, trimEnd?: ms, fadeIn?: ms, fadeOut?: ms, ids?}
- `media.play` (Playback › Preview): Play {id?, from?: ms} [Alt+P]
- `media.pause` (Playback › Preview): Pause {id?}
- `media.toggle`: Play/Pause {id?}
- `media.stop` (Playback › Preview): Stop {id?}
- `media.seek`: Seek {id?, ms}
- `media.info`: Media Info {id?} → {id, name, contentType, bytes, durationMs, video, width, height, probe: {container, audio?, video?}, options, status?}
- `media.posterFrame` (Video Format › Adjust): Poster Frame {id?, ms?: frame time (default: current position)}

## arrange

- `arrange.bringToFront` (Arrange): Bring to Front {ids?} [Cmd+Shift+]]
- `arrange.bringForward` (Arrange): Bring Forward {ids?} [Cmd+]]
- `arrange.sendBackward` (Arrange): Send Backward {ids?} [Cmd+[]
- `arrange.sendToBack` (Arrange): Send to Back {ids?} [Cmd+Shift+[]
- `arrange.reorder` (Arrange): Reorder Objects {id, index: position in the stack (0 = back)}
- `arrange.group` (Arrange): Group {ids?} [Cmd+Alt+G]
- `arrange.ungroup` (Arrange): Ungroup {ids?} [Cmd+Alt+Shift+G]
- `arrange.regroup` (Arrange): Regroup {} [Cmd+Alt+J]
- `arrange.align` (Arrange › Align or Distribute): Align {edge: left|center|right|top|middle|bottom, to?: slide|selection (default: slide for one object), ids?}
- `arrange.distribute` (Arrange › Align or Distribute): Distribute {dir: horizontal|vertical, to?: slide|selection, ids?}
- `arrange.rotateLeft` (Arrange › Rotate or Flip): Rotate Left 90° {ids?}
- `arrange.rotateRight` (Arrange › Rotate or Flip): Rotate Right 90° {ids?}
- `arrange.flipHorizontal` (Arrange › Rotate or Flip): Flip Horizontal {ids?}
- `arrange.flipVertical` (Arrange › Rotate or Flip): Flip Vertical {ids?}
- `arrange.nudge`: Nudge {dx, dy, ids?} (arrow keys: 6 pt, with Alt 1 pt)

## text

- `text.edit`: Edit Text {id?, at?: [paragraph, char], end?: bool, cell?: [row, col], notes?: bool} [Enter]
- `text.exit`: Stop Editing Text {}
- `text.insert`: Type Text {text} (\n = new paragraph, \u000b = line break)
- `text.delete`: Delete Text {dir?: backward|forward|wordBackward|wordForward} [Backspace]
- `text.move`: Move Insertion Point {to: left|right|up|down|wordLeft|wordRight|lineStart|lineEnd|paraStart|paraEnd|start|end, extend?: bool}
- `text.select`: Select Text {anchor: [p, c], caret: [p, c]}
- `text.selectAll`: Select All Text {}
- `text.selectWord`: Select Word {at?: [p, c]}
- `text.selectParagraph`: Select Paragraph {at?: [p, c]}
- `text.set`: Set Text {id?, text, cell?: [r, c]} — replaces the whole text, keeping the first run's formatting
- `text.get`: Get Text {id?} → {text, paragraphs}

## format

- `format.bold` (Home › Font): Bold {on?: bool} [Cmd+B]
- `format.italic` (Home › Font): Italic {on?: bool} [Cmd+I]
- `format.underline` (Home › Font): Underline {on?: bool, style?: sng|dbl|heavy|dotted|dash|wavy} [Cmd+U]
- `format.strikethrough` (Home › Font): Strikethrough {on?: bool, double?: bool} [Cmd+Shift+X]
- `format.superscript` (Home › Font): Superscript {on?: bool} [Cmd+Shift+=]
- `format.subscript` (Home › Font): Subscript {on?: bool} [Cmd+=]
- `format.font` (Home › Font): Font {family}
- `format.size` (Home › Font): Font Size {size: pt}
- `format.grow` (Home › Font): Increase Font Size {} [Cmd+Shift+.]
- `format.shrink` (Home › Font): Decrease Font Size {} [Cmd+Shift+,]
- `format.color` (Home › Font): Font Color {color: #RRGGBB | accent1..6 | tx1… | {scheme, lumMod…}}
- `format.highlight` (Home › Font): Text Highlight Color {color? (absent = none)}
- `format.case` (Home › Font): Change Case {mode: sentence|lower|upper|title|toggle} [Shift+F3]
- `format.caps`: Caps {caps: none|small|all}
- `format.spacing` (Home › Font): Character Spacing {pt} (veryTight -3, tight -1.5, normal 0, loose 3, veryLoose 6)
- `format.clear` (Home › Font): Clear All Formatting {} [Cmd+Space]
- `format.textShadow` (Home › Font): Text Shadow {on?: bool}
- `format.textOutline` (Shape Format › WordArt Styles): Text Outline {color?, width?: pt} (no color = none)
- `format.align` (Home › Paragraph): Align {align: left|center|right|justify|distributed}
- `format.alignLeft` (Home › Paragraph): Align Left {} [Cmd+L]
- `format.alignCenter` (Home › Paragraph): Center {} [Cmd+E]
- `format.alignRight` (Home › Paragraph): Align Right {} [Cmd+R]
- `format.justify` (Home › Paragraph): Justify {} [Cmd+J]
- `format.bullets` (Home › Paragraph): Bullets {on?: bool, char?: •|○|■|□|◆|➢|✓|–, color?, size?: % of text}
- `format.numbering` (Home › Paragraph): Numbering {on?: bool, scheme?: arabicPeriod|arabicParenR|romanUcPeriod|romanLcPeriod|alphaUcPeriod|alphaLcParenR|alphaLcPeriod, start?: n}
- `format.indent` (Home › Paragraph): Increase List Level {} [Tab]
- `format.outdent` (Home › Paragraph): Decrease List Level {} [Shift+Tab]
- `format.lineSpacing` (Home › Paragraph): Line Spacing {lines?: 1.0|1.5|2.0…, pt?: exactly}
- `format.paragraph` (Format): Paragraph… {align?, indentLeft?: pt, indentFirst?: pt (negative = hanging), spaceBefore?: pt, spaceAfter?: pt, lineSpacing?: lines}
- `format.anchor` (Home › Paragraph): Align Text {anchor: top|middle|bottom}
- `format.direction` (Home › Paragraph): Text Direction {dir: horizontal|rotate90|rotate270|stacked}
- `format.columns` (Home › Paragraph): Columns {count, spacing?: pt}
- `format.autofit` (Format Shape › Text Box): Autofit {mode: none|shrink|resize}
- `format.wrap` (Format Shape › Text Box): Wrap Text in Shape {on: bool}
- `format.margins` (Format Shape › Text Box): Text Box Margins {left?, top?, right?, bottom?: pt}
- `format.painter` (Home › Clipboard): Format Painter {sticky?: bool} [Cmd+Shift+C]
- `format.painterApply`: Paste Formatting {ids?} [Cmd+Shift+V]
- `format.state`: Formatting State {} → the effective formatting at the selection (font, size, bold, …)

## design

- `design.theme` (Design › Themes): Themes {name} (see design.themes)
- `design.themes`: Theme Gallery {} → themes, colour schemes and font schemes
- `design.colors` (Design › Variants): Colors {name} | {colors: {accent1: #RRGGBB, …}}
- `design.fonts` (Design › Variants): Fonts {name} | {major, minor}
- `design.background` (Design › Customize): Format Background {color? | gradient? | picture?: base64 | style?: 1..12 | reset?, all?: bool (apply to all), index?}
- `design.hideBackgroundGraphics` (Format Background): Hide Background Graphics {hide?: bool}
- `design.slideSize` (Design › Customize): Slide Size {preset?: widescreen|standard|… | w, h: pt, scale?: maximize|ensureFit|none}
- `design.headerFooter` (Insert › Text): Header and Footer… {date?: bool, dateText?: fixed text, slideNumber?: bool, footer?: bool, footerText?, hideOnTitle?: bool, all?: bool (default true)}

## view

- `view.slideMaster` (View › Master Views): Slide Master {master?: index, layout?: index}
- `view.closeMaster` (Slide Master › Close): Close Master View {}

## master

- `master.insertLayout` (Slide Master › Edit Master): Insert Layout {name?}
- `master.renameLayout` (Slide Master › Edit Master): Rename Layout {name, master?, layout?}
- `master.deleteLayout` (Slide Master › Edit Master): Delete Layout {master?, layout?}
- `master.insertPlaceholder` (Slide Master › Master Layout): Insert Placeholder {kind: content|text|picture|chart|table|media, rect?: [x,y,w,h]}

## transition

- `transition.set` (Transitions › Transition to This Slide): Transition {kind: none|morph|fade|push|wipe|split|reveal|cut|randomBar|shape|uncover|cover|flash|… (transition.list), option?, duration?: ms, index?}
- `transition.options` (Transitions › Transition to This Slide): Effect Options {option, index?}
- `transition.timing` (Transitions › Timing): Timing {duration?: ms, onClick?: bool, after?: ms | null, index?}
- `transition.applyAll` (Transitions › Timing): Apply To All {}
- `transition.list`: Transition Gallery {} → [{id, label, category, duration, options}]

## animation

- `animation.set` (Animations › Animation): Animation Styles {effect: fade|fly|zoom|wipe|appear|spin|pulse|fadeOut|lines|… (animation.list), class?: entrance|emphasis|exit|path, option?, ids?} — replaces the shapes' animations
- `animation.add` (Animations › Advanced Animation): Add Animation {effect, class?, option?, start?: onClick|withPrevious|afterPrevious, duration?: ms, delay?: ms, ids?}
- `animation.remove` (Animation Pane): Remove Animation {index} | {ids?} (all of the shapes' animations)
- `animation.move` (Animations › Timing): Reorder Animation {index, to}
- `animation.timing` (Animations › Timing): Timing {index? (else selected shapes), start?: onClick|withPrevious|afterPrevious, duration?: ms, delay?: ms, repeat?: n, rewind?: bool, trigger?: shape id | null}
- `animation.options` (Animations › Animation): Effect Options {option?, textBuild?: asOne|byParagraph|byWord|byLetter, index?}
- `animation.clear`: Remove All Animations {index?: slide}
- `animation.list`: Animation Gallery {} → [{id, label, class, options}]
- `animation.get`: Animations on Slide {slide?} → [animation]

## table

- `table.insertRowAbove` (Table Layout › Rows & Columns): Insert Above {row?, id?}
- `table.insertRowBelow` (Table Layout › Rows & Columns): Insert Below {row?, id?}
- `table.insertColumnLeft` (Table Layout › Rows & Columns): Insert Left {col?, id?}
- `table.insertColumnRight` (Table Layout › Rows & Columns): Insert Right {col?, id?}
- `table.deleteRow` (Table Layout › Rows & Columns): Delete Rows {row?, id?}
- `table.deleteColumn` (Table Layout › Rows & Columns): Delete Columns {col?, id?}
- `table.merge` (Table Layout › Merge): Merge Cells {from: [r, c], to: [r, c], id?}
- `table.split` (Table Layout › Merge): Split Cells {cell: [r, c], id?}
- `table.style` (Table Design › Table Styles): Table Styles {style: medium2-accent1|light1-accent2|dark1-tx1|grid|none…, id?}
- `table.options` (Table Design › Table Style Options): Table Style Options {headerRow?, totalRow?, bandedRows?, firstColumn?, lastColumn?, bandedColumns?: bool, id?}
- `table.cellFill` (Table Design › Table Styles): Shading {color? | none?, cells?: [[r,c],…] (default: selected cells or all), id?}
- `table.distributeRows` (Table Layout › Cell Size): Distribute Rows {id?}
- `table.distributeColumns` (Table Layout › Cell Size): Distribute Columns {id?}
- `table.columnWidth` (Table Layout › Cell Size): Width {col, width: pt, id?}
- `table.rowHeight` (Table Layout › Cell Size): Height {row, height: pt, id?}
- `table.selectCells`: Select Cells {from: [r,c], to: [r,c], id?}

## comment

- `comment.add` (Review › Comments): New Comment {text, x?, y?, id?: shape} [Cmd+Alt+M]
- `comment.reply` (Comments): Reply {index, text}
- `comment.delete` (Review › Comments): Delete Comment {index? | all?: bool}
- `comment.resolve` (Comments): Resolve Thread {index, resolved?: bool}
- `comment.list`: Comments {slide?} → comments

## review

- `review.accessibility` (Review › Accessibility): Check Accessibility {} → [{slide, shape, issue}]
- `review.spelling` (Review › Proofing): Spelling {} → [{slide, shape, word}] (words not in the built-in list) [F7]

## show

- `show.fromStart` (Slide Show › Start Slide Show): Play from Start {} [Cmd+Shift+Enter]
- `show.fromCurrent` (Slide Show › Start Slide Show): Play from Current Slide {} [Cmd+Enter]
- `show.setup` (Slide Show › Set Up): Set Up Slide Show… {type?: speaker|browsed|kiosk, loop?: bool, noNarration?, noAnimation?, useTimings?, from?, to?}
- `show.customShow` (Slide Show › Start Slide Show): Custom Slide Show {name, slides: [index]} | {name, delete: true}

## document

- `document.inspect`: Inspect Presentation {} → slides with titles, layouts, shape counts; selection; size; theme

## commands

- `commands.list`: List Commands {filter?: substring} → [{id, label, params, enabled}]
