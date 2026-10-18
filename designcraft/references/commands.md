# DesignCraft command catalog

Generated from `designcraft-cli commands` (DesignCraft 0.9.0, 519 commands). Run any of these with
`execute {command, params}` or several with `batch {commands: [...]}`; check one live with `list_commands {filter}`
or `designcraft-cli describe <id>`. `params` use the engine's shorthand: `?` = optional, `a|b` = choices,
`→ {...}` = what it returns. Coordinates are spread points (y down); `page` params say whether they are 0- or 1-based.
Grep this file rather than reading it whole.

## anchor

- `anchor.create` (Type › Hyperlinks & Cross-References › New Hyperlink Destination…): {name} — a text anchor at the insertion point
- `anchor.list` (Text Anchors): {} → [{id, name, story, pos, page}]

## anchored

- `anchored.insert` (Object › Anchored Object › Insert Anchored Object…): {ids, story?, pos? (default: the text insertion point), position?: inline\|aboveLine\|custom, yOffset?, align?: left\|center\|right, spaceBefore?, spaceAfter?, xRelative? \| yRelative?: anchor\|textFrame\|columnEdge\|pageMargin\|pageEdge, xOffset?, objectPoint? \| refPoint?: 0..8, keepWithinColumn?} — moves the items into the text
- `anchored.options` (Object › Anchored Object › Anchored Object Options…): {story?, index? (default: the object at the insertion point), position?: inline\|aboveLine\|custom, yOffset?, align?: left\|center\|right, spaceBefore?, spaceAfter?, xRelative? \| yRelative?: anchor\|textFrame\|columnEdge\|pageMargin\|pageEdge, xOffset?, objectPoint? \| refPoint?: 0..8, keepWithinColumn?}
- `anchored.release` (Object › Anchored Object › Release): {story?, index? (default: the object at the insertion point)} — puts the object back on the page where it is now and removes it from the text
- `anchored.list` (Anchored Objects): {story?} → [{story, index, pos, position, size}]

## app

- `app.links` (Community & Project Links): {} → {discord, website, appPage, github, issues} (ArtCraft Discord, website, DesignCraft page and repository)

## article

- `article.list` (Articles): {} → [{name, items, export}]
- `article.new` (Window › Articles › New Article): {name?, ids? (default: the selection)} → {name}
- `article.add` (Add Selection to Article): {name, ids? (default: the selection)} — appended in order
- `article.remove` (Remove from Article): {name, ids}
- `article.options` (Article Options): {name, to?: new name, export?: bool, order?: [ids] (reorder)}
- `article.delete` (Delete Article): {name}

## book

- `book.new` (File › New › New Book): {path} — an empty book file (.dcbook)
- `book.open` (Open Book): {path} → {documents}
- `book.close` (Close Book): {}
- `book.add` (Add Document): {path, at?: index}
- `book.remove` (Remove Document): {index}
- `book.styleSource` (Style Source): {index}
- `book.list` (Book): {} → {path, styleSource, documents: [{path, pages, firstPage}]}
- `book.paginate` (Update Numbering): {} — each document starts numbering where the previous one ended, and takes its chapter number (automatic: one more than the previous document's; same as previous; or its own start) (files are saved) → {pages, chapters}
- `book.syncStyles` (Synchronize Book): {} — paragraph and character styles and swatches of the style source go into every document (by name)
- `book.exportPdf` (Export Book to PDF…): {path?} — every document in order as one PDF → {path, bytes, pages} (no path: {base64, …})

## bookmark

- `bookmark.rename` (Rename Bookmark): {index, name}
- `bookmark.add` (New Bookmark): {name?, page? (1-based; default: current selection's page or 1)}
- `bookmark.delete` (Delete Bookmark): {index}
- `bookmark.list` (Bookmarks): {}

## button

- `button.set` (Object › Interactive › Convert to Button): {ids?, action: page\|firstPage\|lastPage\|nextPage\|previousPage\|url\|none, page?, url?} — the selected objects act on release in interactive PDF
- `button.clear` (Object › Interactive › Convert to Object): {ids?}
- `button.list` (Buttons): {} → [{id, name, action}]

## changes

- `changes.track` (Type › Track Changes › Track Changes): {on?: bool (default: toggle)}
- `changes.list` (Changes): {} → [{story, start, end, kind: inserted\|deleted, text}]
- `changes.accept` (Accept Change): {story, start} — the change at that position
- `changes.reject` (Reject Change): {story, start} — the change at that position
- `changes.acceptAll` (Type › Track Changes › Accept All Changes): {story?} — deleted text goes, added text stays
- `changes.rejectAll` (Type › Track Changes › Reject All Changes): {story?} — added text goes, deleted text comes back

## color

- `color.settings` (Color Settings): {rgb?: working RGB profile, cmyk?: working CMYK profile, intent?: perceptual\|relative\|saturation\|absolute, bpc?: bool} → {rgb, cmyk, intent, bpc, profiles}
- `color.loadProfile` (Load Profile…): {path} — an ICC profile (.icc/.icm) to use as a working space or proof target
- `color.convert` (Convert Color): {color: {model: rgb, r, g, b} \| {model: cmyk, c, m, y, k} \| {model: gray, k}, to: rgb\|cmyk\|gray\|lab} — through the working spaces
- `color.extractTheme` (Extract Color Theme): {id?: selected image frame} → {from, colors: [up to five RGB hex colours]} — samples the source raster, ignoring transparent pixels; at most 16 million pixels
- `color.sample` (Sample Color (Eyedropper)): {at: [x,y] (spread coords), spread?, target?: fill\|stroke, ids?, matchFrom?: id} → {color: "#rrggbb", swatch, from: image id} — the Eyedropper on a placed image: the image's colour at the point (an unnamed colour) fills the selected text, else the selected objects. With no opaque image pixel there, `matchFrom` gives the object whose attributes apply instead (object.matchAttributes)

## condition

- `condition.list` (Conditions): {} → [{name, color, visible}]
- `condition.new` (Window › Type & Tables › Conditional Text › New Condition…): {name, color?: [r, g, b], visible?} → {name}
- `condition.options` (Condition Options…): {name, to?: new name, color?: [r, g, b], visible?: bool}
- `condition.delete` (Delete Condition): {name} — the text it was applied to stays (shown)
- `condition.apply` (Apply Condition): {name, on?: bool (default true), only?: bool (remove the others)} — to the selected text; `name: null` with `only` removes all

## conveyor

- `conveyor.collect` (Collect): {ids? (default: the selection)} — each object onto the Content Collector conveyor → {count}
- `conveyor.place` (Place): {index? (0), spread?, x?, y?, keep?: bool (stay on the conveyor)} — the Content Placer: the collected object at x/y (top-left)
- `conveyor.list` (Conveyor): {} → [name]
- `conveyor.clear` (Clear Conveyor): {}

## data

- `data.source.select` (Select Data Source…): {path \| bytes\|base64, name, delimiter?: comma\|tab\|semicolon, sheet?} → {fields, records, warnings}
- `data.source.update` (Update Data Source): {} → re-read the linked file
- `data.source.remove` (Remove Data Source): {} → drop the source; placeholders stay
- `data.fields` (Data Fields): {csv? \| rows? \| path? \| bytes? \| base64?, name?, delimiter?, sheet?} → [{name, kind, uses}]; no params reads the linked source and does not attach one
- `data.placeholder.add` (Insert Field): {field, role?: text\|image\|qr\|hyperlink, story?, at?, end?, item?} → {id}
- `data.placeholder.remove` (Remove Field): {id}
- `data.options` (Data Merge Options): {records?, one?, range?, perPage?, arrange?, insets?, columnSpacing?, rowSpacing?, fitting?, center?, linkImages?, limit?}
- `data.preview` (Preview Record): {record?: n} → fill the template with that record (session only)
- `data.preview.stop` (Stop Preview): {} → restore the unfilled template
- `data.merge` (Create Merged Document…): {csv? \| rows? \| path? \| bytes? \| base64?, name?, delimiter?, sheet?, records?, one?, range?, perPage?, arrange?, insets?, columnSpacing?, rowSpacing?, fitting?, center?, linkImages?, limit?, spread?: removed (passing it is an error)} → {records, pages, missingImages, oversetStories, warnings}

## document

- `document.preferences` (Document Preferences): {horizontalUnits?, verticalUnits?: points\|picas\|inches\|millimeters\|…, keyboardIncrement? (pt), kerningIncrement? (1/1000 em: Alt+Left/Right in text), baselineGrid?: {start, increment, relativeTo, color, viewThreshold}, grid?: {horizontal, vertical, subdivisions, color, inBack}, pasteboard?: [h, v], marginColor?, columnColor?, bleedColor?, slugColor?: [r, g, b], advancedType?: {superscriptSize, superscriptPosition, subscriptSize, subscriptPosition} (%), overprintBlack?, glyphFallback? (draw characters the font lacks from fallback fonts; off: as the font's missing-glyph box), rulerOrigin?: spread\|page\|spine (what rulers and X/Y measure from, with the zero point)} → those settings
- `document.inspect` (Inspect Document): {} → pages, spreads, items, stories (with overset), styles, swatches, selection
- `document.list` (List Documents): {}
- `document.history` (History): {}

## edit

- `edit.undo` (Edit › Undo, Cmd+Z): {}
- `edit.redo` (Edit › Redo, Cmd+Shift+Z): {}
- `edit.selectAll` (Edit › Select All, Cmd+A): {} — all items on the active spreads, or all text in the story
- `edit.deselectAll` (Edit › Deselect All, Cmd+Shift+A): {}
- `edit.clear` (Edit › Clear, Delete): {ids?} — delete selected items (or the selected text)
- `edit.copy` (Edit › Copy, Cmd+C): {} → {text} when text is selected (with formatting, footnotes, markers)
- `edit.cut` (Edit › Cut, Cmd+X): {}
- `edit.pasteWithoutFormatting` (Edit › Paste without Formatting, Cmd+Shift+V): {text?} — plain text at the insertion point, in the format there
- `edit.paste` (Edit › Paste, Cmd+V): {inPlace?: bool, spread?: index (0), text?: the system clipboard's text (pastes it unless it is what was copied here; with no insertion point it becomes a new text frame), at?: [x, y] (spread coords: the new text frame's centre)}
- `edit.pasteInto` (Edit › Paste Into, Cmd+Alt+V): {id?} — the copied objects become the content of the selected frame (or `id`), clipped by it
- `edit.pasteInPlace` (Edit › Paste in Place, Cmd+Alt+Shift+V): {spread?: index (0)}
- `edit.duplicate` (Edit › Duplicate, Cmd+Alt+Shift+D): {}
- `edit.preview` (Preview Change): {label, command, params?} — run `command` on the document as it was before the preview began, replacing the last preview; the first call opens a preview named `label` (the undo step's name)
- `edit.commitPreview` (Commit Preview): {} — the open preview becomes one undo step
- `edit.cancelPreview` (Cancel Preview): {} — the document goes back to how it was before the preview
- `edit.pasteSvg` (Paste Vector Art): {svg: markup (what Illustrator, VectorCraft or Figma put on the clipboard), spread?, at?: [x, y] (spread coords of the art's centre; default the first page's centre)} → {ids, warnings} — paths with their fills and strokes, groups as groups, text as outlines
- `edit.stepAndRepeat` (Edit › Step and Repeat…, Cmd+Alt+U): {count?: 1..1000, dx?, dy?, rows?, columns?, ids?} — copies of the selection (or ids) offset by (dx, dy); with rows/columns, a grid of at most 1000 cells, and at most 1000 item copies including group contents → {created, ids: the copies}
- `edit.transparencyBlendSpace` (Edit › Transparency Blend Space › Transparency Blend Space): {space: cmyk\|rgb} — the colour space transparency is composited in for output

## endnote

- `endnote.insert` (Type › Insert Endnote): {text?} — a reference at the insertion point; the first one makes the endnote frame on a new last page → {story, id, frame}
- `endnote.edit` (Edit Endnote): {story, id, text}
- `endnote.delete` (Delete Endnote): {story, id} — removes the reference and its text
- `endnote.list` (Endnotes): {} → [{story, id, number, text}] in numbering order
- `endnote.options` (Type › Document Endnote Options…): {style?: arabic\|upperRoman\|lowerRoman\|upperLetters\|lowerLetters\|kanji, startAt?, prefix?, suffix?, heading?, headingStyle?, paraStyle?, separator?} → the options

## file

- `file.new` (File › New › Document…, Cmd+N): {preset?: "Letter"\|"A4"\|… or a saved preset (file.savePreset), intent?: print\|web\|mobile, units?: points\|picas\|millimeters\|…, width?, height?, pages?, startPage?, facingPages?, columns?, gutter?, margins?: number\|{top,bottom,inside,outside}, bleed?, slug?: n \| [top, bottom, inside, outside], title?, primaryTextFrame?: bool}
- `file.newSample` (Help › Sample Document): {} — a multi-page magazine sample
- `file.presets` (Document Presets): {} → the built-in presets [{name, intent, width, height, units}], then the saved ones (with `saved: true`)
- `file.savePreset` (Save Document Preset): {name, …the settings as file.new} — kept with the preferences; `file.new {preset: name}` uses it. A saved preset of that name is replaced; built-in names are refused
- `file.deletePreset` (Delete Document Preset): {name} — a saved document preset
- `file.open` (File › Open…, Cmd+O): {path} — a DesignCraft or IDML file (recognised by its content, so the extension may be missing), or an InDesign .indd/.indt (recognised by its signature or extension, converted to IDML; its conversion warnings join `warnings`); the fonts in a `Document Fonts` folder beside it load first → {index, documentFonts: faces loaded, warnings: font files skipped, GREP styles whose pattern can't compile, Based on Parent links cleared and, for IDML and InDesign files, package parts missing}
- `file.openBytes` (Open Bytes): {name, base64} — DesignCraft JSON, an IDML package or an InDesign .indd/.indt → {index, warnings}
- `file.openRecent` (Open Recent File): {index} — reopen entry `index` of File › Open Recent (as file.open); a file that is gone is an error and stays listed
- `file.recentFiles` (Recent Files): {} → [{path, name, exists}] File › Open Recent, most recent first
- `file.clearRecent` (File › Open Recent › Clear Recent Files): {} — empty File › Open Recent
- `file.save` (File › Save, Cmd+S): {path?} — a `path` without the .designcraft extension gets it → {path: the file written, bytes}
- `file.saveAs` (File › Save As…, Cmd+Shift+S): {path} — a path without the .designcraft extension gets it → {path: the file written, bytes}
- `file.saveACopy` (File › Save a Copy…): {path} — writes the document without changing which file it is or its unsaved state; a path without the .designcraft extension gets it → {path: the file written, bytes}
- `file.revert` (File › Revert): {} — back to the last saved version (not undoable)
- `file.recovery.list` (Recovery Data): {dir?} → [{uid, path, title, saved}] unsaved documents left by a crash (default: the session's recovery folder)
- `file.recovery.save` (Save Recovery Data): {dir?} — write every unsaved document to the recovery folder (the app does this on a timer)
- `file.recovery.open` (Recover Documents): {dir?} — reopen documents left in the recovery folder (unsaved)
- `file.serialize` (Serialize): {} → {base64, bytes} the .designcraft file
- `file.close` (File › Close, Cmd+W): {index?}
- `file.activate` (Activate Document): {index}
- `file.place` (File › Place…, Cmd+D): {path?\|base64?, name?, frame?: id (place into), spread?, x?, y?, width?: finite number > 0 (null: absent), height? (video/audio), pdfPage?: n (1-based, Image Import Options), pdfCrop?: crop\|art\|trim\|bleed\|media\|contentVisible\|contentAll (the box the graphic shows; `width` is the whole page's), loadCursor? (with no frame to fill and no x/y, an image loads into the place cursor, as File › Place), layoutPage?: n (IDML / .designcraft: that page's objects as a group), page?, rect?: [x0,y0,x1,y1] (text: a new frame there), autoflow? (threads one frame per page column from the first frame on, adding pages until the text fits), removeStyles?, styleMap?: {imported name: document style}, styleConflicts?: useExisting\|redefine\|autoRename, link? (keep the file linked in the Links panel; default: the linkTextFiles preference)} — places an image into `frame` when given; otherwise any explicit x/y/spread/width creates a new frame; otherwise uses the selected empty or graphic frame, or creates a new frame; text files (.txt, .docx, .rtf, .md) and Excel workbooks (.xlsx, as a table) go into the insertion point, the selected frame or a new frame on `page`/`rect`
- `file.exportIdml` (Export IDML…): {path?, embedImages?: true} — writes an IDML package to `path`, or returns {base64} without a path
- `file.openIdml` (Open IDML): {path \| base64, name?} — opens an IDML package, or an InDesign document or template (.indd, .indt: converted to IDML first; its conversion warnings join `warnings`), as a new document (linked images are read next to the file or from its Links/ folder; the fonts in a `Document Fonts` folder beside it load first) → {index, documentFonts, warnings: conversion warnings, package parts missing, font files skipped, GREP styles whose pattern can't compile}
- `file.exportPdf` (File › Export PDF…): {path?, pages?: "1-3,5" \| [1,3] (1-based positions; default all), flatten?: high\|medium\|low\|ppi (Transparency Flattener: spreads with transparency are rasterised), spreads?: bool, fullScreen?: bool, bookmarksPanel?: bool, pageLayout?: single\|continuous\|twoUp\|twoUpCover\|twoUpContinuous, view?: fitPage\|fitWidth\|actual, advanceSeconds?: number (interactive PDF), bleed?: bool (document bleed), marks?: bool \| {crop?, bleed?, pageInfo?, weight?, offset?}, standard?: "none"\|"x4"\|"a2b", compressImages?: bool, tagged?: bool (structure tree: stories as paragraphs, figures with alt text), media?: bool (interactive: embed placed video and sound), title?, author?} → {path, bytes, pages, warnings} (no path: {base64, …})
- `file.exportEpub` (File › Export EPUB (Reflowable)…): {path?, title?, author?, language?: "en", identifier?: str (dc:identifier; a stable urn:uuid by default), coverImage?: path (a PNG or JPEG as the cover), tocTitle?: str (the table of contents' title; from the language by default), cover?: bool (the first page as the cover image), embedFonts?: bool (package the stylesheet's fonts whose licence allows it, whole files), fixedLayout?: bool (pre-paginated: each page as an image with its text)} → {path, bytes, warnings} (no path: {base64, bytes, warnings}); warnings name images without alt text, exported as decorative, and fonts that could not be embedded
- `file.exportFixedEpub` (File › Export EPUB (Fixed Layout)…): {path?, title?, author?, language?} — pre-paginated EPUB → {path, bytes} (no path: {base64, bytes})
- `file.printBooklet` (File › Print Booklet…): {path?, type?: saddleStitch\|twoUpConsecutive, spaceBetween? (pt)} — printer spreads as PDF (pages imposed in booklet order) → {path, bytes, sheets} (no path: {base64, …})
- `file.exportHtml` (File › Export HTML…): {path?, title?, language?} — one self-contained page (styles inline, images embedded), stories and graphics in reading order → {path, bytes, warnings} (no path: {text, bytes, warnings})
- `file.exportPptx` (File › Export PowerPoint…): {path?, pages?: "1-3,5" \| [1,3] (1-based positions; default all), lineBreaks?: keep\|reflow (keep: DesignCraft's lines, spacing and leading; reflow: one box per frame, PowerPoint sets the lines), rasterize?: bool (default true: objects PowerPoint can't show — placed PDF/EPS, type on a path, some effects — go in as 300 ppi images), embedFonts?: bool (default true: the TrueType fonts whose licences allow it), title?, author?} — every page as a slide of editable shapes, pictures, text boxes and tables → {path, bytes, slides, warnings} (no path: {base64, …})
- `file.exportText` (File › Export Text…): {path?, format?: "txt"\|"rtf"\|"tagged" (Tagged Text; default from the path, else txt), story?, frame?} — the story being edited or of the selected frame → {path, bytes} (no path: {text, bytes})
- `file.exportXml` (File › Export XML…): {path?} — the tagged content in reading order → {path, bytes} (no path: {text})
- `file.importXml` (File › Import XML…): {path \| text} — each element's content goes into the next text frame with that tag (child elements of mapped tags become paragraphs in their style) → {placed, unmatched}
- `file.package` (File › Package…): {dir: folder to create, idml?: true, pdf?: false, instructions?: text} — the document (its placed files relinked to Links/), Links/, the font files that draw its text in Document Fonts/ (fallback fonts included; unless their licence restricts it), an IDML copy (linking the files in Links/, nothing embedded), an optional PDF and a report → {dir, files, report}
- `file.printers` (Printers): {} → {printers: [names], default}
- `file.print` (File › Print…, Cmd+P): {printer?, copies?: 1, pages?: "1-3,5", spreads?, marks?, bleed?, dryRun?: bool (export and preview submission without printing)} → {printer, copies, pages, command, bytes}

## find

- `find.objects` (Find Object): {fill?, stroke?: swatch, strokeWeight?, opacity? (0–1), kind?: text\|graphic\|shape\|line\|group, layer?, label?, select?: bool (default true)} → {ids} — Find/Change › Object, through the document
- `find.changeObjects` (Change All (Object)): {…the criteria of find.objects, change: {fill?, stroke?, strokeWeight?, opacity?}} → {changed}
- `find.find` (Edit › Find/Change › Find): {find, grep?: bool, caseSensitive?: bool, wholeWord?: bool, scope?: document\|story\|selection, story?, change?\|first?\|attrs?: ignored (find.change takes them; one request serves all three Find/Change commands)} → matches [{story, start, end, text}]
- `find.change` (Edit › Find/Change › Change All): {find, change, grep?, caseSensitive?, wholeWord?, scope?, story?, first?: bool (change only the first match), attrs?: {character attributes applied to changed text}} → {count}
- `find.next` (Edit › Find Next, Cmd+Alt+F): {find, grep?, caseSensitive?, wholeWord?, scope?: document\|story\|selection, story?, change?\|first?\|attrs?: ignored (find.change takes them; one request serves all three Find/Change commands)} — Selection starts at its original beginning; later calls advance within the scope

## flex

- `flex.add` (Object › Flex Layout › Add to Flex Layout): {ids?} — the selected objects (top level, one spread) in a new Flex Layout container where they are; aligned objects get that direction, Auto size and Space Between, others a wrapping row of their width. One group or empty rectangle frame is converted instead (flex.convert) → {id}
- `flex.convert` (Object › Flex Layout › Convert to Flex Layout): {ids?} — a group (its objects) or a rectangle frame (with what is pasted into it) becomes a Flex Layout container → {id}
- `flex.remove` (Object › Flex Layout › Remove Flex Layout): {ids?} — the container goes; its objects stay where they are, grouped when there are several (a container with its own fill or stroke stays as a frame holding them) → {ids}
- `flex.set` (Flex Layout Options): {ids?, direction?: row\|rowReverse\|column\|columnReverse, wrap?: bool, justify?: flexStart\|center\|flexEnd\|spaceBetween\|spaceAround\|spaceEvenly, align?: start\|center\|end (across), cell?: 0..8 (the alignment grid, row by row from the top left: sets justification and alignment by direction), width?: auto\|fixed\|number, height?: auto\|fixed\|number, padding?: number\|[top, left, bottom, right], gapH?, gapV?} → {changed}
- `flex.reorder` (Reorder in Flex Layout): {id (an object in a container), to?: index \| by?: ±n} — its place in the container's order → {index}

## font

- `font.list` (Fonts in Document): {} → [{family, style, characters, missing, styleMissing, source: bundled\|installed\|document\|added (null when missing), matchStatus: exact\|styleSubstitute\|missing, resolvedFamily, resolvedStyle, replacementFamily, replacementStyle}] (missing first)
- `font.replace` (Type › Find/Replace Font…): {family, style?, toFamily, toStyle?, redefineStyles?: true} — replaces the font in text and (by default) in paragraph and character styles

## footnote

- `footnote.insert` (Type › Insert Footnote): {text?} — a footnote reference at the insertion point; the caret moves into the new footnote's text
- `footnote.options` (Type › Document Footnote Options…): {style?: arabic\|upperRoman\|lowerRoman\|upperLetters\|lowerLetters\|symbols\|kanji, startAt?, restart?: never\|page\|spread\|section, prefix?, suffix?, affixIn?: none\|reference\|text\|both, refPosition?: superscript\|subscript\|normal\|otSuperscript, refCharStyle?, paraStyle?, separator?, spaceBefore?, spaceBetween?, firstBaseline?: ascent\|capHeight\|leading\|xHeight\|emboxHeight\|fixed, firstBaselineMin?, spanColumns?, rule?: {on, weight, color, tint, width, offset, leftIndent}} → the options (no params: just read them)
- `footnote.list` (Footnotes): {story?} → [{story, id, index, anchor, text}] in story order
- `footnote.setText` (Set Footnote Text): {story, id, text} — replaces the footnote's text
- `footnote.delete` (Delete Footnote): {story, id} — deletes the reference (and so the footnote)
- `footnote.goToReference` (Type › Go to Footnote Reference): {} — from footnote text, puts the caret after the footnote's reference

## form

- `form.set` (Object › Interactive › Convert to Form Field): {ids?, kind: textField\|checkBox\|comboBox\|listBox\|signature, name?, value?, options?: [string], multiline?, required?, fontSize?} — interactive PDF form fields
- `form.clear` (Convert to Object): {ids?} — no longer a form field
- `form.list` (Form Fields): {} → [{id, kind, name, value, options}]

## frame

- `frame.create` (Create Frame): {spread?: index \| {kind: doc\|parent, index} (a parent spread: index into `parents` of document.inspect), rect: [x0,y0,x1,y1] (spread coords), shape?: rectangle\|ellipse\|polygon, content?: graphic\|text\|unassigned, sides?: 6, starInset?: 0–100 (%), text?: string, caret?: bool, vertical?: bool (text: a new vertical story)}
- `frame.grid` (Gridify): {rect, cols, rows, gutter? (pt, 12), shape?, content?, spread?} — a grid of frames filling `rect` (frame tools: arrow keys while dragging)

## gap

- `gap.move` (Move Gap): {at: [x, y] (spread), delta?: pt \| dx? \| dy?: a drag (the part along the gap's axis counts), spread?} — Gap tool: the gap at `at` between objects (or an object and the page edge) moves by `delta`; the objects on both sides resize → {axis, changed}

## guide

- `guide.liquid` (Convert to Liquid Guide): {spread?, page, index, on?: bool (default true)}
- `guide.add` (New Guide): {orientation: horizontal\|vertical, position (spread coordinate), spread?, page? (index in the spread; default: the page under `at` or the position), at? (the other coordinate), spreadGuide?: bool, liquid?: bool (a liquid guide, as the Page tool draws from the rulers)} or {orientation: both, point: [x, y], spread?, page?, spreadGuide?: bool, liquid?: bool} → {page, index}; `both` adds a horizontal guide through y and a vertical guide through x as one undo step → {guides: [{page, index}, {page, index}]}
- `guide.move` (Move Guide): {spread?, page, index, position}
- `guide.delete` (Delete Guide): {spread?, page, index}
- `guide.deleteAll` (View › Grids & Guides › Delete All Guides on Spread): {spread?}
- `guide.list` (Guides): {spread?} → [{page, index, orientation, position, spread}]

## hyperlink

- `hyperlink.create` (Type › Hyperlinks & Cross-References › New Hyperlink…): {url? \| email? \| page? (1-based), name?, ids?} — from the selected text, or the selected frames
- `hyperlink.delete` (Delete Hyperlink): {id}
- `hyperlink.list` (Hyperlinks): {}
- `hyperlink.edit` (Hyperlink Options…): {id, name?, url? \| email? \| page? (1-based)}
- `hyperlink.goToSource` (Go To Source): {id} — selects the hyperlink's text or frame

## hyphenation

- `hyphenation.addException` (Edit › Spelling › User Dictionary › Add Hyphenation Exception): {word: "ex~am~ple" (breaks only at ~) or a word with no ~ (never hyphenated)}
- `hyphenation.removeException` (Remove Hyphenation Exception): {word} (with or without ~)
- `hyphenation.list` (Hyphenation Exceptions): {} → [word]

## index

- `index.addReference` (Layout › Index › New Page Reference…): {topics?: [level 1..4] \| topic?: "Level 1 > Level 2" (default: the selected text), sort?: [keys], range?: currentPage\|toEndOfStory\|suppressPageRange\|nextParagraphs\|see\|seeAlso, paragraphs?: n, target?: topic for see/seeAlso} — a marker at the insertion point
- `index.list` (Index Page References): {} → [{story, pos, topics, range, page}]
- `index.generate` (Layout › Index › Generate Index…): {title?: "Index", sectionHeadings?: true, runIn?: false, page?: 1-based page for a new frame, rect?: [x0,y0,x1,y1]} — replaces the existing index → {story, entries}
- `index.update` (Layout › Index › Update Index): {} — regenerate the existing index

## ink

- `ink.list` (Ink Manager): {} → {allToProcess, inks: [{name, process: bool (printed as process), alias?}]} — the spot inks
- `ink.options` (Ink Manager): {allToProcess?: bool, ink?: spot swatch, toProcess?: bool, alias?: spot swatch \| null} — output: spots to process, ink aliases

## layer

- `layer.move` (Move Layer): {id, to: index (0 = top/frontmost)}
- `layer.selectItems` (Select All on Layer): {id}
- `layer.new` (New Layer…): {name?}
- `layer.set` (Layer Options…): {id, name?, color?: [r,g,b] \| layer colour name ("Light Blue", "Red", …), visible?, locked?, printable?, showGuides?, suppressWrapWhenHidden?} — names are unique and not empty
- `layer.delete` (Delete Layer): {id}
- `layer.merge` (Merge Layers): {ids: [layer ids], into?: layer id (default: the first)} — their objects move to `into`, the other layers are deleted
- `layer.deleteUnused` (Delete Unused Layers): {} — layers without objects (one layer always stays)
- `layer.others` (Hide/Lock Others): {id, hide?: bool, lock?: bool, show?: true (Show All Layers), unlock?: true (Unlock All Layers)} — Hide Others / Lock Others act on every layer but `id`
- `layer.activate` (Set Active Layer): {id}

## layout

- `layout.createAlternate` (Layout › Create Alternate Layout…): {name, width, height, rule?: page rule for the copies (default: keep each page's)} — every page copied after the last at the new size (a new section marked `name`), objects following the liquid rules
- `layout.pages.insert` (Layout › Pages › Insert Pages…, Cmd+Shift+P): {count?: 1, after?: page index (default: last), parent?: id\|"A-Parent"\|"A"\|null}
- `layout.rotateSpreadView` (Rotate Spread): {spread?: index (0), angle: 90 (clockwise) \| -90 \| 180 \| 0 (clear)} — turn one spread on screen (output is unaffected)
- `layout.pages.delete` (Layout › Pages › Delete Pages): {pages: [index]}
- `layout.pages.move` (Layout › Pages › Move Pages…): {from, to}
- `layout.pages.duplicateSpread` (Layout › Pages › Duplicate Spread): {spread, atEnd?: bool (Duplicate Spread at End of Document; the Pages panel's New Page button takes a dropped page there), to?: page index the copied pages move to in the same undo step (the Pages panel's Alt-drag)} → {page: the copy's first page (0-based)} — the spread's pages (size, margins, columns, guides, liquid rule) and items
- `layout.pages.applyParent` (Layout › Pages › Apply Parent to Pages…): {pages: [index], parent: id\|"A-Parent"\|"A"\|null (null or "[None]" clears)}
- `layout.parents.new` (Layout › Pages › New Parent…): {prefix?, name?: "Parent"}
- `layout.parents.edit` (Edit Parents): {on?: bool, parent?: id\|"A-Parent"\|"A"} — show parent spreads on the canvas; `parent` shows that parent (and implies on). Turning on without `parent` shows the first parent
- `layout.parents.options` (Parent Options…): {parent: id\|"B-Parent"\|"B", basedOn: id\|"A-Parent"\|"A"\|null (= [None])} — the parent shows its base's items under its own, and so do the pages that use it → {parent, basedOn}
- `layout.marginsAndColumns` (Layout › Margins and Columns…): {pages?: [index] (default all), margins?: number\|{top,bottom,inside,outside}, columns?, gutter?, adjustLayout?: bool (objects follow the margins), parent? (a parent's prefix, label or index)} — document pages take these as their own margins; with `parent` the parent's pages change instead (`pages` then indexes them), and so do the document pages without their own
- `layout.documentSetup` (File › Document Setup…, Cmd+Alt+P): {width?, height?, pages?: count, startPage?: n, facingPages?, binding?: leftToRight\|rightToLeft, intent?: print\|web\|mobile, margins?: n \| {top, bottom, inside, outside} (every page and parent page), bleed?, slug?: n \| [top, bottom, inside, outside], adjustLayout?: bool (objects follow the new page size and margins)} → the document setup (margins: the first page's)
- `layout.pages.toSpread` (Layout › Pages › Add Page to Spread): {page (1-based), spread (0-based)} — the page joins that spread (up to 10 pages; the spread stops shuffling)
- `layout.spreadShuffle` (Layout › Pages › Allow Selected Spread to Shuffle): {spread (0-based), allow: bool} — off keeps the spread's pages together when pages are added or removed
- `layout.pageSize` (Page Size): {pages: [1-based page numbers], width?, height?, preset?: "A4"\|"Letter"\|…, anchor?: 0–8 (reference point that stays put, row-major from the top-left; default 0)} — pages of their own size (Page tool); objects keep their place relative to the anchor, or follow the page's liquid rule
- `layout.pageOptions` (Page Options): {pages: [1-based], showParentOverlay?: bool} — Page tool options (Show Parent Page Overlay: the parent page's size drawn over the page)
- `layout.selectPage` (Select Page): {page: 1-based \| null, ids?: [item ids] (objects selected with it: the Page tool on an object-based page)} — the page the Page tool selects (its handles, the Control panel)
- `layout.section` (Layout › Numbering & Section Options…): {page (1-based; starts a section there), startNumber?: n (1–99999)\|null (continue), style?: arabic\|upperRoman\|lowerRoman\|upperLetters\|lowerLetters\|arabicLeadingZero\|arabicThreeDigits\|arabicFourDigits\|kanji, prefix? (up to 8 characters; no + or comma), includePrefix?, marker?, remove?: bool}
- `layout.chapterNumbering` (Document Chapter Numbering): {style?: arabic\|upperRoman\|lowerRoman\|upperLetters\|lowerLetters\|arabicLeadingZero\|arabicThreeDigits\|arabicFourDigits, start?: n (Start Chapter Numbering at), source?: automatic\|userDefined\|sameAsPrevious} → {chapterNumber, label, style, source, book: the open book holding the document, or null}; no parameters reports the setting
- `layout.numberingOptions` (Apply Numbering & Section Options): {page, …the settings as layout.section, chapter?: {…the settings as layout.chapterNumbering}} — the section and the document's chapter numbering in one undo step; if either is refused nothing changes
- `layout.overrideParentItems` (Layout › Pages › Override All Parent Page Items, Cmd+Alt+Shift+L): {page (0-based), ids?: parent items (default: all on the page's parent page)} → {ids} the page's editable copies
- `layout.removeOverrides` (Layout › Pages › Remove All Local Overrides): {page (0-based)} — deletes the page's overridden copies; the parent items show again
- `layout.detachAll` (Layout › Pages › Detach All Objects from Parent): {page (0-based)} — the page's overridden copies become ordinary items
- `layout.createGuides` (Layout › Create Guides…): {rows?: 0..1000, columns?: 0..1000, rowGutter?: 12, columnGutter?: 12, fitTo?: margins\|page, removeExisting?: false, spread?, page? (index in the spread; default all pages)} — at most 10000 guides per command

## library

- `library.new` (File › New › New Library): {path?} — an empty Object Library (saved to `path` when given)
- `library.open` (Open Library): {path \| json} → {items}
- `library.list` (Library Items): {} → [{index, name, description}]
- `library.json` (Library Contents): {} → the library as JSON text (to save where there's no file system)
- `library.add` (Add Item): {name?, description?} — the selection → {index}
- `library.place` (Place Item): {index, spread?, x?, y?} — at its original position unless x/y (top-left) are given
- `library.remove` (Delete Item): {index}
- `library.close` (Close Library): {}

## line

- `line.create` (Create Line): {spread?, a: [x,y], b: [x,y]}

## links

- `links.copyTo` (Copy Link(s) To…): {dir, assets?: [asset ids] (default: all)} — write the placed files to `dir` and relink to the copies → {copied}
- `links.list` (Links): {} → [{asset, name, path, status: ok\|modified\|missing\|embedded, refused?: why a missing link isn't followed (a path on another computer, a device), pixels, pdfCrop (placed PDFs: the box shown), uses: [{id, page, ppi}]}], then linked text files: [{story, name, path, status (also tooLarge: unchanged size, too big to check), edited (the story was changed in the layout), uses: [{id, page}]}]
- `links.relink` (Window › Links › Relink…): {asset \| story, path} — use another file for every placement of the graphic (keeps the selected PDF page; error if missing), or import another text file into the linked story
- `links.relinkFolder` (Window › Links › Relink to Folder…): {dir?: folder to look in (default: each link's own folder), extension?: e.g. "tif" (Relink File Extension), assets?: [ids], missingOnly?: bool (default true with `dir`)} → {relinked, notFound: [names]}
- `links.update` (Window › Links › Update Link): {asset? \| story?} — reload modified links from their files (all when neither); a linked text file is imported again into its story with the import options it was placed with, replacing edits made in the layout → {updated, warnings}
- `links.embed` (Window › Links › Embed Link): {asset \| story} — keep only the copy in the document (a text file: unlink the story)
- `links.goTo` (Window › Links › Go To Link): {asset \| story} — selects the frames showing the graphic or the linked text

## liquid

- `liquid.pageRule` (Layout › Liquid Layout › Liquid Page Rule): {rule: off\|scale\|reCenter\|guideBased\|objectBased\|controlledByParent (the parent page's rule), pages?: [1-based] (default: all)}
- `liquid.object` (Object Liquid Settings): {ids?, resizeWidth?, resizeHeight?, pinTop?, pinBottom?, pinLeft?, pinRight?} — for object-based pages

## list

- `list.define` (Type › Bulleted & Numbered Lists › Define Lists…): {name, continueAcrossStories?: true, rename?} — paragraphs join it with type.para {listType: numbers, listName}
- `list.delete` (Delete List): {name}

## math

- `math.insert` (Type › Insert Math Expression…): {latex, size?: points (12), x?, y?, spread?} or {id, latex, size?} — at the text insertion point (inline), else as a frame; with `id`: edits that equation
- `math.svg` (Math Expression SVG): {latex, size?} → {svg, width, height} — typeset without placing

## media

- `media.options` (Media Options): {ids?, playOnPageLoad?, loop?, controls?, poster?: {path \| base64+name} \| null (placeholder)} — for placed video and sound
- `media.get` (Media): {id?} → {kind, name, playOnPageLoad, loop, controls, poster}

## note

- `note.new` (Type › Notes › New Note): {text, author?} — at the insertion point → {story, id}
- `note.edit` (Edit Note): {story, id, text?, author?}
- `note.delete` (Type › Notes › Delete Note): {story, id}
- `note.convertToText` (Type › Notes › Convert Note to Text): {story, id} — the note's text replaces its anchor
- `note.list` (Notes): {} → [{story, id, at, author, text}] in story order

## object

- `object.matchAttributes` (Apply Attributes (Eyedropper)): {from: id, ids?} — copy fill, stroke, corners, opacity, effects, wrap
- `object.arrange` (Object › Arrange › Arrange): {to: front\|forward\|backward\|back, ids?}
- `object.bringToFront` (Object › Arrange › Bring to Front, Cmd+Shift+]): {}
- `object.bringForward` (Object › Arrange › Bring Forward, Cmd+]): {}
- `object.sendBackward` (Object › Arrange › Send Backward, Cmd+[): {}
- `object.sendToBack` (Object › Arrange › Send to Back, Cmd+Shift+[): {}
- `object.group` (Object › Group, Cmd+G): {ids?}
- `object.ungroup` (Object › Ungroup, Cmd+Shift+G): {ids?}
- `object.lock` (Object › Lock, Cmd+L): {ids?}
- `object.unlockAll` (Object › Unlock All on Spread, Cmd+Alt+L): {}
- `object.hide` (Object › Hide, Cmd+3): {ids?}
- `object.showAll` (Object › Show All on Spread, Cmd+Alt+3): {}
- `object.setFlags` (Set Visibility / Lock): {ids: [id], hidden?: bool, locked?: bool} — Layers panel eye/lock per object
- `object.fill` (Fill): {swatch? (a swatch's name, e.g. [Paper]), tint?: 0..1, ids?} — at least one; a tint alone keeps each object's own swatch (the Swatches panel's Tint field). With nothing selected: the fill of new shapes
- `object.swapFillStroke` (Swap Fill and Stroke): {ids?} — each object's fill and stroke colours (and tints) trade places; locked objects stay as they are. With nothing selected: those of new shapes
- `object.defaultFillStroke` (Default Fill and Stroke): {ids?} — no fill and a black stroke; locked objects stay as they are. With nothing selected: for new shapes
- `object.stroke` (Stroke): {swatch?, tint?, weight?, align?: center\|inside\|outside, type?: {kind:…}, cap?: butt\|round\|projecting, join?: miter\|round\|bevel, miterLimit?, start?, end?: none\|simple\|simpleWide\|triangle\|triangleWide\|barbed\|curved\|circle\|circleSolid\|square\|squareSolid\|bar, gapSwatch?, gapTint?, gapOverprint?: bool, ids?}
- `object.opacity` (Opacity): {opacity: 0..1, blend?: normal\|multiply\|…, ids?}
- `object.dropShadow` (Object › Effects › Drop Shadow, Cmd+Alt+M): {on?: bool, distance?, angle?, globalLight?: bool, opacity?, size?, spread? (%), color? (swatch), ids?}
- `object.innerShadow` (Object › Effects › Inner Shadow): {on?: bool, distance?, angle?, globalLight?: bool, opacity?, size?, choke? (%), color?, ids?}
- `object.outerGlow` (Object › Effects › Outer Glow): {on?: bool, opacity?, size?, spread? (%), color?, ids?}
- `object.exportOptions` (Object › Object Export Options…): {ids?, artifact?: bool (tagged PDF decoration), rasterize?: bool (EPUB/HTML image), align?: left\|center\|right\|"", pageBreakBefore?: bool, altText?}
- `object.innerGlow` (Object › Effects › Inner Glow): {on?: bool, opacity?, size?, choke? (%), center?: bool (glow from the centre), color?, ids?}
- `object.bevel` (Object › Effects › Bevel and Emboss): {on?: bool, size?, depth? (%), angle?, globalLight?: bool, highlight?, highlightOpacity?, shadow?, shadowOpacity?, ids?}
- `object.satin` (Object › Effects › Satin): {on?: bool, opacity?, angle?, distance?, size?, invert?: bool, color?, ids?}
- `object.directionalFeather` (Object › Effects › Directional Feather): {on?: bool, widths?: [top, left, bottom, right] \| number, ids?}
- `object.effects` (Effects): {effects?: {dropShadow?: {on?, color?, opacity?, angle?, globalLight?, distance?, size?, spread?}, innerShadow?, outerGlow?, innerGlow? {on?, color?, opacity?, size?, choke?, center?, mode? (blend mode: Screen, Multiply, …; Screen by default), technique?: softer\|precise}, bevel?, satin?, feather? (width), featherOptions? {choke? (%), corners?: sharp\|rounded\|diffused}, directionalFeather?, gradientFeather?} (the fields given replace the object's, as the Effects dialog sets them), opacity?: 0..1, blend?, ids?} — every effect at once, one undo step
- `object.feather` (Object › Effects › Basic Feather): {width (0 = off), ids?}
- `object.content` (Object › Content › Content): {type: graphic\|text\|unassigned, ids?}
- `object.textFrameOptions` (Object › Text Frame Options…, Cmd+B): {columns?, gutter?, inset?: number\|[t,l,b,r] (null keeps that side), verticalJustification?: top\|center\|bottom\|justify, columnsKind?: fixedNumber\|fixedWidth, columnWidth? (pt, Fixed Width), firstBaseline?: ascent\|capHeight\|leading\|xHeight\|emboxHeight\|fixed, firstBaselineMin? (pt), autoSize?: off\|heightOnly\|widthOnly\|heightAndWidth\|heightAndWidthProportionally, autoSizeReference?: topLeft\|topCenter\|topRight\|leftCenter\|center\|rightCenter\|bottomLeft\|bottomCenter\|bottomRight (the point that stays put), useMinimumHeight?: bool, minimumHeight? (pt), useMinimumWidth?: bool, minimumWidth? (pt), noLineBreaks?: bool, ignoreWrap?, balanceColumns?, columnRule?: bool, columnRuleWeight? (pt), columnRuleColor? (swatch name), columnRuleTint? (0..1), columnRuleOffset? (pt, horizontal), columnRuleTopInset? (pt), columnRuleBottomInset? (pt), vertical?: bool (sets the story direction of the frames' stories, as Type ▸ Story Direction), ids?}
- `object.cornerOptions` (Object › Corner Options…): {shape: none\|rounded\|inverseRounded\|inset\|bevel\|fancy, size, corners?: [{shape, size}] (4 entries in path order: top-left, top-right, bottom-right, bottom-left; replaces shape and size), ids?}
- `object.textWrap` (Window › Text Wrap, Cmd+Alt+W): {mode?: none\|boundingBox\|contour\|jumpObject\|jumpToNextColumn (boundingBox when absent, unless side or contour is given: then unchanged), offset?: number\|[t,l,b,r], invert?: bool, side?: bothSides\|leftSide\|rightSide\|towardsSpine\|awayFromSpine\|largestArea, contour?: boundingBox\|graphicFrame\|sameAsClipping, content?: bool (the placed graphic instead of its frame; default: whether the selection is the frame's content), ids?}; offset or contour drops an imported custom wrap boundary
- `object.fit` (Object › Fitting › Fitting): {mode: fillProportionally (preserves aspect ratio, covers frame, clips overflow)\|fitProportionally (preserves aspect ratio, shows whole image, may leave empty space)\|fitContentToFrame (stretches content to frame)\|centerContent (keeps current size, positions at fitting alignment)\|fitFrameToContent (resizes frame to content), axis?: both\|height\|width (frame-local sides Fit Frame to Content moves; default both), ids?} — locked objects and objects on locked layers are left as they are
- `object.fittingOptions` (Object › Fitting › Frame Fitting Options…): {autoFit?: bool, fitting?: none\|fillProportionally\|fitProportionally\|fitContentToFrame\|centerContent, align?: 0..8 (reference point, 4 = centre), crop?: n \| [t, l, b, r] (negative adds space), ids?}
- `object.rename` (Rename): {id \| ids?, name}
- `object.align` (Window › Object & Layout › Align › Align): {edge: left\|hcenter\|right\|top\|vcenter\|bottom, to?: selection\|keyObject\|margins\|page\|spread, ids?}
- `object.distribute` (Window › Object & Layout › Align › Distribute): {axis: horizontal\|vertical, by?: centers\|spacing, spacing?: points, ids?}
- `object.clippingPath` (Object › Clipping Path › Clipping Path…): {type?: alpha\|edges (default alpha), threshold?: 0–255 (alpha: opaque above; edges: darker than 255 − threshold counts; default 25), tolerance?: px (2), ids?} — traces the placed graphic and makes the outline the frame (Convert Clipping Path to Frame)
- `object.clippingPathOptions` (Object › Clipping Path › Clipping Path Options…): {type?: none, invert?: bool, includeInsideEdges?: bool, ids?} — without type, invert or includeInsideEdges, reports each selected graphic's clipping path ({items: [{id, type: none\|detectEdges\|alphaChannel\|photoshopPath\|userModifiedPath, anchors, invert, includeInsideEdges, threshold, tolerance, inset, sourceName}]}); type none removes it, invert shows the graphic outside it instead of inside
- `object.primaryTextFrame` (Object › Primary Text Frame): {on?: bool (default: toggle), ids?} — the selected text frame's story becomes the primary story (Smart Text Reflow adds and removes pages for it)
- `object.attributes` (Window › Output › Attributes › Attributes): {overprintFill?, overprintStroke?, overprintGap?, nonprinting?: bool, ids?} — Attributes panel
- `object.globalLight` (Object › Effects › Global Light…): {angle} — the light angle shared by shadows that use Global Light
- `object.label` (Window › Utilities › Script Label › Script Label): {label, ids?} — free text scripts and agents can find objects by
- `object.altText` (Object › Object Export Options): {text, ids?} — alternative text for tagged PDF and EPUB
- `object.transparencyGroup` (Group Transparency): {isolate?: bool, knockout?: bool, ids?} — Effects panel: Isolate Blending, Knockout Group
- `object.findByLabel` (Find by Script Label): {label} → ids of objects whose label is `label`
- `object.setLayer` (Move to Layer): {layer, ids?} — a group member moves its whole top-level group
- `object.reorder` (Reorder Objects): {ids?, above?: id \| below?: id \| index?: n (0 = top of the layer), layer?} — moves the objects (siblings on one spread) in the stacking order: in front of `above` or behind `below` (onto that object's layer), or to `index` in `layer` counted from the top (default: the first object's layer, index 0). Group members stay in their group. Leaves the document (and undo history) alone when nothing would change.
- `object.makeCompoundPath` (Object › Paths › Make Compound Path, Cmd+8): {ids?} — one path from the selected paths (the backmost object's look); paths inside others become holes → {id}
- `object.releaseCompoundPath` (Object › Paths › Release Compound Path, Cmd+Alt+Shift+8): {ids?} — each subpath becomes its own object → {ids}
- `object.pathfinder` (Object › Pathfinder › Pathfinder): {op: add\|subtract\|intersect\|exclude\|minusBack, ids?} — combine the selected shapes into one, which keeps the frontmost object's look and content (a placed graphic stays in it); Subtract keeps the backmost → {id}
- `object.gradientFeather` (Object › Effects › Gradient Feather): {on?: true, radial?, angle?, start?: opacity 0–100 (100), end?: (0), from?: [x,y], to?: [x,y] (spread coords: the Gradient Feather tool's drag), ids?}
- `object.caption` (Object › Captions › Generate Static Caption): {text?: template (default "{name}"; variables {name} {path} {altText} {label} {ppi} {dimensions} {format}), position?: below\|above\|left\|right, offset? (pt, 0), height? (pt, 24), style?: paragraph style, live?: bool (kept current as the source changes), ids?} → {ids}
- `object.pdfLayers` (Object Layers): {id?} → [{name, visible, default}] — the layers of the selected placed PDF
- `object.layerOptions` (Object › Object Layer Options…): {ids?, hidden: [layer name]} — layers of placed PDFs to hide ([] = the file's own settings)
- `object.qrCode` (Object › Generate QR Code…): {type?: url\|text\|sms\|email\|vcard (default url), content (url/text), number?, message?, to?, subject?, body?, name?, phone?, email?, org?, url?, color? (swatch, [Black]), rect? (new object; else into the selected frame, or re-encode a selected code), spread?} → {id, content}
- `object.convertShape` (Object › Convert Shape › Convert Shape): {to: rectangle\|roundedRectangle\|beveledRectangle\|inverseRoundedRectangle\|ellipse\|triangle\|polygon\|line\|orthogonalLine\|openPath\|closedPath, ids?}
- `object.gradient` (Gradient): {kind?: linear\|radial, stops?: [{location: 0–100, color: "#rrggbb"\|{c,m,y,k}(0..100)\|[r,g,b](0..255)\|{model: rgb\|cmyk\|gray, …}(0..1) \| swatch: name (its colour, as dropped on the Gradient panel), opacity?: 0–100, midpoint?: 13–87}], reverse?: bool, angle?: degrees, from?: [x,y], to?: [x,y] (spread coords: the Gradient Swatch tool's drag), target?: fill\|stroke, ids?} → {swatch, kind, stops} — edits the fill's (or the stroke's) gradient (an unnamed gradient unless it equals a gradient swatch)
- `object.color` (Apply Color): {color: "#rrggbb"\|{c,m,y,k}(0..100)\|[r,g,b](0..255)\|{model: rgb\|cmyk\|gray, r,g,b\|c,m,y,k\|k}(0..1), target?: fill\|stroke, text?: bool, ids?} — an unnamed colour (not in the Swatches panel until Add to Swatches) on the selection (with nothing selected, the colour of new shapes); `text`: on the selected text, or the text of the selected frames (Formatting Affects Text)

## page

- `page.transition` (Page Transition): {pages?: [1-based] \| spread? \| all?: bool, kind: blinds\|box\|comb\|cover\|dissolve\|fade\|push\|split\|uncover\|wipe\|zoomIn\|zoomOut\|none, duration?: seconds (1), horizontal?: bool} — for interactive PDF
- `page.transitions` (Page Transitions): {} → [{spread, kind, duration, horizontal}]

## path

- `path.create` (Create Path): {spread?, anchors: [{p:[x,y], in?:[x,y], out?:[x,y]}], closed?: bool}
- `path.appendAnchor` (Add Anchor): {id, anchor: {p, in?, out?} (spread coords), subpath?: index (default the last), at?: end\|start (default end)} — after the subpath's last anchor, or before its first with `at: start`
- `path.setAnchor` (Set Anchor): {id, subpath?: index (default the last), anchor: index\|"first"\|"last", p?, in?, out? (spread coords)} — moves an anchor or its direction lines; with both lines given and collinear it becomes smooth
- `path.reverse` (Object › Paths › Reverse Path): {ids?, subpath?: index (only that subpath of the first target)} — the anchors run the other way (the end point becomes the start)
- `path.close` (Object › Paths › Close Path): {id, subpath?: index (default every subpath)}
- `path.moveAnchors` (Move Anchors): {id, anchors: [[subpath, index]], dx, dy, handle?: in\|out}
- `path.addAnchor` (Add Anchor Point): {id, at: [x,y] (spread coords; the nearest point on the path), tolerance?: pt (default 4)} → {subpath, anchor}
- `path.deleteAnchor` (Delete Anchor Point): {id, subpath, anchor} — removes the point (and the object when no path is left)
- `path.convertAnchor` (Convert Direction Point): {id, subpath, anchor, to?: [x,y] (spread coords: drag out symmetric handles to there), corner?: bool} — without `to`, a smooth point becomes a corner and a corner gets smooth handles
- `path.erase` (Erase): {id, points: [[x,y], …] (spread coords: the Erase tool's drag), tolerance?: pt (default 4)} — removes the stretch of path the drag ran along
- `path.smooth` (Smooth): {id, points: [[x,y], …] (spread coords), tolerance?: pt (default 4)} — re-fits the stretch the drag ran along with fewer, smoother anchors
- `path.join` (Object › Paths › Join): {ids?} — one open path: closes it; two open paths: joins them where their ends are nearest (coincident ends become one point) into the first, and removes the second → {id}
- `path.convertPoints` (Convert Point): {kind: plain\|corner\|smooth\|symmetrical, ids?} — the Direct Selection tool's selected points, or every point of the selected paths: plain (no direction handles), corner (independent handles), smooth (collinear handles), symmetrical (collinear, equal length) → {converted}
- `path.split` (Split Path): {id, at: [x,y] (spread coords; the nearest point on the path)} — Scissors: an open path becomes two, a closed one opens there → {ids}

## place

- `place.styles` (Import Options: Styles): {path \| base64, name} → {paragraph: [name], character: [name], conflicts: [name]} — the styles a Word/RTF file brings (for styleMap / styleConflicts)
- `place.load` (Load Place Cursor): {path \| base64, name?} — load a graphic into the place cursor (then click/drag with the placeGun tool)
- `place.drop` (Place Loaded Graphic): {spread?, x, y, rect?: [x0,y0,x1,y1], frame?: id}

## preflight

- `preflight.run` (Window › Output › Preflight › Preflight Document): {minPpi?: 150} → issues [{severity, kind, message, item?, page?}]

## prefs

- `prefs.set` (Preferences): {showHiddenCharacters?, typographersQuotes?, polygonSides?, starInset?, scaleStrokes?, dimensionsIncludeStroke?, transformationsAreTotals?, absolutePageNumbers?, highlightHj?, highlightKeeps?, highlightCustomTracking?, highlightSubstitutedFonts?, richBlackOutput?, favoriteFonts?: [family], recentFonts?: [family], showFontNamesInEnglish?, smartTextReflow?, autocorrect?, autocorrectList?: [[word, correction]], showAddedText?, showNoteAnchors?, cjkFeatures?: bool\|null (CJK-only menu items and dialogs shown; null follows the interface language), linkTextFiles? (Create Links When Placing Text Files), recoveryMinutes?, recentFilesMax?: 0–100} → all application preferences

## script

- `script.run` (Run Script): {text} — command script lines (`command.id {json}`, JSON lines or a JSON array; `$N.path` refers to earlier results) → {results, steps}

## select

- `select.firstAbove` (Object › Select › First Object Above, Cmd+Alt+Shift+]): {} — the frontmost object on the spread (layers included)
- `select.nextAbove` (Object › Select › Next Object Above, Cmd+Alt+]): {}
- `select.nextBelow` (Object › Select › Next Object Below, Cmd+Alt+[): {}
- `select.lastBelow` (Object › Select › Last Object Below, Cmd+Alt+Shift+[): {} — the backmost object on the spread
- `select.container` (Object › Select › Container): {} — the group or frame holding the selection
- `select.content` (Object › Select › Content): {} — the graphic in a frame, or the first object in a group
- `select.nextInGroup` (Object › Select › Next Object in Group): {}
- `select.previousInGroup` (Object › Select › Previous Object in Group): {}

## selection

- `selection.set` (Select): {ids: [id], add?: bool, content?: bool}
- `selection.toggle` (Toggle Selection): {id}

## snippet

- `snippet.export` (File › Export › Export Selection as Snippet): {path?} — the selected items (with their stories, styles and images) as a .designcraft snippet; no path: {base64}
- `snippet.place` (Place Snippet): {path \| base64, spread?, x?, y?} — items keep their positions unless x/y given (top-left)

## spelling

- `spelling.check` (Edit › Spelling › Check Spelling…, Cmd+I): {story?, suggestions?: true} → [{story, start, end, word, suggestions}]
- `spelling.setWords` (User Dictionary): {words: [word]} — replace the document's user dictionary
- `spelling.words` (User Dictionary Words): {} → [word]
- `spelling.addWord` (Edit › Spelling › Add to Dictionary): {word}
- `spelling.change` (Change): {story, start, end, to}

## states

- `states.create` (Window › Interactive › Object States › Convert Selection to Multi-State Object): {ids? (default: the selection; one group's objects or several objects become states)} → {id, states}
- `states.list` (Object States): {id?} → {states, active}
- `states.show` (Show State): {id?, index? \| name?}
- `states.rename` (State Options): {id?, index, name}
- `states.release` (Release State to Objects): {id?} — back to a plain group (every state shows)

## story

- `story.placeAndLink` (Edit › Place and Link): {story (parent), rect, spread?} — a new frame whose story copies the parent and stays linked → {id, story}
- `story.links` (Linked Stories): {} → [{story, parent, outOfDate}]
- `story.updateLink` (Update Link): {story? (default: every out-of-date linked story)} — the child takes the parent's current content (its own edits are replaced)
- `story.unlink` (Unlink): {story}
- `story.setDirection` (Type › Story Column Direction › Story Column Direction): {story?, frame?: a text frame of the story, direction: leftToRight\|rightToLeft} — column progression, independent of paragraph direction
- `story.setText` (Set Story Text): {story, text} — replace a story's whole text
- `story.replaceRange` (Edit Story): {story, start, end, text} — replace a byte range keeping surrounding formatting
- `story.get` (Get Story): {story? \| frame?} → text, frames, paragraphs, vertical, overset

## strokeStyle

- `strokeStyle.list` (Stroke Styles): {} → [{name, kind}]
- `strokeStyle.new` (Object › Stroke Styles › New Stroke Style…): {name, type: stripes\|dash\|dot, bands?: [[start, width] (fractions of the weight)], pattern?: [dash, gap, …] (pt)} — apply with object.stroke {type: {kind: "style", name}}
- `strokeStyle.delete` (Delete Stroke Style): {name} — strokes using it become solid

## style

- `style.breakLink` (Break Link to Style): {kind: paragraph\|character} — the selected text keeps its look as local formatting, with [No Paragraph Style] / [None]
- `style.compositeFont.list` (List Composite Fonts): {} → composite font definitions
- `style.compositeFont.set` (Set Composite Font): {name, entries: [{name?, characters?, family, style?, relativeSize?, horizontalScale?, verticalScale?, baselineShift?, scaleOption?}]} — replaces a composite font definition; empty characters selects the base entry
- `style.exportTag` (Export Tagging): {style, character?: bool, tag?: p\|h1…h6\|blockquote\|pre\|li\|… (span\|em\|strong\|code\|sup\|sub… for characters; "" = automatic), class?} → the tagging
- `style.paragraph.apply` (Apply Paragraph Style): {name, clearOverrides?: bool}
- `style.character.apply` (Apply Character Style): {name}
- `style.paragraph.redefine` (Redefine Paragraph Style): {name?} — incorporate the first selected paragraph/character's local formatting into its paragraph style; retain character styles; one undo step
- `style.character.redefine` (Redefine Character Style): {name?} — incorporate the first selected character's local formatting into its character style without capturing paragraph attributes; one undo step
- `style.paragraph.create` (New Paragraph Style…): {name, basedOn?, nextStyle?, para?: {paragraph attributes, as type.para names them: align, leftIndent, firstLineIndent, spaceBefore, spaceAfter, …; startAt?: null = continue numbering; grepStyles?: [{style, pattern}]: a pattern that can't compile is an error}, chars?: {character attributes, as type.char names them: fontFamily, fontStyle, size, leading, tracking, fill, …}, fromSelection?: bool}
- `style.paragraph.edit` (Paragraph Style Options…): {name, rename?, basedOn?, nextStyle?, para?: {paragraph attributes, as type.para names them: align, leftIndent, spaceBefore, …; ruleAbove?/ruleBelow?: only the named rule fields change; startAt?: null = continue numbering; kinsoku?: set \| null (default rules); a grepStyles pattern that can't compile is an error}, chars?: {character attributes, as type.char names them: fontFamily, fontStyle, size, leading, tracking, fill, …}}
- `style.paragraph.delete` (Delete Paragraph Style): {name, replaceWith?}
- `style.character.create` (New Character Style…): {name, basedOn?: style \| "[None]", chars?: {character attributes, as type.char names them: fontFamily, fontStyle, size, leading, tracking, fill, …}, fromSelection?: bool (default false)} — if true, capture the first selected character's style/local overrides (caret: typing format), then overlay chars (null unsets); only explicit fill names are validated; paragraph formatting stays inherited; no text target: chars only → {name} (made unique)
- `style.character.edit` (Character Style Options…): {name, rename?, basedOn?: style \| "[None]" \| null, chars?: {character attribute (as type.char names them: fontFamily, fontStyle, size, …): value \| null (no longer set)}} — renaming updates every use
- `style.character.delete` (Delete Character Style): {name, replaceWith?}
- `style.list` (List Styles): {} → paragraph and character style names
- `style.object.apply` (Apply Object Style): {name, ids?} — sets the style's fill, stroke, effects and text frame options on the items
- `style.object.create` (New Object Style…): {name, fromSelection?: true (fill, stroke, effects and text frame options of the first selected item), fill?, paragraphStyle?, effects?: {dropShadow?, feather?, innerShadow?, outerGlow?, innerGlow?, bevel?, satin?, gradientFeather?, directionalFeather?}, dropShadow?: {on?, color?, opacity? (0–1), angle?, globalLight?, distance?, size?, spread?}, feather?: width, innerShadow?, outerGlow?, innerGlow?, bevel?, satin?, gradientFeather?, directionalFeather?} → {name} (made unique)
- `style.object.edit` (Object Style Options…): {name, effects?: {…} \| null (the style no longer sets effects), dropShadow?, feather?, innerShadow?, outerGlow?, innerGlow?, bevel?, satin?, gradientFeather?, directionalFeather?} — effect objects merge field by field into the style's effects (fields as in `document.inspect` item effects); values that aren't finite numbers are refused, the others clamped (opacities 0–1, sizes and distances ≥ 0); items using the style whose effects match the style's (no effects, when the style set none) take the new effects, items with their own effects keep them → {name, updated}
- `style.object.clearOverrides` (Clear Object Style Overrides): {ids?} — each item takes its object style's fill, stroke, effects and text frame options again → {changed}
- `style.group` (Move to Group): {kind: paragraph\|character, names: [style names], group: "Heads" \| "Heads/Display" \| "" (out of any group)} — styles are named Group/Name; every use is renamed → {renamed: {old: new}}
- `style.load` (Load Styles…): {path \| base64, name?: the file's name (`.idml` reads IDML), paragraph?: [name], character?: [name], conflicts?: redefine\|useExisting\|autoRename} — paragraph and character styles of another document (.designcraft or .idml): all of a kind, or the named ones (`[]`: none). The styles, swatches and lists they name come along where this document has none. A style this document defines differently under the same name takes the loaded definition (redefine, the default), stays as it is (useExisting), or the loaded one gets a new name (autoRename) → {paragraph: {added, replaced, renamed: {name: new name}}, character: {…}, swatches: [name]}
- `style.load.list` (List Styles in File): {path \| base64, name?} → {paragraph: [{name, conflict}], character: [{name, conflict}]} — the styles `style.load` would bring; `conflict`: this document defines a style of that name differently
- `style.cell.create` (New Cell Style…): {name, fromSelection?: bool (the target cell's look), fill?, tint?, insets?: n\|[t,l,b,r], vj?: top\|center\|bottom\|justify, stroke?: {weight?, color?, tint?, type?, gapColor?, gapTint?} (all four edges; values as table.setCell's stroke), paragraphStyle?, basedOn?: cell style name, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} → {name}
- `style.cell.apply` (Apply Cell Style): {name, story?, table?, rows?: [a,b] \| row?, cols?: [a,b] \| col?} — the target cells (the whole table when the cursor is in it)
- `style.cell.edit` (Cell Style Options…): {name, …same as style.cell.create} — cells using the style follow
- `style.table.create` (New Table Style…): {name, basedOn?: table style name, header?, body?, footer?, leftColumn?, rightColumn?: cell style names, border?: {weight?, color?, tint?, type?, gapColor?, gapTint?}, altRows?: {first, firstColor, next, nextColor}, spaceBefore?, spaceAfter?} → {name}
- `style.table.apply` (Apply Table Style): {name, story?, table?, rows?: [a,b] \| row?, cols?: [a,b] \| col?}
- `style.table.edit` (Table Style Options…): {name, …same as style.table.create} — tables using the style follow

## swatch

- `swatch.addColorTheme` (Color Theme…): {colors: [one to five RGB hex colours], name?: group name} → {name, swatches} — adds the previewed palette as one undoable swatch group
- `swatch.create` (New Color Swatch…): {name?, color: "#rrggbb"\|{c,m,y,k}(0..100)\|[r,g,b](0..255)\|{model: rgb\|cmyk\|gray, …}(0..1), spot?: bool} \| {name? ("New Gradient Swatch"), gradient: {kind?: linear\|radial, stops: [{location: 0–100, swatch?: a colour swatch's name \| color?, opacity?: 0–100, midpoint?: 13–87}]}} → {name}
- `swatch.new` (New Swatch): {swatch?: name, target?: fill\|stroke} → {name} — the Swatches panel's New Swatch: `swatch` (default: the selection's fill or stroke) as a new swatch. An unnamed colour or gradient becomes a named one (a gradient: "New Gradient Swatch"), still applied; a named swatch is duplicated ("… copy"); with nothing selected and no `swatch`, a new colour swatch
- `swatch.load` (Load Swatches…): {path?\|base64?, replace?: bool} — colour swatches from a swatch exchange (.ase) file; a name the file repeats gets a number ("Red 2") and an unnamed color is named by its value; names already in the document are kept unless `replace` → {added, replaced}
- `swatch.save` (Save Swatches for Exchange…): {path?, names?: [swatch names] (default: all colour swatches)} → {base64} or writes `path` (.ase)
- `swatch.addToSwatches` (Add to Swatches): {swatch?: name (default: the selection's fill), target?: fill\|stroke, name?: new name} — makes an unnamed colour a swatch
- `swatch.options` (Swatch Options…): {name, to?: new name, nameWithValue?: bool, color?: "#rrggbb"\|{c,m,y,k}(0..100)\|[r,g,b]\|{gray}(0..100), spot?: bool, tint?: 0–1 (tint swatches), base?: colour swatch (tint swatches)} → {name} — every use follows a rename; [None], [Registration], [Black] and [Paper] keep their names
- `swatch.addUnnamed` (Add Unnamed Colors): {} — every unnamed colour used becomes a swatch
- `swatch.delete` (Delete Swatch): {name}
- `swatch.newColorGroup` (New Color Group): {name?, swatches?: [names]} — a Swatches panel folder (the swatches move into it) → {name}
- `swatch.moveToGroup` (Move to Color Group): {swatches: [names], group: name \| null (top level)}
- `swatch.ungroupColorGroup` (Ungroup Color Group): {name} — its swatches go back to the top level
- `swatch.renameColorGroup` (Color Group Options): {name, to}

## table

- `table.insert` (Create Table, Cmd+Alt+Shift+T): {rows?: body rows (4), cols? \| columns? (4), headerRows? (0), footerRows? (0), width?} — at the text insertion point
- `table.convertFromText` (Table › Convert Text to Table): {columnSeparator?: tab\|comma, width?: table width (default: the column)} — selected paragraphs become rows
- `table.convertToText` (Table › Convert Table to Text): {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — cells separated by tabs, rows by paragraphs
- `table.insertRow` (Insert Row): {where?: above\|below, count? (1), story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)}
- `table.insertRowAbove` (Table › Insert › Insert Row Above): {count?, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)}
- `table.insertRowBelow` (Table › Insert › Insert Row Below): {count?, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)}
- `table.insertColumn` (Insert Column): {where?: left\|right, count? (1), width?, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)}
- `table.insertColumnLeft` (Table › Insert › Insert Column Left): {count?, width?, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)}
- `table.insertColumnRight` (Table › Insert › Insert Column Right): {count?, width?, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)}
- `table.deleteRow` (Table › Delete › Delete Row): {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — the rows of the target cells
- `table.deleteColumn` (Table › Delete › Delete Column): {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — the columns of the target cells
- `table.delete` (Table › Delete › Delete Table): {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)}
- `table.merge` (Table › Merge Cells): {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — merge the target cell range
- `table.dropCells` (Drag Rows or Columns): {frame, from: [x, y], to: [x, y]} — selected whole rows (or columns) dragged from `from` move to the row (column) at `to`; otherwise a text drag
- `table.placeGraphic` (Table › Convert Cell Type › Convert Cell to Graphic Cell): {path? \| base64?, name?: with base64, fit?: proportional\|fill (default proportional), story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — an image in the target cell (its text is kept but hidden)
- `table.textCell` (Table › Convert Cell Type › Convert Cell to Text Cell): {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — drop the target cells' graphics
- `table.moveRow` (Move Row): {from?, to, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} (0-based; from defaults to the target row) — like dragging a row
- `table.moveColumn` (Move Column): {from?, to, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} (0-based; from defaults to the target column)
- `table.sortRows` (Table › Sort): {column?: 0-based (default: the target cell's), descending?: bool, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — body rows by that column's text (numbers numerically)
- `table.unmerge` (Table › Unmerge Cells): {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)}
- `table.splitHorizontally` (Table › Split Cell Horizontally): {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — each target cell becomes two, one above the other
- `table.splitVertically` (Table › Split Cell Vertically): {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — each target cell becomes two, side by side
- `table.setCell` (Cell Options): {fill?: swatch, tint?: 0..1, insets?: n \| [t,l,b,r], vj? \| verticalJustification?: top\|center\|bottom\|justify, text?, stroke?: {weight?, color?: swatch, tint?: 0..1, type?: solid\|dashed\|dotted\|thickThin\|thinThick\|thinThin\|thickThick\|thinThickThin\|thickThinThick\|wavy\|hashed \| {kind:…}, gapColor?: swatch, gapTint?: 0..1, edges?: name \| [names] (all\|outer\|inner\|top\|left\|bottom\|right\|innerHorizontal\|innerVertical; default all)}, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — top/left/bottom/right are the target range's outer sides, innerHorizontal/innerVertical the lines between its rows/columns
- `table.getCellStroke` (Get Cell Stroke): {story?, table?, rows?, cols?, edges?} → {weight, color, tint, type, gapColor, gapTint, fill, fillTint, edges: count} of the chosen edges of the target cells; a value that differs between them is null
- `table.setRowHeight` (Row Height): {height, mode?: atLeast\|exactly, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)}
- `table.setColumnWidth` (Column Width): {width, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)}
- `table.resizeBorder` (Resize Row or Column): {story?, table?, frame?, axis: column\|row, index, delta? \| size?, keepTableSize?: bool} — moves the border after column/row `index` by `delta` (or makes that column/row `size` wide/high); later columns/rows move along. The last index is the table's end/bottom edge. keepTableSize: on an inner border the next column/row gives or takes the change; on the edge all columns/rows scale proportionally. A dragged row becomes At Least. Refuses a locked `frame`
- `table.distributeColumns` (Table › Distribute Columns Evenly): {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)}
- `table.distributeRows` (Table › Distribute Rows Evenly): {story?, table?, rows?: [a,b] \| row?, cols?: [a,b] \| col?} — equal fixed heights preserving the selected rows' composed total height; may overset cell text; unmerge row-spanning cells first
- `table.options` (Table Options): {direction?: leftToRight\|rightToLeft, border?: {weight?, color?, tint?, type?, gapColor?, gapTint?}, spaceBefore?, spaceAfter?, headerRows?, footerRows?, repeatHeader?, repeatFooter?, altRows?: {first, firstColor, firstTint, next, nextColor, nextTint, skipFirst, skipLast} \| null, altCols?: … \| null, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)}
- `table.convertRowsToHeader` (Table › Convert Rows › To Header): {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — the target rows, at the top of the table or right after its header rows
- `table.convertRowsToBody` (Table › Convert Rows › To Body): {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — the target header rows next to the body, footer rows next to it, or both
- `table.convertRowsToFooter` (Table › Convert Rows › To Footer): {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — the target rows, at the bottom of the table or right before its footer rows
- `table.select` (Select Cells): {story?, table?, rows?: [a,b] \| row?, cols?: [a,b] \| col?, what?: cell\|row\|column\|table}
- `table.selectTable` (Table › Select › Select Table): {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)}
- `table.selectRow` (Table › Select › Select Row): {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)}
- `table.selectColumn` (Table › Select › Select Column): {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)}
- `table.nextCell` (Next Cell): {}
- `table.prevCell` (Previous Cell): {}
- `table.get` (Get Table): {story?, table?, rows?: [a,b] \| row?, cols?: [a,b] \| col?} → rows, columns, cells (text, spans, fill), options

## text

- `text.placeCaret` (Place Caret): {frame, point: [x,y] (spread coords)} — converts empty frames to text frames
- `text.release` (Release): {frame, point, moved: bool, copy?: bool} — ends a press in text: a drag that started in the selected text moves (copy: duplicates) it to the point; a click places the caret
- `text.extendTo` (Extend Text Selection): {frame, point, unit?: word\|line\|paragraph\|story} — moves the selection's focus to the point; with `unit`, after a text.selectAt, the selection grows by whole units from the unit first selected (a drag after a double, triple or quadruple click)
- `text.selectWord` (Select Word): {frame, point} — the word (or run of spaces) under the point
- `text.selectAt` (Select Text Unit): {frame, point, unit: word\|line\|paragraph\|story} — what a double, triple, quadruple or quintuple click selects: the word (or run of spaces) under the point, its line, its paragraph with the paragraph return, or the whole story
- `text.selectSentence` (Select Sentence): {frame, point} — the sentence under the point
- `text.selectParagraph` (Select Paragraph): {frame, point} — the paragraph under the point, without its paragraph return
- `text.selectStory` (Select Story): {frame, point} — all the text of the story under the point, threaded frames included
- `text.select` (Select Text): {story, anchor, focus} (UTF-8 byte offsets into the story text, as find.find reports them: á or — counts 2 or 3)
- `text.insert` (Type): {text, raw?: bool (no typographer's quotes)} — replaces the selected text
- `text.delete` (Delete Text): {forward?: bool, word?: bool}
- `text.move` (Move Caret): {dir: left\|right\|up\|down\|lineStart\|lineEnd\|storyStart\|storyEnd, extend?, word?}
- `text.exitToFrame` (Select Frame): {}
- `text.thread` (Thread Text Frames): {from?, to?, rect?: [x0,y0,x1,y1] (spread coords), spread?, autoflow?: bool} — threads frame `to` right after frame `from` (between `from` and the frame that followed it, if any). `to` is an empty frame or a text frame nothing threads into yet; its text joins the end of the story. Give `rect` in place of `from` or `to` to thread a new text frame made there on `spread`: `{from, rect}` adds it after `from`, `{rect, to}` in front of `to`. autoflow: then add pages with threaded frames until the story fits. Selects the frame that joined the thread. → {story, from, to, overset, pagesAdded}
- `text.unthread` (Break Thread): {frame?, side?: after\|before} — breaks the thread after (or before) `frame` (default: the selected text frame). The frames from the break on stay threaded to each other but become empty; the text stays in the story, overset if the earlier frames can't hold it
- `text.removeFromThread` (Remove Frame from Thread): {frame?} — takes `frame` (default: the selected text frame) out of its thread: the frames before and after it join up and keep the text, `frame` stays empty

## toc

- `toc.generate` (Layout › Table of Contents…): {entries: [{style, level?: 1 (1-9), entryStyle?: paragraph style of its entries (default "TOC Level n"), pageNumber?: "after"\|"before"\|"none", separator?: text between entry and number (default a tab), pageNumberStyle?: character style of the page number, separatorStyle?: character style of the separator, sort?: bool (Sort Entries in Alphabetical Order: among their siblings, each with the entries under it)}] \| styles: [names] (levels 1, 2, …), title?: "Contents", titleStyle?: paragraph style of the title (default "TOC Title"), pageNumbers?: true, replace?: true (regenerate the existing table of contents in place; false makes a new frame), page?: 1-based page for a new frame (its margins), rect?: [x0,y0,x1,y1] (spread coords)} → {story, entries}
- `toc.update` (Layout › Update Table of Contents): {} — regenerate the existing table of contents
- `toc.entries` (Table of Contents Entries): {entries \| styles} → [{level, text, page}] without changing the document

## tool

- `tool.polygonSettings` (Polygon Settings…): {sides?: 3–100, starInset?: 0–100 (%)} → the settings new polygons use
- `tool.select` (Select Tool): {tool: selection\|directSelection\|type\|rectangleFrame\|…}
- `tool.list` (List Tools): {}

## transform

- `transform.move` (Object › Transform › Move): {dx, dy, copy?: bool, ids?, toSpread?, content?: bool (move the placed graphic or pasted-in items inside each frame; the frame stays. Default: whether the selection is content, when neither ids nor copy is given)} → {moved, ids: the objects moved (with copy, the copies)}
- `transform.resize` (Resize): {from: rect, to: rect, content?: bool (scale content), distribute?: bool (Live Distribute: objects keep their size, their centres spread with the bounds), ids?}
- `transform.rotate` (Object › Transform › Rotate): {angle (degrees, CCW), ref?: 0..8 (reference point of the selection bounds, default 4: centre), ids?}
- `transform.scale` (Object › Transform › Scale): {sx, sy, ids?} (about the selection centre)
- `transform.again` (Object › Transform Again › Transform Again, Cmd+Alt+3): {individually?: bool, sequence?: bool, ids?} — repeat the last transform (or the whole sequence applied to this selection), on the selection as a whole or on each object about its own centre
- `transform.clear` (Object › Transform › Clear Transformations): {ids?} — remove rotation, shear and scaling (the object keeps its centre)
- `transform.shear` (Object › Transform › Shear): {angle (degrees), ref?: 0..8 (reference point of the selection bounds, default 4: centre), ids?}
- `transform.flip` (Object › Transform › Flip): {axis: horizontal\|vertical, ref?: 0..8 (reference point of the selection bounds, default 4: centre), ids?}
- `transform.set` (Transform Panel): {x?, y? (measured from the rulers' zero point, view.zeroPoint), width?, height?, scaleX? (%), scaleY? (%), rotation? (°), shear? (°), ref?: 0..8, ids?, content?: bool (the placed graphic inside each frame; the frame stays. Default: whether the selection is content, when no ids are given), bounds?: [x0, y0, x1, y1] (content: the graphic's new bounds on the spread, as its handles drag it)} — reference-point based geometry; rotation and shear are absolute (Transformations are Totals decides whether nested objects measure them on the pasteboard)
- `transform.info` (Transform Values): {ids?} → {scaleX, scaleY (%), rotation, shear (°), content?: the same for a placed graphic} of the first target

## type

- `type.createOutlines` (Type › Create Outlines, Cmd+Shift+O): {ids?} — text frames become compound paths of their glyphs (one per line and text colour, grouped when several, so Ungroup separates the lines) → {ids}
- `type.onPath` (Type on a Path): {id: path, text?, start?: distance along the path, flip?, align?: baseline\|ascender\|descender\|center} → {story} — the text cursor goes into it
- `type.pathOptions` (Type › Type on a Path › Type on a Path Options…): {id?, start?, end?: distance along the path or null (the path's end), flip?, align?: baseline\|ascender\|descender\|center, delete?: true (Delete Type from Path)} — start and end are the brackets: start ≤ end, both on the path
- `type.pickUpFormat` (Apply Text Attributes (Eyedropper)): {frame, point} — the Eyedropper with text selected: the character and paragraph formatting (styles and overrides) of the text under the point go to the selected text
- `type.fillWithPlaceholder` (Type › Fill with Placeholder Text): {frame?, story?}
- `type.char` (Character Formatting): {attrs: {fontFamily?, fontStyle?, size?, leading?: {kind:auto}\|{kind:points,value}, tracking?, kerning?, hScale?, vScale?, baselineShift?, fill?, capitalization?, underline?, …}}
- `type.kernPair` (Kerning): {kerning: {kind: metrics\|optical\|none}\|{kind: manual, value: 1/1000 em}\|null} — at a caret in text, the pair at the caret (the character before the caret takes it); at the start of a story or paragraph, the next typing; a selection or frames take it like `type.char`
- `type.para` (Paragraph Formatting): {attrs: {align?, leftIndent?, firstLineIndent?, spaceBefore?, spaceAfter?, dropCapLines?, dropCapChars?, dropCapStyle?, dropCapAlignLeft?, dropCapScaleDescenders?, hyphenate?: bool (default true), composer?, tabs?, ruleAbove?/ruleBelow?: {on?, weight?, color?, tint?, columnWidth?, offset?, leftIndent?, rightIndent?} (only the named rule fields change), …}}
- `type.align` (Align): {align: left\|center\|right\|leftJustified\|…}
- `type.alignLeft` (Align Left, Cmd+Shift+L): {}
- `type.alignCenter` (Align Center, Cmd+Shift+C): {}
- `type.alignRight` (Align Right, Cmd+Shift+R): {}
- `type.justify` (Justify Left, Cmd+Shift+J): {}
- `type.bold` (Bold, Cmd+Shift+B): {on?: bool} — the family's bold style, keeping italic (style linking); toggles when `on` is left out
- `type.italic` (Italic, Cmd+Shift+I): {on?: bool} — the family's italic style, keeping the weight (style linking); toggles when `on` is left out
- `type.swapFillStroke` (Swap Text Fill and Stroke): {} — swap each selected character's resolved fill/stroke and tints; at a caret, swap the next typing's colors
- `type.underline` (Underline, Cmd+Shift+U): {}
- `type.allCaps` (All Caps, Cmd+Shift+K): {}
- `type.tateChuYoko` (Tate-Chu-Yoko): {on?: bool} — set the selected text horizontally within one em of a vertical line (toggles by default)
- `type.ruby` (Ruby): {text?, type?: group\|perCharacter, alignment?: left\|center\|right\|fullJustify\|jis\|equalAki\|oneAki, position?: aboveRight\|belowLeft, xOffset?, yOffset? (pt), font?, fontStyle? ("" = the text's), size? (pt; null = half the text size), xScale?, yScale? (%), openTypePro?: bool, autoTcyDigits?: 0-9, autoTcyIncludeRoman?: bool, autoTcyAutoScale?: bool, overhang?: none\|oneRuby\|halfRuby\|oneChar\|halfChar\|noLimit, parentSpacing?: noAdjustment\|bothSides\|aki121\|equalAki\|fullJustify, autoAlign?: bool, autoScaling?: bool, scalingPercent? (%), fill?, stroke? (swatch; "" = the text's), fillTint?, strokeTint? (%; null = the text's), strokeWeight? (pt; null = the text's), overprintFill?, overprintStroke?: auto\|on\|off} — the reading set over the selected text and how it is placed; empty text removes it. Per-character ruby separates the readings with U+3000
- `type.kenten` (Kenten): {on?: bool, kind?: sesameDot\|whiteSesameDot\|fisheye\|blackCircle\|smallBlackCircle\|bullseye\|blackTriangle\|whiteTriangle\|whiteCircle\|smallWhiteCircle\|custom, character?: text (custom kind), font?: family (custom kind), fontStyle?, size?: pt (null: half the text size), distance?: pt, position?: aboveRight\|belowLeft, alignment?: center\|start, xScale?: %, yScale?: %, fill?: swatch ("": the text's), fillTint?: %, stroke?: swatch, strokeTint?: %, strokeWeight?: pt, overprintFill?: auto\|on\|off, overprintStroke?: auto\|on\|off} — emphasis marks beside the selected characters (toggles by default; any setting turns them on)
- `type.shatai` (Shatai): {magnification?: % (0 = off), angle?: degrees, adjustRotation?: bool, adjustTsume?: bool} — slant the selected characters by compressing them across a direction
- `type.autoTateChuYoko` (Auto Tate-Chu-Yoko): {digits?: 0..10 (0 = off), includeRoman?: bool} — in vertical text, set runs of up to `digits` half-width digits (and roman letters) across one em, for the selected paragraphs
- `type.gridSettings` (Grid Settings): {alignment?: none\|romanBaseline\|emTop\|emCenter\|emBottom\|icfTop\|icfBottom, firstLineOnly?: bool, gyoudori?: 0..100 (0 = auto), paragraphGyoudori?: bool} — how the selected paragraphs sit on the baseline grid
- `type.rotateRoman` (Rotate Roman Characters in Vertical Text): {on?: bool} — half-width characters stand upright in vertical text, for the selected paragraphs (toggles by default)
- `type.romanWordBreak` (Roman Word Break): {on?: bool} — roman words in the selected paragraphs may break between any two letters, without a hyphen (toggles by default)
- `type.warichu` (Warichu): {on?: bool, lines?: int, size?: number, lineSpacing?: number, align?: auto\|left\|center\|right\|justify, charsBeforeBreak?: int, charsAfterBreak?: int} — set the selection as an inline note in smaller lines inside one line height (toggles by default)
- `type.storyDirection` (Story Direction): {vertical: bool} — the stories of the text selection or the selected frames: vertical lines run top to bottom and follow each other right to left, in every frame of the thread
- `type.kernStep` (Kerning/Tracking Step): {steps?: n (default 1; negative tightens), amount?: 1/1000 em (in place of steps × the document's kerningIncrement)} — with a caret, the manual kerning between the characters at the caret (from the pair's manual value, else 0); with a selection, the tracking of the selected text
- `type.sizeUp` (Increase Point Size, Cmd+Shift+.): {}
- `type.sizeDown` (Decrease Point Size, Cmd+Shift+,): {}
- `type.changeCase` (Type › Change Case): {case: upper\|lower\|title\|sentence} — the selected text, or the stories of selected frames (formatting kept)
- `type.openType` (OpenType): {feature?: dlig\|frac\|ordn\|swsh\|titl\|calt\|zero\|ssNN\|any tag, on?: bool (default: toggle), figures?: tabularLining\|proportionalOldstyle\|proportionalLining\|tabularOldstyle\|default, stylisticSets?: [1–20]} → {features, figures}
- `type.selectionAttrs` (Selection Attributes): {mixed?: bool} → resolved character/paragraph attributes at the text selection; with mixed, paraMixed lists the paragraph attributes that differ across the selected paragraphs; the selection's start as `selectedText` (one line, up to 60 characters)
- `type.openTypeFeatures` (OpenType Features): {} → the OpenType features and stylistic sets the selected text's fonts offer, each with its applied and available state (none, some or all of the selection)
- `type.feature` (Set OpenType Features): {features: {tag: true\|false, …}} — turns OpenType features on or off across the selected text, keeping each run's other features
- `type.tabs.get` (Get Tabs): {style?} → {tabs, leftIndent, firstLineIndent, rightIndent, width, frame?, column?: [x0,y0,x1,y1] (frame inner space)} — the first selected paragraph's (or the style's) stops and indents, and the width of its text column
- `type.tabs.add` (Add Tab): {position (pt from the column's left edge), align?: left\|center\|right\|char, leader? (≤ 8 characters), alignOn? (one character), style?} → {index, tabs} — a stop at the same position is replaced
- `type.tabs.move` (Move Tab): {index, position, style?} → {index, tabs}
- `type.tabs.change` (Change Tab): {index, align?: left\|center\|right\|char, leader?, alignOn?, style?} → {index, tabs}
- `type.tabs.remove` (Delete Tab): {index, style?} → {tabs}
- `type.tabs.clear` (Clear All Tabs): {style?} → {tabs}
- `type.tabs.repeat` (Repeat Tab): {index, width?, style?} → {index, tabs} — repeats the distance from the previous stop (or the left indent) to this one up to the column width less the right indent

## variables

- `variables.list` (Text Variables): {} → [{index, name, type, …, value (page 1)}]
- `variables.define` (Type › Text Variables › Define Text Variable…): {name, type: custom\|lastPageNumber\|chapterNumber\|fileName\|creationDate\|modificationDate\|outputDate\|runningHeader, text?, format?, style?, use?: firstOnPage\|lastOnPage, character?, section?, extension?, before?, after?} — creates or replaces by name
- `variables.delete` (Delete Text Variable): {name} — instances become plain text of their current value
- `variables.insert` (Type › Text Variables › Insert Variable): {name} — at the text insertion point

## view

- `view.zeroPoint` (Ruler Zero Point): {at?: [x, y] (points right of and below the ruler origin — document.preferences rulerOrigin: spread\|page\|spine; kept on the pasteboard), reset?: bool} → {zeroPoint: [x, y], locked}; with neither, reports it. Not an undo step; refused while locked
- `view.lockZeroPoint` (Lock Zero Point): {on?: bool (default: toggle)} → {locked} — a locked zero point can't be dragged, moved or reset

## xml

- `xml.tags` (Tags): {} → {root, tags: [{name, color}], styleMap: [[style, tag]], dtd: bool}
- `xml.newTag` (Window › Utilities › Tags › New Tag): {name, color?: [r, g, b]}
- `xml.deleteTag` (Delete Tag): {name} — tagged objects are untagged
- `xml.tagText` (Tag Text): {tag \| null (untag)} — the selected text becomes an inline element
- `xml.tag` (Tag Frame): {tag (made if new), ids? (default: the selection)} — `tag: null` untags
- `xml.mapStyle` (Map Styles to Tags): {style: paragraph style, tag \| null} — that style's paragraphs export as `<tag>` elements and import back with it
- `xml.structure` (Structure): {} → {root, elements: [{tag, id, kind, text?}]} in reading order
- `xml.loadDtd` (Window › Utilities › Tags › Load DTD…): {path \| text} — keep the DTD for validation and add a tag for each declared element; the root takes the first element's name unless already named → {elements}
- `xml.deleteDtd` (Delete DTD): {}
- `xml.validate` (Validate from Root Element): {} — check the structure (as exported) against the loaded DTD → {valid, problems: [{path, message}]}

## xref

- `xref.insert` (Type › Hyperlinks & Cross-References › Insert Cross-Reference…): {anchor? \| paragraph?: text to find (first paragraph containing it) \| story?: with para? \| para?: 0-based paragraph of `story`, format?: name (default Full Paragraph & Page Number)} — at the insertion point; the text updates itself as the destination moves
- `xref.list` (Cross-References): {} → [{story, pos, target, format, text}]
- `xref.formats` (Cross-Reference Formats): {} → [{name, definition}]
- `xref.defineFormat` (Type › Hyperlinks & Cross-References › Define Cross-Reference Format…): {name, definition} — building blocks: <fullPara />, <paraText />, <paraNum />, <pageNum />, <txtAnchrName />, <chapNum />, <fileName />, <partialPara delim=":" includeDelim="false" />; creates or replaces
- `xref.setFormat` (Set Cross-Reference Format): {story, index, format}
