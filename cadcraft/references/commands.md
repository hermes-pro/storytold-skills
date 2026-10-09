# CADCraft command catalog

Generated from `cadcraft-cli commands` (CADCraft 0.3.0, 295 commands), grouped by menu. Run any of them with
`execute {command, params}` (MCP) or `cadcraft-cli run --cmd 'id {json}'`; type the id or an alias at `command_line`
for the interactive version. `?` = optional, `a|b` = choices, `→ {...}` = what it returns, `hex` = an entity handle.
Points are `[x, y]`. Angles are degrees unless noted. *(prompts)* marks commands that also run interactively.

## File

- `new` (New Drawing...) — aliases: `qnew`: {metric?: bool}
- `open` (Open...): {path} \| {data: base64, name}
- `close` (Close): {index?}
- `closeall` (Close All): {}
- `qsave` (Save) — aliases: `save`: {path?}
- `saveas` (Save As...): {path, format?: dxf\|dwg}
- `document.switch` (Switch Drawing): {index}
- `document.bytes` (Drawing as bytes): {format?: dxf} → {data: base64}
- `pagesetup` (Page Setup Manager...): {layout?: current, paper?: "A4"\|"A3"\|"Letter"\|"ANSI B"\|…, width?, height? (mm), landscape?, margins?: [l,b,r,t] mm, lineweights?, plotArea?, scale?, scaleToFit?, center?, plotStyleTable?}
- `plot` (Print...) — aliases: `print`: {path? (else returns base64 `data`), layout?: current\|"Model", paper?, landscape?, fit?: bool, scale?, lineweights?: bool}
- `exportpdf` (Export to PDF...): {path? (else returns base64 `data`), layout?, paper?, landscape?, fit?, lineweights?}

## Edit

- `undo` (Undo) — aliases: `u`: {count?: n}
- `redo` (Redo) — aliases: `mredo`: {count?: n}
- `cutclip` (Cut): {handles?}
- `copyclip` (Copy): {handles?}
- `copybase` (Copy with Base Point): {handles?, base: [x,y]}
- `pasteclip` (Paste) *(prompts)*: {at?: [x,y]} (default: same offset as copied)
- `pasteorig` (Paste to Original Coordinates): {}
- `erase.selection` (Clear): {}
- `selectall` (Select All) — aliases: `ai_selall`: {}
- `select` (Select) *(prompts)*: {handles: [hex]} \| {window: [[x,y],[x,y]], crossing?: bool} \| {at: [x,y]} \| {clear: true} \| {add?: bool}
- `qselect` (Quick Select...) — aliases: `qs`: {type?: "Line"\|"Circle"\|..., property?, operator?: "="\|"!="\|">"\|"<"\|"*" (wildcard), value?, mode?: new\|append\|exclude, applyTo?: drawing\|selection, layer?, color?} → selected handles
- `selectioncycling` (Selection Cycling): {on?: bool}
- `find` (Find...): {find, replace?, matchCase?: bool, wholeWord?: bool}

## View

- `zoom` (Zoom) *(prompts)* — aliases: `z`: {mode: extents\|all\|window\|previous\|in\|out\|center\|scale\|object, p1?, p2?, center?, height?, factor?}
- `zoom.previous` (Zoom Previous): {}
- `zoom.window` (Zoom Window) *(prompts)*: {p1, p2}
- `zoom.in` (Zoom In): {}
- `zoom.out` (Zoom Out): {}
- `zoom.all` (Zoom All): {}
- `zoom.extents` (Zoom Extents): {}
- `zoom.object` (Zoom Object): {handles?}
- `pan` (Pan) *(prompts)* — aliases: `p`: {delta: [dx,dy]} \| {from, to} \| {center}
- `pan.left` (Pan Left): {}
- `pan.right` (Pan Right): {}
- `pan.up` (Pan Up): {}
- `pan.down` (Pan Down): {}
- `regen` (Regen) — aliases: `re`: {}
- `regenall` (Regen All) — aliases: `rea`: {}
- `redraw` (Redraw) — aliases: `r`: {}
- `vports` (New Viewports...) *(prompts)*: {count?: 1-4, arrangement?, p1?, p2?, layout?}
- `vports.1` (1 Viewport) *(prompts)*: {p1?, p2?, layout?}
- `vports.2` (2 Viewports) *(prompts)*: {p1?, p2?, arrangement?: vertical\|horizontal, layout?}
- `vports.3` (3 Viewports) *(prompts)*: {p1?, p2?, arrangement?: right\|left\|above\|below\|vertical\|horizontal, layout?}
- `vports.4` (4 Viewports) *(prompts)*: {p1?, p2?, layout?}

## Draw

- `line` (Line) *(prompts)* — aliases: `l`: {points: [[x,y],...], closed?: bool}
- `pline` (Polyline) *(prompts)* — aliases: `pl`: {vertices: [[x,y] \| {p:[x,y], bulge, startWidth, endWidth}], closed?, width?}
- `circle` (Circle) *(prompts)* — aliases: `c`: {center, radius} \| {center, diameter} \| {p1, p2} \| {p1, p2, p3}
- `arc` (Arc) *(prompts)* — aliases: `a`: {p1, p2, p3} \| {center, radius, start, end (degrees)} \| {start, center, end}
- `rectang` (Rectangle) *(prompts)* — aliases: `rec`, `rectangle`: {p1, p2 \| dimensions: [l, w] (p2 picks the quadrant) \| area + length\|breadth, rotation? (deg), fillet?, chamfer?: [d1, d2], width?, elevation?, thickness?}
- `polygon` (Polygon) *(prompts)* — aliases: `pol`: {sides, center, radius, inscribed?: bool, angle?} \| {sides, edge: [[x,y],[x,y]]}
- `ellipse` (Ellipse) *(prompts)* — aliases: `el`: {center, major: [dx,dy], ratio, start?, end? (degrees)}
- `point` (Point) *(prompts)* — aliases: `po`: {at: [x,y]} \| {points: [...]}
- `point.multiple` (Multiple Point) *(prompts)*: {points: [...]}
- `xline` (Construction Line) *(prompts)* — aliases: `xl`: {base, through} \| {base, angle (degrees)} \| {base, hor\|ver: true} \| {vertex, start, end} (bisect) \| {handle, distance, side} \| {handle, through} (offset)
- `ray` (Ray) *(prompts)*: {base, through}
- `spline` (Spline) *(prompts)* — aliases: `spl`: {fit: [[x,y],...]} \| {control: [...], degree?}
- `donut` (Donut) *(prompts)* — aliases: `do`, `doughnut`: {center, inside, outside}
- `text` (Single Line Text) *(prompts)* — aliases: `dt`, `dtext`: {at, text, height?, rotation? (degrees), justify?: L\|C\|R\|M\|TL\|TC\|TR\|ML\|MC\|MR\|BL\|BC\|BR}
- `mtext` (Multiline Text) *(prompts)* — aliases: `t`, `mt`: {at, text, height?, width?, attach?: 1..9, rotation?}
- `arc.sce` (Start, Center, End) *(prompts)*: {start, center, end}
- `arc.sca` (Start, Center, Angle) *(prompts)*: {start, center, angle (degrees, + = CCW)}
- `arc.scl` (Start, Center, Length) *(prompts)*: {start, center, length (chord; negative = major arc)}
- `arc.sea` (Start, End, Angle) *(prompts)*: {start, end, angle (degrees, + = CCW)}
- `arc.sed` (Start, End, Direction) *(prompts)*: {start, end, direction (degrees \| [dx,dy])}
- `arc.ser` (Start, End, Radius) *(prompts)*: {start, end, radius (negative = major arc)}
- `arc.cse` (Center, Start, End) *(prompts)*: {center, start, end}
- `arc.csa` (Center, Start, Angle) *(prompts)*: {center, start, angle (degrees)}
- `arc.csl` (Center, Start, Length) *(prompts)*: {center, start, length (chord)}
- `arc.continue` (Continue) *(prompts)*: {end} (tangent from the last line/arc) \| {start, direction, end}
- `circle.cd` (Center, Diameter) *(prompts)*: {center, diameter}
- `circle.2p` (2 Points) *(prompts)*: {p1, p2}
- `circle.3p` (3 Points) *(prompts)*: {p1, p2, p3}
- `circle.ttr` (Tan, Tan, Radius) *(prompts)*: {h1, p1, h2, p2, radius} (lines, circles, arcs, polyline segments; nearest solution to the picks)
- `circle.ttt` (Tan, Tan, Tan) *(prompts)*: {h1, p1, h2, p2, h3, p3}
- `ellipse.axis` (Axis, End) *(prompts)*: {p1, p2, distance} \| {p1, p2, p3} (axis endpoints, then half the other axis)
- `ellipse.arc` (Elliptical Arc) *(prompts)*: {center, major: [dx,dy], ratio, start, end (degrees)} \| {p1, p2, distance, start, end}
- `divide` (Divide) *(prompts)* — aliases: `div`: {handle, segments, block?, align?: bool}
- `measure` (Measure) *(prompts)* — aliases: `me`: {handle, length, block?, align?: bool, from?: [x,y] (end to start at)}
- `revcloud` (Rectangular) *(prompts)*: {p1, p2} \| {points: [...]} \| {freehand: [...]} \| {handle}, arcLength?, style?: normal\|calligraphy, reverse?
- `revcloud.polygonal` (Polygonal) *(prompts)*: {points: [[x,y],...], arcLength?}
- `revcloud.freehand` (Freehand) *(prompts)*: {freehand: [[x,y],...], arcLength?}
- `wipeout` (Wipeout) *(prompts)*: {points: [[x,y],...]} \| {handle (closed polyline), erase?: bool} \| {frames: on\|off\|display}
- `3dpoly` (3D Polyline) *(prompts)* — aliases: `3p`: {points: [[x,y,z?],...], closed?}
- `mline` (Multiline) *(prompts)* — aliases: `ml`: {points, scale?, justification?: top\|zero\|bottom, closed?} (two offset polylines)
- `helix` (Helix) *(prompts)*: {center, baseRadius, topRadius?, height?, turns?, ccw?} (3D polyline approximation)
- `spline.cv` (Control Vertices) *(prompts)*: {control: [[x,y],...], degree?: 1..10 (default 3), closed?}
- `centermark` (Center Mark) *(prompts)*: {handle \| handles} (circles/arcs; lines on the CENTER linetype)
- `centerline` (Center Line) *(prompts)*: {h1, h2} (two lines)
- `hatch` (Hatch...) *(prompts)* — aliases: `h`, `bh`, `-hatch`: {points?: [[x,y]] (internal points) \| handles?: [hex] (closed objects), pattern?: "ANSI31", scale?, angle? (degrees), associative?}
- `gradient` (Gradient...) *(prompts)* — aliases: `gd`: {points? \| handles?, color1?, color2?, angle?}
- `boundary` (Boundary...) *(prompts)* — aliases: `bo`, `bpoly`: {points: [[x,y]]}
- `region` (Region) — aliases: `reg`: {handles?}
- `block` (Make...) *(prompts)* — aliases: `b`, `-block`, `bmake`: {name, base: [x,y], handles?, keep?: "convert"\|"retain"\|"delete", description?}
- `attdef` (Define Attributes...) *(prompts)* — aliases: `att`, `-attdef`: {tag, prompt?, default?, at, height?, invisible?}
- `base` (Base): {at: [x,y]}
- `table` (Table...) *(prompts)* — aliases: `tb`: {at: [x,y], rows (data rows), cols, rowHeight?, colWidth?, cells?: [[text]], title?: text, header?: [text]}
- `table.set` (Set Table Cell): {handle, row, col, text}
- `table.insertrow` (Insert Row): {handle, row? (insert before; default: append), height?}
- `table.deleterow` (Delete Row): {handle, row}
- `table.insertcol` (Insert Column): {handle, col? (insert before; default: append), width?}
- `table.deletecol` (Delete Column): {handle, col}
- `table.merge` (Merge Cells): {handle, row, col, rows, cols}
- `table.unmerge` (Unmerge Cells): {handle, row, col}

## Modify

- `hatchedit` (Hatch Edit) — aliases: `he`: {handles?, pattern?, scale?, angle?}
- `attedit` (Single...) — aliases: `ate`, `eattedit`: {handle, values: {TAG: value}}
- `battman` (Block Attribute Manager...): {name}
- `erase` (Erase) *(prompts)* — aliases: `e`, `delete`: {handles?: [hex]} (default: selection)
- `move` (Move) *(prompts)* — aliases: `m`: {handles?, from?: [x,y], to?: [x,y] \| delta: [dx,dy]}
- `copy` (Copy) *(prompts)* — aliases: `co`, `cp`: {handles?, delta: [dx,dy] \| from,to, count?: n}
- `rotate` (Rotate) *(prompts)* — aliases: `ro`: {handles?, base: [x,y], angle (degrees), copy?: bool}
- `scale` (Scale) *(prompts)* — aliases: `sc`: {handles?, base: [x,y], factor, copy?: bool}
- `mirror` (Mirror) *(prompts)* — aliases: `mi`: {handles?, p1, p2, erase?: bool}
- `stretch` (Stretch) *(prompts)* — aliases: `s`: {window: [[x,y],[x,y]], delta: [dx,dy]}
- `offset` (Offset) *(prompts)* — aliases: `o`: {handle, distance, side: [x,y]}
- `trim` (Trim) *(prompts)* — aliases: `tr`: {handle, pick: [x,y], edges?: [hex]}
- `extend` (Extend) *(prompts)* — aliases: `ex`: {handle, pick: [x,y], edges?: [hex]}
- `fillet` (Fillet) *(prompts)* — aliases: `f`: {h1, p1, h2, p2, radius?} (lines, arcs, circles) \| {handle, polyline: true, radius?}
- `chamfer` (Chamfer) *(prompts)* — aliases: `cha`: {h1, p1, h2, p2, d1?, d2?}
- `explode` (Explode) *(prompts)* — aliases: `x`: {handles?}
- `arrayrect` (Rectangular Array) *(prompts)*: {handles?, rows, cols, rowSpacing, colSpacing}
- `arraypolar` (Polar Array) *(prompts)*: {handles?, center, count, angle? (degrees, default 360), rotate?: bool}
- `break` (Break) *(prompts)* — aliases: `br`: {handle, p1, p2}
- `breakatpoint` (Break At Point): {handle, at}
- `join` (Join) *(prompts)* — aliases: `j`: {handles?}
- `overkill` (Delete Duplicate Objects): {handles?}
- `pedit` (Polyline) *(prompts)* — aliases: `pe`: {handle \| handles, option: close\|open\|join\|width\|fit\|spline\|decurve\|reverse\|ltypegen\|vertex, width?, handles2? (join), fuzz?, action?: move\|insert\|straighten\|width, index?, to?, startWidth?, endWidth?, convert?: bool}
- `splinedit` (Spline) *(prompts)* — aliases: `spe`: {handle, option: close\|open\|reverse\|refit\|purge\|polyline\|move, fit?, index?, to?, precision?}
- `lengthen` (Lengthen) *(prompts)* — aliases: `len`: {handle, pick?: [x,y] (end), delta? \| deltaAngle? (deg) \| percent? \| total? \| totalAngle? (deg) \| to?: [x,y]} ({handle} alone measures)
- `align` (Align) *(prompts)* — aliases: `al`: {handles?, s1, d1, s2?, d2?, scale?: bool}
- `blend` (Blend) *(prompts)* — aliases: `blendcurves`: {h1, p1, h2, p2, continuity?: tangent\|smooth}
- `ncopy` (Copy Nested Objects) *(prompts)*: {handle (block reference), pick?: [x,y] (nearest nested object; default all), delta? \| from,to}
- `chspace` (Change Space) *(prompts)*: {handles?, to?: "model" \| layout name, viewport?: handle}
- `flatten` (Flatten Objects) *(prompts)*: {handles?} (z = 0, 3D polylines become polylines)
- `arraypath` (Path Array) *(prompts)*: {handles?, path (handle), count? (default 6) \| spacing?, align?: bool (default true)}
- `textedit` (Edit Text...) *(prompts)* — aliases: `ed`, `ddedit`: {handle, text} (text, mtext, attribute definitions, dimension text override)
- `grip.move` (Grip Stretch): {handle, index, to} (stretch the grip) \| {handles?, index, baseHandle?, to, mode: "move", copy?} (move about the grip)
- `grip.stretch` (Grip Stretch): {handle, index, to}
- `grip.rotate` (Grip Rotate): {handles?, base \| baseHandle+index, angle (degrees) \| to, copy?}
- `grip.scale` (Grip Scale): {handles?, base \| baseHandle+index, factor \| to, copy?}
- `grip.mirror` (Grip Mirror): {handles?, base \| baseHandle+index, to (second mirror point), copy?}
- `properties` (Properties) — aliases: `pr`, `props`, `ch`: {handles?} → properties of the selection
- `matchprop` (Match Properties) — aliases: `ma`, `painter`: {source, targets: [hex]}

## Dimension

- `dimlinear` (Linear) *(prompts)* — aliases: `dli`, `dimlin`: {p1, p2, at, rotation? (degrees; default: horizontal/vertical from `at`), text?} \| {object: hex, at} (associative)
- `dimaligned` (Aligned) *(prompts)* — aliases: `dal`, `dimali`: {p1, p2, at, text?}
- `dimradius` (Radius) *(prompts)* — aliases: `dra`, `dimrad`: {handle, at?} \| {center, point}
- `dimdiameter` (Diameter) *(prompts)* — aliases: `ddi`, `dimdia`: {handle, at?} \| {center, point}
- `dimangular` (Angular) *(prompts)* — aliases: `dan`, `dimang`: {vertex, p1, p2, at} \| {lines: [hex, hex], at} \| {arc: hex, at} (associative)
- `dimarc` (Arc Length) *(prompts)* — aliases: `dar`: {handle, at}
- `dimordinate` (Ordinate) *(prompts)* — aliases: `dor`, `dimord`: {feature, leader, xtype?: bool}
- `dimcontinue` (Continue) *(prompts)* — aliases: `dco`, `dimcont`: {points: [[x,y]...]} (continues the last linear dimension)
- `dimbaseline` (Baseline) *(prompts)* — aliases: `dba`, `dimbase`: {points: [[x,y]...]} (baseline from the last linear dimension)
- `qdim` (Quick Dimension): {handles?, at: [x,y], vertical?: bool}
- `dim` (Dimension) *(prompts)*: {p1, p2, at}
- `mleader` (Multileader) *(prompts)* — aliases: `mld`: {points: [[arrow], ..., [landing]], text}
- `dimstyle.update` (Update): {handles?}
- `dimoverride` (Override) *(prompts)* — aliases: `dov`, `dimover`: {handles?, <DimStyle fields or DIM* variables: values>, clear?: bool, text?: override text}
- `dimreassociate` (Reassociate Dimensions) *(prompts)* — aliases: `dre`: {handles?} (dimensions; attaches their definition points to the objects under them)
- `dimdisassociate` (Disassociate Dimensions) *(prompts)* — aliases: `dda`: {handles?}
- `dimtedit.home` (Home): {handles?}
- `dimtedit.angle` (Angle): {handles?, angle: degrees}
- `dimtedit.left` (Left): {handles?}
- `dimtedit.center` (Center): {handles?}
- `dimtedit.right` (Right): {handles?}
- `dimtedit` (Dimension Text Edit): {handles?, at?: [x,y], mode?: home\|angle\|left\|center\|right, angle?}
- `dimspace` (Dimension Space): {base: hex, handles: [hex], spacing?: number (default DIMDLI)}
- `dimstyle.dimension` (Dimension Style...): same as `dimstyle`
- `dimstyle.list` (List Dimension Styles): {name?} → styles (with all variables for `name`)
- `dimstyle.rename` (Rename Dimension Style): {from, to}
- `dimstyle.delete` (Delete Dimension Style): {name} (not Standard, the current style or one in use)
- `dimstyle.current` (Set Current Dimension Style): {name}
- `dimstyle.override` (Dimension Style Override): {handles?, <style fields or DIM* variables: values>, clear?: bool} (per-dimension overrides)
- `dimconstraint` (Dimensional Constraint) *(prompts)* — aliases: `dcon`: {type: linear\|aligned\|horizontal\|vertical\|angular\|radius\|diameter, h1, p1?, h2?, p2?, expr? \| value?, name?}

## Insert

- `insert` (Block...) *(prompts)* — aliases: `i`, `-insert`, `ddinsert`: {name, at: [x,y], scale?, rotation? (degrees), attribs?: {TAG: value}, explode?: bool}
- `layout.new` (New Layout): {name?, viewport?: bool (default true)} → {name, viewport}

## Format

- `layout.set` (Switch Layout): {name: "Model" \| layout name}
- `layer` (Layers) — aliases: `la`, `layers`: {}
- `layer.new` (New Layer): {name, color?, linetype?, lineweight? (mm), current?: bool}
- `layer.set` (Set Layer Properties): {name, on?, frozen?, locked?, plot?, color?, linetype?, lineweight?, transparency?, description?, newVpFreeze?, newName?}
- `layer.current` (Make Current) — aliases: `clayer`: {name}
- `layer.delete` (Delete Layer): {name}
- `laymcur` (Make Object's Layer Current): {handles?}
- `laymch` (Layer Match): {handles?, layer}
- `laycur` (Change to Current Layer): {handles?}
- `layiso` (Isolate Layer): {handles?}
- `layuniso` (Unisolate Layer): {}
- `layfrz` (Freeze Layer): {handles?}
- `layoff` (Layer Off): {handles?}
- `laylck` (Lock Layer): {handles?}
- `layulk` (Unlock Layer): {handles?}
- `layon` (Turn All Layers On): {}
- `laythw` (Thaw All Layers): {}
- `layerp` (Previous Layer): {}
- `layerstate.save` (Save Layer State): {name}
- `layerstate.restore` (Restore Layer State): {name}
- `layerstate.list` (List Layer States): {} → states
- `layerstate.delete` (Delete Layer State): {name}
- `layerstate.rename` (Rename Layer State): {from, to}
- `layout` (Layout) — aliases: `lo`: {option: new\|copy\|delete\|rename\|set\|list, name?, to?}
- `layout.delete` (Delete Layout): {name}
- `layout.rename` (Rename Layout): {from?: current layout, to}
- `layout.copy` (Copy Layout): {from, to?}
- `layout.list` (List Layouts): → [{name, tabOrder, page, viewports}]
- `color` (Color...) — aliases: `col`, `colour`: {color: "ByLayer" \| "red" \| 1..255 \| "r,g,b"}
- `linetype` (Linetype...) — aliases: `lt`, `ltype`: {current?: name, load?: name \| "*"}
- `lweight` (Lineweight...) — aliases: `lw`, `lineweight`: {lineweight: mm \| ByLayer}
- `units` (Units...) — aliases: `un`: {lunits?: 1..5, luprec?: 0..8, aunits?: 0..4, auprec?: 0..8, insunits?}
- `limits` (Drawing Limits): {min: [x,y], max: [x,y]}
- `style` (Text Style...) — aliases: `st`: {name, font?, bigFont?, height?, widthFactor?, oblique? (degrees), backwards?, upsideDown?, vertical?, annotative?, current?} → styles
- `style.list` (List Text Styles): {} → text styles
- `style.rename` (Rename Text Style): {from, to}
- `style.delete` (Delete Text Style): {name} (not Standard, the current style or one in use)
- `style.current` (Set Current Text Style): {name}
- `dimstyle` (Dimension Style...) — aliases: `d`, `dst`, `ddim`: {name, current?, <style fields or DIM* variables, e.g. arrowSize / DIMASZ, DIMTSZ, DIMBLK, DIMTAD, DIMLUNIT…>} → styles
- `tablestyle` (Table Style...) — aliases: `ts`: {name, textHeight?, margin?, title?, header?, current?} → styles
- `mleaderstyle` (Multileader Style...) — aliases: `mls`: {name, arrowSize?, textHeight?, landingGap?, dogleg?, textStyle?, current?} → styles
- `ddptype` (Point Style...): {pdmode, pdsize}
- `rename` (Rename...): {table: layer\|linetype\|style\|dimstyle\|block, from, to}

## Tools

- `draworder.front` (Bring to Front): {handles?}
- `draworder.back` (Send to Back): {handles?}
- `dist` (Distance) *(prompts)* — aliases: `di`: {p1, p2}
- `id` (ID Point) *(prompts)*: {at}
- `list` (List) *(prompts)* — aliases: `li`, `ls`: {handles?}
- `area` (Area) *(prompts)* — aliases: `aa`: {points: [[x,y],...]} \| {handle}
- `time` (Time): {}
- `status` (Status): {}
- `count` (Count): {block?}
- `dsettings` (Drafting Settings...) — aliases: `ds`, `se`: {snapunit?: [x,y], gridunit?: [x,y], polarang? (degrees), gridmajor?}
- `setvar` (Set Variable) — aliases: `set`: {name, value}
- `cal` (QuickCalc) — aliases: `quickcalc`, `qc`: {expr: "(3+4)*2^2", vars?: {x: 1}}
- `massprop` (Region/Mass Properties): {handles?}
- `radius.measure` (Radius): {handle}
- `angle.measure` (Angle): {vertex, p1, p2} \| {h1, h2}
- `gccoincident` (Coincident) *(prompts)*: {h1, p1?, h2?, p2?, h3?, p3?} (h = handle; p = "start"/"end"/"mid"/"center"/"v<i>"/"seg<i>"/"object" or a pick point [x, y])
- `gcperpendicular` (Perpendicular) *(prompts)*: {h1, p1?, h2?, p2?, h3?, p3?} (h = handle; p = "start"/"end"/"mid"/"center"/"v<i>"/"seg<i>"/"object" or a pick point [x, y])
- `gcparallel` (Parallel) *(prompts)*: {h1, p1?, h2?, p2?, h3?, p3?} (h = handle; p = "start"/"end"/"mid"/"center"/"v<i>"/"seg<i>"/"object" or a pick point [x, y])
- `gctangent` (Tangent) *(prompts)*: {h1, p1?, h2?, p2?, h3?, p3?} (h = handle; p = "start"/"end"/"mid"/"center"/"v<i>"/"seg<i>"/"object" or a pick point [x, y])
- `gchorizontal` (Horizontal) *(prompts)*: {h1, p1?, h2?, p2?, h3?, p3?} (h = handle; p = "start"/"end"/"mid"/"center"/"v<i>"/"seg<i>"/"object" or a pick point [x, y])
- `gcvertical` (Vertical) *(prompts)*: {h1, p1?, h2?, p2?, h3?, p3?} (h = handle; p = "start"/"end"/"mid"/"center"/"v<i>"/"seg<i>"/"object" or a pick point [x, y])
- `gccollinear` (Collinear) *(prompts)*: {h1, p1?, h2?, p2?, h3?, p3?} (h = handle; p = "start"/"end"/"mid"/"center"/"v<i>"/"seg<i>"/"object" or a pick point [x, y])
- `gcconcentric` (Concentric) *(prompts)*: {h1, p1?, h2?, p2?, h3?, p3?} (h = handle; p = "start"/"end"/"mid"/"center"/"v<i>"/"seg<i>"/"object" or a pick point [x, y])
- `gcsmooth` (Smooth) *(prompts)*: {h1, p1?, h2?, p2?, h3?, p3?} (h = handle; p = "start"/"end"/"mid"/"center"/"v<i>"/"seg<i>"/"object" or a pick point [x, y])
- `gcsymmetric` (Symmetric) *(prompts)*: {h1, p1?, h2?, p2?, h3?, p3?} (h = handle; p = "start"/"end"/"mid"/"center"/"v<i>"/"seg<i>"/"object" or a pick point [x, y])
- `gcequal` (Equal) *(prompts)*: {h1, p1?, h2?, p2?, h3?, p3?} (h = handle; p = "start"/"end"/"mid"/"center"/"v<i>"/"seg<i>"/"object" or a pick point [x, y])
- `gcfix` (Fix) *(prompts)*: {h1, p1?, h2?, p2?, h3?, p3?} (h = handle; p = "start"/"end"/"mid"/"center"/"v<i>"/"seg<i>"/"object" or a pick point [x, y])
- `autoconstrain` (AutoConstrain) *(prompts)*: {handles?, tolerance?, angleTolerance? (degrees), types?: [names]}
- `constraintbar` (Constraint Bars) *(prompts)*: {mode?: show\|hide\|showall\|hideall, handles?}
- `constraintbar.showall` (Show All Constraint Bars): {}
- `constraintbar.hideall` (Hide All Constraint Bars): {}
- `dcaligned` (Aligned) *(prompts)*: {h1, p1?, h2?, p2?, expr? \| value?, name?}
- `dchorizontal` (Horizontal) *(prompts)*: {h1, p1?, h2?, p2?, expr? \| value?, name?}
- `dcvertical` (Vertical) *(prompts)*: {h1, p1?, h2?, p2?, expr? \| value?, name?}
- `dcangular` (Angular) *(prompts)*: {h1, p1?, h2?, p2?, expr? \| value?, name?}
- `dcradius` (Radius) *(prompts)*: {h1, p1?, h2?, p2?, expr? \| value?, name?}
- `dcdiameter` (Diameter) *(prompts)*: {h1, p1?, h2?, p2?, expr? \| value?, name?}
- `dcdisplay` (Dynamic Dimensions) *(prompts)*: {mode?: show\|hide\|showall\|hideall, handles?}
- `dcdisplay.showall` (Show All Dynamic Dimensions): {}
- `dcdisplay.hideall` (Hide All Dynamic Dimensions): {}
- `delconstraint` (Delete Constraints) *(prompts)*: {handles? \| ids?: [n]}
- `parameters` (Parameters Manager) — aliases: `par`, `parametersclose`: {} lists; {name, expr \| value, description?} sets (new name = user parameter) and re-solves; {delete: name}
- `constraintsettings` (Constraint Settings) — aliases: `csettings`: {infer?, distanceTolerance?, angleTolerance?, autoTypes?: [names], barsVisible?, barTransparency?, dimsVisible?}

## Layouts & plotting

- `viewport.set` (Viewport Properties): {handle? (default: selected viewports), scale?: paper units per model unit \| "1:50", viewHeight?, center?: [x,y], locked?, freeze?: [layer], thaw?: [layer], colors?: {layer: color \| null}}
- `vplayer` (Viewport Layer Freeze): {handle?, freeze?: [layer], thaw?: [layer], colors?: {layer: color ("red" \| 1..255 \| "r,g,b") \| null to clear}}

## Parametric

- `dclinear` (Linear) *(prompts)*: {h1, p1?, h2?, p2?, expr? \| value?, name?}
- `constraints.inspect` (Inspect Constraints): {} → constraints, glyph anchors, parameters, settings

## Other

- `qselect.info` (Quick Select Properties): {applyTo?: drawing\|selection, type?} → object types with counts and the properties available for `type`
- `view.set` (Set View): {center: [x,y], height}
- `view.get` (Get View): {}
- `leader` (Leader) — aliases: `lead`: {points: [[x,y]...], text?}
- `wblock` (Write Block) — aliases: `w`: {path, name? \| handles?, base?}
- `purge` (Purge) — aliases: `pu`, `-purge`: {} (unused blocks, layers, linetypes, styles)
- `blocks.list` (List Blocks): {}
- `reverse` (Reverse) *(prompts)*: {handles?} (lines, polylines, 3D polylines, splines)
- `mview` (Viewports) *(prompts)* — aliases: `mv`: {p1?, p2? (default: printable area), count?: 1-4, arrangement?: vertical\|horizontal\|left\|right\|above\|below, layout?}
- `mspace` (Model Space (in viewport)) — aliases: `ms`: {handle?: viewport, at?: [x,y] paper point inside a viewport} (default: the last active or first viewport)
- `pspace` (Paper Space) — aliases: `ps`: {}
- `properties.set` (Set Properties): {handles?, layer?, color?, linetype?, lineweight?, ltscale?, transparency?, visible?, <geometry fields: radius, center, start, end, text, height, rotation…>}
- `ltscale` (Linetype Scale) — aliases: `lts`: {scale}
- `drawing.inspect` (Inspect Drawing): {entities?: bool, limit?: n}
- `entities` (Query Entities): {type?, layer?, window?: [[x,y],[x,y]], limit?, offset?}
- `ortho` (Ortho Mode): {on?: bool}
- `grid` (Grid Display): {on?: bool}
- `snap` (Snap Mode): {on?: bool}
- `polar` (Polar Tracking): {on?: bool}
- `otrack` (Object Snap Tracking): {on?: bool}
- `dynmode` (Dynamic Input): {on?: bool}
- `lwdisplay` (Show/Hide Lineweight): {on?: bool}
- `isodraft` (Isometric Drafting): {on?: bool}
- `transparencydisplay` (Show/Hide Transparency): {on?: bool}
- `qpmode` (Quick Properties): {on?: bool}
- `osnap` (Object Snap) — aliases: `os`, `ddosnap`: {on?: bool, modes?: ["end","mid",...] \| osmode?: n}
- `getvar` (Get Variable): {name}
- `sysvars` (List System Variables): {}
- `measuregeom` (Measure Geometry): {mode: distance\|radius\|angle\|area, ...}
- `geomconstraint` (Geometric Constraint) *(prompts)* — aliases: `gcon`: {type: coincident\|collinear\|concentric\|fix\|parallel\|perpendicular\|horizontal\|vertical\|tangent\|smooth\|symmetric\|equal, h1, p1?, h2?, p2?, h3?, p3?}
