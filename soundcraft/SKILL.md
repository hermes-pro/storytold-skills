---
name: soundcraft
description: "Audio editing, recording and mixing with SoundCraft (Pro Tools-style DAW): podcast and voice-over cleanup, music mixing and mastering, trimming, fades, crossfades, EQ, compression, reverb, sound effects, stems, loudness (LUFS) and WAV / AIFF / FLAC bounces."
version: 0.4.0
author: storytold
license: MIT
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [Creative, Audio, Music, Podcast, Mixing, Mastering, DAW, Sound, MCP]
    related_skills: [storytold, storytold-install, filmcraft, effectcraft]
---

# SoundCraft

SoundCraft is a free, open-source clean-room take on Avid Pro Tools (storytold Crafting Apps). An agent
drives it through an MCP server (`soundcraft-cli mcp`) or one-shot CLI commands. Sessions stay editable:
clips are non-destructive, and plugins, sends and automation stay live until you bounce.

## When to Use

Use it for **anything you'd do in a DAW**:

- podcasts, interviews, voice-overs, audiobooks: trim, cut ums and gaps, fade, EQ, compress, de-ess, hit a loudness target
- music: multitrack mixes, gain and pan, inserts, reverb or delay busses, automation, mastering limiter, stems
- sound design and effects: layering, pitch shift, time stretch, reverse, built-in synths, drum synth and sampler from MIDI notes
- converting, resampling or normalizing audio files; measuring peak, true peak and LUFS

Pick a different Crafting App when:

| The job is… | Use |
|---|---|
| Cutting video, or audio that must stay in sync with picture edits | `filmcraft` |
| Motion graphics, animation, compositing (with or without a soundtrack) | `effectcraft` |
| Only a format change or one-filter fix on a file | `soundcraft-cli convert`, or ffmpeg |

## Setup

1. If tools named `mcp_soundcraft_*` are available, use them. This is the preferred way.
2. Otherwise check for the CLI with `soundcraft-cli --version`. If it's missing, load the
   `storytold-install` skill and run its `setup soundcraft`. Then ask the user to start a new session
   or run `/reload-mcp` so the MCP tools appear.
3. Until the MCP tools appear, use the CLI one-shots (see **CLI** below).

Bare `soundcraft-cli mcp` is **headless**: a full engine with no window and no audio device, so nothing
plays out loud. Everything works except the APP_ONLY tools. For the user to watch live, they run
`soundcraft --control 0` (it prints `SOUNDCRAFT_CONTROL_PORT=<port>`) and the server is started as
`soundcraft-cli mcp --connect <port>`. Close it later with `soundcraft-cli app --port <port> app.quit`.

Bare `mcp` can read and write any absolute path. To confine it, start it with
`--automation-read-root DIR --automation-write-root DIR` (existing folders; give the same folder twice,
or you can't reopen what you saved). Then every open/import/sampler load must be inside the read root and
every save/bounce/export inside the write root; relative paths resolve against the server's working
directory. Refusals read ``automation path rejected: outside the write root C:\work: C:/Windows/Temp/x.wav``;
with no write root: `automation filesystem access is not granted: write authority is absent: …`. A session
whose audio lies outside the read root opens with those files under `missing`. The roots can't be combined
with `--connect`.

## Mental Model

- A **session** (`.scraft` JSON + an `Audio Files/` folder) holds **tracks** (audio, aux, master,
  instrument, midi, vca, folder), **busses**, markers, a tempo/meter map and the edit **selection**.
  Default: 48 kHz, 24-bit, 120 bpm, Slip mode. Imports are converted to the session rate. Importing
  `kick.wav` a second time makes a track named `kick 1`.
- **Clips** sit on a track's playlist and point into a **source** with an `offset`. Edits never touch
  the source file. `inspect_session` lists each clip's `id`, `start`, `end`, `length`, `fade_in/out`, `gain_db`.
- **Positions** are samples (integers), `{"seconds": 2.5}`, or strings: `"0:12.500"`, `"bars_beats:5|1|000"`,
  `"timecode:00:00:10:00"`. MIDI notes use ticks (960 per quarter note).
- **Every action is a command** (478 of them): `execute {command, params}`, or `batch {calls: [...]}` for
  several. Find them with `list_commands {filter: "fade"}` or grep `references/commands.md`.
- Omitted `tracks` / `start` / `end` / `clips` fall back to the **current selection**. Pass them explicitly.
  `track` (one name/id) and `tracks` (an array, or a single name) are both accepted by most commands.
- Signal flow: clip → track inserts (slots 0–9) → fader/pan → sends to busses → output `Main`.
  An **aux** track whose input is a bus is a return. A **master** track puts inserts on the whole mix.
- Everything is undoable: `execute edit.undo`; `execute engine.history` lists the undo stack.

## Tools (Hermes names them `mcp_soundcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `new_session {name?, sample_rate?, template?: blank\|demo}` | Start fresh (the demo is a 9-track song to experiment with) |
| `open_session {path}` / `save_session {path?, replace?}` | `.scraft` files; save copies the audio into `Audio Files/` next to it. Saving over a different existing file needs `replace: true` |
| `import_audio {path, track?, at?}` | WAV AIFF FLAC MP3 OGG AAC/M4A ALAC CAF. New track (named after the file) unless `track`. Returns `track`, `clip`, `source` ids |
| `execute {command, params}` | Run one command; errors come back as text (see Pitfalls) |
| `batch {calls, keep_going?}` | Several commands in order, stops at the first error. With `keep_going` it runs them all and returns `{command, ok, result\|error}` per call (flagged as an error if any failed) |
| `list_commands {filter?}` | Command ids, menu path, params doc, `enabled` + `disabled_reason` |
| `inspect_session {detail?: summary\|full}` | Verify work. `full` adds every insert's params |
| `bounce_mix {path, format?, bit_depth?, start?, end?, normalize?}` | Render to WAV/AIFF/FLAC; returns `seconds`, `peak_db`, `true_peak_db`, `lufs`. For one bus alone: `execute file.bounce_mix {path, source:"Verb", start, end}` |
| `parity` | Feature-parity report (rarely needed) |
| `screenshot`, `ui_inspect`, `ui_set`, `menu_invoke`, `click`, `drag`, `key` | APP_ONLY (with `--connect`) |

Resources: `soundcraft://session` (session JSON), `soundcraft://commands` (the catalog).
Handy queries: `execute track.inspect {track}`, `clip.inspect {clip}`, `engine.plugins` (plugin params),
`session.audio_health` (clips pointing at missing or short audio; `healthy: true` when fine).

## Plugins and Processing

Built-ins (`references/plugins.md` has every param, default and range): `eq_1band`, `eq_7band`, `compressor`,
`expander_gate`, `de_esser`, `maximizer`, `channel_strip`, `room_reverb`, `plate_reverb`, `mod_delay`,
`chorus`, `flanger`, `phaser`, `saturator`, `lofi`, `rectifier`, `pitch_shifter`, `time_shift`, `gain`,
`trim`, `invert`, `dc_offset_removal`, `signal_generator`, `dither`, instruments `subtractive_synth`, `drum_synth`,
`sampler` (plays an audio file across the keyboard).
There is **no noise-reduction plugin**: use `expander_gate` or `edit.strip_silence`, or ffmpeg `afftdn` before import.

- **Live insert:** `mix.insert {track, plugin, params}` → returns its `slot`. Change later with
  `mix.insert_param {track, slot, param, value}` / `mix.insert_params`; `mix.insert_bypass`, `mix.insert_remove`.
- **Instruments:** `mix.instrument {track, plugin}` swaps an instrument track's instrument;
  `mix.instrument_param {track, param, value}` sets one of its params (clamped into range).
- **Choice params take the index** (`eq_1band type: 3` = High Pass). Toggles are `0/1` (`hpf_on: 1`).
- **AudioSuite (offline render into a new clip):** `audiosuite.process {process, params, clips: [id]}` with any
  plugin id, or `normalize {target_db}`, `gain {db}`, `reverse`, `invert`, `time_stretch {ratio}`,
  `pitch_shift {semitones}`, `varispeed {speed}`. The new clip is named `<clip>-<proc>` (`voice-reve`); on save,
  same-named renders get their own files (`tone-reve.wav`, `tone-reve_01.wav`), so nothing is overwritten.

## Procedure

1. **Plan** the deliverable: length, format (WAV/FLAC/AIFF; MP3 via ffmpeg afterwards), loudness target
   (podcast −16 LUFS stereo, music streaming ≈ −14 LUFS, true peak ≤ −1 dBTP).
2. **Set up:** `new_session`, `import_audio` each file (absolute paths), keep the returned track and clip ids.
3. **Edit:** trim, cut, move, fades. Check positions with `track.inspect` after each step.
4. **Mix:** inserts, volume/pan, busses and sends, automation, a master track with a limiter.
5. **Bounce** with explicit `start` and `end`, read `peak_db` / `lufs`, adjust and re-bounce until on target.
6. **Verify** the file independently (see Verification), then `save_session` if the user wants the editable session.

### Recipe: podcast cleanup to −16 LUFS (tested)

```text
new_session {name:"Episode"}
import_audio {path:"/abs/voice.wav"}                     → track 2 "voice", clip 3
execute track.rename {track:"voice", name:"Host"}
execute edit.trim_to_selection {tracks:["Host"], start:{seconds:1.3}, end:{seconds:11.7}}   # cut head/tail
execute edit.move_clips {clips:[3], to:0}
execute edit.mode {mode:"shuffle"}                       # deletions close the gap
execute edit.clear {tracks:["Host"], start:{seconds:5}, end:{seconds:7}}   # remove a flub
execute edit.mode {mode:"slip"}
execute edit.fades_create {tracks:["Host"], start:0, end:{seconds:0.5}}            # fade in
execute edit.fades_create {tracks:["Host"], start:{seconds:7.9}, end:{seconds:8.4}} # fade out (range must reach the clip end)
execute mix.insert {track:"Host", plugin:"eq_7band", params:{hpf_on:1, hpf_freq:80, high_mid_freq:3500, high_mid_gain:2}}
execute mix.insert {track:"Host", plugin:"compressor", params:{threshold:-24, ratio:3, attack:5, release:120, makeup:4}}
execute mix.insert {track:"Host", plugin:"de_esser", params:{freq:6500, threshold:-28}}
execute track.new {kind:"master", format:"stereo"}        → id; named "Master 1"
execute mix.insert {track:"Master 1", plugin:"maximizer", params:{threshold:-4, ceiling:-1.5}}
execute edit.select_none
bounce_mix {path:"/abs/probe.wav", start:0, end:"0:08.400"}   → lufs −18.0, peak −12.6
execute mix.volume {tracks:["Host"], delta_db: 2.0}        # target − measured; re-bounce and nudge until ±0.5
bounce_mix {path:"/abs/episode.wav", start:0, end:"0:08.400", bit_depth:"16"}   → −16.0 LUFS, peak −10.6
```

Checked on 0.8.0 with ffmpeg `ebur128` and ffprobe: −16.0 LUFS, −10.6 dBFS, 8.4 s, 48 kHz stereo
`pcm_s16le`; the waveform shows the fade-in and fade-out. (The test voice was a −20 LUFS synthetic signal;
real speech has more peak, so the maximizer works harder.) A limiter makes gain changes non-linear, so
iterate rather than computing once.

### Recipe: music mix with a reverb bus (tested)

```text
new_session {name:"Song"}
import_audio kick.wav, bass.wav, pad.wav                  → tracks "kick", "bass", "pad"
execute mix.new_bus {name:"Verb"}
execute track.new {kind:"aux", format:"stereo", name:"Verb Return"}
execute track.input {tracks:["Verb Return"], input:"Verb"}
execute mix.insert {track:"Verb Return", plugin:"plate_reverb", params:{mix:100, decay:2.0}}   # 100% wet on a return
execute mix.send {track:"pad", bus:"Verb", level_db:-6}
execute mix.send {track:"kick", bus:"Verb", level_db:-14}
batch {calls:[{command:"mix.volume", params:{tracks:["kick"], db:-3}}, …bass -4, pad -8]}
execute mix.pan {tracks:["bass"], pan:-0.3}
execute mix.insert {track:"bass", plugin:"saturator", params:{drive:9}}
execute automation.set_point {track:"pad", param:"volume", at:{seconds:6}, value:-8}
execute automation.set_point {track:"pad", param:"volume", at:{seconds:8}, value:-60}   # fade-out ride
execute markers.add {name:"Drop", at:"bars_beats:3|1|000"}
execute track.new {kind:"master", format:"stereo"}        # a hot mix without a limiter clips (see Pitfalls)
execute mix.insert {track:"Master 1", plugin:"maximizer", params:{threshold:-2, ceiling:-1}}
bounce_mix {path:"/abs/song.wav", start:0, end:{seconds:10}}   # 8 s of clips; the extra 2 s keep the reverb tail
bounce_mix {path:"/abs/song.flac", format:"flac", bit_depth:"16", start:0, end:{seconds:10}}
execute file.bounce_stems {dir:"/abs/stems"}               → "Song - kick.wav", … (source tracks only, 8 s each)
execute file.bounce_mix {path:"/abs/verb.wav", source:"Verb", start:0, end:{seconds:10}}   # the bus alone
```

On 0.8.0: 10.0 s 48 kHz stereo WAV (24-bit) and FLAC, three stems, and the reverb tail visible after 8 s
in the waveform. The maximizer added 2 dB (−21.4 → −19.4 LUFS with quiet test tones). An unknown
`source` fails with ``unknown bus `Nope` ``.

### Recipe: play a sample from MIDI with the Sampler (tested)

```text
execute event.tempo {bpm:100}
execute track.new {kind:"instrument", instrument:"sampler", name:"Keys"}       → track id
execute mix.sampler_load {track:"Keys", path:"/abs/note.wav", params:{root_note:60}}   → {source, frames, …}
execute midi.new_clip {track:"Keys", start:0, length:"bars_beats:3|1|000"}       → {clip: 9, …}
batch {calls:[{command:"midi.note_add", params:{clip:9, pitch:60, start_ticks:0, length_ticks:480}},
              … pitch 64 at 960, 67 at 1920, 72 at 2880]}
bounce_mix {path:"/abs/keys.wav", start:0, end:{seconds:3}}
```

The four notes came out at 263, 333, 390 and 527 Hz (C4 E4 G4 C5 from a C4 sample), each cut to the note
length (`play_mode` 0 = Gate; 1 = One Shot plays the whole sample). Other params (`loop_mode`,
`key_low`/`key_high`, `attack`, `release`, …) are in `references/plugins.md`. `mix.sampler_clear {track}`
unloads the sample.

### More building blocks (tested)

- **Split / move / crossfade:** `edit.separate {tracks, at}` splits (new clip id in `track.inspect`);
  `edit.move_clips {clips, by | to}` (`by` in samples or `{seconds}`); `edit.fades_create` over a range that
  spans the boundary of two butted clips gives a fade-out + fade-in pair (`shape: "equal power"`): a 3.8–4.2 s
  range over a split at 4 s made a 0.4 s overlap.
- **Trim one clip / fade one clip:** `edit.trim_clip {clip, start?, end?}` moves its edges (1–9 s of a 12 s
  clip → `{start:48000, end:432000}`); `edit.fades_create {clip, side:"in"|"out", length:24000, shape?}` fades
  it without a range (`length` is samples only; `{seconds}` fails with `length must be a positive sample count`).
- **Remove silences:** `edit.select {tracks, start, end}` then `edit.strip_silence {threshold_db:-40, min_length_ms:200}`
  (tone-gap-tone-gap-tone → 3 clips). Run `edit.select_none` afterwards.
- **Clip gain:** `clip.gain {clips:[id], db:-6}` (or `delta_db`); `clip.gain_nudge_up` / `_down {clips}` step 1 dB.
- **Offline effects:** `audiosuite.process {process:"time_stretch", params:{ratio:1.1}, clips:[3]}` → clip 10 % longer;
  `{process:"normalize", params:{target_db:-1}}`; `{process:"eq_1band", params:{type:3, freq:100}}`; `reverse`, `invert`.
  `pitch_shift {semitones}` is clamped to ±24 (36 came out as +24).
- **Test tone / room tone:** `audiosuite.process {process:"signal_generator", params:{waveform:0, freq:1000, level:-20},
  tracks:["Tone"], start:{seconds:10}, end:{seconds:11}}` puts a new 1 s clip on each listed audio track.
- **Synth parts / sound effects from MIDI:** `event.tempo {bpm:100}`; `track.new {kind:"instrument",
  instrument:"subtractive_synth", name:"Lead"}`; `midi.new_clip {track:"Lead", start:0, length:"bars_beats:3|1|000"}`
  → clip id (use the returned one); `midi.note_add {clip, pitch:60, start_ticks:0, length_ticks:960, velocity?}`.
  A `drum_synth` track played notes 36, 42 and 38 (kick, hat, snare). `file.export_midi {path}` writes a `.mid`.
  The synths are quiet by default (`level` −6 dB): `mix.instrument_param {track:"Lead", param:"level", value:0}`
  brought a 3-note line to −20 LUFS.

## Formats

- **Import:** WAV/BWF/RF64, AIFF, FLAC, MP3, OGG Vorbis, AAC/M4A, ALAC, CAF, and the audio of MP4/MOV.
- **Bounce / convert output:** WAV, AIFF, FLAC only, 16 / 24 / 32f bit (`bit_depth` is a string: `"16"`).
  The format follows `format` or the `.flac`/`.aiff` extension. Other extensions are refused:
  ``cannot write `mp3` files (supported: wav, aif, aiff, flac)``. Make MP3/AAC/OGG with ffmpeg from the WAV:
  `ffmpeg -i mix.wav -b:a 192k mix.mp3`.
- `normalize: true` on a bounce is a **peak** normalize to −0.1 dBFS, not loudness.

## CLI (no MCP needed)

```bash
soundcraft-cli info FILE                                 # audio: rate, channels, seconds; .scraft: session text report
soundcraft-cli convert in.wav out.flac [--bit-depth 16|24|32f] [--rate 48000] [--normalize]
soundcraft-cli run [--in S.scraft | --demo] --cmd 'file.import_audio={"path":"/abs/v.wav"}' \
    --cmd 'mix.insert={"track":"v","plugin":"compressor","params":{"threshold":-24}}' \
    --bounce out.flac [--start 0:00.000 --end 0:12.000] [--save S.scraft] [--inspect]
soundcraft-cli script cmds.txt [--in S] [--save S] --bounce out.wav     # one `ID {json}` per line
soundcraft-cli commands [FILTER] · describe ID · plugins · parity [--write PATH]
soundcraft-cli app [--port P] METHOD [JSON]              # call a running app's control channel
soundcraft-cli mcp [--connect PORT] [--demo] [--automation-read-root DIR] [--automation-write-root DIR]
```

`run`/`script` print one JSON result per command plus the bounce report. `--start/--end` take time
strings (`0:04.000`), not JSON (`{"seconds":4}` fails with `cannot parse position`). Malformed `--cmd` JSON
stops the run (`mix.insert: bad JSON: key must be a string at line 1 column 2`). `--save` over an existing
session replaces it and keeps the old one in `Backups/S backup N.scraft` next to it. `convert` refuses bad
values (``--bit-depth: expected 16, 24 or 32f, got `12` ``, ``--rate: expected a sample rate in Hz, got `0` ``).

## Pitfalls

- **A live edit selection limits the bounce.** After `edit.select` or `edit.strip_silence`, `bounce_mix` without
  `start`/`end` renders only the selection. Run `edit.select_none` and always pass **both** `start` and `end`
  — `end` alone is ignored (asked for 4 s, got the full 12 s), and the session end cuts off reverb/delay tails.
- **Clipping is reported, not prevented.** `peak_db: 2.98` came back while the 24-bit WAV was hard-clipped
  at 0 dBFS (ffmpeg `volumedetect`: 108 480 samples at 0 dB). Keep `peak_db` ≤ −1 (master `maximizer` with
  `ceiling: -1`) before delivering.
- **AudioSuite drops clip gain** for most processes (`reverse`, `normalize`, `time_stretch`, plugin renders):
  it renders without it and resets `gain_db` to 0. `invert` keeps it. It also **ignores unknown params**
  (normalize's is `target_db`, not `level_db`). Apply clip gain after the render.
- **Unknown clip ids don't error** in most edit commands: `clip.gain {clips:[999]}` returns `{"clips":1}`,
  `edit.move_clips` returns `moved: 0`, `audiosuite.process` returns `processed: 0`. Check those counts.
  (`clip.inspect` does fail: `no such clip`.)
- **Saving over another existing file is refused:** ``… already exists: pass `replace: true` to replace it``.
  Re-saving the session's own file is fine.
- **Master names are fixed:** `track.new {kind:"master", name:"Master"}` ignores the name (it's `Master 1`).
  Use the returned ids.
- **Slip mode overwrites.** `edit.move_clips` onto a neighbour trims it (moving back leaves a gap), and
  `edit.duplicate` lays the copy right after the range over whatever was there.
- **Mono tracks panned centre are −3 dB** per side in the stereo bounce (pan law).
- `edit.fades_create` needs a range covering a clip start, end or boundary, otherwise:
  `the selection must cover a clip start, end or the boundary between two clips`.
- Relative paths resolve against the server's working directory. Use absolute paths everywhere.
- Error texts are precise — read them: ``unknown command `edit.x` ``, ``unknown plugin `noise_reduction` ``,
  `` `compressor` has no parameter `thresh` `` (`mix.insert`, `mix.instrument {params}`),
  `` `compressor` has no parameter(s): thresh `` and `parameter(s) need a numeric value: ratio` (`mix.insert_params`),
  `unknown track "Nope"`, `no such clip`,
  `` `edit.cut` is not available: make an edit selection first ``.

## Verification

- `inspect_session` / `track.inspect`: clip positions, fades, inserts (`detail:"full"` for params), sends, automation.
- Every `bounce_mix` reply: `seconds` equals the intended length; `peak_db` ≤ −1; `lufs` near the target.
- Independently: `ffprobe -show_entries stream=codec_name,sample_rate,channels:format=duration out.wav`,
  `ffmpeg -i out.wav -af ebur128=peak=true -f null -` (LUFS, true peak), and
  `ffmpeg -i out.wav -lavfi showwavespic=s=1200x300 wave.png`, then **look** at the PNG for cut words, clicks,
  missing fades or a flat-topped (clipped) waveform.
- `execute session.audio_health` before saving or delivering: `healthy: true`, `issue_count: 0`.
- After `save_session`, `soundcraft-cli info Session.scraft` lists tracks, clips and files. `open_session`
  returns `missing: []` when every audio file was found.
- A session's stored paths resolve against its own folder (`../media/v.wav` works). Paths on another
  computer are refused, not read: `open_session` lists `\\192.0.2.1\share\x.wav: not opened: the path is on
  another computer` under `missing`, and those clips bounce silent (`session.audio_health` → `unavailable_audio`).
  Copy the audio locally and re-import it.

## References

Grep these rather than reading them whole, e.g. `grep -n sampler ${HERMES_SKILL_DIR}/references/commands.md`.

- `references/commands.md`: all 478 commands with params, grouped by area.
- `references/plugins.md`: all 27 built-in plugins with param ids, defaults and ranges, plus the AudioSuite-only processes.
- Upstream docs: https://github.com/storytold/soundcraft/tree/main/docs (`mcp.md`, `control-protocol.md`).
