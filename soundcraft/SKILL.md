---
name: soundcraft
description: "Audio editing, recording and mixing with SoundCraft (Pro Tools-style DAW): podcast and voice-over cleanup, music mixing and mastering, trimming, fades, crossfades, EQ, compression, reverb, sound effects, stems, loudness (LUFS) and WAV / AIFF / FLAC bounces."
version: 0.1.0
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
- sound design and effects: layering, pitch shift, time stretch, reverse, built-in synths and drum synth from MIDI notes
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

## Mental Model

- A **session** (`.scraft` JSON + an `Audio Files/` folder) holds **tracks** (audio, aux, master,
  instrument, midi, vca, folder), **busses**, markers, a tempo/meter map and the edit **selection**.
  Default: 48 kHz, 24-bit, 120 bpm, Slip mode. Imports are converted to the session rate.
- **Clips** sit on a track's playlist and point into a **source** with an `offset`. Edits never touch
  the source file. `inspect_session` lists each clip's `id`, `start`, `end`, `length`, `fade_in/out`, `gain_db`.
- **Positions** are samples (integers), `{"seconds": 2.5}`, or strings: `"0:12.500"`, `"bars_beats:5|1|000"`,
  `"timecode:00:00:10:00"`. MIDI notes use ticks (960 per quarter note).
- **Every action is a command** (460 of them): `execute {command, params}`, or `batch {calls: [...]}` for
  several. Find them with `list_commands {filter: "fade"}` or grep `references/commands.md`.
- Omitted `tracks` / `start` / `end` / `clips` fall back to the **current selection**. Pass them explicitly.
  `track` (one name/id) and `tracks` (an **array**) are both accepted by most commands.
- Signal flow: clip → track inserts (slots 0–9) → fader/pan → sends to busses → output `Main`.
  An **aux** track whose input is a bus is a return. A **master** track puts inserts on the whole mix.
- Everything is undoable: `execute edit.undo`; `execute engine.history` lists the undo stack.

## Tools (Hermes names them `mcp_soundcraft_<tool>`)

| Tool | Use it for |
|---|---|
| `new_session {name?, sample_rate?, template?: blank\|demo}` | Start fresh (the demo is a 9-track song to experiment with) |
| `open_session {path}` / `save_session {path?}` | `.scraft` files; save copies the audio into `Audio Files/` next to it |
| `import_audio {path, track?, at?}` | WAV AIFF FLAC MP3 OGG AAC/M4A ALAC CAF. New track (named after the file) unless `track`. Returns `track`, `clip`, `source` ids |
| `execute {command, params}` | Run one command; errors come back as text (see Pitfalls) |
| `batch {calls, keep_going?}` | Several commands in order, stops at the first error |
| `list_commands {filter?}` | Command ids, menu path, params doc, `enabled` + `disabled_reason` |
| `inspect_session {detail?: summary\|full}` | Verify work. `full` adds every insert's params |
| `bounce_mix {path, format?, bit_depth?, start?, end?, normalize?}` | Render to WAV/AIFF/FLAC; returns `seconds`, `peak_db`, `true_peak_db`, `lufs` |
| `parity` | Feature-parity report (rarely needed) |
| `screenshot`, `ui_inspect`, `ui_set`, `menu_invoke`, `click`, `drag`, `key` | APP_ONLY (with `--connect`) |

Resources: `soundcraft://session` (session JSON), `soundcraft://commands` (the catalog).
Handy queries: `execute track.inspect {track}`, `clip.inspect {clip}`, `engine.plugins` (plugin params).

## Plugins and Processing

Built-ins (`references/plugins.md` has every param, default and range): `eq_1band`, `eq_7band`, `compressor`,
`expander_gate`, `de_esser`, `maximizer`, `channel_strip`, `room_reverb`, `plate_reverb`, `mod_delay`,
`chorus`, `flanger`, `phaser`, `saturator`, `lofi`, `rectifier`, `pitch_shifter`, `time_shift`, `gain`,
`trim`, `invert`, `dc_offset_removal`, `signal_generator`, `dither`, instruments `subtractive_synth`, `drum_synth`.
There is **no noise-reduction plugin**: use `expander_gate` or `edit.strip_silence`, or ffmpeg `afftdn` before import.

- **Live insert:** `mix.insert {track, plugin, params}` → returns its `slot`. Change later with
  `mix.insert_param {track, slot, param, value}` / `mix.insert_params`; `mix.insert_bypass`, `mix.insert_remove`.
- **Choice params take the index** (`eq_1band type: 3` = High Pass). Toggles are `0/1` (`hpf_on: 1`).
- **AudioSuite (offline render into a new clip):** `audiosuite.process {process, params, clips: [id]}` with any
  plugin id, or `normalize {target_db}`, `gain {db}`, `reverse`, `invert`, `time_stretch {ratio}`,
  `pitch_shift {semitones}`, `varispeed {speed}`.

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
bounce_mix {path:"/abs/probe.wav", start:0, end:"0:08.400"}   → lufs −18.55, peak −3.5
execute mix.volume {tracks:["Host"], delta_db: 2.55}       # target − measured; re-bounce and nudge until ±0.5
bounce_mix {path:"/abs/episode.wav", start:0, end:"0:08.400", bit_depth:"16"}   → −16.0 LUFS, peak −1.5
```

Checked with ffmpeg `ebur128`: −16.0 LUFS, −1.5 dBFS, 8.4 s, 48 kHz stereo 16-bit. Without the master
maximizer the same chain measured −22.4 LUFS / −7.5 dBFS. A limiter makes gain changes non-linear, so
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
execute mix.volume {tracks:["kick"], db:-3} · {tracks:["bass"], db:-4} · {tracks:["pad"], db:-8}
execute mix.pan {tracks:["bass"], pan:-0.3}
execute mix.insert {track:"bass", plugin:"saturator", params:{drive:9}}
execute automation.set_point {track:"pad", param:"volume", at:{seconds:6}, value:-8}
execute automation.set_point {track:"pad", param:"volume", at:{seconds:8}, value:-60}   # fade-out ride
execute markers.add {name:"Drop", at:"bars_beats:3|1|000"}
execute track.new {kind:"master", format:"stereo"}        # without it this mix peaked +0.57 dBFS (clipped)
execute mix.insert {track:"Master 1", plugin:"maximizer", params:{threshold:-2, ceiling:-1}}
bounce_mix {path:"/abs/song.wav", start:0, end:{seconds:10}}   # 8 s of clips; the extra 2 s keep the reverb tail
                                                                # → −8.0 LUFS, peak −1.0
bounce_mix {path:"/abs/song.flac", format:"flac", bit_depth:"16", start:0, end:{seconds:10}}
execute file.bounce_stems {dir:"/abs/stems"}               → "Song - kick.wav", … (source tracks only)
```

### More building blocks (tested)

- **Split / move / crossfade:** `edit.separate {tracks, at}` splits (new clip id in `track.inspect`);
  `edit.move_clips {clips, by | to}` (`by` in samples or `{seconds}`); `edit.fades_create` over a range that
  spans the boundary of two butted clips gives a fade-out + fade-in pair (`shape: "equal power"`).
- **Remove silences:** `edit.select {tracks, start, end}` then `edit.strip_silence {threshold_db:-40, min_length_ms:200}`.
- **Clip gain:** `clip.gain {clips:[id], db:-6}` (or `delta_db`).
- **Offline effects:** `audiosuite.process {process:"time_stretch", params:{ratio:1.1}, clips:[3]}` → clip 10 % longer;
  `{process:"normalize", params:{target_db:-1}}`; `{process:"eq_1band", params:{type:3, freq:100}}`.
- **Synth parts / sound effects from MIDI:** `event.tempo {bpm:100}`; `track.new {kind:"instrument",
  instrument:"subtractive_synth", name:"Lead"}`; `midi.new_clip {track:"Lead", start:0, length:"bars_beats:3|1|000"}`
  → clip id (use the returned one); `midi.note_add {clip, pitch:60, start_ticks:0, length_ticks:960, velocity?}`.
  A `drum_synth` track played notes 36, 38 and 42 (kick, snare, hat). `file.export_midi {path}` writes a `.mid`.
  The synth is quiet by default (−29 LUFS for a 3-note line), so raise the fader or the synth's `level`.

## Formats

- **Import:** WAV/BWF/RF64, AIFF, FLAC, MP3, OGG Vorbis, AAC/M4A, ALAC, CAF, and the audio of MP4/MOV.
- **Bounce / convert output:** WAV, AIFF, FLAC only, 16 / 24 / 32f bit (`bit_depth` is a string: `"16"`).
  The format follows `format` or the `.flac`/`.aiff` extension. **No MP3/AAC/OGG output** — make those with
  ffmpeg from the WAV: `ffmpeg -i mix.wav -b:a 192k mix.mp3`.
- `normalize: true` on a bounce is a **peak** normalize to −0.1 dBFS, not loudness.

## CLI (no MCP needed)

```bash
soundcraft-cli info FILE                                 # audio: rate, channels, seconds; .scraft: session text report
soundcraft-cli convert in.wav out.flac [--bit-depth 16|24|32f] [--rate 48000] [--normalize]
soundcraft-cli run [--in S.scraft | --demo] --cmd 'file.import_audio={"path":"/abs/v.wav"}' \
    --cmd 'mix.insert={"track":"v","plugin":"compressor","params":{"threshold":-24}}' \
    --bounce out.flac [--start 0:00.000 --end 0:12.000] [--save S.scraft] [--inspect]
soundcraft-cli script cmds.txt [--in S] --bounce out.wav     # one `ID {json}` per line
soundcraft-cli commands [FILTER] · describe ID · plugins
```

`run`/`script` print one JSON result per command plus the bounce report. `--start/--end` take time
strings (`0:04.000`), not JSON (`{"seconds":4}` fails with `cannot parse position`).

## Pitfalls

- **A live edit selection limits the bounce.** After `edit.select` or `edit.strip_silence`, `bounce_mix` without
  `start`/`end` renders only the selection. Run `edit.select_none` and always pass **both** `start` and `end`
  — `end` alone is ignored, and the session end cuts off reverb/delay tails.
- **Clipping is reported, not prevented.** `peak_db: 0.57` came back while the 24-bit WAV was hard-clipped
  at 0 dBFS. Keep `peak_db` ≤ −1 (master `maximizer` with `ceiling: -1`) before delivering.
- **`.mp3` paths silently get WAV data** from both `bounce_mix` and `convert`. Bounce WAV, then use ffmpeg.
- **AudioSuite file-name collisions lose audio.** The rendered file is `<clip name>-<process>.wav`, so two
  clips with the same name (splits, strip-silence pieces, the same file imported twice) overwrite each other on
  `save_session`; after reopening, both clips play the last render. `clip.rename` each clip uniquely first.
- **AudioSuite drops clip gain** (renders without it and resets `gain_db` to 0) and **ignores unknown params**
  (normalize's is `target_db`, not `level_db`). Apply clip gain afterwards.
- **Names aren't unique.** Importing `kick.wav` twice makes two tracks named `kick`; `track.new {kind:"master",
  name:"Master"}` ignores the name (it's `Master 1`). Use the returned ids.
- **Mono tracks panned centre are −3 dB** per side in the stereo bounce (pan law).
- `edit.fades_create` needs a range covering a clip start, end or boundary, otherwise:
  `the selection must cover a clip start, end or the boundary between two clips`.
- `edit.duplicate` in Slip mode lays the copy right after the range and **overwrites** what was there.
- `tracks` must be an array: `{tracks:"tone"}` fails with `no tracks: pass track/tracks or select tracks`.
- Relative paths resolve against the server's working directory. Use absolute paths everywhere.
- Error texts are precise — read them: `unknown command`, `unknown plugin`, `` `compressor` has no parameter `thresh` ``,
  `no track named …`, `no such clip`, `make an edit selection first`.
- `soundcraft-cli --help` ends with a few stray lines of Rust source; that's cosmetic.

## Verification

- `inspect_session` / `track.inspect`: clip positions, fades, inserts (`detail:"full"` for params), sends, automation.
- Every `bounce_mix` reply: `seconds` equals the intended length; `peak_db` ≤ −1; `lufs` near the target.
- Independently: `ffprobe -show_entries stream=codec_name,sample_rate,channels:format=duration out.wav`,
  `ffmpeg -i out.wav -af ebur128=peak=true -f null -` (LUFS, true peak), and
  `ffmpeg -i out.wav -lavfi showwavespic=s=1200x300 wave.png`, then **look** at the PNG for cut words, clicks,
  missing fades or a flat-topped (clipped) waveform.
- After `save_session`, `soundcraft-cli info Session.scraft` lists tracks, clips and files.

## References

- `references/commands.md`: all 460 commands with params, grouped by area. Grep it rather than reading it whole.
- `references/plugins.md`: all 26 built-in plugins with param ids, defaults and ranges, plus the AudioSuite-only processes.
- Upstream docs: https://github.com/storytold/soundcraft/tree/main/docs (`mcp.md`, `control-protocol.md`).
