# SoundCraft built-in plugins

Generated from `execute engine.plugins` (SoundCraft 0.3.0, 26 plugins). Use the `id` with
`mix.insert {track, plugin, params}` (live insert, slots 0–9) or `audiosuite.process {process: id, params, clips}` (offline render).
Each param: `id` default [min..max unit]; choice params take the **index** (`{0:Peak|1:Low Shelf…}`); toggles are 0/1.
Unknown param ids are rejected by `mix.insert` (`` `compressor` has no parameter `thresh` ``) but silently ignored by `audiosuite.process`.

## Eq

### `eq_1band` — EQ 1-Band

- `type` 0 — 0=Peak, 1=Low Shelf, 2=High Shelf, 3=High Pass, 4=Low Pass, 5=Notch, 6=Band Pass
- `freq` 1000 [20..20000 Hz]
- `gain` 0 [-24..24 Db]
- `q` 1 [0.1..10 None]
- `output_gain` 0 [-24..24 Db]

### `eq_7band` — EQ 7-Band

- `input_gain` 0 [-24..24 Db]
- `hpf_on` 0 [0..1 Toggle]
- `hpf_freq` 80 [10..2000 Hz]
- `hpf_slope` 1 — 0=6 dB/oct, 1=12 dB/oct, 2=18 dB/oct, 3=24 dB/oct
- `low_shelf_freq` 100 [20..1000 Hz]
- `low_shelf_gain` 0 [-24..24 Db]
- `low_shelf_q` 0.707 [0.3..2 None]
- `low_mid_freq` 250 [20..2000 Hz]
- `low_mid_gain` 0 [-24..24 Db]
- `low_mid_q` 1 [0.1..10 None]
- `mid_freq` 1000 [100..8000 Hz]
- `mid_gain` 0 [-24..24 Db]
- `mid_q` 1 [0.1..10 None]
- `high_mid_freq` 4000 [500..20000 Hz]
- `high_mid_gain` 0 [-24..24 Db]
- `high_mid_q` 1 [0.1..10 None]
- `high_shelf_freq` 8000 [1000..20000 Hz]
- `high_shelf_gain` 0 [-24..24 Db]
- `high_shelf_q` 0.707 [0.3..2 None]
- `lpf_on` 0 [0..1 Toggle]
- `lpf_freq` 18000 [1000..20000 Hz]
- `lpf_slope` 1 — 0=6 dB/oct, 1=12 dB/oct, 2=18 dB/oct, 3=24 dB/oct
- `output_gain` 0 [-24..24 Db]

## Dynamics

### `compressor` — Compressor/Limiter

- `threshold` -20 [-60..0 Db]
- `ratio` 4 [1..100 Ratio]
- `attack` 10 [0.01..300 Ms]
- `release` 100 [5..3000 Ms]
- `knee` 6 [0..24 Db]
- `makeup` 0 [0..40 Db]
- `sc_hpf_on` 0 [0..1 Toggle]
- `sc_hpf_freq` 100 [20..500 Hz]
- `limiter` 0 [0..1 Toggle]
- `lookahead` 0 [0..10 Ms]
- `mix` 100 [0..100 Percent]

### `expander_gate` — Expander/Gate

- `threshold` -40 [-80..0 Db]
- `ratio` 100 [1..100 Ratio]
- `range` 80 [0..80 Db]
- `attack` 0.5 [0.01..100 Ms]
- `hold` 50 [0..2000 Ms]
- `release` 100 [1..4000 Ms]

### `de_esser` — De-Esser

- `freq` 6000 [2000..16000 Hz]
- `range` 10 [0..40 Db]
- `threshold` -30 [-60..0 Db]
- `listen` 0 [0..1 Toggle]

### `maximizer` — Maximizer

- `threshold` 0 [-30..0 Db]
- `ceiling` -0.3 [-30..0 Db]
- `release` 50 [1..1000 Ms]

### `channel_strip` — Channel Strip

- `input_gain` 0 [-24..24 Db]
- `gate_on` 0 [0..1 Toggle]
- `gate_threshold` -50 [-80..0 Db]
- `gate_range` 40 [0..80 Db]
- `gate_release` 150 [1..4000 Ms]
- `comp_on` 0 [0..1 Toggle]
- `comp_threshold` -18 [-60..0 Db]
- `comp_ratio` 3 [1..100 Ratio]
- `comp_attack` 10 [0.01..300 Ms]
- `comp_release` 120 [5..3000 Ms]
- `comp_makeup` 0 [0..40 Db]
- `eq_on` 1 [0..1 Toggle]
- `hpf_on` 0 [0..1 Toggle]
- `hpf_freq` 80 [10..2000 Hz]
- `low_gain` 0 [-24..24 Db]
- `low_freq` 100 [20..1000 Hz]
- `mid_gain` 0 [-24..24 Db]
- `mid_freq` 1000 [100..8000 Hz]
- `mid_q` 1 [0.1..10 None]
- `high_gain` 0 [-24..24 Db]
- `high_freq` 8000 [1000..20000 Hz]
- `output_gain` 0 [-24..24 Db]

## Reverb

### `room_reverb` — Room Reverb

- `mix` 25 [0..100 Percent]
- `pre_delay` 10 [0..250 Ms]
- `decay` 1.2 [0.1..20 Seconds]
- `size` 50 [0..100 Percent]
- `damping` 6000 [1000..20000 Hz]
- `diffusion` 70 [0..100 Percent]
- `width` 100 [0..100 Percent]
- `low_cut` 20 [20..1000 Hz]

### `plate_reverb` — Plate Reverb

- `mix` 30 [0..100 Percent]
- `pre_delay` 20 [0..250 Ms]
- `decay` 2.5 [0.1..20 Seconds]
- `size` 50 [0..100 Percent]
- `damping` 10000 [1000..20000 Hz]
- `diffusion` 85 [0..100 Percent]
- `width` 100 [0..100 Percent]
- `low_cut` 20 [20..1000 Hz]

## Delay

### `mod_delay` — Mod Delay

- `time` 250 [1..2000 Ms]
- `feedback` 30 [-99..99 Percent]
- `mix` 30 [0..100 Percent]
- `mod_rate` 0.5 [0.01..10 Hz]
- `mod_depth` 0 [0..100 Percent]
- `lpf` 12000 [500..20000 Hz]

## Modulation

### `chorus` — Chorus

- `rate` 0.8 [0.05..5 Hz]
- `depth` 50 [0..100 Percent]
- `delay` 12 [5..30 Ms]
- `feedback` 0 [0..90 Percent]
- `mix` 50 [0..100 Percent]
- `spread` 100 [0..100 Percent]

### `flanger` — Flanger

- `rate` 0.25 [0.02..5 Hz]
- `depth` 70 [0..100 Percent]
- `delay` 2 [0.1..10 Ms]
- `feedback` 50 [-95..95 Percent]
- `mix` 50 [0..100 Percent]

### `phaser` — Phaser

- `rate` 0.5 [0.02..5 Hz]
- `depth` 70 [0..100 Percent]
- `stages` 2 — 0=2, 1=4, 2=6, 3=8, 4=12
- `feedback` 40 [-95..95 Percent]
- `center` 800 [100..4000 Hz]
- `mix` 50 [0..100 Percent]

## Harmonic

### `saturator` — Saturator

- `drive` 6 [0..36 Db]
- `bias` 0 [0..100 Percent]
- `tone` 20000 [1000..20000 Hz]
- `mix` 100 [0..100 Percent]
- `output` 0 [-24..12 Db]

### `lofi` — Lo-Fi

- `bits` 8 [1..24 None]
- `sample_rate` 11025 [500..48000 Hz]
- `noise` 0 [0..100 Percent]
- `mix` 100 [0..100 Percent]

### `rectifier` — Rectifier

- `mode` 1 — 0=Half Wave, 1=Full Wave
- `mix` 100 [0..100 Percent]
- `output` 0 [-24..12 Db]

## PitchShift

### `pitch_shifter` — Pitch Shifter

- `semitones` 0 [-24..24 Semitones]
- `cents` 0 [-100..100 Cents]
- `mix` 100 [0..100 Percent]

## Other

### `time_shift` — Time Shift

- `delay_ms` 0 [0..1000 Ms]
- `delay_samples` 0 [0..10000 None]

### `gain` — Gain

- `gain` 0 [-96..24 Db]

### `trim` — Trim

- `gain` 0 [-96..12 Db]
- `invert` 0 [0..1 Toggle]

### `invert` — Invert

- (no parameters)

### `dc_offset_removal` — DC Offset Removal

- `cutoff` 5 [1..40 Hz]

### `signal_generator` — Signal Generator

- `waveform` 0 — 0=Sine, 1=Square, 2=Saw, 3=Triangle, 4=White Noise, 5=Pink Noise
- `freq` 1000 [20..20000 Hz]
- `level` -20 [-96..0 Db]

## Dither

### `dither` — Dither

- `bits` 0 — 0=16, 1=20, 2=24
- `noise_shaping` 0 [0..1 Toggle]

## Instrument

### `subtractive_synth` — Subtractive Synth (instrument: `track.new {kind: instrument, instrument: id}`)

- `osc1_wave` 0 — 0=Saw, 1=Square, 2=Sine, 3=Triangle
- `osc2_wave` 0 — 0=Saw, 1=Square, 2=Sine, 3=Triangle
- `osc2_semitones` 0 [-24..24 Semitones]
- `osc2_detune` 7 [-100..100 Cents]
- `osc_mix` 50 [0..100 Percent]
- `cutoff` 2000 [20..20000 Hz]
- `resonance` 20 [0..100 Percent]
- `filter_env_amount` 30 [-100..100 Percent]
- `amp_attack` 5 [0.5..5000 Ms]
- `amp_decay` 200 [1..5000 Ms]
- `amp_sustain` 70 [0..100 Percent]
- `amp_release` 300 [1..10000 Ms]
- `filter_attack` 5 [0.5..5000 Ms]
- `filter_decay` 300 [1..5000 Ms]
- `filter_sustain` 30 [0..100 Percent]
- `filter_release` 300 [1..10000 Ms]
- `glide` 0 [0..1000 Ms]
- `velocity` 70 [0..100 Percent]
- `level` -6 [-48..6 Db]

### `drum_synth` — Drum Synth (instrument: `track.new {kind: instrument, instrument: id}`)

- `level` -6 [-48..6 Db]
- `kick_tune` 0 [-12..12 Semitones]
- `kick_decay` 450 [50..2000 Ms]
- `snare_tune` 0 [-12..12 Semitones]
- `snare_snappy` 60 [0..100 Percent]
- `snare_decay` 220 [50..1000 Ms]
- `hat_decay` 80 [20..500 Ms]
- `open_hat_decay` 600 [100..3000 Ms]
- `tom_tune` 0 [-12..12 Semitones]
- `tom_decay` 500 [50..2000 Ms]
- `cymbal_decay` 2000 [200..6000 Ms]

## AudioSuite-only processes

`audiosuite.process {process, params, clips}` also takes these (from the engine source):

- `normalize` {target_db: -0.1} (peak)
- `gain` {db: 0}
- `reverse`, `invert`, `duplicate` (no params)
- `time_stretch` {ratio: 1.0, 0.25..4; 2 = twice as long, pitch kept}
- `pitch_shift` {semitones: 0, -24..24; length kept}
- `varispeed` {speed: 1.0, 0.25..4; changes length and pitch}
