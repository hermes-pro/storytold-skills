# FigCraft layer properties (`node.set`)

Generated from the live `node.set` docs and `frame.presets` (FigCraft 0.6.0, 95 keys). These keys go in
`set_properties {ids, props}`, in `create_node {props}` and in `node.create`/`frame.create` `props`. Unknown keys are an
error that lists every known key. Grep this file rather than reading it whole.

## Value forms (tested)

- Colour: `"#RRGGBB"` or `"#RRGGBBAA"`. `fill`/`stroke` set one solid paint; `fills`/`strokes` take a list, bottom first.
- Paints in `fills`: `"#hex"`, `{"type":"solid","color":"#hex","opacity"?}`,
  `{"type":"linearGradient","stops":["#a","#b"]}` (default runs top → bottom),
  stops as `[{"position":0..1,"color":"#hex"}]`, optional `from`/`to` handles in the unit box; `radialGradient` alike.
  Images: `image.place {path, parent?, x, y, width, height, mode: fill|fit|crop|tile}`; patterns: `fill.pattern`.
- Effects: `[{"type":"dropShadow","color":"#00000040","offset":[0,4],"radius":8,"spread"?:0,"showBehind"?:false}]`,
  `innerShadow` alike, `{"type":"layerBlur","radius":120}`, `backgroundBlur`, `noise`, `texture`, `glass`
  (`effect.add {type}` adds one with its defaults).
- `cornerRadius`: a number or `[tl,tr,br,bl]`. `padding`: a number or `[top,right,bottom,left]`.
- `lineHeight`: `"auto"`, px, or `"150%"`. `letterSpacing`: px or `"2%"`.
- `fontStyle` is a style name the family has: `text.fonts {family}` lists them (`[]` = the family is not installed and
  the text silently falls back). Inter has Regular, Italic, SemiBold ("Semi Bold" works too), Bold.
- `sizingH`/`sizingV`: `fixed`, `hug` (auto layout frames and text) or `fill` (children of an auto layout frame).
- `constraints`: `{"horizontal": "left|right|leftRight|center|scale", "vertical": "top|bottom|topBottom|center|scale"}`.

## What inspect returns

`get_node` / `inspect_document` nodes carry: `id, name, type` (FRAME, GROUP, COMPONENT, COMPONENT_SET, INSTANCE, TEXT,
RECTANGLE, ELLIPSE, STAR, POLYGON, VECTOR, LINE, SECTION, BOOLEAN_OPERATION…), `x, y` (relative to the parent frame),
`width, height, absoluteBounds`, `fills, strokes, strokeWeight, effects, cornerRadius, clip, opacity`, `layout {mode, gap,
padding, mainAlign, crossAlign, …}`, `sizing {horizontal, vertical}`, text fields (`characters, fontFamily, fontStyle,
fontSize, lineHeight, letterSpacing, textAlign, textAutoResize, styledRuns`), `boundVariables {field: VariableID}`,
`styles {fill, stroke, effect, grid, text}`, instances' `mainComponent` and `componentProperties`, components'
`componentPropertyDefinitions`, `overrides`, `interactions`, `devStatus`, `annotations`, `devResources`, and `children`.

## Layer

- `name`
- `visible`
- `locked`
- `opacity` (0-1)
- `blend`
- `constrainProportions`
- `description`
- `pluginData` {k: v}

## Geometry

- `x`
- `y` (relative to the parent frame; groups don't count)
- `width`
- `height`
- `rotation` (degrees)
- `cornerRadius` (n or [tl,tr,br,bl])
- `cornerSmoothing` (0-1)
- `constraints` {horizontal, vertical}
- `pointCount`
- `innerRadius`
- `arcStart`
- `arcSweep`
- `arcInner`

## Fill, stroke, effects

- `fills` (paints or colours)
- `fill` (colour)
- `strokes`
- `stroke` (colour)
- `strokeWeight`
- `strokeAlign` (inside|center|outside)
- `strokeSides` [t,r,b,l]
- `strokeTopWeight / strokeRightWeight / strokeBottomWeight / strokeLeftWeight` (one side; turns on individual strokes)
- `strokeCap / startCap / endCap`
- `strokeJoin`
- `miterAngle` (degrees: sharper joins bevel; or miterLimit as a ratio)
- `dashes` [..]
- `widthProfile` (preset uniform|wedge|taper|eye|rounded|pinch, [[t, scale], ...] or null)
- `brush` (preset id, {preset, spacing, sizeJitter, rotationJitter, scatter, seed} or null)
- `effects`
- `clip`
- `isMask`
- `grids`
- `exports`
- `booleanOperation` (a boolean group's operation, or an operand's own; null: the group's)
- `operandOperation` (a layer in a boolean group: how it combines with the operands below it; null: the group's)

## Auto layout (on the frame)

- `layout` (null|horizontal|vertical|grid|{...})
- `gap`
- `crossGap`
- `padding` (n or [t,r,b,l])
- `paddingTop/Right/Bottom/Left`
- `mainAlign` (min|center|max, or the auto gaps spaceBetween|spaceAround|spaceEvenly)
- `crossAlign` (min|center|max|baseline: first text baselines, horizontal layouts)
- `contentAlign` (wrapped lines: auto = packed where crossAlign says | spaceBetween)
- `wrap` (rows of a horizontal layout, columns of a vertical one)
- `strokesIncluded` (the frame's inside stroke takes up space)
- `reverseZ` (canvas stacking: true = first on top)
- `columnGap / rowGap` (aliases of gap / crossGap)
- `gridColumns`
- `gridRows`
- `columnTracks / rowTracks` ([120 | "1fr" | "auto" | {sizing, value}])

## Auto layout (on a child)

- `gridColumn / gridRow` (0-based cell anchor, null = auto)
- `gridColumnSpan`
- `gridRowSpan`
- `gridAlignH / gridAlignV` (a grid child's alignment in its cell: min|center|max, auto/null = the frame's)
- `sizingH / sizingV` (fixed|hug|fill)
- `absolute` (ignore auto layout; follows constraints)
- `minWidth`
- `maxWidth`
- `minHeight`
- `maxHeight` (null removes)

## Text

- `characters`
- `fontFamily`
- `fontStyle`
- `fontSize`
- `lineHeight` (auto|px|"150%")
- `letterSpacing` (px|"2%")
- `textAlign` (left|center|right|justified)
- `textAlignVertical`
- `textAutoResize` (widthAndHeight|height|none|truncate)
- `textDecoration`
- `textDecorationStyle` (solid|dotted|wavy)
- `textDecorationThickness / textDecorationOffset` (auto|px|"10%" of the font size; the offset runs from the baseline down to an underline's top edge)
- `textDecorationSkipInk` (underlines break around descenders)
- `textDecorationColor` (colour, or auto/null: the text's)
- `textCase` (original|upper|lower|title|smallCaps)
- `paragraphSpacing`
- `paragraphIndent`
- `listStyle` (none|bulleted|numbered; with start/end: the paragraphs those chars touch)
- `indentation` (list nesting level 0-8, same range rule)
- `listSpacing` (px between list items, in place of paragraphSpacing)
- `hangingPunctuation`
- `hangingList` (markers outside the box)
- `leadingTrim` (vertical trim: none|capHeight)
- `maxLines`
- `features` ({tag: bool}, e.g. {"liga": false, "tnum": true})
- `fontVariations / variationSettings` ({axis: number}, e.g. {"wght": 550, "wdth": 85}; null = none)

## Prototype

- `interactions`
- `overflow`

## Frame presets (`frame.create {preset}`)

- Phone: iPhone 16 393×852, iPhone 16 Pro 402×874, iPhone 16 Pro Max 440×956, iPhone 16 Plus 430×932, iPhone SE 320×568, Android Compact 412×917, Android Medium 700×840
- Tablet: iPad mini 8.3 744×1133, iPad Pro 11" 834×1194, iPad Pro 12.9" 1024×1366, Surface Pro 8 1440×960, Android Expanded 1280×800
- Desktop: MacBook Air 1280×832, MacBook Pro 14" 1512×982, MacBook Pro 16" 1728×1117, Desktop 1440×1024, Wireframe 1440×1024, TV 1280×720
- Presentation: Slide 16:9 1920×1080, Slide 4:3 1024×768
- Watch: Apple Watch Series 10 42mm 187×223, Apple Watch 41mm 176×215, Apple Watch 45mm 198×242
- Paper: A4 595×842, A5 420×595, A6 297×420, Letter 612×792, Tabloid 792×1224
- Social media: Instagram post 1080×1350, Instagram story 1080×1920, Facebook post 1200×630, X post 1200×675, LinkedIn post 1200×1200, YouTube thumbnail 1280×720, Dribbble shot 1600×1200


## Also accepted (not in the node.set doc string)

- `devStatus` (none|readyForDev|completed): handoff status of a top-level frame or section (tested)
- `sectionContentsHidden`, `maskType` (alpha|vector|luminance): see upstream docs/mcp.md
