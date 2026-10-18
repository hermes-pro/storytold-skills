# DeckCraft command catalog

Generated from `deckcraft-cli commands` (DeckCraft 0.8.0): 321 commands. Run one with `run_command {command, params}`, or several with `batch`.
Grep this file for a verb (`grep -n 'table[.]' commands.md`) rather than reading it whole.
`?` = optional, `a|b` = choices, `→` = what it returns. Unknown keys in command params are ignored silently (the MCP tools themselves refuse unknown arguments), so copy names exactly.
`(Tab › Group)` is where the command sits in the desktop UI; `[keys]` is its shortcut.

Groups: `file` (19), `slide` (19), `window` (1), `edit` (12), `section` (5), `shape` (33), `insert` (18), `chart` (3), `smartArt` (13), `draw` (1), `picture` (12), `media` (9), `guide` (4), `arrange` (15), `selection` (3), `font` (4), `text` (16), `format` (46), `design` (14), `view` (4), `handout` (1), `notes` (1), `master` (6), `transition` (6), `animation` (11), `table` (21), `comment` (7), `review` (11), `show` (4), `document` (1), `commands` (1)

## file

- `file.new` (File): New Presentation {theme?: name, template?: starter name, size?: [w,h] pt, blank?: bool} [Cmd+N]
- `file.templates`: Starter Templates {} → [{name, summary, theme, slides}]
- `file.open` (File): Open… {path} [Cmd+O]
- `file.adopt`: Open {path, token?} (a presentation the host read in the background and staged with Session::stage_loaded; without one, reads path like file.open)
- `file.openBytes`: Open Data {name, data: base64}
- `file.save` (File): Save {path?, format?: deckcraft|pptx} [Cmd+S]
- `file.saveAs` (File): Save As… {path, format?} [Cmd+Shift+S]
- `file.saveTemplate` (File): Save as Template… {path}
- `file.saveBytes`: Save to Data {format?: deckcraft|pptx} → {data: base64}
- `file.export` (File): Export… {path, format?: png|jpeg|pptx|deckcraft|outline|pdf|gif (else by path), slide?: index, all?: bool, scale?: px per pt, layout?: slides|notes|handouts (pdf), perPage?: 1|2|3|4|6|9, paper?: letter|a4|legal|a3 (pdf), orientation?: portrait|landscape (pdf), dpi?, slides?: [index]|range ("1-3,5"), includeHidden?, textLayer?, frame?, width?: px 16-3840|small|medium|large|extraLarge (gif), secondsPerSlide?: 0.1-600 (gif; 5), loop?: bool (gif; true: forever)} → {path, bytes} or {files} (png, jpeg); gif adds frames, width, height, secondsPerSlide
- `file.info` (File): Info {} → {title, path, format, dirty, slides, hiddenSlides, sections, bytes?, properties}
- `file.render`: Render Slide {slide?: index, scale?, edit?: bool} → {png: base64, width, height}
- `file.close` (File): Close {} [Cmd+W]
- `file.properties` (File): Properties {title?, subject?, author?, keywords?, comments?, category?, company?} → properties
- `file.recovery.save`: Save AutoRecover Information {} → {written}
- `file.recovery.list`: Recovered Presentations {} → [{uid, path, title, saved}]
- `file.recovery.open`: Open Recovered Presentations {} → {opened: [document index]}
- `file.recovery.discard`: Discard Recovered Presentations {uid?: one entry (else all)}
- `file.revert`: Revert {}

## slide

- `slide.colorAt`: Color At {slide?: index, x, y (slide units), scale?: px per unit (2)} → {color: "RRGGBB", alpha: 0..255, x, y}: the colour drawn at a point of the slide (the Eyedropper)
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
- `slide.notes` (View): Notes {text | body: formatted notes (as in slide.inspect's notesBody), index?} (text as typed: untouched notes keep their formatting)
- `slide.rename`: Rename Slide {name, index?}
- `slide.fromOutline` (Insert › Slides From): Slides from Outline… {text, markdown?: bool (headings are slides, list items bullets)}
- `slide.reuse` (Home › Slides › New Slide): Reuse Slides… {path? | data: base64, name?, slides?: [index] (0-based, default all), keepFormatting?: bool (default false: use the destination theme), at?: index (default after the current slide)}
- `slide.inspect`: Inspect Slide {index?} → the slide's shapes with ids, kinds, boxes, text, fills, animations, transition, notes (text, and notesBody with its formatting)

## window

- `window.next` (Window): Next Window {index?} [Cmd+`]

## edit

- `edit.undo` (Edit): Undo {} [Cmd+Z]
- `edit.redo` (Edit): Redo {} [Cmd+Y]
- `edit.cut` (Home › Clipboard): Cut {scope?: slides} → {text, html?} [Cmd+X]
- `edit.copy` (Home › Clipboard): Copy {scope?: slides} → {text, html?} [Cmd+C]
- `edit.paste` (Home › Clipboard): Paste {text?: plain text to paste, html?: rich text from another app, scope?: slides} [Cmd+V]
- `edit.pasteSpecial` (Home › Clipboard): Paste Special {as: destinationTheme|keepSource|picture|text} — Use Destination Theme, Keep Source Formatting, Picture (PNG), Keep Text Only
- `edit.pasteText` (Edit): Paste and Match Formatting {text?} [Cmd+Shift+V]
- `edit.duplicate` (Edit): Duplicate {ids?} [Cmd+D]
- `edit.delete` (Edit): Delete {ids?, scope?: slides} [Delete]
- `edit.selectAll` (Edit): Select All {scope?: slides} [Cmd+A]
- `edit.deselect`: Deselect {} [Escape]
- `edit.select`: Select Objects {ids: [id], add?: bool, toggle?: bool}

## section

- `section.add` (Home › Slides › Section): Add Section {name?, at?: slide index}
- `section.rename` (Home › Slides › Section): Rename Section {index, name}
- `section.remove` (Home › Slides › Section): Remove Section {index, slides?: bool (also delete its slides)}
- `section.removeAll` (Home › Slides › Section): Remove All Sections {}
- `section.move`: Move Section {index, to}

## shape

- `shape.insert` (Insert › Illustrations): Shapes {preset: rect|roundRect|ellipse|triangle|rightArrow|star5|… (see shape.presets), rect: [x,y,w,h] pt, text?: string}
- `shape.presets`: Shape Gallery {} → [{name, label, category}]
- `shape.action` (Insert › Links): Action Settings {on?: click|hover, action: none|next|previous|first|last|lastViewed|endShow|playMedia|slide|url|customShow|program, slide?: index, url?, show?: custom show name, path?, highlight?: bool, tooltip?, ids?}
- `shape.connect`: Connect Shapes {from: shape id, to: shape id, fromSite?, toSite?: site index (default: the closest pair), id?: existing line to glue (else a new connector), preset?: straightConnector1|bentConnector3|curvedConnector3} → {id}
- `shape.freeform` (Insert › Shapes): Freeform {points: [[x, y], …] slide pt (≥ 2), closed?: bool (filled shape), smooth?: bool (curve through the points)} → {id}
- `shape.sites`: Connection Sites {id} → [[x, y]] connection sites in slide points
- `shape.move`: Move {dx?: pt (relative), dy?: pt (relative), ids?} | {x?: pt (absolute), y?: pt (absolute), ids?}
- `shape.resize` (Shape Format › Size): Size {w?: pt, h?: pt, lockAspect?: bool, ids?}
- `shape.setBounds`: Position and Size {x, y, w, h, ids?}
- `shape.rotate` (Shape Format › Arrange › Rotate): Rotation {deg?: absolute, by?: relative, ids?, gesture?: move|end}
- `shape.sizePosition` (Shape Format › Size): Size and Position… {x?, y?: pt, w?, h?: pt, rot?: deg, scaleW?, scaleH?: percent of the current size (100 = unchanged), lockAspect?: bool, ids?} — with none of those keys, opens the dialog
- `shape.flip` (Shape Format › Arrange › Rotate): Flip {axis: horizontal|vertical, ids?}
- `shape.adjust`: Adjust Shape {index, value (file units), ids?}
- `shape.change` (Shape Format › Insert Shapes › Edit Shape): Change Shape {preset, ids?}
- `shape.smoothCorners` (Shape Format › Insert Shapes › Edit Shape): Smooth Corners {smoothing: 0..100 (%), radius?: pt (default: the rounded rectangle's own), ids?} → rectangle outline with smoothed (squircle) corners
- `shape.fill` (Shape Format › Shape Styles): Shape Fill {color? | none?: true | gradient?: {stops: [[pos, color]], angle?, kind?: linear|radial} | picture?: base64 | pattern?: {preset, fg, bg} | transparency?: 0..1 | reset?: true, ids?}; pictureProps?: {tile?: bool, offsetX?, offsetY?: pt, scaleX?, scaleY?: 0..10, align?: tl|t|tr|l|ctr|r|bl|b|br, mirror?: none|x|y|xy, stretch?: [l, t, r, b] fractions, rotateWithShape?: bool} adjusts a picture fill
- `shape.line` (Shape Format › Shape Styles): Shape Outline {color?, none?, width?: pt, dash?: solid|dot|dash|lgDash|dashDot|sysDot|sysDash, cap?: flat|round|square, join?: round|bevel|miter, compound?: single|double|thickThin|thinThick|triple, head?: none|triangle|stealth|diamond|oval|arrow, tail?, headSize?: sm|med|lg, tailSize?, reset?, ids?}
- `shape.effects` (Shape Format › Shape Styles): Shape Effects {shadow?: none|outer|inner|perspective|{color, blur, dist, dir}, glow?: none|{color, radius}, softEdges?: pt, reflection?: none|tight|half|full, bevel?: none|circle|…, threeD?: {camera?: preset, rotX?, rotY?, rotZ?: deg, z?: pt, bevelTop?, bevelBottom?: none|circle|…, bevelTopW?, bevelTopH?, bevelBottomW?, bevelBottomH?, depth?, contour?: pt, material?, lighting?, reset?: true}, shadowProps?: {color?, transparency?: 0..1, blur?: pt, dist?: pt, dir?: deg}, glowProps?: {color?, transparency?, radius?: pt}, reflectionProps?: {transparency?, size?: 0..1, dist?: pt, blur?: pt}, reset?, ids?} (the *Props keys adjust the current effect, adding a default one when there is none)
- `shape.quickStyle` (Home › Drawing): Quick Styles {index: 0..41 (theme style row×accent), ids?}
- `shape.rename` (Selection Pane): Rename {name, id?}
- `shape.altText` (Shape Format › Accessibility): Alt Text {text, decorative?: bool, ids?}
- `shape.visible` (Selection Pane): Show/Hide {visible?: bool, ids?}
- `shape.lock` (Selection Pane): Lock {locked?: bool (default: toggle), ids?} (a group locks or unlocks with everything in it)
- `shape.setDefault`: Set as Default Shape {}
- `shape.merge` (Shape Format › Insert Shapes › Merge Shapes): Merge Shapes {op: union|combine|fragment|intersect|subtract, ids?: shapes in selection order (the first one's formatting is kept)} → {ids}
- `shape.editPoints` (Shape Format › Insert Shapes › Edit Shape): Edit Points {on?: bool (default: toggle), id?} — enter or leave Edit Points for one selected shape; entering turns a preset into a freeform
- `shape.points`: Points {id?} → {id, paths: [[[x, y] slide pt]], types: [[smooth|straight|corner]]} vertices of a freeform
- `shape.movePoint`: Move Point {path?: 0, index, x, y: slide pt, id?}
- `shape.addPoint`: Add Point {path?: 0, segment: index of the vertex ending it, t?: 0..1 (0.5), id?}
- `shape.pointType`: Point Type {path?: 0, index, type: smooth|straight|corner, id?} — smooth: handles in line and equal; straight: in line; corner: independent
- `shape.moveHandle`: Move Handle {path?: 0, index, side: in|out, x, y: slide pt, type?: smooth|straight|corner (default: read from the handles), id?}
- `shape.deletePoint`: Delete Point {path?: 0, index, id?}
- `shape.inspect`: Inspect Shape {id} → full shape JSON plus its effective box

## insert

- `insert.icon` (Insert › Illustrations): Icons {name: star|arrow-right|… (see insert.icons), rect?: [x,y,w,h]}
- `insert.icons`: Icon Gallery {} → [{name, label, category}]
- `insert.textBox` (Insert › Text): Text Box {rect?: [x,y,w,h], text?: string}
- `insert.picture` (Insert › Images › Pictures): Picture from File… {path? | data: base64, name?, rect?: [x,y,w,h]}
- `insert.photoAlbum` (Insert › Images): Photo Album… {pictures?: [{path?|data: base64, name?, rot?: deg, brightness?: -1..1, contrast?: -1..1} | {text}], layout?: fit|1|2|4|1title|2title|4title, frame?: none|rect|rounded|simple, captions?: bool, grayscale?: bool, theme?: name} — omit pictures to open the dialog
- `insert.photoAlbumEdit` (Insert › Images): Edit Photo Album… {album?: id, pictures?: same as insert.photoAlbum, layout?, frame?, captions?, grayscale?, theme?} — omit pictures to reopen the dialog on the current album
- `insert.table` (Insert › Tables): Table… {rows, cols, rect?}
- `insert.chart` (Insert › Illustrations): Chart… {type?: column|bar|line|pie|doughnut|area|scatter|stackedColumn|…, rect?, categories?: [..], series?: [{name, values}]}
- `insert.audio` (Insert › Media › Audio): Audio from File… {path? | data: base64, name?, rect?}
- `insert.video` (Insert › Media › Video): Video from File… {path? | data: base64, name?, rect?}
- `insert.wordArt` (Insert › Text): WordArt {text?, style?: 0..}
- `insert.slideNumber` (Insert › Text): Slide Number {}
- `insert.dateTime` (Insert › Text): Date & Time {format?: datetime1..datetime13, update?: bool, language?: en-US|en-GB|fr-FR|ja-JP|sv-SE} — no keys opens the dialog
- `insert.symbol` (Insert › Symbols): Symbol {text: character(s)}
- `insert.hyperlink` (Insert › Links): Link {url? | slide?: index, tooltip?, text?: shown when nothing is selected, highlightClick?, ids?} [Cmd+K]
- `insert.smartArt` (Insert › Illustrations): SmartArt {kind: list|process|cycle|hierarchy|pyramid|matrix, items?: [text] (leading tabs = sub-points), nodes?: [{text, level}]} → {id}
- `insert.actionButton` (Insert › Illustrations): Action Buttons {kind: back|forward|beginning|end|home|information|return|movie|document|sound|help|custom, rect?}
- `insert.zoom` (Insert › Links): Zoom {kind?: slide|section|summary (default slide); slides?: [index] (slide and summary zooms); sections?: [index] (section zoom); returnToZoom?: bool (default: on for section and summary, off for slide)}

## chart

- `chart.type` (Chart Design › Type): Change Chart Type {type, id?}
- `chart.data` (Chart Design › Data): Edit Data {categories?: [..], levels?: [[..]] (outer category levels, innermost first), series?: [{name, values}], id?}
- `chart.options` (Chart Design › Chart Layouts): Chart Elements {title?: string|null, legend?: b|t|l|r|null, dataLabels?: bool, gridlines?: bool, palette?, binCount?: n|null, binSize?: n|null, subtotals?: [point index], quartiles?: exclusive|inclusive, upDownBars?: bool, id?}

## smartArt

- `smartArt.nodes` (SmartArt Design › Create Graphic): Text Pane {id?} → {id, kind, nodes: [{text, level}]} (id: the SmartArt group or one of its shapes; default the selection)
- `smartArt.setNodes` (SmartArt Design › Create Graphic): Edit SmartArt Text {id?, nodes?: [{text, level}], lines?: [string] (leading tabs set the level), index?, text?, title?} (index + text edits one node; title: its Name and Title box)
- `smartArt.addNode` (SmartArt Design › Create Graphic): Add Shape {id?, index?, position?: after|before|below|above|assistant, text?} → {index} (default: after the last node)
- `smartArt.removeNode` (SmartArt Design › Create Graphic): Remove Shape {id?, index} (its sub-points move up one level)
- `smartArt.promote` (SmartArt Design › Create Graphic): Promote {id?, index}
- `smartArt.demote` (SmartArt Design › Create Graphic): Demote {id?, index}
- `smartArt.layout` (SmartArt Design › Layouts): Change Layout {id?, kind: list|blockList|hBulletList|process|chevron|verticalProcess|stepUp|cycle|blockCycle|radial|hierarchy|pyramid|invertedPyramid|matrix|titledMatrix|pictureList|pictureCaption|pictureProcess|pictureHList|timeline|venn|target|textCycle|continuousCycle|horizontalHierarchy|gridMatrix|gear|funnel|segmentedCycle|multidirectionalCycle|orgChart|halfCircleOrgChart|cycleMatrix|segmentedPyramid|pie|nameTitleOrgChart|verticalBoxList|trapezoidList|tableList|accentProcess|continuousBlockProcess|bendingProcess|linearVenn|stackedVenn|nestedTarget}
- `smartArt.fromText` (Home › Paragraph): Convert to SmartArt {id?, kind?} → {id} (a text box or placeholder becomes a SmartArt graphic in its place: one node per paragraph, indent levels kept)
- `smartArt.toText` (SmartArt Design › Reset): Convert to Text {id?} → {id} (the graphic becomes a text box of its outline, bulleted by level)
- `smartArt.toShapes` (SmartArt Design › Reset): Convert to Shapes {id?} (the graphic becomes a plain group of its shapes; the outline is dropped)
- `smartArt.picture` (SmartArt Design › Create Graphic): Insert Picture in SmartArt {id?, index, data?: base64 | path?: string | reset?: bool} (the node's picture placeholder in picture layouts)
- `smartArt.style` (SmartArt Design › SmartArt Styles): SmartArt Styles {id?, style: flat|subtle|intense|outline|polished|inset|cartoon|powder|brick}
- `smartArt.colors` (SmartArt Design › SmartArt Styles): Change Colors {id?, colors: colorful|range23|range34|range45|range56|accent1|…|accent6|accent1Grad|…|accent6Grad}

## draw

- `draw.inkToShape` (Draw › Convert): Ink to Shape {} → {shapes: [ids], kept: n} turns recognisable ink strokes on the slide into lines, rectangles, ellipses and triangles

## picture

- `picture.crop` (Picture Format › Size): Crop {left?: fraction 0..1, top?: fraction 0..1, right?: fraction 0..1, bottom?: fraction 0..1, ids?}
- `picture.adjust` (Picture Format › Adjust): Corrections {brightness?: -1..1, contrast?: -1..1, saturation?: 0..4, grayscale?: bool, transparency?: 0..1, reset?: bool, ids?}
- `picture.reset` (Picture Format › Adjust): Reset Picture {ids?}
- `picture.change` (Picture Format › Adjust): Change Picture {path? | data: base64, name?, ids?}
- `picture.removeBackground` (Picture Format › Adjust): Remove Background {tolerance?: 0..100 (how different a colour may be from the edge's, default 20), ids?}
- `picture.style` (Picture Format › Picture Styles): Picture Styles {style: simpleFrameWhite|dropShadowRectangle|softEdgeOval|… | none (see picture.styles), ids?}
- `picture.styles`: Picture Style Gallery {} → [{id, label}]
- `picture.recolor` (Picture Format › Adjust › Color): Recolor {preset: none|grayscale|sepia|washout|bw25|bw50|bw75|accent1Dark…accent6Dark|accent1Light…accent6Light|tx2Dark|tx2Light (see picture.recolors), ids?}
- `picture.recolors`: Recolor Gallery {} → [{id, label}]
- `picture.transparentColor` (Picture Format › Adjust › Color): Set Transparent Color {color: #RRGGBB | none: true, ids?} (pixels of that colour become transparent)
- `picture.artisticEffect` (Picture Format › Adjust): Artistic Effects {effect: none|artisticBlur|artisticPencilGrayscale|artisticLineDrawing|artisticFilmGrain|artisticCutout|artisticGlowEdges|artisticPhotocopy, ids?}
- `picture.compress` (Picture Format › Adjust): Compress Pictures {ppi?: 330|220|150|96 (default 220), deleteCropped?: bool (default true), all?: bool (every picture in the presentation; default the selected pictures), ids?} → {pictures, before, after}

## media

- `media.options` (Playback): Playback {autoplay?, loop?, rewind?, acrossSlides?, hide?, fullScreen?, volume?: 0..1, trimStart?: ms, trimEnd?: ms, fadeIn?: ms, fadeOut?: ms, ids?}
- `media.play` (Playback › Preview): Play {id?, from?: ms} [Alt+P]
- `media.pause` (Playback › Preview): Pause {id?}
- `media.toggle`: Play/Pause {id?}
- `media.stop` (Playback › Preview): Stop {id?}
- `media.seek`: Seek {id?, ms}
- `media.info`: Media Info {id?} → {id, name, contentType, bytes, durationMs, video, width, height, probe: {container, audio?, video?}, options, status?}
- `media.posterFrame` (Video Format › Adjust): Poster Frame {id?, ms?: frame time (default: current position)}
- `media.gifPlay`: Play/Pause GIF {id?, play?: bool (default: toggle)} → {id, playing}

## guide

- `guide.add` (View › Show › Guides): Add Guide {vertical: bool, pos?: pt (default: the slide's centre)} → {index}. `defaults: true` adds the two centre guides when there are none
- `guide.move`: Move Guide {index, pos: pt}
- `guide.delete`: Delete Guide {index}
- `guide.list`: Guides {} → [{vertical, pos}]

## arrange

- `arrange.bringToFront` (Arrange): Bring to Front {ids?} [Cmd+Shift+]]
- `arrange.bringForward` (Arrange): Bring Forward {ids?} [Cmd+]]
- `arrange.sendBackward` (Arrange): Send Backward {ids?} [Cmd+[]
- `arrange.sendToBack` (Arrange): Send to Back {ids?} [Cmd+Shift+[]
- `arrange.reorder` (Arrange): Reorder Objects {id, index: position among its siblings (0 = back; a group's child stays in its group)} → {index}
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

## selection

- `selection.select` (Selection Pane): Select {ids | id, toggle?: bool (Ctrl+click), add?: bool} → {selected}: objects in groups too; a hidden object picked from the list is shown
- `selection.showAll` (Selection Pane): Show All {} shows every object on the slide, inside groups too
- `selection.hideAll` (Selection Pane): Hide All {} hides every top-level object on the slide

## font

- `font.used`: Fonts in Presentation {} → [family] (theme fonts resolved)
- `font.replace` (Home › Editing › Replace): Replace Fonts {from, to} — every explicit use of family `from`, theme fonts included → {replaced}
- `font.add`: Add Font {data: base64 TTF/OTF/TTC} → {faces} added for this session
- `font.rescan` (Home › Font): Rescan Installed Fonts {} → {faces, families} (fonts installed since start-up)

## text

- `text.edit`: Edit Text {id?, at?: [paragraph, char], end?: bool, cell?: [row, col], notes?: bool} [Enter]
- `text.exit`: Stop Editing Text {}
- `text.autocorrect` (Tools): AutoCorrect Options {on?, twoInitials?, sentenceCaps?, days?, capsLock?, fractions?: bool, add?: [from, to], remove?: from} → the options and the replacement list
- `text.insert`: Type Text {text} (\n = new paragraph, \u000b = line break)
- `text.compose`: Compose Text {text, active?: [start, end]} — an input method's composition (preedit) at the insertion point; empty text cancels it
- `text.commit`: Commit Composition {text} — the input method's result replaces its composition, as one undo step
- `text.delete`: Delete Text {dir?: backward|forward|wordBackward|wordForward} — the word directions are Ctrl+Backspace/Delete: they work from the start of a selection without deleting it [Backspace]
- `text.move`: Move Insertion Point {to: left|right|up|down|wordLeft|wordRight|lineStart|lineEnd|paraStart|paraEnd|paraUp|paraDown|start|end, extend?: bool} — left/right are on screen: in a right-to-left paragraph left goes forward
- `text.select`: Select Text {anchor: [p, c], caret: [p, c]}
- `text.selectAll`: Select All Text {}
- `text.selectWord`: Select Word {at?: [p, c]}
- `text.selectParagraph`: Select Paragraph {at?: [p, c]}
- `text.set`: Set Text {id?, text, cell?: [r, c]} — replaces the whole text, keeping the first run's formatting
- `text.get`: Get Text {id?} → {text, paragraphs}
- `text.find` (Home › Editing): Find {text, matchCase?: bool, wholeWords?: bool} → [{slide, shape (null = notes), cell?: [row, col], para, start, end}] (char offsets in the paragraph)
- `text.replace` (Home › Editing): Replace {text, with, matchCase?, wholeWords?, at?: a text.find match (replace just that one; default: replace all)} → {replaced}

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
- `format.color` (Home › Font): Font Color {color: #RRGGBB|accent1..6|tx1…|{scheme, lumMod…}}
- `format.textTransparency` (Shape Format › WordArt Styles): Text Transparency {value: 0..1} — 0 opaque, 1 invisible; keeps the text's colour (inherited colours included)
- `format.language` (Review › Language): Language {lang?, noProof?: bool} (proofing language of the selected text, and Do Not Check Spelling)
- `format.highlight` (Home › Font): Text Highlight Color {color? (absent = none)}
- `format.case` (Home › Font): Change Case {mode?: cycle|sentence|lower|upper|title|toggle} — cycle (Shift+F3, the default) goes lowercase → Capitalize Each Word → UPPERCASE; a caret in a word changes that word [Shift+F3]
- `format.caps`: Caps {caps: none|small|all}
- `format.spacing` (Home › Font): Character Spacing {pt} (veryTight -3, tight -1.5, normal 0, loose 3, veryLoose 6)
- `format.clear` (Home › Font): Clear All Formatting {} [Cmd+Space]
- `format.fontDialog` (Home › Font): Font… {family?, size?: pt, bold?: bool, italic?: bool, underline?: none|sng|dbl|heavy|dotted|dash|wavy, color?, strike?: none|sng|dbl, baseline?: none|super|sub|<fraction>, caps?: none|small|all, spacing?: pt} — with none of these, opens the Font dialog [Cmd+T]
- `format.textShadow` (Home › Font): Text Shadow {on?: bool}
- `format.textOutline` (Shape Format › WordArt Styles): Text Outline {color?, width?: pt} (no color = none)
- `format.textWarp` (Shape Format › WordArt Styles): Text Transform {preset: a prstTxWarp name or none, adj?: [finite raw guide values, at most 8]} — none clears the transform; omitted adj uses the preset's defaults
- `format.align` (Home › Paragraph): Align {align: left|center|right|justify|justifyLow|distributed}
- `format.rtl` (Home › Paragraph): Right-to-Left Text Direction {on?: bool} (off = left-to-right; switching mirrors left/right alignment)
- `format.alignLeft` (Home › Paragraph): Align Left {} [Cmd+L]
- `format.alignCenter` (Home › Paragraph): Center {} [Cmd+E]
- `format.alignRight` (Home › Paragraph): Align Right {} [Cmd+R]
- `format.justify` (Home › Paragraph): Justify {} [Cmd+J]
- `format.bullets` (Home › Paragraph): Bullets {on?: bool, char?: •|○|■|□|◆|➢|✓|–, color?, size?: % of text}
- `format.numbering` (Home › Paragraph): Numbering {on?: bool, scheme?: arabicPeriod|arabicParenR|romanUcPeriod|romanLcPeriod|alphaUcPeriod|alphaLcParenR|alphaLcPeriod, start?: n, color?, size?: % of text}
- `format.indent` (Home › Paragraph): Increase List Level {} [Tab]
- `format.outdent` (Home › Paragraph): Decrease List Level {} [Shift+Tab]
- `format.lineSpacing` (Home › Paragraph): Line Spacing {lines?: 1.0|1.5|2.0…, pt?: exactly}
- `format.paragraph` (Format): Paragraph… {align?, indentLeft?: pt, indentFirst?: pt (negative = hanging), spaceBefore?: pt, spaceAfter?: pt, lineSpacing?: lines}
- `format.ruler`: Ruler {} → {x, y, width, rotated, marginLeft, indent, tabs: [{pos, align}], defaultTab} for the paragraph with the caret (x, y: the text area's top-left in slide pt)
- `format.paragraphDialog` (Home › Paragraph): Paragraph… {align?: left|center|right|justify|justLow|distributed, indentLeft?: pt, indentRight?: pt, special?: none|first|hanging, specialBy?: pt, indentFirst?: pt, spaceBefore?: pt, spaceAfter?: pt, spaceBeforeKind?: pts|pct, spaceAfterKind?: pts|pct, lineSpacing?: lines, lineSpacingPt?: pt} — with none of these, opens the Paragraph dialog
- `format.tabs` (Home › Paragraph): Tabs… {set?: [{pos, align?}] (replaces all), add?: {pos, align?: l|ctr|r|dec}, move?: {from, to}, remove?: pos, clear?: bool, defaultTab?: pt} on the selected paragraphs; with none of them, opens the Tabs dialog (pos in pt from the text area's left)
- `format.anchor` (Home › Paragraph): Align Text {anchor: top|middle|bottom}
- `format.direction` (Home › Paragraph): Text Direction {dir: horizontal|rotate90|rotate270|stacked}
- `format.columns` (Home › Paragraph): Columns {count, spacing?: pt}
- `format.autofit` (Format Shape › Text Box): Autofit {mode: none|shrink|resize}
- `format.wrap` (Format Shape › Text Box): Wrap Text in Shape {on: bool}
- `format.margins` (Format Shape › Text Box): Text Box Margins {left?: pt, top?: pt, right?: pt, bottom?: pt}
- `format.painter` (Home › Clipboard): Format Painter {sticky?: bool} [Cmd+Shift+C]
- `format.painterApply`: Paste Formatting {ids?} [Cmd+Shift+V]
- `format.state`: Formatting State {} → the effective formatting at the selection (font, size, bold, …)

## design

- `design.theme` (Design › Themes): Themes {name} (see design.themes)
- `design.browseTheme` (Design › Themes): Browse for Themes… {path} | {name, data: base64} — apply the theme of a .thmx, .pptx or .potx file
- `design.themes`: Theme Gallery {} → themes, colour schemes, font schemes and effect schemes
- `design.colors` (Design › Variants): Colors {} opens Create New Theme Colors | {name} | {colors: {dk1|lt1|dk2|lt2|accent1..6|hlink|folHlink: #RRGGBB}}
- `design.variant` (Design › Variants): Variants {index: 0..3} (see design.variants)
- `design.variants`: Variant Gallery {} → the current theme's four colour variants and which is applied
- `design.fonts` (Design › Variants): Fonts {} opens Create New Theme Fonts | {name} | {major, minor}
- `design.effects` (Design › Variants): Effects {name} (see design.themes)
- `design.background` (Design › Customize): Format Background {color? | gradient? | picture?: base64 | pattern? | style?: 1..12 | reset?, all?: bool, index?, transparency?: 0..1, pictureProps?: {tile?, offsetX?, offsetY?: pt, scaleX?, scaleY?: 0.01..10, align?, mirror?, stretch?: [l,t,r,b], rotateWithShape?}, copy?: bool}
- `design.hideBackgroundGraphics` (Format Background): Hide Background Graphics {hide?: bool}
- `design.slideSize` (Design › Customize): Slide Size {preset: widescreen|standard|…, orientation?: portrait|landscape, scale?: maximize|ensureFit|none} | {w: pt, h: pt, orientation?: portrait|landscape, scale?: maximize|ensureFit|none}
- `design.headerFooter` (Insert › Text): Header and Footer… {date?: bool, dateText?: fixed text, slideNumber?: bool, footer?: bool, footerText?, hideOnTitle?: bool, all?: bool (default true)}
- `design.ideas`: Design Ideas {slide?} → [{id, label}] ideas for the slide
- `design.applyIdea` (Home › Designer): Apply Design Idea {id, slide?}

## view

- `view.slideMaster` (View › Master Views): Slide Master {master?: index, layout?: index}
- `view.handoutMaster` (View › Master Views): Handout Master {} (creates the handout master with header, date, footer and page number if the deck has none)
- `view.notesMaster` (View › Master Views): Notes Master {} (creates the notes master with header, date, slide image, notes body, footer and page number if the deck has none)
- `view.closeMaster` (Slide Master › Close): Close Master View {}

## handout

- `handout.placeholders` (Handout Master › Placeholders): Handout Placeholders {header?: bool, date?: bool, footer?: bool, pageNumber?: bool} (show or hide each)

## notes

- `notes.placeholders` (Notes Master › Placeholders): Notes Placeholders {header?, date?, slideImage?, body?, footer?, pageNumber?: bool} (show or hide each)

## master

- `master.insertLayout` (Slide Master › Edit Master): Insert Layout {name?}
- `master.renameLayout` (Slide Master › Edit Master): Rename Layout {name, master?, layout?}
- `master.deleteLayout` (Slide Master › Edit Master): Delete Layout {master?, layout?}
- `master.insertPlaceholder` (Slide Master › Master Layout): Insert Placeholder {kind: content|text|picture|chart|table|media, rect?: [x,y,w,h]}
- `master.preserve` (Slide Master › Edit Master): Preserve {preserve?: bool}
- `master.placeholders` (Slide Master › Edit Master): Layout Placeholders {title?: bool, footers?: bool}

## transition

- `transition.set` (Transitions › Transition to This Slide): Transition {kind: none|morph|fade|push|wipe|split|reveal|cut|randomBar|shape|uncover|cover|flash|… (transition.list), option?, duration?: ms, index?}
- `transition.options` (Transitions › Transition to This Slide): Effect Options {option, index?}
- `transition.timing` (Transitions › Timing): Timing {duration?: ms, onClick?: bool, after?: ms | null, index?}
- `transition.sound` (Transitions › Timing): Sound {builtin?: chime|click|camera|whoosh|drumRoll|laser | path? | data: base64, name?, none?: true (No Sound), stopPrevious?: true, loop?: bool (Loop Until Next Sound), index?} — the sound plays as the slide comes in
- `transition.applyAll` (Transitions › Timing): Apply To All {}
- `transition.list`: Transition Gallery {} → [{id, label, category, duration, options}]

## animation

- `animation.set` (Animations › Animation): Animation Styles {effect: fade|fly|zoom|wipe|appear|spin|pulse|fadeOut|lines|… (animation.list), class?: entrance|emphasis|exit|path, option?, ids?} — replaces the shapes' animations
- `animation.add` (Animations › Advanced Animation): Add Animation {effect, class?, option?, start?: onClick|withPrevious|afterPrevious, duration?: ms, delay?: ms, ids?}
- `animation.remove` (Animation Pane): Remove Animation {index} | {ids? (all of the shapes' animations)}
- `animation.move` (Animations › Timing): Reorder Animation {index, to}
- `animation.timing` (Animations › Timing): Timing {index? (else selected shapes), start?: onClick|withPrevious|afterPrevious, duration?: ms, delay?: ms, repeat?: n, rewind?: bool, trigger?: shape id | null}
- `animation.options` (Animations › Animation): Effect Options {option?, textBuild?: asOne|byParagraph|byWord|byLetter, index?}
- `animation.clear`: Remove All Animations {index?: slide}
- `animation.painter` (Animations › Advanced Animation): Animation Painter {sticky?: bool, id?} [Alt+Shift+C]
- `animation.painterApply`: Apply Animation {ids?} [Alt+Shift+V]
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
- `table.split` (Table Layout › Merge): Split Cells {cell?: [r, c] (else the edited cell), id?} | {row?: index, col?: index, id?}
- `table.style` (Table Design › Table Styles): Table Styles {style: medium2-accent1|light1-accent2|dark1-tx1|grid|none…, id?}
- `table.options` (Table Design › Table Style Options): Table Style Options {headerRow?: bool, totalRow?: bool, bandedRows?: bool, firstColumn?: bool, lastColumn?: bool, bandedColumns?: bool, id?}
- `table.cellFill` (Table Design › Table Styles): Shading {color? | none?, cells?: [[r,c],…] (default: selected cells or all), id?}
- `table.borders` (Table Design › Draw Borders): Borders {which: all|outside|inside|insideH|insideV|top|bottom|left|right|diagDown|diagUp|none, color?, width?: pt, dash?: solid|dash|dot…, cells?: [[r,c],…] (default: selected cells or all), id?}
- `table.cellMargins` (Table Layout › Alignment): Cell Margins {preset?: normal|none|narrow|wide, left?, right?, top?, bottom?: pt, cells?, id?}
- `table.cellAlign` (Table Layout › Alignment): Align Cell Text {anchor: top|middle|bottom, cells?, id?}
- `table.distributeRows` (Table Layout › Cell Size): Distribute Rows {id?}
- `table.distributeColumns` (Table Layout › Cell Size): Distribute Columns {id?}
- `table.columnWidth` (Table Layout › Cell Size): Width {col, width: pt, keepTotal?: bool (the next column absorbs the change), id?}
- `table.rowHeight` (Table Layout › Cell Size): Height {row, height: pt, id?}
- `table.drawLine` (Table Design › Draw Borders): Draw Table {from: [x, y], to: [x, y] slide pt, id?: table (default: the one under `from`)} splits the cells the line crosses
- `table.eraseLine` (Table Design › Draw Borders): Table Eraser {at: [x, y] slide pt, id?, tol?: pt (default 6)} merges the two cells on either side of the nearest border
- `table.selectCells`: Select Cells {from: [r,c], to: [r,c], id?}

## comment

- `comment.add` (Review › Comments): New Comment {text, x?, y?, id?: shape} [Cmd+Alt+M]
- `comment.reply` (Comments): Reply {index, text}
- `comment.delete` (Review › Comments): Delete Comment {index? | all?: bool}
- `comment.resolve` (Comments): Resolve Thread {index, resolved?: bool}
- `comment.list`: Comments {slide?} → comments
- `comment.next` (Review › Comments): Next Comment {slide?, index?} → {slide, index, text}
- `comment.prev` (Review › Comments): Previous Comment {slide?, index?} → {slide, index, text}

## review

- `review.accessibility` (Review › Accessibility): Check Accessibility {} → [{slide, shape, issue}]
- `review.spelling` (Review › Proofing): Spelling {lang?, ignore?:[word]} → [{slide, shape?, row?, col?, notes?, para, start, end, word, lang, suggestions}] (shapes, table cells and notes; repeated words as {repeated, deleteFrom}; runs marked noProof skipped; each run in its own language, lang? for runs without one; Hunspell dictionaries installed on the system, else a built-in list of common misspellings) [F7]
- `review.spellingChange` (Review › Proofing): Change Spelling {shape, word, to, all?, para?, start?, row?, col?} → {changed} (replace the whole word in that shape's text, the one at para/start, or in every shape with all)
- `review.addToDictionary` (Review › Proofing): Add to Dictionary {word} → {word, file} (append to the user dictionary file; not an undo step)
- `review.dictionary` (Review › Proofing): Spelling Dictionary {lang?} → {lang, available, found, folders} (whether review.spelling has a dictionary, and which file)
- `review.thesaurus` (Review › Proofing): Thesaurus {word? (default: the selected word, or the word at the caret)} → {word, senses: [{word, synonyms}]}
- `review.replaceWord`: Insert Synonym {with}: replace the selected word (or the word at the caret) while editing text
- `review.compare` (Review › Compare): Compare {path} | {name, data: base64} — compare with a revised copy → {name, changes}
- `review.revisions`: Revisions {} → {name, changes: [{kind: inserted|deleted|changed, slide, revised, details}]}
- `review.accept` (Review › Compare): Accept Revision {index} | {all: true}
- `review.endCompare` (Review › Compare): End Review {}

## show

- `show.fromStart` (Slide Show › Start Slide Show): Play from Start {} [Cmd+Shift+Enter]
- `show.fromCurrent` (Slide Show › Start Slide Show): Play from Current Slide {} [Cmd+Enter]
- `show.setup` (Slide Show › Set Up): Set Up Slide Show… {type?: speaker|browsed|kiosk, loop?: bool, noNarration?, noAnimation?, useTimings?, showMediaControls?, from?, to?, custom?: name}
- `show.customShow` (Slide Show › Start Slide Show): Custom Slide Show {name, slides: [index]} | {name, delete: true}

## document

- `document.inspect`: Inspect Presentation {} → slides with titles, layouts, shape counts; selection; size; theme

## commands

- `commands.list`: List Commands {filter?: substring} → [{id, label, params, enabled}]
