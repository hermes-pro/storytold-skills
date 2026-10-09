# SoundCraft command catalog

Generated from `list_commands` (SoundCraft 0.3.0, 460 commands). Run with `execute {command, params}`
or `batch {calls:[{command, params}]}`; `soundcraft-cli describe ID` shows one. `?` = optional, `a|b` = choices.
Positions: samples (int), `{"seconds": x}`, or `"0:12.500"` / `"bars_beats:5|1|000"`. Tracks by id or name; clips by id.
Omitted `tracks`/`start`/`end`/`clips` fall back to the current selection (an error such as `make an edit selection first` means: pass them).

## session — Session files

- `session.new` (File › New) [Cmd+N]: {name?: 'Untitled', sample_rate?: 48000, bit_depth?: 24, template?: blank|demo}
- `session.open` (File › Open Session) [Cmd+O]: {path}
- `session.close` (File › Close Session) [Cmd+Shift+W]: {}
- `session.save` (File › Save Session) [Cmd+S]: {path?}
- `session.save_as` (File › Save Session As) [Cmd+Shift+S]: {path}
- `session.save_copy` (File › Save Session Copy In): {path}
- `session.save_template` (File › Save As Template): {path}
- `session.revert` (File › Revert Session to Saved): {}
- `session.inspect` (Inspect Session): {detail?: summary|full}
- `session.format_time` (Format Time): {at: samples, format?: bars_beats|min_secs|timecode|feet_frames|samples}

## file — Import, bounce, export

- `file.import_audio` (File › Import › Audio) [Cmd+Shift+I]: {path | paths: [..], track?: target track, at?: position, new_tracks?: true}
- `file.import_midi` (File › Import › MIDI) [Cmd+Alt+I]: {path, at?}
- `file.import_video` (File › Import › Video) [Cmd+Ctrl+I]: {path, at?} — adds a Video track clip for the movie's picture (H.264, ProRes, Motion JPEG) and imports its audio onto a new track
- `file.bounce_mix` (File › Bounce Mix) [Cmd+Alt+B]: {path, format?: wav|aiff|flac, bit_depth?: 16|24|32f, start?, end?, source?: main|bus name, normalize?: false, dither?: true, fold_down?: stereo}
- `file.bounce_stems` (Bounce Stems): {dir, format?: wav|aiff|flac, bit_depth?: 16|24|32f, start?, end?, fold_down?: stereo}
- `file.export_midi` (File › Export › MIDI): {path, tracks?}
- `file.export_session_text` (File › Export › Session Info as Text): {path?}
- `file.export_clips` (Export Clips as Files): {dir, clips?, format?: wav}
- `file.export_selected_tracks_as_session` (File › Export › Selected Tracks as New Session): {path, tracks?}
- `file.export_sibelius` (File › Export › Sibelius): {path, tracks?} — MIDI tracks as MusicXML (.musicxml)
- `file.send_to_sibelius` (File › Send To... › Sibelius): {path?, tracks?} — writes MusicXML for a notation program (to the temp folder when no `path`)
- `file.print_score` (File › Print Score) [Cmd+P]: {path?, tracks?} — engraves the MIDI tracks as a printable SVG page
- `file.score_setup` (File › Score Setup): {title?, composer?, bars_per_system?: 1..16, show_track_names?: bool} — returns the current setup
- `file.export_clip_groups` (Export Clip Groups): {path, clips?} — writes a .scgrp clip group file with its audio
- `file.import_clip_groups` (File › Import › Clip Groups): {path, track?: first target track, at?}
- `file.get_info` (File › Get Info): {}
- `file.import_session_data` (File › Import › Session Data) [Alt+Shift+I]: {path, tracks?: [names]} — imports tracks (clips, playlists, mixer, automation, audio) from another session

## edit — Selection, editing, fades, clips on the timeline

- `edit.undo` (Edit › Undo) [Cmd+Z]: {}
- `edit.redo` (Edit › Redo) [Cmd+Shift+Z]: {}
- `edit.restore_last_selection` (Edit › Restore Last Selection) [Cmd+Alt+Z]: {}
- `edit.cut` (Edit › Cut) [Cmd+X]: {tracks?, start?, end?}
- `edit.copy` (Edit › Copy) [Cmd+C]: {tracks?, start?, end?}
- `edit.paste` (Edit › Paste) [Cmd+V]: {tracks?, at?}
- `edit.clear` (Edit › Clear) [Cmd+B]: {tracks?, start?, end?}
- `edit.cut_clip_gain` (Edit › Cut Special › Clip Gain) [Cmd+Ctrl+X]: {}
- `edit.clear_clip_gain` (Edit › Clear Special › Clip Gain) [Cmd+Ctrl+B]: {}
- `edit.cut_all_automation` (Edit › Cut Special › All Automation): {}
- `edit.clear_all_automation` (Edit › Clear Special › All Automation): {}
- `edit.clear_pan_automation` (Edit › Clear Special › Pan Automation): {}
- `edit.clear_plugin_automation` (Edit › Clear Special › Plugin Automation): {}
- `edit.paste_repeat_to_fill` (Edit › Paste Special › Repeat to Fill Selection) [Cmd+Alt+V]: {}
- `edit.select_all` (Edit › Select All) [Cmd+A]: {}
- `edit.select` (Set Edit Selection): {tracks?: [id|name], start?, end?, clips?: [id], exact?: bool (ignore edit groups)}
- `edit.select_none` (Deselect All): {}
- `edit.selection_to_timeline` (Edit › Selection › Change Timeline to Match Edit) [Alt+Shift+5]: {}
- `edit.timeline_to_selection` (Edit › Selection › Change Edit to Match Timeline) [Alt+Shift+6]: {}
- `edit.move_selection_left` (Edit › Selection › Move Edit Left) [Cmd+Alt+L]: {}
- `edit.move_selection_right` (Edit › Selection › Move Edit Right) [Cmd+Alt+']: {}
- `edit.halve_selection` (Edit › Selection › Halve Edit): {}
- `edit.double_selection` (Edit › Selection › Double Edit): {}
- `edit.extend_selection_up` (Edit › Selection › Extend Edit Up): {}
- `edit.extend_selection_down` (Edit › Selection › Extend Edit Down): {}
- `edit.remove_selection_top` (Edit › Selection › Remove Edit from Top): {}
- `edit.remove_selection_bottom` (Edit › Selection › Remove Edit from Bottom): {}
- `edit.duplicate` (Edit › Duplicate) [Cmd+D]: {tracks?, start?, end?}
- `edit.repeat` (Edit › Repeat) [Alt+R]: {count: n}
- `edit.shift` (Edit › Shift) [Alt+H]: {by: samples|{seconds}, later?: bool}
- `edit.insert_silence` (Edit › Insert Silence) [Cmd+Shift+E]: {tracks?, start?, end?}
- `edit.separate` (Edit › Separate › At Selection) [Cmd+E]: {tracks?, at?|start/end}
- `edit.separate_on_grid` (Edit › Separate › On Grid): {tracks?, start?, end?}
- `edit.separate_at_transients` (Edit › Separate › At Transients): {sensitivity?: 0..1}
- `edit.heal` (Edit › Heal Separation) [Cmd+H]: {tracks?, start?, end?}
- `edit.trim_to_selection` (Edit › Trim › To Selection) [Cmd+T]: {tracks?, start?, end?}
- `edit.trim_start_to_insertion` (Edit › Trim › Start to Insertion) [Alt+Shift+7]: {tracks?, at?}
- `edit.trim_end_to_insertion` (Edit › Trim › End to Insertion) [Alt+Shift+8]: {tracks?, at?}
- `edit.trim_to_file_boundaries` (Edit › Trim › To File Boundaries): {clips?}
- `edit.trim_to_fill_selection` (Edit › Trim › To Fill Selection): {}
- `edit.mute_clips` (Edit › Mute) [Cmd+M]: {clips?}
- `edit.copy_to_new_playlist` (Edit › Copy Selection to... › New Playlist): {}
- `edit.strip_silence` (Edit › Strip Silence) [Cmd+U]: {threshold_db?: -48, min_length_ms?: 50, pad_before_ms?: 5, pad_after_ms?: 20}
- `edit.fades_create` (Edit › Fades › Create) [Cmd+F]: {shape?: linear|equal power|s-curve|exponential|logarithmic, tracks?, start?, end?}
- `edit.fades_delete` (Edit › Fades › Delete): {tracks?, start?, end?}
- `edit.fade_to_start` (Edit › Fades › Fade to Start) [Cmd+Ctrl+D]: {}
- `edit.fade_to_end` (Edit › Fades › Fade to End) [Cmd+Ctrl+G]: {}
- `edit.nudge` (Nudge) [Plus/Minus]: {direction: 1|-1, count?: n}
- `edit.mode` (Edit Mode) [F1-F4]: {mode: shuffle|slip|spot|grid|relative_grid}
- `edit.tool` (Edit Tool) [F5-F10]: {tool: zoom|trim|selector|grabber|scrubber|pencil|smart}
- `edit.move_clips` (Move Clips): {clips?: [id], by?: samples, to?: position (first clip start), track?: target}
- `edit.consolidate` (Edit › Consolidate) [Alt+Shift+3]: {tracks?, start?, end?}
- `edit.cut_pan_automation` (Edit › Cut Special › Pan Automation): {tracks?, start?, end?} — cuts pan automation only to the clipboard
- `edit.cut_plugin_automation` (Edit › Cut Special › Plugin Automation): {tracks?, start?, end?} — cuts plug-in automation only
- `edit.copy_all_automation` (Edit › Copy Special › All Automation): {tracks?, start?, end?} — copies automation only (no clips)
- `edit.copy_pan_automation` (Edit › Copy Special › Pan Automation): {tracks?, start?, end?}
- `edit.copy_plugin_automation` (Edit › Copy Special › Plugin Automation): {tracks?, start?, end?}
- `edit.copy_clip_gain` (Edit › Copy Special › Clip Gain): {tracks?, start?, end?} — copies the clip gain curve under the selection
- `edit.paste_clip_gain` (Paste Clip Gain): {tracks?, at?} — pastes copied clip gain onto the clips under the paste range
- `edit.copy_clip_effects` (Edit › Copy Special › Clip Effects): {clips?} — copies the first clip's clip-effect settings
- `edit.cut_clip_effects` (Edit › Cut Special › Clip Effects): {clips?} — copies then removes clip-effect settings
- `edit.clear_clip_effects` (Edit › Clear Special › Clip Effects): {clips?} — removes clip-effect settings (and bypass)
- `edit.paste_clip_effects` (Paste Clip Effects): {clips?}
- `edit.paste_merge_midi` (Edit › Paste Special › Merge MIDI): {tracks?, at?} — merges copied MIDI notes into existing MIDI clips instead of replacing them
- `edit.paste_merge_markers` (Edit › Paste Special › Merge Markers): {at?} — adds the copied markers at the insertion point, skipping any that already exist there
- `edit.paste_to_current_automation` (Edit › Paste Special › To Current Automation Type): {tracks?, at?, param?} — pastes copied automation into the shown lane (track view) or `param`, rescaled to its range
- `edit.play_timeline` (Edit › Selection › Play Timeline): {} — plays the timeline selection
- `edit.duplicate_extend` (Edit › Selection › Duplicate and Extend Edit): {tracks?, start?, end?} — duplicates the selection and extends the selection over the copy
- `edit.extend_up_to_members` (Edit › Selection › Extend Edit Up to Members): {} — adds the parent folder of each selected member and its members
- `edit.extend_down_to_members` (Edit › Selection › Extend Edit Down to Members): {} — adds the members of selected folder tracks (recursively)
- `edit.marker_lane_move_up` (Edit › Selection › Move Edit Selection To Marker Lane Above): {} — the selection's marker ruler lane (1..5) moves up
- `edit.marker_lane_move_down` (Edit › Selection › Move Edit Selection To Marker Lane Below): {}
- `edit.marker_lane_extend_up` (Edit › Selection › Extend Edit Selection To Marker Lane Above): {} — adds the marker ruler lane above to the selection
- `edit.marker_lane_extend_down` (Edit › Selection › Extend Edit Selection To Marker Lane Below): {}
- `edit.space_clips` (Edit › Space Clips…): {clips?, gap?: samples|{seconds} (default 0), mode?: end_to_start|start_to_start}
- `edit.snap_next` (Edit › Snap to › Next): {clips?} — moves each clip so its end meets the start of the next clip
- `edit.snap_previous` (Edit › Snap to › Previous): {clips?} — moves each clip so its start meets the end of the previous clip
- `edit.copy_to_target_playlist` (Edit › Copy Selection to... › Target Playlist): {tracks?, start?, end?} — copies the selection into each track's target playlist
- `edit.copy_to_duplicate_playlist` (Edit › Copy Selection to... › Duplicate of Main Playlist): {tracks?, start?, end?}
- `edit.move_to_target_playlist` (Edit › Move Selection to... › Target Playlist): {tracks?, start?, end?} — copies to the target playlist and clears it from the main
- `edit.move_to_new_playlist` (Edit › Move Selection to... › New Playlist): {tracks?, start?, end?}
- `edit.move_to_duplicate_playlist` (Edit › Move Selection to... › Duplicate of Main Playlist): {tracks?, start?, end?}
- `edit.tce_to_timeline` (Edit › TCE Edit to Timeline Selection): {clip?, start?, end?} — time-stretches the clip to fill the timeline selection (pitch preserved)
- `edit.automation_coalesce_volume_to_clip_gain` (Edit › Automation › Coalesce Volume Automation to Clip Gain): {tracks?} — folds the whole volume curve into clip gain; the fader goes to 0 dB
- `edit.automation_coalesce_clip_gain_to_volume` (Edit › Automation › Coalesce Clip Gain to Volume Automation): {tracks?} — folds all clip gain into volume automation
- `edit.automation_trim_to_all` (Edit › Automation › Trim to All Enabled): {tracks?, start?, end?} — offsets every enabled lane in the selection so it starts at the current control value
- `edit.automation_glide_to_all` (Edit › Automation › Glide to All Enabled): {tracks?, start?, end?} — ramps every enabled lane from its value at the start to the current value at the end
- `edit.automation_glide_pan` (Edit › Automation › Glide Pan Only): {tracks?, start?, end?}
- `edit.copy_audio_as_midi` (Edit › Copy Special › Audio as MIDI): {track?, start?, end?} — monophonic pitch tracking of the selected audio

## clip — Clip properties (gain, name, loop, lock)

- `clip.edit_lock` (Clip › Edit Lock/Unlock) [Cmd+L]: {clips?}
- `clip.time_lock` (Clip › Time Lock/Unlock) [Ctrl+Alt+L]: {clips?}
- `clip.send_to_back` (Clip › Send to Back) [Alt+Shift+B]: {clips?}
- `clip.bring_to_front` (Clip › Bring to Front) [Alt+Shift+F]: {clips?}
- `clip.rating` (Clip › Rating › Rating) [Cmd+Alt+0-5]: {clips?, rating: 0..5}
- `clip.group` (Clip › Group) [Cmd+Alt+G]: {clips?}
- `clip.ungroup` (Clip › Ungroup) [Cmd+Alt+U]: {clips?}
- `clip.ungroup_all` (Clip › Ungroup All): {}
- `clip.loop` (Clip › Loop) [Cmd+Alt+L]: {clips?, count?: n, length?: samples}
- `clip.rename` (Clip › Rename) [Cmd+Alt+Shift+R]: {clip?, name}
- `clip.gain` (Clip Gain): {clips?, db | delta_db}
- `clip.gain_render` (Clip › Clip Gain › Render): {clips?}
- `clip.gain_bypass` (Clip › Clip Gain › Bypass): {clips?}
- `clip.identify_sync_point` (Clip › Identify Sync Point) [Cmd+,]: {clip?, at?}
- `clip.quantize_to_grid` (Clip › Quantize to Grid) [Cmd+0]: {clips?}
- `clip.color` (Clip Color): {clips?, color: [r,g,b] | null}
- `clip.elastic_properties` (Clip › Elastic Properties) [Alt+5]: {clips?, ratio?: 1.0} — on Elastic Audio tracks (polyphonic/rhythmic/monophonic/x-form) the stretch is rendered pitch-preserving; elsewhere it is varispeed
- `clip.remove_warp` (Clip › Remove Warp): {clips?}
- `clip.place_source` (Place Audio File): {source: id, track?: id|name (default: a new track), at?: position}
- `clip.capture` (Clip › Capture) [Cmd+R]: {name?}
- `clip.inspect` (Inspect Clip): {clip}
- `clip.regroup` (Clip › Regroup) [Cmd+Alt+R]: {clips?} — puts the clips back into one clip group (reusing their most common group)
- `clip.unloop` (Clip › Unloop): {clips?, mode?: remove|flatten} — remove = keep only the original clip; flatten = keep the copies as ordinary clips
- `clip.effects_set` (Set Clip Effects): {clips?, params: {name: number}} — stores clip-effect settings on the clips
- `clip.effects_bypass` (Clip › Clip Effects › Bypass): {clips?, value?: bool} (toggles when omitted)
- `clip.effects_render` (Clip › Clip Effects › Render): {clips?} — renders clip gain and fades into new audio and clears the clip effects
- `clip.conform_to_tempo` (Clip › Conform to Tempo): {clips?, source_bpm?} — stretches audio clips so their length in bars follows the session tempo; the first conform records the clip's tempo
- `clip.remove_pitch_shift` (Clip › Remove Pitch Shift): {clips?} — re-renders vari-speed (stretched) clips with pitch preserved

## track — Tracks, routing, playlists, freeze/bounce

- `track.new` (Track › New) [Cmd+Shift+N]: {count?: 1, format?: mono|stereo|5.1…, kind?: audio|aux|master|midi|instrument|vca|folder, name?, timebase?: samples|ticks, instrument?: plugin id}
- `track.group` (Track › Group) [Cmd+G]: {name?, tracks?, edit?: true, mix?: true}
- `track.ungroup` (Delete Group): {group: id|name}
- `track.group_toggle` (Toggle Group Active): {group: id|name}
- `track.duplicate` (Track › Duplicate) [Alt+Shift+D]: {tracks?, playlists?: true, automation?: true, inserts?: true, sends?: true}
- `track.split_into_mono` (Track › Split into Mono): {tracks?}
- `track.make_inactive` (Track › Make Inactive): {tracks?, inactive?: bool}
- `track.move_to_new_folder` (Track › Move to New Folder) [Cmd+Alt+Shift+N]: {tracks?, name?}
- `track.change_width` (Track › Change Track Width › Change Track Width): {tracks?, format: mono|stereo|…}
- `track.delete` (Track › Delete): {tracks?}
- `track.rename` (Rename Track): {track, name}
- `track.comments` (Track Comments): {track, comments}
- `track.color` (Track Color): {tracks?, color: [r,g,b] | palette index}
- `track.height` (Track Height): {tracks?, height: micro|mini|small|medium|large|jumbo|extreme}
- `track.view` (Track View): {tracks?, view: waveform|blocks|notes|volume|pan|mute|<automation id>}
- `track.hide` (Hide Track): {tracks?, hidden?: bool}
- `track.pin` (Pin Track): {tracks?}
- `track.move` (Move Track): {track, to: index}
- `track.freeze` (Track › Freeze): {tracks?}
- `track.commit` (Track › Commit) [Alt+Shift+C]: {tracks?}
- `track.bounce` (Track › Bounce) [Cmd+Alt+Shift+B]: {tracks?}
- `track.bypass_inserts` (Track › Bypass Inserts › All): {tracks?, bypass?: bool}
- `track.mute_sends` (Track › Mute Sends › All): {tracks?, mute?: bool}
- `track.set_record_to_input_only` (Track › Set Record Tracks to Input Only) [Alt+K]: {}
- `track.scroll_to` (Track › Scroll to Track) [Cmd+Alt+F]: {track}
- `track.clear_clip_indicators` (Track › Clear All Clip Indicators) [Alt+C]: {}
- `track.clear_trim_automation` (Track › Clear Trim Automation): {tracks?}
- `track.create_click` (Track › Create Click Track): {}
- `track.playlist_new` (New Playlist): {track?, name?}
- `track.playlist_duplicate` (Duplicate Playlist): {track?, name?}
- `track.playlist_select` (Select Playlist): {track?, index | name}
- `track.playlist_delete_unused` (Delete Unused Playlists): {track?}
- `track.folder_toggle` (Open/Close Folder): {track, open?: bool}
- `track.vca` (Assign to VCA): {tracks?, vca: VCA track id|name | null}
- `track.playlist_promote` (Promote to Main Playlist): {track, playlist: index, start?, end?} (copy that range from an alternate playlist into the active one)
- `track.input` (Track Input): {tracks?, input: none|bus name|hardware name}
- `track.output` (Track Output): {tracks?, output: main|none|bus name}
- `track.timebase` (Track Timebase): {tracks?, ticks: bool}
- `track.elastic` (Elastic Audio): {tracks?, algorithm?: polyphonic|rhythmic|monophonic|varispeed|x-form|none}
- `track.inspect` (Inspect Track): {track}
- `track.object` (Object / Bed): {tracks?, object?: bool} — routes the tracks as immersive objects (true) or to the bed; toggles when `object` is omitted
- `track.convert_aux_to_folder` (Track › Convert Aux to Routing Folder): {tracks?} — aux inputs become routing folders; tracks feeding their input bus become members
- `track.extract_midi` (Track › Extract MIDI to New Track): {tracks?} — copies the MIDI clips of each MIDI/instrument track to a new MIDI track
- `track.save_preset` (Track › Save Track Preset): {path, track?} — writes the track's type, width, mixer, inserts, sends and instrument as JSON
- `track.load_preset` (Load Track Preset): {path, tracks?} — applies a saved track preset's mixer, inserts, sends and instrument
- `track.bypass_inserts_ae` (Track › Bypass Inserts › Inserts A-E): {tracks?, bypass?: bool}
- `track.bypass_inserts_fj` (Track › Bypass Inserts › Inserts F-J): {tracks?, bypass?: bool}
- `track.bypass_eq` (Track › Bypass Inserts › EQ): {tracks?, bypass?: bool} — EQ plug-ins only
- `track.bypass_dynamics` (Track › Bypass Inserts › Dynamics): {tracks?, bypass?: bool}
- `track.bypass_reverb` (Track › Bypass Inserts › Reverb): {tracks?, bypass?: bool}
- `track.bypass_delay` (Track › Bypass Inserts › Delay): {tracks?, bypass?: bool}
- `track.bypass_modulation` (Track › Bypass Inserts › Modulation): {tracks?, bypass?: bool}
- `track.mute_sends_ae` (Track › Mute Sends › Sends A-E): {tracks?, mute?: bool} (toggles when omitted)
- `track.mute_sends_fj` (Track › Mute Sends › Sends F-J): {tracks?, mute?: bool} (toggles when omitted)
- `track.write_midi_rtp` (Track › Write MIDI Real-Time Properties): {tracks?} — writes the track's real-time properties (velocity, transpose, duration, delay) into its notes and resets them
- `track.trim_automation_write` (Write Trim Automation): {tracks?, start?, end?, db} — writes a relative volume trim (dB) over a range
- `track.coalesce_trim` (Track › Coalesce Trim Automation): {tracks?} — adds trim automation into volume automation and removes the trim
- `track.coalesce_vca` (Track › Coalesce VCA Controller Automation): {tracks?} — for selected VCA masters: folds VCA level/automation into every member's volume automation, then resets the VCA
- `track.designate_target_playlist` (Track › Designate as Target Playlist): {tracks?, index?} — the active playlist (or `index`) becomes the target for Copy/Move Selection to
- `track.show_target_playlist` (Track › Show Target Playlist): {tracks?} — makes the target playlist the main playlist
- `track.toggle_recent_playlist` (Track › Toggle Recent Playlist) [Ctrl+Alt+Shift+Left]: {tracks?} — swaps to the previously shown playlist

## mix — Mixer: volume, pan, mute/solo, inserts, sends, busses

- `mix.volume` (Set Volume): {tracks?, db: -144..12 | delta_db}
- `mix.pan` (Set Pan): {tracks?, pan: -1..1, index?: 0|1}
- `mix.mute` (Mute) [Shift+M]: {tracks?, value?: bool}
- `mix.solo` (Solo) [Shift+S]: {tracks?, value?: bool, exclusive?: bool}
- `mix.solo_safe` (Solo Safe): {tracks?, value?: bool}
- `mix.clear_solos` (Clear All Solos): {}
- `mix.clear_mutes` (Clear All Mutes): {}
- `mix.record_arm` (Record Enable) [Shift+R]: {tracks?, value?: bool}
- `mix.input_monitor` (Input Monitoring) [Shift+I]: {tracks?, value?: bool}
- `mix.phase_invert` (Phase Invert): {tracks?, value?: bool}
- `mix.trim` (Input Trim): {tracks?, db}
- `mix.automation_mode` (Automation Mode): {tracks?, mode: off|read|touch|latch|touch/latch|write|trim}
- `mix.insert` (Insert Plugin): {track?, slot?: 0..9 | a..j, plugin: id, params?: {id: value}}
- `mix.insert_remove` (Remove Insert): {track?, slot}
- `mix.insert_bypass` (Bypass Insert): {track?, slot, value?: bool}
- `mix.insert_param` (Set Plugin Parameter): {track?, slot, param, value}
- `mix.insert_params` (Set Plugin Parameters): {track?, slot, params: {id: value}, preset?: name}
- `mix.insert_move` (Move Insert): {track?, from, to}
- `mix.send` (Assign Send): {track?, slot?: 0..9|a..j, bus: name, level_db?: 0, pre_fader?: false}
- `mix.send_remove` (Remove Send): {track?, slot}
- `mix.send_level` (Send Level): {track?, slot, db?, pan?, mute?, pre_fader?}
- `mix.new_bus` (New Bus): {name, format?: stereo}
- `mix.surround_pan` (Set Surround Pan): {tracks?, x?: -1..1 (left..right), y?: -1..1 (back..front), z?: 0..1 (height), divergence?: 0..1, center?: 0..100, lfe_db?: -144..12, clear?: bool}
- `mix.send_surround_pan` (Set Send Surround Pan): {track?, slot: 0..9|a..j, x?, y?, z?, divergence?, center?, lfe_db?, clear?: bool}
- `mix.insert_state` (Store Plugin State): {track, slot: 0..9 | "a".."j" | "instrument", state: base64 | null} → {bytes}. Not undoable and not journaled (states can be large).

## automation — Automation breakpoints and passes

- `automation.set_point` (Add Automation Breakpoint): {track?, param: volume|pan|mute|send_a_level|plugin:a:<id>, at, value}
- `automation.write_range` (Write Automation): {track?, param, start?, end?, value}
- `automation.clear` (Clear Automation): {track?, param?, start?, end?}
- `automation.thin` (Edit › Automation › Thin) [Cmd+Alt+T]: {tracks?, tolerance?: 0.1}
- `automation.thin_all` (Edit › Automation › Thin All): {tolerance?: 0.1}
- `automation.write_to_current` (Edit › Automation › Write to Current) [Cmd+/]: {tracks?}
- `automation.write_to_all` (Edit › Automation › Write to All Enabled) [Cmd+Alt+/]: {tracks?}
- `automation.volume_to_clip_gain` (Edit › Automation › Convert Volume Automation to Clip Gain): {tracks?}
- `automation.clip_gain_to_volume` (Edit › Automation › Convert Clip Gain to Volume Automation): {tracks?}
- `automation.copy_to_send` (Edit › Automation › Copy to Send) [Cmd+Alt+H]: {tracks?, send: slot}

## audiosuite — Offline (destructive-copy) processing

- `audiosuite.process` (AudioSuite Process): {process: <plugin id> | normalize | reverse | invert | gain | duplicate | time_stretch | pitch_shift | varispeed | signal_generator, params?: {..}, clips?}

## markers — Memory locations

- `markers.add` (New Memory Location) [Enter]: {name?, at?, start?, end?, kind?: marker|selection|none, ruler?: 1..5}
- `markers.delete` (Delete Memory Location): {number | id}
- `markers.edit` (Edit Memory Location): {number | id, name?, comments?, at?, color?}
- `markers.recall` (Recall Memory Location) [Period + n + Period]: {number}
- `markers.next` (Go to Next Marker): {}
- `markers.previous` (Go to Previous Marker): {}

## event — Tempo, meter, time operations, MIDI events

- `event.tempo` (Tempo Change): {bpm, at?: position (default session start)}
- `event.tempo_remove` (Remove Tempo Change): {at}
- `event.meter` (Event › Time Operations › Change Meter): {numerator, denominator, at?: position}
- `event.tempo_scale` (Event › Tempo Operations › Scale): {factor}
- `event.tempo_constant` (Event › Tempo Operations › Constant): {bpm, start?, end?}
- `event.insert_time` (Event › Time Operations › Insert Time): {start?, length | end}
- `event.cut_time` (Event › Time Operations › Cut Time): {start?, end?}
- `event.quantize` (Event › MIDI Operations › Quantize) [Alt+0]: {grid?: 1/16 | ticks, strength?: 100, swing?: 0, clips?}
- `event.transpose` (Event › MIDI Operations › Transpose) [Alt+T]: {semitones, clips?}
- `event.change_velocity` (Event › MIDI Operations › Change Velocity): {set?|add?|scale?|min?,max?, clips?}
- `event.change_duration` (Event › MIDI Operations › Change Duration) [Alt+P]: {set?|add?|scale?|legato?: gap, clips?}
- `event.remove_duplicate_notes` (Event › Remove Duplicate Notes): {clips?}
- `event.add_key_change` (Event › Add Key Change): {key: 'C major', at?}
- `event.renumber_bars` (Event › Renumber Bars): {}
- `event.all_notes_off` (Event › All MIDI Notes Off) [Cmd+Shift+.]: {}
- `event.midi_note` (Add MIDI Note): {clip, pitch, start_ticks, length_ticks, velocity?: 100}
- `event.time_ops_window` (Event › Time Operations › Time Operations Window): {} — tempo/meter map, song start and selection for the Time Operations window
- `event.tempo_ops_window` (Event › Tempo Operations › Tempo Operations Window): {}
- `event.midi_ops_window` (Event › MIDI Operations › MIDI Operations Window): {} — input quantize and stored performances
- `event.move_song_start` (Event › Time Operations › Move Song Start): {to: position} — moves the song start; tick-based clips and later tempo/meter events move with it
- `event.tempo_linear` (Event › Tempo Operations › Linear): {start?, end?, start_bpm?, end_bpm, resolution?: '1/8'|ticks}
- `event.tempo_parabolic` (Event › Tempo Operations › Parabolic): {start?, end?, start_bpm?, end_bpm, curvature?: -1..1 (0.5), resolution?}
- `event.tempo_s_curve` (Event › Tempo Operations › S-Curve): {start?, end?, start_bpm?, end_bpm, resolution?}
- `event.tempo_stretch` (Event › Tempo Operations › Stretch): {start?, end?, factor? | length?: new length} — scales the tempo inside the selection so it lasts `factor` times as long
- `event.select_split_notes` (Event › MIDI Operations › Select/Split Notes): {clips?, pitch_from?: 0, pitch_to?: 127, action?: select|split} — split moves the matching notes to a new MIDI track
- `event.input_quantize` (Event › MIDI Operations › Input Quantize): {enabled?: bool, grid?: '1/16'|ticks, strength?: 0..100, swing?: 0..100}
- `event.step_input` (Event › MIDI Operations › Step Input): {track?, pitch?: 60 | pitches?: [..], duration?: '1/8'|ticks, velocity?: 100, rest?: bool, advance?: true}
- `event.restore_performance` (Event › MIDI Operations › Restore Performance): {clips?} — returns MIDI clips to their stored original performance
- `event.flatten_performance` (Event › MIDI Operations › Flatten Performance): {clips?} — makes the current notes the performance that Restore returns to
- `event.midi_track_offsets` (Event › MIDI Track Offsets): {track?, offset?: samples|{seconds}} — sets (or lists) per-track MIDI playback offsets
- `event.midi_rtp` (Event › MIDI Real-Time Properties): {tracks?, velocity?: ±127, transpose?: ±127, duration?: % (100), delay?: ticks, clear?: bool}
- `event.extract_chords` (Event › Extract Chords from Selection): {tracks?, start?, end?} — names the chord in each bar and adds it as a marker on Markers 2
- `event.beat_detective` (Event › Beat Detective): {tracks?, start?, end?, sensitivity?: 0.5, separate?: false, set_tempo?: false}
- `event.identify_beat` (Event › Identify Beat) [Cmd+I]: {start?, end?, bars?: 1, beats?: 0} — sets the tempo so the selection lasts that many bars
- `event.retrospective_record` (Event › Retrospective Record): {track?, notes?: [{pitch, start?: position | start_ticks?, length_ticks?: 240, velocity?: 100}]} — turns captured MIDI into a clip (input quantize applies)

## midi — MIDI clips and notes

- `midi.notes` (List MIDI Notes): {clip}
- `midi.new_clip` (New MIDI Clip): {track, start?, end?|length?} (default: the edit selection, or 1 bar)
- `midi.note_add` (Add Note): {clip, pitch, start_ticks, length_ticks?: 480, velocity?: 100, channel?: 0}
- `midi.note_edit` (Edit Note): {clip, index, pitch?, start_ticks?, length_ticks?, velocity?}
- `midi.note_delete` (Delete Notes): {clip, indices: [n]}
- `midi.notes_move` (Move Notes): {clip, indices: [n], ticks?: 0, semitones?: 0}

## transport — Transport (play/stop/locate)

- `transport.play` (Play) [Space]: {from?: position}
- `transport.stop` (Stop) [Space]: {}
- `transport.toggle` (Play/Stop) [Space]: {}
- `transport.record` (Record) [Cmd+Space]: {}
- `transport.pause` (Pause): {}
- `transport.half_speed` (Half-Speed Playback) [Shift+Space]: {}
- `transport.play_selection` (Edit › Selection › Play Edit) [Alt+[]: {}
- `transport.rtz` (Return to Zero) [Home]: {}
- `transport.go_to_end` (Go to End) [End]: {}
- `transport.rewind` (Rewind): {seconds?: 1}
- `transport.fast_forward` (Fast Forward): {seconds?: 1}
- `transport.locate` (Locate): {at: position}
- `transport.status` (Transport Status): {}

## engine — Engine queries

- `engine.commands` (List Commands): {filter?}
- `engine.history` (Window › Undo History): {}
- `engine.plugins` (List Plugins): {}
- `engine.parity` (Parity Report): {}
- `engine.clap_plugins` (List CLAP Plugins): {rescan?: bool} → [{id: "clap:…", plugin_id, name, vendor, version, description, features, category, is_instrument, path}]
- `engine.vst3_plugins` (List VST3 Plugins): {rescan?: bool} → [{id: "vst3:<class id hex>", class_id, name, vendor, version, sdk_version, sub_categories, category, is_instrument, path}]

## setup — Setup, I/O, hardware, MIDI studio

- `setup.session` (Setup › Session) [Cmd+2]: {frame_rate?: '29.97 Drop'…, bit_depth?: 16|24|32f, timecode_start?: position, name?}
- `setup.preferences` (Setup › Preferences): {}
- `setup.reset_edit_state` (Reset Edit Settings): {}
- `setup.hardware` (Setup › Hardware): {device?, buffer_size?: 16..8192} — audio interface settings (sample rate is the session's)
- `setup.playback_engine` (Setup › Playback Engine): {device?, buffer_size?: 16..8192, delay_compensation?: bool}
- `setup.disk_allocation` (Setup › Disk Allocation): {path?, track?} — the record folder for the session, or for one track
- `setup.peripherals` (Setup › Peripherals): {settings?: {name: number|bool|string}} — control surface / sync device settings
- `setup.io` (Setup › I/O): {action?: list|create_bus|rename_bus|delete_bus|create_output|rename_output|delete_output, name?, new_name?, format?: stereo, first_channel?: 0}
- `setup.current_timecode` (Setup › Current Timecode Position): {timecode: 'HH:MM:SS:FF'} — sets the session start so the insertion point reads this timecode
- `setup.current_feet_frames` (Setup › Current Feet+Frames Position): {feet_frames: 'F+FF'} — the feet+frames reading at the insertion point
- `setup.external_timecode_offset` (Setup › External Timecode Offset): {frames?: ±, samples?: ±} — offset applied to incoming timecode
- `setup.video_sync_offset` (Setup › Video Sync Offset): {frames?: ±, samples?: ±} — offset between audio and video playback
- `setup.click_countoff` (Setup › Click/Countoff): {volume_db?: -60..12, accent_note?: 0..127, normal_note?: 0..127, accent_velocity?, normal_velocity?, countoff?: bool, countoff_bars?: 1..16, only_during_record?: bool}
- `setup.keyboard_shortcuts` (Setup › Keyboard Shortcuts): {filter?} — every command shortcut
- `setup.midi_studio` (Setup › MIDI › MIDI Studio): {devices?: [names]} — the MIDI devices in the studio
- `setup.midi_beat_clock` (Setup › MIDI › MIDI Beat Clock): {enabled?: bool, offset?: samples, destination?: name}
- `setup.midi_input_filter` (Setup › MIDI › MIDI Input Filter): {filter?: [notes|pitch_bend|mono_aftertouch|poly_aftertouch|program|cc|sysex|realtime], allow?: [...]} — filtered kinds are not recorded
- `setup.midi_input_devices` (Setup › MIDI › MIDI Input Devices): {enable?: [names], disable?: [names]}
- `setup.transcription_settings` (Setup › Transcription Settings): {enabled?: bool, language?: 'en'}
- `setup.main_format` (Main Output Format): {format: stereo|LCR|Quad|5.0|5.1|6.1|7.0|7.1|7.1.2|5.1.4|7.1.4|9.1.6|1st Order Ambisonics…}

## options — Options toggles

- `options.loop_record` (Options › Loop Record) [Alt+L]: {value?: bool}
- `options.quickpunch` (Options › QuickPunch) [Cmd+Shift+P]: {value?: bool}
- `options.pre_post_roll` (Options › Pre/Post-Roll) [Cmd+K]: {value?: bool}
- `options.loop_playback` (Options › Loop Playback) [Cmd+Shift+L]: {value?: bool}
- `options.link_timeline_edit` (Options › Link Timeline and Edit Selection) [Shift+/]: {value?: bool}
- `options.link_track_edit` (Options › Link Track and Edit Selection): {value?: bool}
- `options.insertion_follows_playback` (Options › Insertion Follows Playback): {value?: bool}
- `options.tab_to_transient` (Options › Tab to Transient) [Cmd+Alt+Tab]: {value?: bool}
- `options.mirrored_midi` (Options › Mirrored MIDI Editing): {value?: bool}
- `options.automation_follows_edit` (Options › Automation Follows Edit): {value?: bool}
- `options.markers_follow_edit` (Options › Markers Follow Edit): {value?: bool}
- `options.layered_editing` (Options › Layered Editing): {value?: bool}
- `options.click` (Options › Click): {value?: bool}
- `options.countoff` (Count Off): {value?: bool}
- `options.midi_merge` (MIDI Merge): {value?: bool}
- `options.pre_fader_metering` (Options › Pre-Fader Metering): {value?: bool}
- `options.delay_compensation` (Options › Delay Compensation): {value?: bool}
- `options.destructive_record` (Options › Destructive Record): {value?: bool}
- `options.trackpunch` (Options › TrackPunch) [Cmd+Shift+T]: {value?: bool}
- `options.scrolling` (Options › Edit Window Scrolling › Edit Window Scrolling): {mode: none|after_playback|page|continuous|center}
- `options.solo_mode` (Options › Solo Mode › Solo Mode): {mode: sip|afl|pfl, latch?: bool, xor?: bool}
- `options.keyboard_focus` (Keyboard Focus): {focus?: commands|clips|groups|none} — toggles Commands Keyboard Focus when omitted
- `options.pre_roll` (Pre-Roll Amount): {length: samples|{seconds}}
- `options.post_roll` (Post-Roll Amount): {length}
- `options.destructive_punch` (Options › DestructivePunch): {value?: bool} (toggles when omitted)
- `options.transport_online` (Options › Transport Online): {value?: bool} (toggles when omitted)
- `options.dynamic_transport` (Options › Dynamic Transport): {value?: bool} (toggles when omitted)
- `options.marker_target_follows_selection` (Options › Marker Target Follows First Selected Track): {value?: bool} (toggles when omitted)
- `options.midi_thru` (Options › MIDI Thru): {value?: bool} (toggles when omitted)
- `options.auto_spot_clips` (Options › Auto-Spot Clips): {value?: bool} (toggles when omitted)
- `options.keyboard_lock` (Options › Edit/Tool Mode Keyboard Lock): {value?: bool} (toggles when omitted)
- `options.calibration_mode` (Options › Calibration Mode): {value?: bool} (toggles when omitted)
- `options.midi_live_mode` (Options › MIDI Live Mode): {value?: bool} (toggles when omitted)
- `options.low_latency_monitoring` (Options › Low Latency Monitoring): {value?: bool} (toggles when omitted)
- `options.prepare_dpe_tracks` (Options › Prepare DPE Tracks): {tracks?} — consolidates each record-armed (or given) audio track into one continuous clip for destructive punch

## view — View and window toggles (mostly UI)

- `view.zoom_in` (Zoom In) [Cmd+]]: {}
- `view.zoom_out` (Zoom Out) [Cmd+[]: {}
- `view.zoom_set` (Set Zoom): {samples_per_px}
- `view.zoom_preset` (Zoom Preset) [Cmd+Ctrl+1-5]: {preset: 1..5, store?: bool}
- `view.zoom_to_selection` (Zoom to Selection) [Alt+F]: {width_px?: 1200}
- `view.zoom_fit` (Fill Window With Session) [Alt+A]: {width_px?: 1200}
- `view.scroll` (Scroll Timeline): {to?: position, by_px?: n}
- `view.waveform_zoom` (Waveform Zoom) [Cmd+Alt+[ / ]]: {factor?: 2 | value}
- `view.ruler` (View › Rulers › Rulers): {ruler: bars_beats|min_secs|timecode|feet_frames|samples|tempo|meter|markers|key|chords, visible?: bool}
- `view.main_counter` (View › Main Counter › Main Counter): {format: bars_beats|min_secs|timecode|feet_frames|samples}
- `view.sub_counter` (Sub Counter): {format?: … | null}
- `view.grid` (Grid Value): {value: '1/16' | '1 bar' | '1/8t' | '1/4.' | {seconds} | {frames} | {samples}, lines?: bool}
- `view.grid_lines` (Show Grid Lines): {value?: bool}
- `view.nudge` (Nudge Value): {value: like grid}
- `view.edit_comments` (View › Edit Window Views › Comments): {value?: bool} (toggles when omitted)
- `view.edit_mic_preamps` (View › Edit Window Views › Mic Preamps): {value?: bool} (toggles when omitted)
- `view.edit_instruments` (View › Edit Window Views › Instruments): {value?: bool} (toggles when omitted)
- `view.edit_inserts_ae` (View › Edit Window Views › Inserts A-E): {value?: bool} (toggles when omitted)
- `view.edit_inserts_fj` (View › Edit Window Views › Inserts F-J): {value?: bool} (toggles when omitted)
- `view.edit_sends_ae` (View › Edit Window Views › Sends A-E): {value?: bool} (toggles when omitted)
- `view.edit_sends_fj` (View › Edit Window Views › Sends F-J): {value?: bool} (toggles when omitted)
- `view.edit_io` (View › Edit Window Views › I/O): {value?: bool} (toggles when omitted)
- `view.edit_object` (View › Edit Window Views › Object): {value?: bool} (toggles when omitted)
- `view.edit_realtime_properties` (View › Edit Window Views › Real-Time Properties): {value?: bool} (toggles when omitted)
- `view.edit_track_color` (View › Edit Window Views › Track Color): {value?: bool} (toggles when omitted)
- `view.edit_marker_controls` (View › Edit Window Views › Marker Controls): {value?: bool} (toggles when omitted)
- `view.edit_pinned_tracks` (View › Edit Window Views › Pinned Tracks): {value?: bool} (toggles when omitted)
- `view.edit_all` (View › Edit Window Views › All): {} — shows every Edit window column
- `view.edit_minimal` (View › Edit Window Views › Minimal): {} — hides every optional Edit window column
- `view.ruler_timecode2` (View › Rulers › Timecode 2): {visible?: bool}
- `view.ruler_markers2` (View › Rulers › Markers 2): {visible?: bool}
- `view.ruler_markers3` (View › Rulers › Markers 3): {visible?: bool}
- `view.ruler_markers4` (View › Rulers › Markers 4): {visible?: bool}
- `view.ruler_markers5` (View › Rulers › Markers 5): {visible?: bool}
- `view.ruler_all_markers` (View › Rulers › All Marker Rulers): {visible?: bool} — shows (or hides) all five marker rulers
- `view.ruler_all` (View › Rulers › All): {} — shows every ruler
- `view.ruler_minimal` (View › Rulers › Minimal): {} — only the main time ruler and markers
- `view.ruler_tempo_editor` (View › Rulers › Tempo › Tempo Editor): {value?: bool} (toggles when omitted)
- `view.ruler_key_staff` (View › Rulers › Key Signature › Key Signature Staff): {value?: bool} (toggles when omitted)
- `view.marker_track_lane` (View › Marker Displays › Track Lane): {value?: bool} (toggles when omitted)
- `view.marker_ruler_lines` (View › Marker Displays › Ruler Lines): {value?: bool} (toggles when omitted)
- `view.marker_folder_lines` (View › Marker Displays › Folder Lines): {value?: bool} (toggles when omitted)
- `view.marker_ruler_lane_color` (View › Marker Displays › Ruler Lane Color): {value?: bool} (toggles when omitted)
- `view.marker_track_lane_color` (View › Marker Displays › Track Lane Color): {value?: bool} (toggles when omitted)
- `view.midi_input_display` (View › Other Displays › MIDI Input Display): {value?: bool} (toggles when omitted)
- `view.midi_editor_clip_effects` (View › Other Displays › Lower Dock › MIDI Editor › Clip Effects): {value?: bool} (toggles when omitted)
- `view.clip_sync_point` (View › Clip › Sync Point): {value?: bool} (toggles when omitted)
- `view.clip_processing_state` (View › Clip › Processing State): {value?: bool} (toggles when omitted)
- `view.clip_name` (View › Clip › Name): {value?: bool} (toggles when omitted)
- `view.clip_channel_name` (View › Clip › Channel Name): {value?: bool} (toggles when omitted)
- `view.clip_scene_take` (View › Clip › Scene And Take): {value?: bool} (toggles when omitted)
- `view.clip_rating` (View › Clip › Rating): {value?: bool} (toggles when omitted)
- `view.clip_overlap_shadows` (View › Clip › Overlap Shadows): {value?: bool} (toggles when omitted)
- `view.clip_transparency` (View › Clip › Transparency): {value?: bool} (toggles when omitted)
- `view.clip_overwrite_indicator` (View › Clip › Overwrite Indicator): {value?: bool} (toggles when omitted)
- `view.clip_copy_move_indicators` (View › Clip › Copy/Move Indicators): {value?: bool} (toggles when omitted)
- `view.clip_gain_line` (View › Clip › Clip Gain Line): {value?: bool} (toggles when omitted)
- `view.clip_gain_info` (View › Clip › Clip Gain Info): {value?: bool} (toggles when omitted)
- `view.clip_effects_status` (View › Clip › Clip Effects Status): {value?: bool} (toggles when omitted)
- `view.clip_ara_note_overlay` (View › Clip › ARA Note Overlay): {value?: bool} (toggles when omitted)
- `view.clip_time_current` (View › Clip › Current Time): {}
- `view.clip_time_original` (View › Clip › Original Time Stamp): {}
- `view.clip_time_user` (View › Clip › User Time Stamp): {}
- `view.clip_time_none` (View › Clip › No Time): {}
- `view.clip_all_channels` (View › Clip › Display on All Channels): {value?: bool} (toggles when omitted)
- `view.waveform_peak` (View › Waveforms › Peak): {}
- `view.waveform_power` (View › Waveforms › Power): {}
- `view.waveform_rectified` (View › Waveforms › Rectified): {value?: bool} (toggles when omitted)
- `view.waveform_outlines` (View › Waveforms › Outlines): {value?: bool} (toggles when omitted)
- `view.waveform_overlapped_crossfades` (View › Waveforms › Overlapped Crossfades): {value?: bool} (toggles when omitted)
- `view.automation_trim_playlist` (View › Automation › Trim Playlist): {value?: bool} (toggles when omitted)
- `view.automation_composite_playlist` (View › Automation › Composite Playlist): {value?: bool} (toggles when omitted)
- `view.expanded_sends_all` (View › Expanded Sends › All): {} — expands every send in the sends view
- `view.expanded_sends_none` (View › Expanded Sends › None): {}
- `view.expanded_send_a` (View › Expanded Sends › Send A): {value?: bool} (toggles when omitted)
- `view.expanded_send_b` (View › Expanded Sends › Send B): {value?: bool} (toggles when omitted)
- `view.expanded_send_c` (View › Expanded Sends › Send C): {value?: bool} (toggles when omitted)
- `view.expanded_send_d` (View › Expanded Sends › Send D): {value?: bool} (toggles when omitted)
- `view.expanded_send_e` (View › Expanded Sends › Send E): {value?: bool} (toggles when omitted)
- `view.expanded_send_f` (View › Expanded Sends › Send F): {value?: bool} (toggles when omitted)
- `view.expanded_send_g` (View › Expanded Sends › Send G): {value?: bool} (toggles when omitted)
- `view.expanded_send_h` (View › Expanded Sends › Send H): {value?: bool} (toggles when omitted)
- `view.expanded_send_i` (View › Expanded Sends › Send I): {value?: bool} (toggles when omitted)
- `view.expanded_send_j` (View › Expanded Sends › Send J): {value?: bool} (toggles when omitted)
- `view.track_number` (View › Track Number): {value?: bool} (toggles when omitted)
- `view.track_transcription_lane` (View › Track Transcription Lane): {value?: bool} (toggles when omitted)
- `view.dropped_video_frame_indicator` (View › Dropped Video Frame Indicator): {value?: bool} (toggles when omitted)
- `view.transport_counters` (View › Transport › Counters): {value?: bool} (toggles when omitted)
- `view.transport_midi_controls` (View › Transport › MIDI Controls): {value?: bool} (toggles when omitted)
- `view.transport_synchronization` (View › Transport › Synchronization): {value?: bool} (toggles when omitted)
- `view.transport_ableton_link` (View › Transport › Ableton Link): {value?: bool} (toggles when omitted)
- `view.transport_output_meters` (View › Transport › Output Meters): {value?: bool} (toggles when omitted)
- `view.transport_expanded` (View › Transport › Expanded): {value?: bool} (toggles when omitted)
- `view.flags` (View Flags): {prefix?} — lists the view/option flags that are on

## video — Video track

- `video.online` (Options › Video Track Online): {value?: bool} (toggles when omitted) — when offline the Video window and the Video track stop decoding pictures
- `video.offset` (Set Video Start): {track?: video track (default: the first), at: position} — moves the track's video clips so the picture starts at `at` (e.g. '01:00:00:00')
- `video.list` (Movies): {} — movies used by Video tracks (path, size, rate, codec, online file)

## app — App

- `app.quit` (Quit) [Cmd+Q]: {}
