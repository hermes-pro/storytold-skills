# MaterialCraft node library

Generated from `materialcraft-cli nodes` (= `library_list`; MaterialCraft 0.1.2, 222 nodes). Add one with
`node_add {def: "<id>", params: {...}}`, set one with `node_param {id, param, value}`. Line format:
`` `id` (Label): what it does. In: ports. Out: ports. Params: `param` type=default [min..max] or {index option} ``.
Port kinds: Gray, Color, Any. Enum values are passed as the **index**. Colors are shown as sRGB `"#rrggbb"`, the
form `node_param` takes (it stores linear RGBA: `"#808080"` reads back as 0.216; an array `[r, g, b, a]` is taken as
linear). A gradient is set as `[[pos, "#rrggbb"], ...]`. Ranges are the UI ranges: the engine does not clamp
values outside them. Grep this file rather than reading it whole.

Categories: Atomic nodes (24), Graph items (5), Texture generators/Patterns (38), Texture generators/Noises (51), Filters/Adjustments (25), Filters/Blending (10), Filters/Channels (2), Filters/Blurs (6), Filters/Effects (20), Filters/Normal map (10), Filters/Tiling (3), Filters/Transforms (5), Filters/Flood fill (8), Material filters/PBR utilities (6), Material filters/Blending (2), Material filters/Weathering (7)

## Atomic nodes

- `bitmap` (Bitmap): A bitmap resource of the package, resampled to the node size. In: none. Out: `output` Color. Params: `resource` text="".
- `blend` (Blend): Blends a foreground over a background with a blending mode, weighted by opacity and an optional mask. In: `foreground` Any, `background` Any, `mask` Gray. Out: `output` Any. Params: `opacity` float=1 [0..1]; `mode` enum=0 {0 Copy, 1 Add (Linear dodge), 2 Subtract, 3 Multiply, 4 Add Sub, 5 Max (Lighten), 6 Min (Darken), 7 Switch, 8 Divide, 9 Overlay, 10 Screen, 11 Soft light, 12 Difference, 13 Color dodge, 14 Color burn, 15 Hard light}; `alpha` enum=0 {0 Use source alpha, 1 Ignore alpha}.
- `blur` (Blur): Gaussian blur. In: `input` Any. Out: `output` Any. Params: `intensity` float=2 [0..32].
- `channels_shuffle` (Channels Shuffle): Builds a color image from any channels of two inputs. In: `input1` Any, `input2` Any. Out: `output` Color. Params: `red` enum=0 {0 Input 1 red, 1 Input 1 green, 2 Input 1 blue, 3 Input 1 alpha, 4 Input 2 red, 5 Input 2 green, 6 Input 2 blue, 7 Input 2 alpha, 8 Black, 9 White}; `green` enum=1 {0 Input 1 red, 1 Input 1 green, 2 Input 1 blue, 3 Input 1 alpha, 4 Input 2 red, 5 Input 2 green, 6 Input 2 blue, 7 Input 2 alpha, 8 Black, 9 White}; `blue` enum=2 {0 Input 1 red, 1 Input 1 green, 2 Input 1 blue, 3 Input 1 alpha, 4 Input 2 red, 5 Input 2 green, 6 Input 2 blue, 7 Input 2 alpha, 8 Black, 9 White}; `alpha` enum=3 {0 Input 1 red, 1 Input 1 green, 2 Input 1 blue, 3 Input 1 alpha, 4 Input 2 red, 5 Input 2 green, 6 Input 2 blue, 7 Input 2 alpha, 8 Black, 9 White}.
- `curve` (Curve): Remaps values through a tone curve. In: `input` Any. Out: `output` Any. Params: `curve` curve=curve.
- `directional_blur` (Directional Blur): Blurs along one direction. In: `input` Any. Out: `output` Any. Params: `intensity` float=10 [0..64]; `angle` float=0 [-1..1].
- `directional_warp` (Directional Warp): Offsets the input along a direction, by an intensity map. In: `input` Any, `intensity_input` Gray. Out: `output` Any. Params: `intensity` float=10 [0..64]; `angle` float=0 [-1..1].
- `distance` (Distance): Grows white areas of a mask into a distance gradient; with a source, spreads its colors outward. In: `mask` Gray, `source` Any. Out: `output` Any. Params: `distance` float=10 [0..256]; `combine` bool=false.
- `emboss` (Emboss): Lights the input with the relief of a height map. In: `input` Any, `height` Gray. Out: `output` Any. Params: `intensity` float=5 [0..32]; `light_angle` float=0.375 [-1..1]; `highlight` color="#ffffff"; `shadow` color="#000000".
- `gradient_dynamic` (Gradient (Dynamic)): Maps a grayscale input through the colors of a row of a gradient image. In: `input` Gray, `gradient` Color. Out: `output` Color. Params: `position` float=0.5 [0..1]; `orientation` enum=0 {0 Horizontal, 1 Vertical}.
- `gradient_map` (Gradient Map): Maps grayscale values to colors along a gradient. In: `input` Gray. Out: `output` Any. Params: `gradient` gradient=gradient(2 keys); `mode` enum=0 {0 Color, 1 Grayscale}.
- `grayscale_conversion` (Grayscale Conversion): Weighted sum of the RGBA channels. In: `input` Color. Out: `output` Gray. Params: `red` float=0.333 [0..1]; `green` float=0.333 [0..1]; `blue` float=0.333 [0..1]; `alpha` float=0 [0..1]; `flatten_alpha` bool=false.
- `hsl` (HSL): Hue, saturation and lightness adjustments (0.5 = unchanged). In: `input` Color. Out: `output` Color. Params: `hue` float=0.5 [0..1]; `saturation` float=0.5 [0..1]; `lightness` float=0.5 [0..1].
- `levels` (Levels): Remaps the input range, midtones and output range. In: `input` Any. Out: `output` Any. Params: `in_low` float=0 [0..1]; `in_mid` float=0.5 [0..1]; `in_high` float=1 [0..1]; `out_low` float=0 [0..1]; `out_high` float=1 [0..1].
- `normal` (Normal): Converts a height map to a tangent-space normal map. In: `input` Gray. Out: `output` Color. Params: `intensity` float=1 [0..10]; `format` enum=0 {0 OpenGL, 1 DirectX}; `height_alpha` bool=false.
- `pixel_processor` (Pixel Processor): Computes every pixel with a function graph ($pos, $size; sample the inputs). In: `input0` Any, `input1` Any, `input2` Any, `input3` Any. Out: `output` Any. Params: `function` function=function; `output` enum=0 {0 Color, 1 Grayscale}.
- `value_processor` (Value Processor): Computes one value with a function graph and outputs it as a uniform image. In: `input0` Any. Out: `output` Any. Params: `function` function=function.
- `sharpen` (Sharpen): Unsharp mask. In: `input` Any. Out: `output` Any. Params: `intensity` float=1 [0..10].
- `transformation` (Transformation 2D): Offsets, scales and rotates the input. In: `input` Any. Out: `output` Any. Params: `offset` float2=[0, 0] [-1..1]; `scale` float2=[1, 1] [0.01..10]; `rotation` float=0 [-1..1]; `filtering` enum=0 {0 Bilinear, 1 Nearest}; `matte` color="#000000" a0.
- `uniform` (Uniform Color): A single color or gray value. In: none. Out: `output` Any. Params: `color` color="#bcbcbc"; `mode` enum=0 {0 Color, 1 Grayscale}.
- `warp` (Warp): Distorts the input along the slopes of a gradient map. In: `input` Any, `gradient` Gray. Out: `output` Any. Params: `intensity` float=1 [0..32].
- `fx_map` (FX-Map): Instances up to three patterns on a grid, at random positions or in a random quadtree, with per-instance scale, rotation, position and luminance jitter. Scale 1 fills an instance's cell. Unconnected: soft discs. Tiles. In: `pattern0` Gray, `pattern1` Gray, `pattern2` Gray. Out: `output` Gray. Params: `mode` enum=2 {0 Grid, 1 Random, 2 Quadtree}; `count` int=64 [1..20000]; `x_amount` int=4 [1..256]; `y_amount` int=4 [1..256]; `subdivisions` int=3 [0..8]; `split_chance` float=0.5 [0..1]; `scale` float=0.9 [0..2]; `scale_random` float=0.2 [0..1]; `rotation` float=0 [-1..1]; `rotation_random` float=0 [0..1]; `position_random` float=0 [0..1]; `luminance` float=1 [0..1]; `luminance_random` float=0.4 [0..1]; `pattern_random` float=1 [0..1]; `blending` enum=0 {0 Max, 1 Add, 2 Alpha over}; `seed_offset` int=0 [0..10000].
- `svg` (SVG): Draws SVG path data (M L H V C S Q T Z, absolute and relative; y points down) filled and optionally stroked, anti-aliased. In: none. Out: `output` Color. Params: `path` text="M50 4 C80 20 94 55 52 96 L50 90 L48 96 C6 55 20 20 50 4 Z M49 22 Q46 55 50 84 Q54 55 51 22 Z"; `units` enum=1 {0 0..1, 1 0..100}; `fill` color="#ffffff"; `fill_rule` enum=1 {0 Even-odd, 1 Non-zero}; `stroke_width` float=0 [0..64]; `stroke` color="#bcbcbc".
- `text` (Text): Draws text with a built-in single-stroke font (A–Z, a–z, 0–9, punctuation). \n starts a new line. In: none. Out: `output` Color. Params: `text` text="MaterialCraft"; `size` float=0.09 [0..1]; `position` float2=[0.5, 0.5] [0..1]; `alignment` enum=1 {0 Left, 1 Center, 2 Right}; `color` color="#ffffff"; `weight` float=0.7 [0.05..3]; `letter_spacing` float=1 [0..5]; `line_spacing` float=1 [0..5]; `rotation` float=0 [-1..1]; `tiling` bool=true.

## Graph items

- `input_color` (Input Color): A color image input of the graph. In: none. Out: `output` Color. Params: `identifier` text="input"; `default` color="#bcbcbc".
- `input_grayscale` (Input Grayscale): A grayscale image input of the graph. In: none. Out: `output` Gray. Params: `identifier` text="input"; `default` color="#bcbcbc".
- `output` (Output): An output of the graph: a material channel (usage) or any image. In: `input` Any. Out: `output` Any. Params: `identifier` text="output"; `usage` enum=0 {0 Base color, 1 Normal, 2 Roughness, 3 Metallic, 4 Height, 5 Ambient occlusion, 6 Emissive, 7 Opacity, 8 Specular, 9 Any}.
- `dot` (Dot): A reroute point for wires. In: `input` Any. Out: `output` Any. Params: none.
- `graph_instance` (Graph Instance): Another graph of the package, used as a node. In: none. Out: `output` Any. Params: `graph` text="".

## Texture generators/Patterns

- `shape_splatter` (Shape Splatter): Scatters the pattern input (or a shape) with random scale, rotation and luminance; the mask input sets where instances land. In: `pattern` Gray, `mask` Gray. Out: `output` Gray. Params: `shape` enum=3 {0 Square, 1 Disc, 2 Paraboloid, 3 Bell, 4 Gaussian, 5 Thorn, 6 Pyramid, 7 Brick, 8 Gradation, 9 Waves, 10 Half bell, 11 Ridged bell, 12 Crescent, 13 Capsule, 14 Cone, 15 Hexagon}; `count` int=300 [1..20000]; `size` float=0.05 [0..1]; `size_random` float=0.5 [0..1]; `rotation_random` float=1 [0..1]; `luminance_random` float=0.4 [0..1]; `blending` enum=0 {0 Max, 1 Add, 2 Alpha over}.
- `brick_generator` (Brick Generator): Rows of bricks with mortar gaps, bevels and random heights. In: none. Out: `output` Gray. Params: `bricks_x` int=4 [1..64]; `bricks_y` int=8 [1..64]; `offset` float=0.5 [0..1]; `gap` float=0.04 [0..0.5]; `bevel` float=0.12 [0..1]; `height_random` float=0.3 [0..1]; `lum_random` float=0 [0..1].
- `checker` (Checker): A checkerboard. In: none. Out: `output` Gray. Params: `tiling` int=4 [1..64].
- `gradient_linear_1` (Gradient Linear 1): A ramp from black to white. In: none. Out: `output` Gray. Params: `tiling` int=1 [1..16]; `vertical` bool=false.
- `gradient_linear_2` (Gradient Linear 2): A mirrored ramp (white in the middle). In: none. Out: `output` Gray. Params: `tiling` int=1 [1..16]; `vertical` bool=false.
- `gradient_radial` (Gradient Radial): White at the center fading outward. In: none. Out: `output` Gray. Params: `radius` float=0.5 [0..1].
- `hexagons` (Hexagons): A honeycomb of beveled hexagons. In: none. Out: `output` Gray. Params: `tiling` int=4 [1..64]; `size` float=0.9 [0..1]; `bevel` float=0.3 [0..1].
- `polygon` (Polygon): A regular polygon. In: none. Out: `output` Gray. Params: `sides` int=6 [3..32]; `scale` float=0.8 [0..1]; `angle` float=0 [-1..1]; `gradient` float=0 [0..1]; `tiling` int=1 [1..16].
- `scratches` (Scratches): Random thin scratches. In: none. Out: `output` Gray. Params: `count` int=60 [0..1000]; `length` float=0.25 [0..1]; `width` float=1 [0.1..8]; `angle` float=0.1 [-1..1]; `angle_random` float=0.2 [0..1].
- `shape` (Shape): A single shape, optionally tiled. In: none. Out: `output` Gray. Params: `pattern` enum=1 {0 Square, 1 Disc, 2 Paraboloid, 3 Bell, 4 Gaussian, 5 Thorn, 6 Pyramid, 7 Brick, 8 Gradation, 9 Waves, 10 Half bell, 11 Ridged bell, 12 Crescent, 13 Capsule, 14 Cone, 15 Hexagon}; `tiling` int=1 [1..64]; `size` float=0.8 [0..2]; `size_xy` float2=[1, 1] [0..2]; `angle` float=0 [-1..1].
- `splatter` (Splatter): Scattered shapes of random size and gray. In: none. Out: `output` Gray. Params: `pattern` enum=4 {0 Square, 1 Disc, 2 Paraboloid, 3 Bell, 4 Gaussian, 5 Thorn, 6 Pyramid, 7 Brick, 8 Gradation, 9 Waves, 10 Half bell, 11 Ridged bell, 12 Crescent, 13 Capsule, 14 Cone, 15 Hexagon}; `count` int=64 [1..2000]; `size` float=0.08 [0..1]; `size_random` float=0.6 [0..1]; `lum_random` float=0.5 [0..1].
- `star` (Star): A star shape. In: none. Out: `output` Gray. Params: `points` int=5 [2..32]; `inner` float=0.45 [0..1]; `scale` float=0.8 [0..1]; `tiling` int=1 [1..16].
- `stripes` (Stripes): Parallel bands with soft edges. In: none. Out: `output` Gray. Params: `count` int=8 [1..128]; `width` float=0.5 [0..1]; `softness` float=0 [0..1]; `angle` float=0 [-1..1].
- `tile_generator` (Tile Generator): Places a shape on a grid with per-tile random size, position, rotation and luminance. In: none. Out: `output` Gray. Params: `pattern` enum=0 {0 Square, 1 Disc, 2 Paraboloid, 3 Bell, 4 Gaussian, 5 Thorn, 6 Pyramid, 7 Brick, 8 Gradation, 9 Waves, 10 Half bell, 11 Ridged bell, 12 Crescent, 13 Capsule, 14 Cone, 15 Hexagon}; `x_amount` int=8 [1..128]; `y_amount` int=8 [1..128]; `scale` float=0.9 [0..2]; `size_xy` float2=[1, 1] [0..2]; `scale_random` float=0 [0..1]; `offset` float=0 [0..1]; `position_random` float=0 [0..1]; `rotation_random` float=0 [0..1]; `lum_random` float=0 [0..1]; `mask_random` float=0 [0..1].
- `tile_sampler` (Tile Sampler): Like Tile Generator, but each tile shows the pattern input. In: `pattern` Gray, `scale_map` Gray. Out: `output` Gray. Params: `x_amount` int=8 [1..128]; `y_amount` int=8 [1..128]; `scale` float=1 [0..2]; `scale_random` float=0 [0..1]; `offset` float=0 [0..1]; `position_random` float=0 [0..1]; `rotation_random` float=0 [0..1]; `lum_random` float=0 [0..1]; `blend` enum=0 {0 Max, 1 Add}.
- `weave` (Weave): Interlaced threads (height). In: none. Out: `output` Gray. Params: `tiling` int=6 [1..64]; `width` float=0.8 [0..1].
- `waveform` (Waveform): Sine bands. In: none. Out: `output` Gray. Params: `count` int=8 [1..128]; `amplitude` float=0 [0..1]; `angle` float=0 [-1..1].
- `grid_lines` (Grid Lines): A grid of lines. In: none. Out: `output` Gray. Params: `tiling` int=8 [1..128]; `width` float=0.06 [0..1]; `softness` float=0 [0..0.5].
- `dots_grid` (Dots Grid): Round dots on a grid (perforated metal, polka dots). In: none. Out: `output` Gray. Params: `tiling` int=8 [1..128]; `radius` float=0.6 [0..1]; `softness` float=0 [0..0.5]; `staggered` bool=true.
- `diamond_grid` (Diamond Grid): Beveled diamond (45°) tiles. In: none. Out: `output` Gray. Params: `tiling` int=4 [1..64]; `gap` float=0.05 [0..0.5]; `bevel` float=0.15 [0..1]; `lum_random` float=0.3 [0..1].
- `herringbone` (Herringbone): Planks laid in a herringbone pattern. In: none. Out: `output` Gray. Params: `tiling` int=2 [1..32]; `length` int=3 [2..8]; `gap` float=0.08 [0..0.5]; `bevel` float=0.2 [0..1]; `lum_random` float=0.3 [0..1].
- `basketweave` (Basketweave): Squares of parallel planks alternating direction. In: none. Out: `output` Gray. Params: `tiling` int=4 [1..64]; `strips` int=3 [1..16]; `gap` float=0.08 [0..0.5]; `bevel` float=0.2 [0..1]; `lum_random` float=0.3 [0..1].
- `chevron` (Chevron): Zigzag bands. In: none. Out: `output` Gray. Params: `count` int=8 [1..128]; `zigs` int=4 [1..64]; `height` float=1 [0..8]; `width` float=0.5 [0..1]; `softness` float=0.1 [0..1].
- `fish_scales` (Fish Scales): Overlapping rows of round scales (height). In: none. Out: `output` Gray. Params: `tiling` int=6 [1..64]; `radius` float=0.65 [0.5..1]; `lum_random` float=0.2 [0..1].
- `triangle_grid` (Triangle Grid): Beveled triangle tiles. In: none. Out: `output` Gray. Params: `tiling` int=6 [1..64]; `gap` float=0.04 [0..0.5]; `bevel` float=0.12 [0..1]; `lum_random` float=0.3 [0..1].
- `spiral` (Spiral): An Archimedean spiral. In: none. Out: `output` Gray. Params: `turns` float=6 [0..64]; `width` float=0.5 [0..1]; `softness` float=0.3 [0..1]; `tiling` int=1 [1..16].
- `concentric_rings` (Concentric Rings): Rings around the center. In: none. Out: `output` Gray. Params: `count` float=8 [0..64]; `width` float=0.5 [0..1]; `softness` float=0.3 [0..1]; `tiling` int=1 [1..16].
- `gradient_axial` (Gradient Axial): A ramp from point 1 (black) to point 2 (white). In: none. Out: `output` Gray. Params: `point_1` float2=[0.2, 0.5] [0..1]; `point_2` float2=[0.8, 0.5] [0..1].
- `gradient_circular` (Gradient Circular): A ramp around the center (by angle). In: none. Out: `output` Gray. Params: `angle` float=0 [-1..1]; `tiling` int=1 [1..16].
- `cross` (Cross): A plus-shaped cross. In: none. Out: `output` Gray. Params: `length` float=0.8 [0..1]; `thickness` float=0.25 [0..1]; `softness` float=0 [0..1]; `angle` float=0 [-1..1]; `tiling` int=1 [1..32].
- `rounded_rectangle` (Rounded Rectangle): A rectangle with rounded corners. In: none. Out: `output` Gray. Params: `size` float2=[0.8, 0.6] [0..1]; `radius` float=0.2 [0..1]; `softness` float=0 [0..1]; `angle` float=0 [-1..1]; `tiling` int=1 [1..32].
- `ring` (Ring): A circular ring. In: none. Out: `output` Gray. Params: `radius` float=0.6 [0..1]; `width` float=0.15 [0..1]; `softness` float=0.05 [0..1]; `tiling` int=1 [1..32].
- `arc_pavement` (Arc Pavement): Cobblestones laid in overlapping fan-shaped arcs. In: none. Out: `output` Gray. Params: `tiling` int=3 [1..32]; `bands` int=4 [1..16]; `stones` int=7 [1..32]; `gap` float=0.08 [0..0.5]; `bevel` float=0.25 [0..1]; `lum_random` float=0.3 [0..1].
- `octagon_tiles` (Octagon Tiles): Octagons with small square tiles between them. In: none. Out: `output` Gray. Params: `tiling` int=4 [1..64]; `gap` float=0.03 [0..0.5]; `bevel` float=0.08 [0..1]; `lum_random` float=0.3 [0..1].
- `planks` (Planks): Rows of floor boards of random length, staggered. In: none. Out: `output` Gray. Params: `rows` int=8 [1..64]; `length` float=0.33 [0.02..1]; `length_random` float=0.5 [0..1]; `gap` float=0.06 [0..0.5]; `bevel` float=0.15 [0..1]; `lum_random` float=0.3 [0..1].
- `tread_plate` (Tread Plate): Raised diagonal bars alternating direction, like metal floor plates (height). In: none. Out: `output` Gray. Params: `tiling` int=6 [1..64]; `length` float=1 [0..1.4]; `width` float=0.3 [0.01..1].
- `paint_strokes` (Paint Strokes): Overlapping brush strokes with bristle streaks and ragged ends. In: none. Out: `output` Gray. Params: `count` int=150 [1..5000]; `length` float=0.35 [0..1]; `width` float=0.07 [0..0.5]; `angle` float=0 [-1..1]; `angle_random` float=0.08 [0..1]; `bristles` int=20 [1..256]; `luminance_random` float=0.5 [0..1]; `blending` enum=2 {0 Max, 1 Add, 2 Alpha over}.
- `scratches_generator` (Scratches Generator): Thin tapered scratches that bend along a direction field (gray = angle in turns) and land where the mask is bright. In: `direction` Gray, `mask` Gray. Out: `output` Gray. Params: `count` int=200 [0..5000]; `length` float=0.25 [0..1]; `width` float=1 [0.1..16]; `angle` float=0 [-1..1]; `angle_random` float=0.15 [0..1]; `curvature` float=0.1 [0..1]; `field_intensity` float=0.25 [0..1]; `luminance_random` float=0.6 [0..1].

## Texture generators/Noises

- `anisotropic_noise` (Anisotropic Noise): Streaks of value noise stretched along one axis. In: none. Out: `output` Gray. Params: `scale` float=4 [1..64]; `scale_y` float=64 [1..512]; `smoothness` float=0.5 [0..1]; `interpolation` float=1 [0..1].
- `bnw_spots_1` (BnW Spots 1): Contrasted black and white spots. In: none. Out: `output` Gray. Params: `scale` float=8 [1..64]; `roughness` float=0.5 [0..1].
- `bnw_spots_2` (BnW Spots 2): Rounder black and white spots. In: none. Out: `output` Gray. Params: `scale` float=6 [1..64]; `roughness` float=0.3 [0..1].
- `bnw_spots_3` (BnW Spots 3): Fine black and white speckles. In: none. Out: `output` Gray. Params: `scale` float=16 [1..64]; `roughness` float=0.6 [0..1].
- `cells_1` (Cells 1): Distance to the nearest cell point (soft bumps). In: none. Out: `output` Gray. Params: `scale` float=8 [1..64]; `disorder` float=1 [0..1].
- `cells_2` (Cells 2): Cell borders (second minus first distance). In: none. Out: `output` Gray. Params: `scale` float=8 [1..64]; `disorder` float=1 [0..1].
- `cells_3` (Cells 3): Flat cells, each a random gray. In: none. Out: `output` Gray. Params: `scale` float=8 [1..64]; `disorder` float=1 [0..1].
- `cells_4` (Cells 4): Chebyshev cells: square bumps. In: none. Out: `output` Gray. Params: `scale` float=8 [1..64]; `disorder` float=1 [0..1].
- `clouds_1` (Clouds 1): Soft fractal clouds. In: none. Out: `output` Gray. Params: `scale` float=4 [1..32]; `roughness` float=0.5 [0..1].
- `clouds_2` (Clouds 2): Warped, wispy clouds. In: none. Out: `output` Gray. Params: `scale` float=3 [1..32]; `roughness` float=0.55 [0..1].
- `clouds_3` (Clouds 3): Detailed, contrasted clouds. In: none. Out: `output` Gray. Params: `scale` float=6 [1..32]; `roughness` float=0.6 [0..1].
- `creased` (Creased): Ridged fractal noise: folds and creases. In: none. Out: `output` Gray. Params: `scale` float=3 [1..32]; `roughness` float=0.55 [0..1]; `warp` float=0.3 [0..1].
- `crystal_1` (Crystal 1): Faceted crystal plates. In: none. Out: `output` Gray. Params: `scale` float=6 [1..64].
- `crystal_2` (Crystal 2): Sharp crystal shards. In: none. Out: `output` Gray. Params: `scale` float=6 [1..64].
- `dirt` (Dirt): Clumps of dirt. In: none. Out: `output` Gray. Params: `scale` float=6 [1..64]; `density` float=0.5 [0..1].
- `dust` (Dust): Sparse specks of dust. In: none. Out: `output` Gray. Params: `density` float=0.02 [0..0.2]; `size` float=1 [0..8].
- `fractal_sum_base` (Fractal Sum Base): Sum of Perlin noise octaves. In: none. Out: `output` Gray. Params: `scale` float=2 [1..64]; `octaves` int=8 [1..12]; `roughness` float=0.5 [0..1].
- `fur` (Fur): Short directional fibers. In: none. Out: `output` Gray. Params: `scale` float=1 [0.1..4]; `angle` float=0.25 [-1..1]; `length` float=8 [0..64].
- `gaussian_noise` (Gaussian Noise): Smoothly interpolated value noise. In: none. Out: `output` Gray. Params: `scale` float=16 [1..256].
- `grunge_map_1` (Grunge Map 1): Stains and blotches. In: none. Out: `output` Gray. Params: `scale` float=3 [1..32]; `contrast` float=0.5 [0..1].
- `grunge_map_2` (Grunge Map 2): Speckled grime. In: none. Out: `output` Gray. Params: `scale` float=5 [1..32]; `contrast` float=0.5 [0..1].
- `grunge_map_3` (Grunge Map 3): Streaky leaks. In: none. Out: `output` Gray. Params: `scale` float=4 [1..32]; `contrast` float=0.5 [0..1].
- `liquid` (Liquid): Domain-warped flowing noise. In: none. Out: `output` Gray. Params: `scale` float=3 [1..32]; `warp` float=0.6 [0..2].
- `moisture_noise` (Moisture Noise): Damp patches with soft edges. In: none. Out: `output` Gray. Params: `scale` float=4 [1..32]; `contrast` float=0.5 [0..1].
- `perlin_noise` (Perlin Noise): Single-octave gradient noise. In: none. Out: `output` Gray. Params: `scale` float=8 [1..256]; `disorder` float=0 [0..1].
- `plasma` (Plasma): Interfering sine waves through noise. In: none. Out: `output` Gray. Params: `scale` float=4 [1..32].
- `turbulence` (Turbulence): Billowing absolute-value fractal noise. In: none. Out: `output` Gray. Params: `scale` float=4 [1..32]; `roughness` float=0.5 [0..1].
- `voronoi` (Voronoi): Cellular noise with a choice of distance and output. In: none. Out: `output` Gray. Params: `scale` float=8 [1..64]; `disorder` float=1 [0..1]; `metric` enum=0 {0 Euclidean, 1 Manhattan, 2 Chebyshev}; `style` enum=2 {0 F1, 1 F2, 2 F2 - F1, 3 Cell id}.
- `white_noise` (White Noise): Independent random value per pixel. In: none. Out: `output` Any. Params: `mode` enum=0 {0 Grayscale, 1 Color}.
- `value_noise` (Value Noise): Fractal value noise: smooth blocks of random values. In: none. Out: `output` Gray. Params: `scale` float=8 [1..256]; `octaves` int=1 [1..10]; `roughness` float=0.5 [0..1].
- `ridged_fractal` (Ridged Fractal): Ridged multi-octave noise: sharp crests like mountain ridges. In: none. Out: `output` Gray. Params: `scale` float=4 [1..64]; `octaves` int=6 [1..10]; `roughness` float=0.5 [0..1]; `sharpness` float=2 [0.5..8].
- `voronoi_fractal` (Voronoi Fractal): Several octaves of cell bumps. In: none. Out: `output` Gray. Params: `scale` float=4 [1..64]; `octaves` int=4 [1..8]; `roughness` float=0.5 [0..1]; `disorder` float=1 [0..1].
- `cells_fractal` (Cells Fractal): Several octaves of cell borders: cracked, crystalline networks. In: none. Out: `output` Gray. Params: `scale` float=4 [1..64]; `octaves` int=3 [1..8]; `roughness` float=0.5 [0..1]; `disorder` float=1 [0..1].
- `directional_noise` (Directional Noise): Fractal noise stretched along one axis: streaks and brushed patterns. In: none. Out: `output` Gray. Params: `scale` float=2 [1..64]; `scale_across` float=24 [1..256]; `octaves` int=5 [1..10]; `roughness` float=0.5 [0..1]; `vertical` bool=false.
- `fibers` (Fibers): Thin, nearly parallel fibers. In: none. Out: `output` Gray. Params: `density` float=96 [4..512]; `length` float=2 [1..32]; `sharpness` float=12 [1..64]; `vertical` bool=false.
- `messy_fibers` (Messy Fibers): Tangled fibers in both directions, warped by clouds. In: none. Out: `output` Gray. Params: `density` float=64 [4..512]; `warp` float=0.5 [0..2]; `sharpness` float=10 [1..64].
- `leather` (Leather): Leather grain: small bumpy cells split by creases, over soft clouds. In: none. Out: `output` Gray. Params: `scale` float=24 [2..128]; `crease` float=0.25 [0..1]; `warp` float=0.4 [0..1]; `clouds` float=0.3 [0..1].
- `microscope` (Microscope View): Strongly warped cell walls, like tissue under a microscope. In: none. Out: `output` Gray. Params: `scale` float=6 [1..64]; `warp` float=0.6 [0..2]; `width` float=0.15 [0.01..1].
- `gaussian_spots` (Gaussian Spots): Scattered soft round spots of random size and intensity. In: none. Out: `output` Gray. Params: `scale` float=8 [1..64]; `size` float=0.3 [0.01..1]; `size_random` float=0.5 [0..1]; `density` float=0.8 [0..1].
- `crackle` (Crackle): Wiggly cracks along cell borders, with finer secondary cracks. In: none. Out: `output` Gray. Params: `scale` float=5 [1..64]; `width` float=0.08 [0.005..0.5]; `disorder` float=0.5 [0..2]; `amount` float=1 [0..1].
- `sand_dunes` (Sand Dunes): Wind-shaped dunes: gentle windward slopes, steep lee sides and fine ripples. In: none. Out: `output` Gray. Params: `count` int=6 [1..64]; `warp` float=0.6 [0..2]; `steepness` float=0.3 [0.05..0.95]; `ripples` float=0.15 [0..1].
- `wood_grain` (Wood Grain): Distorted growth rings and fibers of sawn wood (grain along X). In: none. Out: `output` Gray. Params: `rings` float=16 [1..128]; `stretch` float=6 [1..32]; `sharpness` float=3 [0.5..16]; `fibers` float=0.3 [0..1].
- `marble` (Marble): Thin veins from sine bands warped by fractal noise. In: none. Out: `output` Gray. Params: `scale` float=2 [1..32]; `turbulence` float=3 [0..10]; `sharpness` float=4 [1..64]; `direction` enum=2 {0 Horizontal, 1 Vertical, 2 Diagonal}.
- `stones` (Stones): Packed rounded stones with gaps (height). In: none. Out: `output` Gray. Params: `scale` float=6 [1..64]; `gap` float=0.06 [0..0.5]; `bevel` float=0.25 [0.01..1]; `height_random` float=0.4 [0..1]; `detail` float=0.2 [0..1]; `disorder` float=1 [0..1].
- `ripples` (Ripples): Interfering waves, like a water surface. In: none. Out: `output` Gray. Params: `scale` float=8 [1..32]; `waves` int=10 [1..32]; `warp` float=0.3 [0..2].
- `concrete` (Concrete): Cement clouds with small air pits and fine grain. In: none. Out: `output` Gray. Params: `scale` float=4 [1..32]; `pits` float=0.3 [0..1]; `pit_size` float=0.5 [0..1]; `roughness` float=0.6 [0..1].
- `bark` (Bark): Deep vertical bark furrows. In: none. Out: `output` Gray. Params: `scale` float=8 [1..64]; `stretch` float=1 [1..16]; `warp` float=0.4 [0..2]; `roughness` float=0.5 [0..1].
- `perlin_noise_3d` (Perlin Noise 3D): Fractal 3D gradient noise; Z scrubs through the volume. Tiles. In: none. Out: `output` Gray. Params: `scale` float=4 [1..64]; `octaves` int=5 [1..10]; `roughness` float=0.5 [0..1]; `z` float=0 [0..16]; `contrast` float=0.5 [0..1].
- `simplex_noise_3d` (Simplex Noise 3D): Fractal simplex noise sampled on a 4D torus; Z moves through it. Tiles at any scale. In: none. Out: `output` Gray. Params: `scale` float=4 [1..64]; `octaves` int=5 [1..10]; `roughness` float=0.5 [0..1]; `z` float=0 [0..16]; `contrast` float=0.5 [0..1].
- `worley_noise_3d` (Worley Noise 3D): Cellular noise from 3D feature points; Z scrubs through the cells. Tiles. In: none. Out: `output` Gray. Params: `distance` enum=0 {0 F1, 1 F2, 2 F2 - F1}; `jitter` float=1 [0..1]; `scale` float=6 [1..64]; `octaves` int=1 [1..10]; `roughness` float=0.5 [0..1]; `z` float=0 [0..16]; `contrast` float=0.5 [0..1].
- `cracks` (Cracks): A connected network of thin cracks along warped cell borders, with finer branching cracks. White = crack. In: none. Out: `output` Gray. Params: `scale` float=5 [1..32]; `width` float=1.5 [0..16]; `warp` float=0.5 [0..1]; `branches` float=0.5 [0..1].

## Filters/Adjustments

- `auto_levels` (Auto Levels): Stretches the input to the full 0..1 range. In: `input` Any. Out: `output` Any. Params: none.
- `clamp` (Clamp): Clamps values between a minimum and a maximum. In: `input` Any. Out: `output` Any. Params: `min` float=0 [0..1]; `max` float=1 [0..1].
- `color_to_mask` (Color to Mask): White where the input is close to a key color. In: `input` Color. Out: `output` Gray. Params: `color` color="#ff0000"; `range` float=0.2 [0..1]; `softness` float=0.1 [0..1].
- `contrast_luminosity` (Contrast/Luminosity): Contrast and brightness (0 = unchanged). In: `input` Any. Out: `output` Any. Params: `contrast` float=0 [-1..1]; `luminosity` float=0 [-1..1].
- `exposure` (Exposure): Exposure in stops. In: `input` Any. Out: `output` Any. Params: `stops` float=0 [-10..10].
- `gamma` (Gamma): Raises values to a power. In: `input` Any. Out: `output` Any. Params: `gamma` float=1 [0.01..10].
- `histogram_range` (Histogram Range): Compresses values into a range around a position. In: `input` Gray. Out: `output` Gray. Params: `range` float=0.5 [0..1]; `position` float=0.5 [0..1].
- `histogram_scan` (Histogram Scan): Thresholds the input at a position with adjustable contrast. In: `input` Gray. Out: `output` Gray. Params: `position` float=0.5 [0..1]; `contrast` float=0.5 [0..1]; `invert` bool=false.
- `histogram_shift` (Histogram Shift): Shifts values with wrap-around. In: `input` Gray. Out: `output` Gray. Params: `position` float=0.5 [0..1].
- `invert` (Invert): 1 minus the input (alpha kept). In: `input` Any. Out: `output` Any. Params: `alpha` bool=false.
- `posterize` (Posterize): Quantizes values to a number of steps. In: `input` Any. Out: `output` Any. Params: `steps` int=4 [2..256].
- `replace_color` (Replace Color): Shifts colors near a source color towards a target color. In: `input` Color. Out: `output` Color. Params: `source` color="#ff0000"; `target` color="#0000ff"; `range` float=0.3 [0..1].
- `threshold` (Threshold): White above the threshold, black below. In: `input` Gray. Out: `output` Gray. Params: `threshold` float=0.5 [0..1].
- `colorize` (Colorize): Tints a grayscale image between two colors. In: `input` Gray. Out: `output` Color. Params: `dark` color="#3f3027"; `light` color="#f3e1bc".
- `channel_mixer` (Channel Mixer): Each output channel as a weighted sum of the input channels. In: `input` Color. Out: `output` Color. Params: `red_rg` float2=[1, 0] [-2..2]; `red_b` float=0 [-2..2]; `green_rg` float2=[0, 1] [-2..2]; `green_b` float=0 [-2..2]; `blue_rg` float2=[0, 0] [-2..2]; `blue_b` float=1 [-2..2].
- `remap` (Remap): Maps the input range linearly onto the output range. In: `input` Any. Out: `output` Any. Params: `in_min` float=0 [0..1]; `in_max` float=1 [0..1]; `out_min` float=0 [0..1]; `out_max` float=1 [0..1]; `clamp` bool=true.
- `smoothstep` (Smoothstep): A smooth S-shaped step from the low edge (black) to the high edge (white). In: `input` Any. Out: `output` Any. Params: `low` float=0.25 [0..1]; `high` float=0.75 [0..1].
- `s_curve` (S-Curve Contrast): Raises contrast around a pivot with a smooth S curve (keeps black and white). In: `input` Any. Out: `output` Any. Params: `amount` float=0.5 [0..1]; `pivot` float=0.5 [0.01..0.99].
- `channel_levels` (Channel Levels): Levels with a separate input range per channel. In: `input` Any. Out: `output` Any. Params: `low` color="#000000" a0; `high` color="#ffffff"; `gamma` float=1 [0.1..4].
- `auto_levels_channels` (Auto Levels per Channel): Stretches each color channel separately to the full 0..1 range. In: `input` Any. Out: `output` Any. Params: none.
- `invert_channels` (Invert Channels): Inverts the chosen channels. In: `input` Any. Out: `output` Any. Params: `red` bool=true; `green` bool=true; `blue` bool=true; `alpha` bool=false.
- `clamp_channels` (Clamp Channels): Clamps each channel between its own minimum and maximum. In: `input` Any. Out: `output` Any. Params: `min` color="#000000" a0; `max` color="#ffffff".
- `color_variation` (Color Variation): Random hue, saturation and value shifts: per region when a flood fill index map is connected, else from soft noise. In: `input` Color, `index` Color. Out: `output` Color. Params: `hue` float=0.03 [0..0.5]; `saturation` float=0.15 [0..1]; `value` float=0.2 [0..1]; `scale` float=4 [1..64].
- `histogram_select` (Histogram Select): White where values lie in a band around the position, fading out with the contrast. In: `input` Gray. Out: `output` Gray. Params: `position` float=0.5 [0..1]; `range` float=0.25 [0..1]; `contrast` float=0.5 [0..1].
- `quantize_color` (Quantize Color): Reduces the image to a palette of its most representative colors (k-means), with optional ordered dithering. In: `input` Color. Out: `output` Color. Params: `colors` int=8 [2..64]; `dither` float=0 [0..1].

## Filters/Blending

- `height_blend` (Height Blend): Blends two height maps by which is higher, with a soft contrast; also outputs the mask. In: `top` Gray, `bottom` Gray, `mask` Gray. Out: `height` Gray, `blend_mask` Gray. Params: `offset` float=0.5 [0..1]; `contrast` float=0.9 [0..1].
- `alpha_merge` (Alpha Merge): Puts a grayscale image in a color image's alpha. In: `input` Color, `alpha` Gray. Out: `output` Color. Params: none.
- `switch` (Switch): Outputs input A or input B. In: `a` Any, `b` Any. Out: `output` Any. Params: `use_b` bool=false.
- `lerp` (Lerp): Linear interpolation from A to B by a mask (or a constant position without one). In: `input_a` Any, `input_b` Any, `mask` Gray. Out: `output` Any. Params: `position` float=0.5 [0..1].
- `minimum` (Minimum): The darker of A and B, per channel. In: `input_a` Any, `input_b` Any. Out: `output` Any. Params: none.
- `maximum` (Maximum): The brighter of A and B, per channel. In: `input_a` Any, `input_b` Any. Out: `output` Any. Params: none.
- `multiply` (Multiply): A times B. In: `input_a` Any, `input_b` Any. Out: `output` Any. Params: none.
- `difference` (Difference): The absolute difference of A and B. In: `input_a` Any, `input_b` Any. Out: `output` Any. Params: none.
- `add` (Add): A plus B. In: `input_a` Any, `input_b` Any. Out: `output` Any. Params: `clamp` bool=true.
- `subtract` (Subtract): A minus B. In: `input_a` Any, `input_b` Any. Out: `output` Any. Params: `clamp` bool=true.

## Filters/Channels

- `rgba_merge` (RGBA Merge): Builds a color image from four grayscale channels. In: `r` Gray, `g` Gray, `b` Gray, `a` Gray. Out: `output` Color. Params: none.
- `rgba_split` (RGBA Split): Splits a color image into four grayscale channels. In: `input` Color. Out: `r` Gray, `g` Gray, `b` Gray, `a` Gray. Params: none.

## Filters/Blurs

- `anisotropic_blur` (Anisotropic Blur): A Gaussian blur stronger along one direction. In: `input` Any. Out: `output` Any. Params: `intensity` float=4 [0..32]; `anisotropy` float=0.5 [0..1]; `angle` float=0 [-1..1].
- `non_uniform_blur` (Non Uniform Blur): Blurs more where the blur map is white. In: `input` Any, `blur_map` Gray. Out: `output` Any. Params: `intensity` float=4 [0..32].
- `radial_blur` (Radial Blur): Zoom blur from a center. In: `input` Any. Out: `output` Any. Params: `intensity` float=0.2 [0..1]; `center` float2=[0.5, 0.5] [0..1].
- `slope_blur` (Slope Blur): Smears the input along the slopes of a map, like flowing material. In: `input` Any, `slope` Gray. Out: `output` Any. Params: `intensity` float=8 [-64..64]; `samples` int=8 [1..32]; `mode` enum=0 {0 Blur, 1 Min, 2 Max}.
- `median` (Median): Median of each neighbourhood: removes specks while keeping edges. In: `input` Any. Out: `output` Any. Params: `size` enum=0 {0 3 × 3, 1 5 × 5}.
- `unsharp_mask` (Unsharp Mask): Sharpens by adding back the difference from a blurred copy. In: `input` Any. Out: `output` Any. Params: `radius` float=2 [0..32]; `amount` float=1 [0..5]; `threshold` float=0 [0..1].

## Filters/Effects

- `ambient_occlusion` (Ambient Occlusion): Darkens creases of a height map. In: `height` Gray. Out: `output` Gray. Params: `spread` float=0.15 [0..1]; `intensity` float=0.5 [0..1].
- `bevel` (Bevel): Rounds the edges of a mask into a height ramp. In: `input` Gray. Out: `output` Gray. Params: `distance` float=0.05 [-1..1]; `smoothing` float=0 [0..1].
- `curvature` (Curvature): Convexity (white) and concavity (black) of a normal map. In: `normal` Color. Out: `output` Gray. Params: `intensity` float=1 [0..10].
- `dilation` (Dilation): Grows bright areas (maximum filter). In: `input` Any. Out: `output` Any. Params: `radius` int=2 [0..64].
- `erosion` (Erosion): Shrinks bright areas (minimum filter). In: `input` Any. Out: `output` Any. Params: `radius` int=2 [0..64].
- `edge_detect` (Edge Detect): White along the edges of a mask. In: `input` Gray. Out: `output` Gray. Params: `width` float=2 [0..32]; `roundness` float=0.5 [0..1].
- `glow` (Glow): A soft glow around bright areas. In: `input` Any. Out: `output` Any. Params: `threshold` float=0.5 [0..1]; `size` float=8 [0..64]; `amount` float=0.5 [0..2].
- `highpass` (Highpass): Keeps the fine detail, centered on gray. In: `input` Any. Out: `output` Any. Params: `radius` float=6 [0..64].
- `mosaic` (Mosaic): Pixelates into blocks. In: `input` Any. Out: `output` Any. Params: `cells` int=16 [1..512].
- `swirl` (Swirl): Twists the image around its center. In: `input` Any. Out: `output` Any. Params: `amount` float=0.5 [-4..4]; `radius` float=0.5 [0..1].
- `vignette` (Vignette): Darkens towards the borders. In: `input` Any. Out: `output` Any. Params: `amount` float=0.5 [0..1]; `softness` float=0.5 [0..1].
- `quantize` (Quantize Grayscale): Snaps gray values to steps with soft transitions. In: `input` Gray. Out: `output` Gray. Params: `steps` int=4 [2..64]; `smoothness` float=0.1 [0..1].
- `sobel` (Sobel Edges): Edge strength from the Sobel operator. In: `input` Gray. Out: `output` Gray. Params: `intensity` float=1 [0..10].
- `outer_glow` (Outer Glow): A glow fading outward from a mask (by exact distance). In: `input` Gray. Out: `output` Gray. Params: `size` float=16 [0..256]; `intensity` float=1 [0..1]; `falloff` float=2 [0.25..8].
- `inner_shadow` (Inner Shadow): Darkens the inside of a mask along the edges facing the light. In: `input` Gray. Out: `output` Gray. Params: `angle` float=-0.125 [-1..1]; `distance` float=6 [0..64]; `size` float=8 [0..128]; `opacity` float=0.75 [0..1].
- `drop_shadow` (Drop Shadow): An offset, blurred shadow under a mask. In: `input` Gray. Out: `output` Gray, `shadow` Gray. Params: `angle` float=-0.125 [-1..1]; `distance` float=8 [0..128]; `size` float=4 [0..64]; `opacity` float=0.75 [0..1].
- `height_curvature` (Curvature from Height): Convex areas above 0.5, concave below, from a height map. In: `input` Gray. Out: `output` Gray. Params: `radius` float=2 [0.25..32]; `intensity` float=1 [0..10].
- `outline` (Outline): A line of constant width around the edges of a mask. In: `input` Gray. Out: `output` Gray. Params: `width` float=4 [0..64]; `position` enum=1 {0 Outside, 1 Center, 2 Inside}.
- `ambient_occlusion_fast` (Ambient Occlusion (Fast)): Horizon-based ambient occlusion of a height map: how much of the sky each pixel sees within the radius. In: `height` Gray. Out: `output` Gray. Params: `radius` float=12 [1..128]; `height_depth` float=0.3 [0..1]; `intensity` float=1 [0..2].
- `pixelate_color` (Pixelate Color): Averages the image over blocks (separate X and Y counts). In: `input` Any. Out: `output` Any. Params: `x_cells` int=32 [1..1024]; `y_cells` int=32 [1..1024].

## Filters/Normal map

- `height_to_normal` (Height to Normal): Same as Normal: a normal map from a height map. In: `input` Gray. Out: `output` Color. Params: `intensity` float=1 [0..10]; `format` enum=0 {0 OpenGL, 1 DirectX}.
- `normal_blend` (Normal Blend): Combines two normal maps (reoriented normal mapping). In: `base` Color, `detail` Color, `mask` Gray. Out: `output` Color. Params: `opacity` float=1 [0..1].
- `normal_invert` (Normal Invert): Flips the green (and optionally red) channel: OpenGL / DirectX. In: `input` Color. Out: `output` Color. Params: `red` bool=false; `green` bool=true.
- `normal_normalize` (Normal Normalize): Rescales normals to unit length. In: `input` Color. Out: `output` Color. Params: none.
- `normal_intensity` (Normal Intensity): Strengthens or flattens a normal map. In: `input` Color. Out: `output` Color. Params: `intensity` float=1 [0..10].
- `normal_to_height` (Normal to Height): Reconstructs a height map from a normal map. In: `input` Color. Out: `output` Gray. Params: `intensity` float=1 [0..10].
- `normal_combine` (Normal Combine): Combines a detail normal map over a base one (whiteout blending). In: `base` Color, `detail` Color. Out: `output` Color. Params: `intensity` float=1 [0..4].
- `normal_rotate` (Normal Rotate): Rotates the directions of a normal map (for rotated textures). In: `input` Color. Out: `output` Color. Params: `angle` float=0 [-1..1].
- `normal_sobel` (Normal Sobel): A normal map from a height map with Sobel slopes (smoother than plain differences). In: `input` Gray. Out: `output` Color. Params: `intensity` float=1 [0..10]; `format` enum=0 {0 OpenGL, 1 DirectX}.
- `normal_from_height_hq` (Normal from Height HQ): A smooth normal map from a height map with 5×5 Sobel slopes. In: `input` Gray. Out: `output` Color. Params: `intensity` float=1 [0..10]; `format` enum=0 {0 OpenGL, 1 DirectX}.

## Filters/Tiling

- `make_it_tile` (Make It Tile): Cross-fades the borders so a photo tiles. In: `input` Any. Out: `output` Any. Params: `blend` float=0.25 [0..0.5].
- `safe_transform` (Safe Transform): Tiling-safe transform: whole-number tiling, offsets and 90° rotations. In: `input` Any. Out: `output` Any. Params: `tile` int=1 [1..64]; `offset` float2=[0, 0] [-1..1]; `rotation` enum=0 {0 0°, 1 90°, 2 180°, 3 270°}; `flip` bool=false.
- `tile_random` (Tile Random): Cuts the image into a grid and shows a randomly offset, flipped and rotated window of the input in each tile (breaks up repetition). In: `input` Any. Out: `output` Any. Params: `x_amount` int=4 [1..256]; `y_amount` int=4 [1..256]; `offset_random` float=1 [0..1]; `rotate` bool=true; `flip` bool=true; `luminance_random` float=0 [0..1].

## Filters/Transforms

- `mirror` (Mirror): Mirrors one half of the image onto the other. In: `input` Any. Out: `output` Any. Params: `axis` enum=0 {0 Horizontal, 1 Vertical, 2 Corner}; `flip` bool=false.
- `kaleidoscope` (Kaleidoscope): Repeats a wedge of the image around the center. In: `input` Any. Out: `output` Any. Params: `segments` int=6 [2..64]; `angle` float=0 [-1..1].
- `cartesian_to_polar` (Cartesian to Polar): Wraps the image around the center. In: `input` Any. Out: `output` Any. Params: none.
- `polar_to_cartesian` (Polar to Cartesian): Unwraps a circular image into bands. In: `input` Any. Out: `output` Any. Params: none.
- `skew` (Skew): Shears the image. In: `input` Any. Out: `output` Any. Params: `amount` float=0.25 [-2..2]; `vertical` bool=false.

## Filters/Flood fill

- `flood_fill` (Flood Fill): Finds every connected white region of a tile mask (regions crossing the edges are one) and writes an index map: R, G = region center, B = random id, A = 1. In: `input` Gray. Out: `output` Color. Params: `threshold` float=0.5 [0..1].
- `flood_fill_to_random_grayscale` (Flood Fill to Random Grayscale): A random gray per region. In: `input` Color. Out: `output` Gray. Params: `min` float=0 [0..1]; `max` float=1 [0..1].
- `flood_fill_to_random_color` (Flood Fill to Random Color): A random color per region. In: `input` Color. Out: `output` Color. Params: `saturation` float=0.7 [0..1]; `lightness` float=0.5 [0..1]; `lightness_random` float=0.3 [0..1].
- `flood_fill_to_gradient` (Flood Fill to Gradient): A linear gradient across each region's bounding box. In: `input` Color. Out: `output` Gray. Params: `angle` float=0 [-1..1]; `angle_random` float=0 [0..1]; `slope_random` float=0 [0..1].
- `flood_fill_to_bbox_size` (Flood Fill to BBox Size): Each region's bounding-box size. In: `input` Color. Out: `output` Gray. Params: `mode` enum=2 {0 Width, 1 Height, 2 Max, 3 Min, 4 Area}.
- `flood_fill_to_position` (Flood Fill to Position): Each region's center position (R = X, G = Y). In: `input` Color. Out: `output` Color. Params: none.
- `flood_fill_to_grayscale` (Flood Fill to Grayscale): Each region takes the value of the input at its center. In: `input` Color, `source` Gray. Out: `output` Gray. Params: none.
- `flood_fill_to_color` (Flood Fill to Color): Each region takes the color of the input at its center. In: `input` Color, `source` Color. Out: `output` Color. Params: none.

## Material filters/PBR utilities

- `pbr_base_material` (PBR Base Material): A uniform PBR material: base color, normal, roughness, metallic, height and ambient occlusion. In: none. Out: `base_color` Color, `normal` Color, `roughness` Gray, `metallic` Gray, `height` Gray, `ambient_occlusion` Gray. Params: `base_color` color="#bcbcbc"; `roughness` float=0.5 [0..1]; `metallic` float=0 [0..1]; `height` float=0.5 [0..1]; `ao` float=1 [0..1].
- `height_normal_ao` (Height to Normal and AO): A normal map and an ambient occlusion map from one height map. In: `height` Gray. Out: `normal` Color, `ambient_occlusion` Gray. Params: `normal_intensity` float=1 [0..10]; `ao_spread` float=0.15 [0..1]; `ao_depth` float=0.5 [0..1].
- `albedo_safe` (Albedo Safe Color): Keeps base colors inside the physically plausible range (sRGB 30-240). In: `input` Color. Out: `output` Color. Params: none.
- `metallic_mask` (Metallic From Mask): Turns a mask into a clean metallic map (fully metallic or not). In: `input` Gray. Out: `output` Gray. Params: `threshold` float=0.5 [0..1].
- `material_color_adjust` (Material Color Adjust): Hue, saturation and value of a base color, optionally through a mask. In: `input` Color, `mask` Gray. Out: `output` Color. Params: `hue` float=0 [-0.5..0.5]; `saturation` float=0 [-1..1]; `value` float=0 [-1..1].
- `metal_base_color` (Metal Base Color): The measured base color (linear reflectance) of a common metal, with metallic = 1. In: none. Out: `base_color` Color, `metallic` Gray. Params: `metal` enum=0 {0 Iron, 1 Silver, 2 Aluminum, 3 Gold, 4 Copper, 5 Chromium, 6 Nickel, 7 Titanium, 8 Cobalt, 9 Platinum}.

## Material filters/Blending

- `material_blend` (Material Blend): Blends two whole PBR materials by a mask (white = material 2). In: `base_color_1` Color, `normal_1` Color, `roughness_1` Gray, `metallic_1` Gray, `height_1` Gray, `base_color_2` Color, `normal_2` Color, `roughness_2` Gray, `metallic_2` Gray, `height_2` Gray, `mask` Gray. Out: `base_color` Color, `normal` Color, `roughness` Gray, `metallic` Gray, `height` Gray. Params: `opacity` float=1 [0..1].
- `material_height_blend` (Material Height Blend): Blends two whole PBR materials by their heights: the higher one shows, with a soft transition. In: `base_color_1` Color, `normal_1` Color, `roughness_1` Gray, `metallic_1` Gray, `height_1` Gray, `base_color_2` Color, `normal_2` Color, `roughness_2` Gray, `metallic_2` Gray, `height_2` Gray. Out: `base_color` Color, `normal` Color, `roughness` Gray, `metallic` Gray, `height` Gray, `mask` Gray. Params: `height_offset` float=0.5 [0..1]; `contrast` float=0.9 [0..1].

## Material filters/Weathering

- `edge_wear` (Edge Wear): A mask of worn, exposed edges from the convex areas of a height map (or a curvature map), broken up by noise. In: `height` Gray, `curvature` Gray. Out: `output` Gray. Params: `width` float=4 [0.25..64]; `amount` float=0.5 [0..1]; `noise_scale` float=8 [1..64]; `noise_amount` float=0.5 [0..1]; `contrast` float=0.6 [0..1].
- `dirt_mask` (Dirt Mask): A mask of dirt gathering in cavities of a height map (and dark ambient occlusion), broken up by noise. In: `height` Gray, `ao` Gray. Out: `output` Gray. Params: `spread` float=16 [0.5..128]; `amount` float=0.5 [0..1]; `noise_scale` float=8 [1..64]; `noise_amount` float=0.5 [0..1]; `contrast` float=0.6 [0..1].
- `dust_mask` (Dust Mask): A mask of dust settling on surfaces facing a direction (from a normal map) and on flat areas. In: `normal` Color. Out: `output` Gray. Params: `direction` float=0.25 [-1..1]; `flat` float=0.3 [0..1]; `amount` float=0.5 [0..1]; `noise_scale` float=8 [1..64]; `noise_amount` float=0.5 [0..1]; `contrast` float=0.6 [0..1].
- `rust` (Rust): A mask of rust blotches and pitting; with a mask input it grows out from the mask (edges, cavities). In: `mask` Gray. Out: `output` Gray. Params: `amount` float=0.45 [0..1]; `scale` float=6 [1..64]; `spread` float=12 [0..128]; `pitting` float=0.5 [0..1]; `contrast` float=0.7 [0..1].
- `moss` (Moss / Lichen): Fuzzy moss clumps (gathering in low areas) or round lichen rosettes (on high areas) of an optional height map. In: `height` Gray. Out: `output` Gray. Params: `style` enum=0 {0 Moss, 1 Lichen}; `amount` float=0.5 [0..1]; `scale` float=6 [1..64]; `height_bias` float=0.5 [0..1]; `contrast` float=0.6 [0..1].
- `leaks` (Leaks): Streaky drips running down from a mask (unconnected: random stains), fading with length and meandering. In: `mask` Gray. Out: `output` Gray. Params: `length` float=0.35 [0..1]; `length_random` float=0.7 [0..1]; `streaks` float=32 [1..256]; `wobble` float=0.3 [0..1].
- `edge_damage` (Edge Damage): Chips the edges of a height mask (white = material) in chunky, ragged bites; also outputs the damage mask. In: `height` Gray. Out: `output` Gray, `mask` Gray. Params: `width` float=8 [0..64]; `amount` float=0.5 [0..1]; `scale` float=12 [1..64]; `roughness` float=0.5 [0..1]; `depth` float=1 [0..1].
