# VectorCraft live effects

Generated from `apply_effect {}` (VectorCraft 0.7.0). Apply with `apply_effect {effect: id, params}`; edit later with
`run_command effect.setParams`, remove with `effect.remove`. Raster effects render at the document raster-effects resolution.

## Convert to Shape

- `convertToShape.rectangle` (Rectangle): {relative: bool (true), extraW: pt (18), extraH: pt (18), width: pt (absolute, 100), height: pt (absolute, 100)}
- `convertToShape.roundedRectangle` (Rounded Rectangle): {relative: bool (true), extraW: pt (18), extraH: pt (18), width, height (absolute), radius: pt (9)}
- `convertToShape.ellipse` (Ellipse): {relative: bool (true), extraW: pt (18), extraH: pt (18), width, height (absolute)}

## Distort & Transform

- `distort.freeDistort` (Free Distort): {corners: [[x,y]×4] new positions of the bounding-box corners TL, TR, BR, BL in unit box coordinates (identity [[0,0],[1,0],[1,1],[0,1]])}
- `distort.puckerBloat` (Pucker & Bloat): {amount: % (-200 pucker … 200 bloat, default 0)}
- `distort.roughen` (Roughen): {size: 0..100 (5), relative: bool (true: % of size; false: pt), detail: per inch 0..100 (10), points: "smooth"|"corner", seed: int (0)}
- `distort.transform` (Transform): {scaleH: % (100), scaleV: % (100), moveH: pt (0), moveV: pt (0), rotate: deg (0), copies: int (0), reflectX: bool, reflectY: bool}
- `distort.tweak` (Tweak): {h: amount (10), v: amount (10), relative: bool (true: % of size), anchors: bool (true), in: bool (true), out: bool (true), seed: int (0)}
- `distort.twist` (Twist): {angle: deg (-3600..3600, 10)}
- `distort.zigZag` (Zig Zag): {size: (10), relative: bool (false: pt; true: % of size), ridges: per segment 0..100 (4), points: "smooth"|"corner"}

## Path

- `path.offsetPath` (Offset Path): {offset: pt (10; negative insets), joins: "miter"|"round"|"bevel", miterLimit: (4)}
- `path.outlineStroke` (Outline Stroke): {width?: pt (defaults to the stroke's weight)} the outline of the stroke the effect is on (on a fill or the object: the top stroke), with its caps, joins, dashes, alignment, width profile and arrowheads

## Stylize

- `stylize.roundCorners` (Round Corners): {radius: pt (10)}
- `stylize.scribble` (Scribble): {angle: deg (30), overlap: pt (0), strokeWidth: pt (3), curviness: % (5), spacing: pt (5), variation: pt (0.5), seed: int (0)} (simplified: a single hatching scribble outlined to a filled shape)
- `stylize.dropShadow` (Drop Shadow, raster): {mode: blend mode ("multiply"), opacity: % (75), x: pt (7), y: pt (7), blur: pt (5), color: "#rrggbb" ("#000000")}
- `stylize.innerGlow` (Inner Glow, raster): {mode: blend mode ("screen"), opacity: % (75), blur: pt (5), color: "#rrggbb" ("#ffffff"), source: "edge"|"center"}
- `stylize.outerGlow` (Outer Glow, raster): {mode: blend mode ("screen"), opacity: % (75), blur: pt (5), color: "#rrggbb" ("#ffff00")}
- `stylize.feather` (Feather, raster): {radius: pt (5)}

## Blur

- `blur.gaussian` (Gaussian Blur, raster): {radius: pt (5)}

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
