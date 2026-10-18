# VectorCraft live effects

Generated from `apply_effect {}` (VectorCraft 0.13.1, 89 effects). Apply with `apply_effect {effect: id, params}`; edit later with
`command_run effect.setParams`, remove with `effect.remove`. Raster effects render at the document raster-effects resolution.
Grep this file rather than reading it whole.

## 3D and Materials

- `threeD.revolve` (Revolve): {angle: degrees (0..360, 360), offset: pt (0..100000, 0), edge: left|right, rotationX: degrees (0), rotationY: degrees (0), rotationZ: degrees (0), perspectiveAngle: degrees (0..160, 0; 0 is none, wider brings the eye nearer), perspective: % (0..100; the earlier form, read as the perspectiveAngle that shows the same view), segments: integer (8..128, 64), shade: bool (true), lightColor: #rrggbb (white, #ffffff; legacy directional light color), lights: null or array of 1..10 objects (color: #rrggbb, intensity: % 0..100, rotation: degrees -180..180, height: degrees 0..90, softness: % 0..100, behind: bool; overrides the single-light fields; ambient is shared), lightRotation: degrees (-180..180, 125.26; round the object on the page, 0 on its right, counterclockwise), lightHeight: degrees (0..90, 30; 0 beside the object, 90 straight in front), lightBehind: bool (false; true lights it from behind), lightIntensity: % (0..100, 80), lightSoftness: % (0..100, 0; how far round the object the light reaches), ambient: % (0..200, 25; Ambient Light), lightAzimuth: degrees (the earlier form: with lightElevation, read as the lightRotation, lightHeight and lightBehind of the same light), lightElevation: degrees (the earlier form, with lightAzimuth), cap: bool (true, close circular ends of open profiles; partial-sweep cut sides stay open), expandVisibleOnly: bool (true, trim covered opaque solid surfaces only on Expand Appearance)}. Shaded surfaces use smooth vector gradients automatically; intersecting profiles use approximate painter visibility.
- `threeD.extrude` (Extrude & Bevel): {depth: pt (0..2000, 50), twist: degrees (0..360, 0; the back turned against the front), taper: % (1..100, 100; the back's size), cap: bool (true: solid; false: hollow), bevel: none|classic|rounded|cove|step|ogee (none), bevelWidth: pt (0..1000, 4), bevelHeight: pt (0..1000, 4), bevelRepeat: integer (1..32, 1), bevelSpace: % (0..90, 0; flat between repeats), bevelInside: bool (false: added around the shape; true: carved into it), bevelBothSides: bool (false), rotationX: degrees (-180..180, -21.88), rotationY: degrees (-180..180, -23.4), rotationZ: degrees (-180..180, 9.06; the defaults are the Off-Axis Front position), perspectiveAngle: degrees (0..160, 0; 0 is none, wider brings the eye nearer), perspective: % (0..100; the earlier form, read as the perspectiveAngle that shows the same view), shade: bool (true), lightColor: #rrggbb (white, #ffffff; legacy directional light color), lights: null or array of 1..10 objects (color: #rrggbb, intensity: % 0..100, rotation: degrees -180..180, height: degrees 0..90, softness: % 0..100, behind: bool; overrides the single-light fields; ambient is shared), lightRotation: degrees (-180..180, 125.26; round the object on the page, 0 on its right, counterclockwise), lightHeight: degrees (0..90, 30; 0 beside the object, 90 straight in front), lightBehind: bool (false; true lights it from behind), lightIntensity: % (0..100, 80), lightSoftness: % (0..100, 0; how far round the object the light reaches), ambient: % (0..200, 25; Ambient Light), lightAzimuth: degrees (the earlier form: with lightElevation, read as the lightRotation, lightHeight and lightBehind of the same light), lightElevation: degrees (the earlier form, with lightAzimuth)}. The front face is the art, extruded backwards about the centre of its bounds; painted with the top fill (else the top stroke).
- `threeD.inflate` (Inflate): {depth: pt (0..2000, 0; flat depth between front and back), twist: degrees (0..360, 0; the back turned against the front), taper: % (1..100, 100; the back's size), cap: bool (true: solid; false: no back, a shell open behind), volume: % (0..100, 50; 50 rounds the edge like a half sphere), bothSides: bool (false: flat back), rotationX: degrees (-180..180, -21.88), rotationY: degrees (-180..180, -23.4), rotationZ: degrees (-180..180, 9.06; the defaults are the Off-Axis Front position), perspectiveAngle: degrees (0..160, 0; 0 is none, wider brings the eye nearer), perspective: % (0..100; the earlier form, read as the perspectiveAngle that shows the same view), shade: bool (true), lightColor: #rrggbb (white, #ffffff; legacy directional light color), lights: null or array of 1..10 objects (color: #rrggbb, intensity: % 0..100, rotation: degrees -180..180, height: degrees 0..90, softness: % 0..100, behind: bool; overrides the single-light fields; ambient is shared), lightRotation: degrees (-180..180, 125.26; round the object on the page, 0 on its right, counterclockwise), lightHeight: degrees (0..90, 30; 0 beside the object, 90 straight in front), lightBehind: bool (false; true lights it from behind), lightIntensity: % (0..100, 80), lightSoftness: % (0..100, 0; how far round the object the light reaches), ambient: % (0..200, 25; Ambient Light), lightAzimuth: degrees (the earlier form: with lightElevation, read as the lightRotation, lightHeight and lightBehind of the same light), lightElevation: degrees (the earlier form, with lightAzimuth)}. Painted with the top fill (else the top stroke).
- `threeD.rotate` (Rotate): {rotationX: degrees (-180..180, -21.88), rotationY: degrees (-180..180, -23.4), rotationZ: degrees (-180..180, 9.06; the defaults are the Off-Axis Front position), perspectiveAngle: degrees (0..160, 0; 0 is none, wider brings the eye nearer), perspective: % (0..100; the earlier form, read as the perspectiveAngle that shows the same view), shade: bool (true), lightColor: #rrggbb (white, #ffffff; legacy directional light color), lights: null or array of 1..10 objects (color: #rrggbb, intensity: % 0..100, rotation: degrees -180..180, height: degrees 0..90, softness: % 0..100, behind: bool; overrides the single-light fields; ambient is shared), lightRotation: degrees (-180..180, 125.26; round the object on the page, 0 on its right, counterclockwise), lightHeight: degrees (0..90, 30; 0 beside the object, 90 straight in front), lightBehind: bool (false; true lights it from behind), lightIntensity: % (0..100, 80), lightSoftness: % (0..100, 0; how far round the object the light reaches), ambient: % (0..200, 25; Ambient Light), lightAzimuth: degrees (the earlier form: with lightElevation, read as the lightRotation, lightHeight and lightBehind of the same light), lightElevation: degrees (the earlier form, with lightAzimuth)}. Turns the flat art in 3D about the centre of its bounds; every fill and stroke keeps its paint, shaded as one plane.

## Convert to Shape

- `convertToShape.rectangle` (Rectangle): {relative: bool (true), extraW: pt (18), extraH: pt (18), width: pt (absolute, 100), height: pt (absolute, 100)}
- `convertToShape.roundedRectangle` (Rounded Rectangle): {relative: bool (true), extraW: pt (18), extraH: pt (18), width, height (absolute), radius: pt (9)}
- `convertToShape.ellipse` (Ellipse): {relative: bool (true), extraW: pt (18), extraH: pt (18), width, height (absolute)}

## Distort & Transform

- `distort.freeDistort` (Free Distort): {corners: [[x,y]×4] (new positions of the bounding-box corners TL, TR, BR, BL in unit box coordinates; identity [[0,0],[1,0],[1,1],[0,1]])}
- `distort.puckerBloat` (Pucker & Bloat): {amount: % (-200 pucker … 200 bloat, default 0)}
- `distort.roughen` (Roughen): {size: 0..100 (5), relative: bool (true: % of size; false: pt), detail: per inch 0..100 (10), points: "smooth"|"corner", seed: int (0)}
- `distort.transform` (Transform): {scaleH: % (100), scaleV: % (100), moveH: pt (0; right = +), moveV: pt (0; down = +), rotate: deg (0; counter-clockwise), copies: 0..1000 (0; each copy transforms the last again), reflectX: bool (false; flips left to right), reflectY: bool (false; flips top to bottom), reference: 0..8 (4; the point of the bounds' 9-point grid it scales, rotates and reflects about: 0 top left, 4 centre, 8 bottom right), random: bool (false; each scale goes a random share of the way from 100 % to its value, each move and the angle a random share of theirs, differently for each object and the same on every redraw)}
- `distort.tweak` (Tweak): {h: amount (10), v: amount (10), relative: bool (true: % of size), anchors: bool (true), in: bool (true), out: bool (true), seed: int (0)}
- `distort.twist` (Twist): {angle: deg (-3600..3600, 10)}
- `distort.zigZag` (Zig Zag): {size: (10), relative: bool (false: pt; true: % of size), ridges: per segment 0..100 (4), points: "smooth"|"corner"}

## Path

- `path.offsetPath` (Offset Path): {offset: pt (10; negative insets), joins: "miter"|"round"|"bevel", miterLimit: (4)}
- `path.outlineObject` (Outline Object): {} type is drawn, exported and expanded as its glyph outlines and stays editable, and the effects after it reshape those outlines; paths and images do not change
- `path.outlineStroke` (Outline Stroke): {width?: pt (defaults to the stroke's weight)} the outline of the stroke the effect is on (on a fill or the object: the top stroke), with its caps, joins, dashes, alignment, width profile and arrowheads

## Stylize

- `stylize.roundCorners` (Round Corners): {radius: pt (10)}
- `stylize.scribble` (Scribble): {angle: deg (30; stored above -180 and up to 180: 270 becomes -90, -180 becomes 180), overlap: pt (0; Path Overlap: a positive value extends each line beyond the path, a negative one ends it inside), overlapVariation: pt (0..100, 0.5; how far each line's ends move along it), strokeWidth: pt (3), curviness: % (5), curvinessVariation: % (0..100, 0; how far each turn's curviness moves from curviness), spacing: pt (5), spacingVariation: pt (0..100, 0.5; how far each line's ends move across it), variation: pt (the earlier form, read as overlapVariation and spacingVariation unless those are given), seed: int (0)} (simplified: a single hatching scribble outlined to a filled shape)
- `stylize.dropShadow` (Drop Shadow, raster): {mode: blend mode ("multiply"), opacity: % (75), x: pt (7), y: pt (7), blur: pt (5), shade: "color"|"darkness" ("color"), color: "#rrggbb" ("#000000"), darkness: % (100)} (shade "darkness": the shadow is the object's own colors with `darkness` percent of black added instead of `color`: in a CMYK document their cyan, magenta and yellow stay and their black K becomes K + darkness × (1 − K); in an RGB document each channel is multiplied by 1 − darkness)
- `stylize.innerGlow` (Inner Glow, raster): {mode: blend mode ("screen"), opacity: % (75), blur: pt (5), color: "#rrggbb" ("#ffffff"), source: "center"|"edge" ("edge")}
- `stylize.outerGlow` (Outer Glow, raster): {mode: blend mode ("screen"), opacity: % (75), blur: pt (5), color: "#rrggbb" ("#ffff00")}
- `stylize.feather` (Feather, raster): {radius: pt (5)}
- `stylize.glowingEdges` (Glowing Edges, raster): {edgeWidth: pt 1..14 (2), edgeBrightness: 0..20 (6), smoothness: pt 1..15 (5)} finds alpha-weighted Sobel edges and draws bright coloured outlines on black

## Blur

- `blur.gaussian` (Gaussian Blur, raster): {radius: pt (5)}
- `blur.radial` (Radial Blur, raster): {amount: 1..100 (10; spin: an arc of `amount`°, zoom: the content scaled by up to about ±amount/2 %), method: "spin"|"zoom" ("spin"), quality: "draft"|"good"|"best" ("good"; 16, 64 or 256 samples)} blurs around the object's centre
- `blur.smart` (Smart Blur, raster): {radius: pt 0.1..100 (3), threshold: levels 0.1..100 (25; only colours closer than this blur together, so edges stay sharp), quality: "low"|"medium"|"high" ("medium"; 5, 7 or 9 samples across), blurMode: "normal"|"edgeOnly"|"overlayEdge" ("normal"; edgeOnly: the edges in white on black, overlayEdge: the edges in white over the blur)}. A pixel is on an edge when one of the pixels the search reads within the radius (all of them for a small radius, a grid of samples for a wide one) or one of its four nearest pixels differs from it by more than the threshold in a channel and its channels (alpha included) add up to at least that pixel's, so a step gives a line about as wide as the radius, and at least one pixel wide, on the side with the larger sum; the white and the black keep each pixel's coverage

## Artistic

- `artistic.cutout` (Cutout, raster): {levels: 2..8 (4; steps per colour channel: more levels, more flat colours), edgeSimplicity: 0..10 (4; simpler, smoother edges), edgeFidelity: 1..3 (2; keeps more of the edges' detail)} redraws the object as flat pieces of coloured paper, each piece painted in the average colour that falls into it, keeping its coverage. Original visual approximation; chosen VectorCraft defaults.
- `artistic.filmGrain` (Film Grain, raster): {grain: 0..20 (4; monochrome noise in shadows and midtones), highlightArea: 0..20 (0; widens the bright highlight area), intensity: 0..10 (10; highlight strength and quieter highlight grain)}. Smooth document-space grain follows translations; minification uses approximate footprint filtering. Coverage and pure white are preserved; black takes light speckles, and saturated colour channels may clip. Grain 0 with either highlightArea 0 or intensity 0 leaves the art unchanged. Original visual approximation; chosen VectorCraft defaults.
- `artistic.neonGlow` (Neon Glow, raster): {glowSize: -24..24 (5; above 0 the light areas glow, below 0 the dark ones; farther from 0 spreads the glow wider), glowBrightness: 0..50 (15; a stronger glow over dimmer greys), color: "#rrggbb" ("#4da6ff"; the glow's colour)} redraws the object in greys lit by a coloured glow, keeping its coverage. Original visual approximation; chosen VectorCraft defaults.
- `artistic.posterEdges` (Poster Edges, raster): {edgeThickness: 0..10 (2; wider lines), edgeIntensity: 0..10 (1; darker lines, on fainter edges too), posterization: 0..6 (2; posterization + 2 levels per colour channel)} reduces the object's colours and draws black lines on its edges, keeping its coverage. Original visual approximation; chosen VectorCraft defaults.

## Brush Strokes

- `brushStrokes.accentedEdges` (Accented Edges, raster): {edgeWidth: pt 1..14 (2), edgeBrightness: 0..50 (38; high: white chalk, low: black ink), smoothness: 1..15 (5; softens the object first and leaves its faint edges out)} accentuates the object's edges
- `brushStrokes.angledStrokes` (Angled Strokes, raster): {directionBalance: 0..100 (50; 0: every stroke a left diagonal, 100: every stroke a right diagonal, between: light areas right, dark areas left), strokeLength: pt 3..50 (15), sharpness: 0..10 (3)} repaints the object with diagonal strokes, the light areas' going the opposite way to the dark areas'
- `brushStrokes.crosshatch` (Crosshatch, raster): {strokeLength: pt 3..50 (9), sharpness: 0..20 (6), strength: 1..3 (1; passes of hatching)} keeps the object's detail under pencil hatching along both diagonals and roughens its edges
- `brushStrokes.darkStrokes` (Dark Strokes, raster): {balance: 0..10 (5; the higher, the more of the object counts as dark), blackIntensity: 0..10 (6), whiteIntensity: 0..10 (2)} paints the dark areas closer to black with short strokes and the light areas with long white strokes
- `brushStrokes.inkOutlines` (Ink Outlines, raster): {strokeLength: pt 1..50 (4), darkIntensity: 0..50 (20), lightIntensity: 0..50 (10)} redraws the object in pen and ink: fine outlines over its edges and ink strokes in its shadows
- `brushStrokes.spatter` (Spatter, raster): {sprayRadius: pt 0..25 (10; colours scattered up to 0.4 × this), smoothness: 1..15 (5; larger, smoother grains)} renders the object as if sprayed with a spatter airbrush
- `brushStrokes.sprayedStrokes` (Sprayed Strokes, raster): {strokeLength: pt 0..20 (12), sprayRadius: pt 0..25 (7; strokes scattered up to 0.3 × this), strokeDirection: "rightDiagonal"|"horizontal"|"leftDiagonal"|"vertical" ("rightDiagonal")} repaints the object with sprayed, angled strokes of its main colours
- `brushStrokes.sumiE` (Sumi-e, raster): {strokeWidth: pt 3..15 (10), strokePressure: 0..15 (2; more ink), contrast: 0..40 (16)} paints the object in the Japanese style, as if with a wet brush full of black ink on rice paper: soft, blurred edges and rich blacks, the colours keeping their hue and the object its shape

## Distort

- `distort.diffuseGlow` (Diffuse Glow, raster): {graininess: 0..10 (6; white grain, thicker in the glow), glowAmount: 0..20 (10), clearAmount: 0..20 (15; the higher, the more of the image stays clear of glow)} renders the object as if seen through a soft diffusion filter: its highlights glow white under see-through white grain
- `distort.glass` (Glass, raster): {distortion: 0..20 (5), smoothness: 1..15 (3), texture: "blocks"|"canvas"|"frosted"|"tinyLens"|"loaded" ("frosted"; "loaded" draws the image in textureImage and draws Frosted when there is none; the others are surfaces made in code), textureImage?: {path} | {name?, dataBase64} | string (Load Texture…: an image file that File › Place reads, within the renderer's pixel allowance, stored as its gray levels in a grayscale PNG in base64; a file sets texture to "loaded" unless texture is given, and the stored string, as effect.list gives it, is kept as it is), scaling: % 50..200 (100), invert: bool (false; turns the surface's heights over)} makes the object look as if seen through glass. A loaded texture lies one image pixel per point at 100 %, centered on the object's center and repeated; each pixel's luma is the surface's height, from 0 for black to 1 pt for white, and a transparent pixel counts as middle gray
- `distort.oceanRipple` (Ocean Ripple, raster): {rippleSize: 1..15 (9), rippleMagnitude: 0..20 (9)} adds randomly spaced ripples, as if the object were under water

## Sharpen

- `sharpen.unsharpMask` (Unsharp Mask, raster): {amount: % 1..500 (50), radius: pt 0.1..250 (1; σ of the blur edges are found against), threshold: levels 0..255 (0; smaller differences are left alone)}

## Sketch

- `sketch.halftonePattern` (Halftone Pattern, raster): {size: pt 1..12 (1; how far apart the screen's dots, rings or lines are), contrast: 0..50 (5; 50 draws pure black and white), patternType: "circle"|"dot"|"line" ("dot"; rings round the object's centre, dots on a square grid, horizontal lines)} redraws the object in black ink on white paper through a halftone screen whose ink covers as much as the colour is dark, keeping its coverage. Original visual approximation; chosen VectorCraft defaults.

## Pixelate

- `pixelate.colorHalftone` (Color Halftone, raster): {maxRadius: pt 4..127 (8; the radius of a dot at full strength, which fills its square cell), channel1: screen angle deg -360..360 (108), channel2: deg (162), channel3: deg (90), channel4: deg (45)} screens each colour channel (red, green, blue: channels 1 to 3; in CMYK documents cyan, magenta, yellow, black: 1 to 4) at its angle into dots whose area follows the channel's mean over their cell
- `pixelate.crystallize` (Crystallize, raster): {cellSize: pt 3..300 (10)} redraws the object as polygon crystals of solid colour around random points about cellSize apart
- `pixelate.mezzotint` (Mezzotint, raster): {type: "fineDots"|"mediumDots"|"grainyDots"|"coarseDots"|"shortLines"|"mediumLines"|"longLines"|"shortStrokes"|"mediumStrokes"|"longStrokes" ("fineDots")} turns each colour channel fully on or off against a random pattern of dots, lines or strokes: fully saturated colours
- `pixelate.pointillize` (Pointillize, raster): {cellSize: pt 3..300 (5)} redraws the object as randomly placed dots of its colours on a white canvas

## Texture

- `texture.craquelure` (Craquelure, raster): {crackSpacing: pt 2..100 (15; how far apart the cracks are), crackDepth: 0..10 (6; how deep and wide the cracks are, and how high the plates and the tones stand), crackBrightness: 0..10 (9; how brightly the plaster is lit)} paints the object on relief plaster cracked into plates and along the contours of its tones
- `texture.grain` (Grain, raster): {intensity: 0..100 (40), contrast: 0..100 (50; the image's contrast, 50 leaves it as it is), grainType: "regular"|"soft"|"sprinkles"|"clumped"|"contrasty"|"enlarged"|"stippled"|"horizontal"|"vertical"|"speckle" ("regular")} adds grain in 1 pt grains (2 pt Enlarged, clumps Clumped, streaks Horizontal and Vertical); Sprinkles and Stippled use the background colour, white
- `texture.mosaicTiles` (Mosaic Tiles, raster): {tileSize: pt 2..100 (12), groutWidth: 1..15 (3; the grout is half a point wide per step), lightenGrout: 0..10 (9; how light the grout is)} lays the object in irregular tiles bevelled at their edges, with sunken grout between them
- `texture.patchwork` (Patchwork, raster): {squareSize: pt 0..10 (4; 0 draws 1 pt squares), relief: 0..25 (8)} redraws the object in squares of the colour around their centres, raised to heights that follow its highlights and shadows, a little more or less at random, lit from the top left
- `texture.stainedGlass` (Stained Glass, raster): {cellSize: pt 2..50 (10), borderThickness: 1..20 (4; the lead between the panes, half a point wide per step, in the foreground colour: black), lightIntensity: 0..10 (3; a light behind the object's centre, fading out towards its corners)} redraws the object as single-coloured panes around random points about cellSize apart
- `texture.texturizer` (Texturizer, raster): {texture: "brick"|"burlap"|"canvas"|"sandstone" ("canvas"; surfaces made in code), scaling: % 50..200 (100), relief: 0..50 (4), lightDirection: "bottom"|"bottomLeft"|"left"|"topLeft"|"top"|"topRight"|"right"|"bottomRight" ("top"), invert: bool (false; turns the surface's heights over)} paints the object on a surface in relief

## Video

- `video.deinterlace` (De-Interlace, raster): {eliminate: "odd"|"even" ("odd"; which field lines are taken out), create: "duplication"|"interpolation" ("duplication"; a line taken out becomes a copy of the line above, or the average of the lines above and below)} the field lines are the rows of the document's raster grid (Document Raster Effects Settings › Resolution), numbered from 1 at the top of the page
- `video.ntscColors` (NTSC Colors, raster): {} makes colours a television signal can't carry (luma plus chroma past 110 % of white, or luma minus chroma below −20 %) less saturated, keeping their brightness

## Color Adjustments

- `adjust.brightnessContrast` (Brightness/Contrast): {brightness: -100..100 (0; bends the tones, black and white stay), contrast: -100..100 (0)} recolours the object's fills, strokes, type, meshes and embedded images (each colour keeps its model)
- `adjust.curves` (Curves): {points: "x,y x,y …" or [[x, y], …] (input, output 0..255; a smooth monotone curve through them, flat past the ends; "0,0 128,128 255,255"), channel: "rgb"|"red"|"green"|"blue" ("rgb")} recolours as Brightness/Contrast does
- `adjust.hueSaturation` (Hue/Saturation): {hue: deg -180..180 (0), saturation: -100..100 (0), lightness: -100..100 (0), colorize: bool (false; true: every colour takes hue `hue` (0..360) at saturation (100 + saturation) / 2 %)} recolours as Brightness/Contrast does
- `adjust.levels` (Levels): {inputBlack: 0..255 (0), inputWhite: 0..255 (255), gamma: 0.1..10 (1; above 1 lightens the midtones), outputBlack: 0..255 (0), outputWhite: 0..255 (255), channel: "rgb"|"red"|"green"|"blue" ("rgb")} recolours as Brightness/Contrast does
- `adjust.shiftToColor` (Shift to Color): {color: "#rrggbb" ("#ff8000"), amount: 0..100 % (50), preserveLightness: bool (true: colours take the target's hue and saturation and keep their lightness; false: they mix with it)} recolours as Brightness/Contrast does
- `adjust.temperatureTint` (Temperature/Tint): {temperature: -100 (cooler) .. 100 (warmer) (0), tint: -100 (greener) .. 100 (more magenta) (0)} recolours as Brightness/Contrast does

## Warp

- `warp.arc` (Arc): {bend: % (-100..100, 50), horizontal: % distortion (0), vertical: % distortion (0), orientation: "horizontal"|"vertical"}
- `warp.arcLower` (Arc Lower): {bend: % (-100..100, 50), horizontal: % distortion (0), vertical: % distortion (0), orientation: "horizontal"|"vertical"}
- `warp.arcUpper` (Arc Upper): {bend: % (-100..100, 50), horizontal: % distortion (0), vertical: % distortion (0), orientation: "horizontal"|"vertical"}
- `warp.arch` (Arch): {bend: % (-100..100, 50), horizontal: % distortion (0), vertical: % distortion (0), orientation: "horizontal"|"vertical"}
- `warp.bulge` (Bulge): {bend: % (-100..100, 50), horizontal: % distortion (0), vertical: % distortion (0), orientation: "horizontal"|"vertical"}
- `warp.shellLower` (Shell Lower): {bend: % (-100..100, 50), horizontal: % distortion (0), vertical: % distortion (0), orientation: "horizontal"|"vertical"}
- `warp.shellUpper` (Shell Upper): {bend: % (-100..100, 50), horizontal: % distortion (0), vertical: % distortion (0), orientation: "horizontal"|"vertical"}
- `warp.flag` (Flag): {bend: % (-100..100, 50), horizontal: % distortion (0), vertical: % distortion (0), orientation: "horizontal"|"vertical"}
- `warp.wave` (Wave): {bend: % (-100..100, 50), horizontal: % distortion (0), vertical: % distortion (0), orientation: "horizontal"|"vertical"}
- `warp.fish` (Fish): {bend: % (-100..100, 50), horizontal: % distortion (0), vertical: % distortion (0), orientation: "horizontal"|"vertical"}
- `warp.rise` (Rise): {bend: % (-100..100, 50), horizontal: % distortion (0), vertical: % distortion (0), orientation: "horizontal"|"vertical"}
- `warp.fisheye` (Fisheye): {bend: % (-100..100, 50), horizontal: % distortion (0), vertical: % distortion (0), orientation: "horizontal"|"vertical"}
- `warp.inflate` (Inflate): {bend: % (-100..100, 50), horizontal: % distortion (0), vertical: % distortion (0), orientation: "horizontal"|"vertical"}
- `warp.squeeze` (Squeeze): {bend: % (-100..100, 50), horizontal: % distortion (0), vertical: % distortion (0), orientation: "horizontal"|"vertical"}
- `warp.twist` (Twist): {bend: % (-100..100, 50), horizontal: % distortion (0), vertical: % distortion (0), orientation: "horizontal"|"vertical"}

## Pathfinder

- `pathfinder.add` (Add): {} (groups and layers: live Pathfinder over the members)
- `pathfinder.intersect` (Intersect): {} (groups and layers: live Pathfinder over the members)
- `pathfinder.exclude` (Exclude): {} (groups and layers: live Pathfinder over the members)
- `pathfinder.subtract` (Subtract): {} (groups and layers: live Pathfinder over the members)
- `pathfinder.minusBack` (Minus Back): {} (groups and layers: live Pathfinder over the members)
- `pathfinder.divide` (Divide): {} (groups and layers: live Pathfinder over the members)
- `pathfinder.trim` (Trim): {} (groups and layers: live Pathfinder over the members)
- `pathfinder.merge` (Merge): {} (groups and layers: live Pathfinder over the members)
- `pathfinder.crop` (Crop): {} (groups and layers: live Pathfinder over the members)
- `pathfinder.outline` (Outline): {} (groups and layers: live Pathfinder over the members)

## cropMarks

- `cropMarks` (Crop Marks): {style?: "roman"|"japanese" (default: the japaneseCropMarks preference when applied)} trim marks in [Registration] around the object's bounds, following it

## rasterize

- `rasterize` (Rasterize, raster): {colorModel: "document" (the document's mode, RGB or CMYK)|"grayscale"|"bitmap" ("document"), useDocumentResolution: bool (true: Document Raster Effects Settings › Resolution), resolution: ppi 1..2400 (72; with useDocumentResolution false), background: "white"|"transparent" ("transparent"), antiAlias: "none"|"art"|"type" ("art"; none: hard edges), clippingMask: bool (false; the image clipped to the art's outline), addAround: pt 0..1000 (0; room around the art)} draws the object as an image of square pixels over its bounds and the room around them, leaving its paths, type and other art as they are; when it is the object's only raster effect, Expand Appearance makes the image Object › Rasterize makes
