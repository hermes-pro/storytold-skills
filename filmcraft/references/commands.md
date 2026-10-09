# FilmCraft command catalog

Generated from `command_list` (FilmCraft 0.4.0, 675 commands). Run any of these with `command_run {id, params}` (or several with `command_batch`); `filmcraft-cli describe <id>` shows one in full. Times: 254016000000 ticks per second; most time params also accept `seconds`, `frame` or `timecode`. `params` are the engine's own docs (`str`, `int`, `?` = optional).

## audio

- `audio.toggleScrubbing` Toggle Audio During Scrubbing [Shift+S]
- `audio.voiceover.settings` Voice-Over Record Settings: {"source":str?,"inputChannel":n?,"name":str?,"countdownSoundCues":bool?,"prerollSeconds":f64?,"postrollSeconds":f64?}
- `audio.voiceover.start` Start Voice-over Recording: {"track":"A1"\|id?,"time":ticks?,"preroll":seconds?}
- `audio.voiceover.stop` Stop Voice-over Recording: {"time":ticks?,"dir":str?,"discard":bool?}
- `audio.voiceover.sync` Sync Voice-over Capture: {"time":ticks?}

## captions

- `captions.add` Add Caption at Playhead (Sequence › Captions) [Cmd+Alt+C]: {"track":id\|"C1"?,"text":str?,"time":ticks?,"seconds":f64?,"durationSeconds":f64=3}
- `captions.delete` Delete Captions: {"captions":[id]?,"ripple":bool=false}
- `captions.deleteTrack` Delete Caption Track: {"track":id\|"C1"}
- `captions.export` Captions… (File › Export): {"path":str,"format":"srt\|vtt\|scc\|mcc\|stl\|ttml\|dfxp"? (default: from the extension),"track":id\|"C1"?,"dropFrame":bool=true}
- `captions.goTo` Go to Caption: {"caption":id}
- `captions.hideAll` Hide All Caption Tracks (Sequence › Captions)
- `captions.import` Import Captions…: {"path":str,"name":str?}
- `captions.list` List Captions: {"track":id\|"C1"?}
- `captions.merge` Merge Captions: {"captions":[id]?}
- `captions.move` Move Captions: {"captions":[id]?,"delta":ticks\|"deltaFrames":i64}
- `captions.newTrack` Add New Caption Track… (Sequence › Captions) [Cmd+Alt+A]: {"format":"Subtitle\|CEA-608\|CEA-708\|Teletext","name":str?,"language":str?}
- `captions.next` Go to Next Caption Segment (Sequence › Captions) [Cmd+Alt+Down]
- `captions.previous` Go to Previous Caption Segment (Sequence › Captions) [Cmd+Alt+Up]
- `captions.select` Select Captions: {"captions":[id],"add":bool?}
- `captions.setStyle` Caption Track Style: {"track":id\|"C1","font":str?,"size":f32?,"color":"#rrggbb[aa]"?,"background":bool?,"backgroundColor":"#rrggbbaa"?,"align":"left\|center\|right"?,"anchor":"top\|middle\|bottom"?,"margin":0..0.45 (fraction of frame height)?,"lineSpacing":f32?,"outline":f32?,"outlineColor":str?,"reset":bool?}
- `captions.setText` Edit Caption Text: {"caption":id?,"text":str?,"speaker":str\|null?}
- `captions.setTimes` Set Caption In/Out: {"caption":id?,"startTime\|startFrame\|startSeconds\|startTimecode":…,"endTime\|endFrame\|endSeconds\|endTimecode":…}
- `captions.setTrack` Caption Track Settings: {"track":id\|"C1","name":str?,"format":str?,"language":str?,"enabled":bool?,"locked":bool?,"syncLock":bool?}
- `captions.showActiveOnly` Show Active Caption Tracks Only (Sequence › Captions): {"track":id\|"C1"?}
- `captions.showAll` Show All Caption Tracks (Sequence › Captions)
- `captions.split` Split Caption: {"caption":id?,"time":ticks?}
- `captions.trim` Trim Caption: {"caption":id,"edge":"in\|out","delta":ticks\|"deltaFrames":i64}

## clip

- `clip.audioChannels` Audio Channels… (Clip › Modify) [Shift+G]: {"items":[id]?,"format":"mono\|stereo\|5.1\|adaptive","clips":[[channel]]?,"channels":[channel]?}
- `clip.audioGain` Audio Gain… (Clip › Audio Options) [G]: {"clips":[id]?,"mode":"set\|adjust\|normalizeMax\|normalizeAll"?,"db":f64,"relative":bool?}
- `clip.audioPeak` Audio Clip Peak Amplitude: {"clips":[id]?}
- `clip.automateToSequence` Automate to Sequence… (Clip): {"items":[id]?,"ordering":"sort\|selection","placement":"sequentially\|unnumberedMarkers","method":"insert\|overwrite","overlapFrames":n=30,"stillFrames":n?,"videoTransition":bool=true,"audioTransition":bool=true,"ignoreAudio":bool=false,"ignoreVideo":bool=false}
- `clip.breakoutToMono` Breakout to Mono (Clip › Audio Options): {"items":[id]?}
- `clip.clearPosterFrame` Clear Poster Frame [Alt+P]: {"item":id?}
- `clip.createMulticam` Create Multi-Camera Source Sequence… (Clip): {"items":[id]?,"name":str?,"method":"in\|out\|timecode\|marker\|audio","ignoreHours":bool?,"marker":str?,"offset":frames?,"audio":"camera1\|all\|switch","cameraNames":"clip\|track\|metadata","processedBin":bool?,"reference":item?}
- `clip.editOffline` Edit Offline… (Clip): {"item":id?,"mediaName":str?,"tapeName":str?,"description":str?,"scene":str?,"shot":str?,"logNote":str?}
- `clip.editSubclip` Edit Subclip… (Clip): {"item":id?,"start":ticks?,"end":ticks?,"startFrame":i64?,"endFrame":i64?,"restrictTrims":bool?,"convertToMaster":bool?}
- `clip.enable` Enable (Clip) [Shift+E]: {"clips":[id]?}
- `clip.extractAudio` Extract Audio (Clip › Audio Options): {"items":[id]?,"dir":str?}
- `clip.fieldOptions` Field Options… (Clip › Video Options): {"clips":[id]?,"reverseFieldDominance":bool=false,"processing":"none\|alwaysDeinterlace\|flickerRemoval"}
- `clip.fillFrame` Fill frame (Clip › Video Options): {"clips":[id]?}
- `clip.fitToFrame` Fit to frame (Clip › Video Options): {"clips":[id]?}
- `clip.frameHold` Add Frame Hold (Clip › Video Options): {"clips":[id]?,"time":ticks?}
- `clip.frameHoldOptions` Frame Hold Options… (Clip › Video Options): {"clips":[id]?,"enabled":bool=true,"holdOn":"sourceTimecode\|sequenceTime\|in\|out\|playhead","time":ticks?,"timecode":str?,"holdFilters":bool=false}
- `clip.generateAudioWaveform` Generate Audio Waveform (Clip): {"items":[id]?}
- `clip.group` Group (Clip) [Cmd+G]
- `clip.insertFrameHoldSegment` Insert Frame Hold Segment (Clip › Video Options): {"clip":id?,"time":ticks?,"seconds":f64=2}
- `clip.interpretFootage` Interpret Footage… (Clip › Modify): {"items":[id]?,"colorSpace":"auto"\|"<color space id>"}
- `clip.link` Link (Clip) [Cmd+L]: {"clips":[id]?}
- `clip.makeSubclip` Make Subclip… (Clip) [Cmd+U]: {"item":id?,"clip":id?,"name":str?,"start":ticks?,"end":ticks?,"startFrame":i64?,"endFrame":i64?,"restrictTrims":bool=true}
- `clip.mergeClips` Merge Clips… (Clip): {"items":[id]?,"method":"in\|out\|timecode\|marker\|audio","name":str?,"removeVideoAudio":bool?,"ignoreHours":bool?,"marker":str?,"offset":frames?}
- `clip.modifyTimecode` Timecode… (Clip › Modify): {"item":id?,"timecode":"HH:MM:SS:FF"?,"frame":i64?,"tapeName":str?,"reset":bool?}
- `clip.multicamEnable` Enable (Clip › Multi-Camera): {"clips":[id]?,"enabled":bool?}
- `clip.multicamFlatten` Flatten (Clip › Multi-Camera): {"clips":[id]?}
- `clip.nest` Nest… (Clip): {"name":str}
- `clip.nudgeVolumeDown1` Nudge Volume -1dB
- `clip.nudgeVolumeDown3` Nudge Volume -3dB
- `clip.nudgeVolumeUp1` Nudge Volume +1dB
- `clip.nudgeVolumeUp3` Nudge Volume +3dB
- `clip.remix` Remix: {"clip":id?,"duration":ticks?,"seconds":f64?,"frame":n?,"timecode":str?,"segments":0..100?,"variations":0..100?}
- `clip.remix.enable` Enable Remix (Clip › Remix): {"clip":id?}
- `clip.remix.properties` Remix Properties… (Clip › Remix): {"clip":id?,"duration":ticks?,"seconds":f64?,"frame":n?,"timecode":str?,"segments":0..100?,"variations":0..100?}
- `clip.remix.revert` Revert Remix (Clip › Remix): {"clip":id?}
- `clip.rename` Rename… (Clip): {"clip":id?,"item":id?,"name":str}
- `clip.replaceFromBin` From Bin (Clip › Replace With Clip): {"clips":[id]?,"item":id?,"keepSourceIn":bool=false}
- `clip.replaceFromSource` From Source Monitor (Clip › Replace With Clip): {"clips":[id]?}
- `clip.replaceFromSourceMatchFrame` From Source Monitor, Match Frame (Clip › Replace With Clip): {"clips":[id]?}
- `clip.restoreCaptionsFromSource` Restore Captions from Source Clip (Clip)
- `clip.revealInProject` Reveal in Project: {"clip":id?}
- `clip.scaleToFrameSize` Scale to Frame Size (Clip › Video Options)
- `clip.sceneEditDetection` Scene Edit Detection… (Clip): {"clips":[id]?,"sensitivity":0..100=50,"minShotFrames":n=6,"applyCuts":bool=true,"createSubclips":bool=false,"generateMarkers":bool=false,"wait":bool=false}
- `clip.setPosterFrame` Set Poster Frame [Cmd+P]: {"item":id?,"time":ticks?}
- `clip.setTimeInterpolation` Set Time Interpolation: {"clips":[id]?,"mode":"frameSampling\|frameBlending\|opticalFlow"}
- `clip.sourceSettings` Source Settings… (Clip): {"item":id?}
- `clip.speedDuration` Speed/Duration… (Clip) [Cmd+R]: {"clips":[id]?,"speed":percent=100,"reverse":bool,"ripple":bool,"interpolation":"frameSampling\|frameBlending\|opticalFlow"?}
- `clip.synchronize` Synchronize… (Clip): {"method":"in\|out\|timecode\|marker\|audio","clips":[id]?,"reference":clip?,"track":"V1"\|"A1"?,"ignoreHours":bool?,"marker":str?,"offset":frames?}
- `clip.timeInterpolation.frameBlending` Frame Blending (Clip › Video Options › Time Interpolation): {"clips":[id]?}
- `clip.timeInterpolation.frameSampling` Frame Sampling (Clip › Video Options › Time Interpolation): {"clips":[id]?}
- `clip.timeInterpolation.opticalFlow` Optical Flow (Clip › Video Options › Time Interpolation): {"clips":[id]?}
- `clip.ungroup` Ungroup (Clip) [Cmd+Shift+G]
- `clip.updateMetadata` Update Metadata… (Clip): {"items":[id]?}
- `clip.volumeDown` Decrease Clip Volume [[]
- `clip.volumeDownMany` Decrease Clip Volume Many [Shift+[]
- `clip.volumeUp` Increase Clip Volume []]
- `clip.volumeUpMany` Increase Clip Volume Many [Shift+]]

## clipMixer

- `clipMixer.release` Release Clip Mixer Control: {"track":"A1"\|id,"lane":"volume\|pan","time":ticks?}
- `clipMixer.set` Audio Clip Mixer Adjust: {"clip":id,"effect":"volume"\|"panner","param":"level"\|"balance","value":f64,"keyframe":bool?,"time":ticks?,"begin":bool?}
- `clipMixer.setMode` Audio Clip Mixer Automation Mode: {"track":"A1"\|id,"mode":"Off\|Read\|Latch\|Touch\|Write"}
- `clipMixer.touch` Touch Clip Mixer Control: {"track":"A1"\|id,"lane":"volume\|pan","value":f64,"time":ticks?}

## color

- `color.spaces` List Colour Spaces

## command

- `command.list` List Commands

## edit

- `edit.clear` Clear (Edit) [Backspace]: {"clips":[id]?}
- `edit.consolidateDuplicates` Consolidate Duplicates (Edit)
- `edit.copy` Copy (Edit) [Cmd+C]
- `edit.cut` Cut (Edit) [Cmd+X]
- `edit.deselectAll` Deselect All (Edit) [Cmd+Shift+A]
- `edit.duplicate` Duplicate (Edit) [Cmd+Shift+/]
- `edit.editOriginal` Edit Original (Edit) [Cmd+E]: {"items":[id]?}
- `edit.find` Find… (Edit) [Cmd+F]: {"scope":"project\|timeline"?,"column":str?,"operator":"contains\|matches\|beginsWith\|endsWith\|doesNotContain"?,"text":str?,"rows":[{"column":str,"operator":str,"text":str}]?,"matchAll":bool=true,"caseSensitive":bool=false,"in":"all\|clips\|markers"?}
- `edit.findNext` Find Next (Edit)
- `edit.label` Label: {"label":"Violet\|Iris\|…"}
- `edit.label.blue` Blue (Edit › Label): {"items":[id]?,"clips":[id]?}
- `edit.label.brown` Brown (Edit › Label): {"items":[id]?,"clips":[id]?}
- `edit.label.caribbean` Caribbean (Edit › Label): {"items":[id]?,"clips":[id]?}
- `edit.label.cerulean` Cerulean (Edit › Label): {"items":[id]?,"clips":[id]?}
- `edit.label.forest` Forest (Edit › Label): {"items":[id]?,"clips":[id]?}
- `edit.label.green` Green (Edit › Label): {"items":[id]?,"clips":[id]?}
- `edit.label.iris` Iris (Edit › Label): {"items":[id]?,"clips":[id]?}
- `edit.label.lavender` Lavender (Edit › Label): {"items":[id]?,"clips":[id]?}
- `edit.label.magenta` Magenta (Edit › Label): {"items":[id]?,"clips":[id]?}
- `edit.label.mango` Mango (Edit › Label): {"items":[id]?,"clips":[id]?}
- `edit.label.purple` Purple (Edit › Label): {"items":[id]?,"clips":[id]?}
- `edit.label.rose` Rose (Edit › Label): {"items":[id]?,"clips":[id]?}
- `edit.label.tan` Tan (Edit › Label): {"items":[id]?,"clips":[id]?}
- `edit.label.teal` Teal (Edit › Label): {"items":[id]?,"clips":[id]?}
- `edit.label.violet` Violet (Edit › Label): {"items":[id]?,"clips":[id]?}
- `edit.label.yellow` Yellow (Edit › Label): {"items":[id]?,"clips":[id]?}
- `edit.paste` Paste (Edit) [Cmd+V]
- `edit.pasteAttributes` Paste Attributes… (Edit) [Cmd+Alt+V]: {"clips":[id]?,"motion":bool=true,"opacity":bool=true,"timeRemapping":bool=true,"volume":bool=true,"channelVolume":bool=true,"panner":bool=true,"effects":bool\|[effectId]=true,"scaleTimes":bool=true}
- `edit.pasteInsert` Paste Insert (Edit) [Cmd+Shift+V]
- `edit.redo` Redo (Edit) [Cmd+Shift+Z]
- `edit.removeAttributes` Remove Attributes… (Edit): {"clips":[id]?,"motion":bool=true,"opacity":bool=true,"timeRemapping":bool=true,"volume":bool=true,"channelVolume":bool=true,"panner":bool=true,"effects":bool\|[effectId]=true}
- `edit.removeUnused` Remove Unused (Edit)
- `edit.rippleDelete` Ripple Delete (Edit) [Shift+Delete]: {"clips":[id]?}
- `edit.selectAll` Select All (Edit) [Cmd+A]
- `edit.selectAllMatching` Select All Matching (Edit): {"clips":[id]?}
- `edit.selectLabelGroup` Select Label Group (Edit › Label)
- `edit.undo` Undo (Edit) [Cmd+Z]

## effects

- `effects.addKeyframe` Add/Remove Keyframe: {"clip":id,"effect":str\|index,"param":str,"mask":n?,"time":ticks?}
- `effects.apply` Apply Effect: {"clips":[id]?,"effect":"gaussian_blur\|Gaussian Blur\|…"}
- `effects.deleteKeyframe` Delete Keyframe: {"clip":id,"effect":str\|index,"param":str,"mediaTime":ticks}
- `effects.list` List Effects: {"kind":"Video"\|"Audio"\|"VideoTransition"\|"AudioTransition"?,"folder":"Video Transitions/Wipe"?,"detail":bool?}
- `effects.moveKeyframe` Move Keyframe: {"clip":id,"effect":str\|index,"param":str,"mediaTime":ticks,"to":ticks}
- `effects.remove` Remove Effect: {"clip":id,"index":n}
- `effects.reset` Reset Effect: {"clip":id,"index":n}
- `effects.setDefaultTransition` Set Selected as Default Transition: {"effect":"constant_power\|constant_gain\|exponential_fade\|<video transition>"}
- `effects.setInterpolation` Keyframe Interpolation: {"clip":id,"effect":str\|index,"param":str,"mediaTime":ticks,"interpolation":"linear\|bezier\|autoBezier\|continuousBezier\|hold\|easeIn\|easeOut"}
- `effects.setKeyframe` Edit Keyframe: {"clip":id,"effect":str\|index,"param":str,"mediaTime":ticks,"value":any?,"inInfluence":0..1?,"outInfluence":0..1?}
- `effects.setParam` Set Effect Parameter: {"clip":id,"effect":"motion"\|index,"param":str,"mask":n?,"value":num\|[x,y]\|"#rrggbb"\|bool\|path,"time":ticks?,"merge":bool?,"begin":bool?}
- `effects.toggleAnimation` Toggle Animation: {"clip":id,"effect":str\|index,"param":str,"mask":n?}
- `effects.toggleEnabled` Toggle Effect: {"clip":id,"index":n}

## essentialSound

- `essentialSound.applyPreset` Apply Sound Preset: {"clips":[id]?,"preset":str,"type":"dialogue\|music\|sfx\|ambience"?}
- `essentialSound.autoMatch` Auto-Match Loudness: {"clips":[id]?,"target":lufs?}
- `essentialSound.clearType` Clear Audio Type: {"clips":[id]?}
- `essentialSound.deletePreset` Delete Sound Preset: {"name":str,"type":"dialogue\|music\|sfx\|ambience"?}
- `essentialSound.generateDucking` Generate Ducking Keyframes: {"clips":[id]?}
- `essentialSound.inspect` Inspect Essential Sound: {"clips":[id]?}
- `essentialSound.savePreset` Save Sound Preset: {"clips":[id]?,"name":str}
- `essentialSound.set` Essential Sound Setting: {"clips":[id]?,"key":"repair.noise.on\|repair.noise.amount\|repair.humHz\|clarity.eqPreset\|creative.reverbPreset\|ducking.reduceDb\|volume.levelDb\|mute\|…","value":any,"values":{key:value}?,"begin":bool?}
- `essentialSound.setType` Set Audio Type: {"clips":[id]?,"type":"dialogue\|music\|sfx\|ambience"}

## events

- `events.clear` Clear All Events
- `events.list` List Events: {"level":"info\|warning\|error"?,"since":id?}

## export

- `export.formats` List Export Formats
- `export.presets.delete` Delete Export Preset: {"name":str}
- `export.presets.export` Export Export Presets: {"path":str,"names":[str]?}
- `export.presets.favorite` Favorite Export Preset: {"name":str,"favorite":bool?}
- `export.presets.get` Get Export Preset: {"name":str}
- `export.presets.import` Import Export Presets: {"path":str}
- `export.presets.list` List Export Presets: {"query":str?,"category":str?,"format":str?,"favorites":bool?}
- `export.presets.save` Save Export Preset: {"name":str,"from":str?,"settings":ExportSettings?,"category":str?,"description":str?,"overwrite":bool=true, …flat overrides}
- `export.queue.add` Send to Export Queue [Alt+Shift+M]: {…settings params,"path":str\|dir?,"sequences":[id]?,"ranges":[range]?,"start":bool?,"wait":bool?}
- `export.queue.cancel` Cancel Queued Export: {"id":id?,"wait":bool?}
- `export.queue.clear` Clear Finished Exports: {"all":bool=false}
- `export.queue.list` List Export Queue
- `export.queue.move` Reorder Queued Export: {"id":id,"to":index?,"by":int?}
- `export.queue.remove` Remove Queued Export: {"id":id}
- `export.queue.retry` Retry Queued Export: {"id":id,"start":bool?,"wait":bool?}
- `export.queue.start` Start Export Queue: {"wait":bool=false}
- `export.queue.stop` Stop Export Queue
- `export.quick` Quick Export: {"preset":str?,"path":str?,"wait":bool?, …settings params}
- `export.resolve` Resolve Export Settings: {…settings params, "path":str?}

## file

- `file.autoSaveNow` Auto Save Now
- `file.autoSaveStatus` Auto Save Status
- `file.close` Close (File) [Cmd+W]: {"item":id?}
- `file.closeAllOtherProjects` Close All Other Projects (File)
- `file.closeAllProjects` Close All Projects (File): {"force":bool?}
- `file.closeProject` Close Project (File) [Cmd+Shift+W]: {"force":bool?}
- `file.discardRecovery` Discard Unsaved Changes: {"id":str?,"all":bool?}
- `file.exportAaf` AAF… (File › Export): {"path":str,"sequence":id?,"mixdownVideo":bool?,"mixdownFormat":"mov\|mxf"?,"breakoutToMono":bool?,"audio":"embedded\|separate\|linked"?,"audioFormat":"wav\|aiff\|mxf"?,"sampleRate":int?,"bitDepth":"16\|24"?,"trimAudio":bool?,"handles":frames?,"renderAudioEffects":bool?,"smallSectors":bool?}
- `file.exportAle` Avid Log Exchange… (File › Export): {"path":str,"items":[id]?}
- `file.exportEdl` EDL… (File › Export): {"path":str}
- `file.exportFcp7Xml` Final Cut Pro XML… (File › Export): {"path":str}
- `file.exportFcpxml` FCPXML… (File › Export): {"path":str}
- `file.exportFrame` Export Frame: {"path":str?,"format":"png\|tiff\|bmp"?,"import":bool?}
- `file.exportGraphicsTemplate` Motion Graphics Template… (File › Export): as graphics.template.export
- `file.exportInterchange` Export Interchange: {"format":"edl\|xml\|fcpxml\|otio\|aaf\|omf"=xml,"path":str,"sequence":id?}
- `file.exportMedia` Media… (File › Export): {"path":str,"preset":str?,"settings":ExportSettings?,"format":"h264\|hevc\|prores\|dnxhr\|apv\|mjpeg\|mxf-op1a\|mxf-opatom\|png\|tiff\|bmp\|gif\|wav\|aiff"?,"width":u32?,"height":u32?,"fps":f64?,"bitrateKbps":u32?,"bitrateMode":"cbr\|vbr1Pass\|vbr2Pass"?,"hardwareEncoding":"off\|auto"?,"scale":f32=1,"audio":bool=true,"quality":0..100,"burnCaptions":bool=false,"captionSidecar":"srt\|vtt"?,"loudnessLufs":f64?,"proresProfile":"proxy\|lt\|standard\|hq"?,"dnxProfile":"lb\|sq\|hq\|hqx"?,"apvProfile":"422-10\|422-12\|444-10\|444-12"?,"mxfVideoCodec":"dnxhr\|proRes\|h264"?,"sequence":id?,"range":"entire\|inOut\|workArea\|custom"?,"startSeconds":f64?,"endSeconds":f64?,"wait":bool=false}
- `file.exportOmf` OMF… (File › Export): {"path":str,"sequence":id?,"title":str?,"audio":"embedded\|separate"?,"audioFormat":"wav\|aiff"?,"sampleRate":int?,"bitDepth":"16\|24"?,"trimAudio":bool?,"handles":frames?,"renderAudioEffects":bool?,"breakoutToMono":bool?}
- `file.exportOtio` OpenTimelineIO… (File › Export): {"path":str}
- `file.exportSelectionProject` Selection as FilmCraft Project… (File › Export): {"path":str,"items":[id]?}
- `file.import` Import… (File) [Cmd+I]: {"paths":[str],"bin":binId?,"imageSequence":bool?}
- `file.importAaf` Import AAF…: {"path":str}
- `file.importDemoFootage` Demo Footage (File › Import From): {"scene":"OceanSunset\|Aurora\|CityNight\|Dunes\|Plasma\|Forest"}
- `file.importFromMediaBrowser` Import from Media Browser (File) [Cmd+Alt+I]: {"paths":[str]?,"imageSequence":bool?}
- `file.importImageSequence` Import Image Sequence… (File): {"path":str,"bin":binId?}
- `file.listAutoSaves` Browse Auto-Saves
- `file.mediaProperties` Selection… (File › Get Media File Properties for) [Cmd+Shift+H]: {"items":[id]?}
- `file.mediaPropertiesFile` File… (File › Get Media File Properties for): {"path":str}
- `file.newAdjustmentLayer` Adjustment Layer… (File › New): {"seconds":f64=5}
- `file.newBarsAndTone` Bars and Tone… (File › New): {"seconds":f64=10}
- `file.newBin` Bin (File › New) [Cmd+B]: {"name":str,"parent":binId?}
- `file.newBinFromSelection` Bin From Selection (File › New) [Shift+B]: {"items":[id]?,"name":str?}
- `file.newBlackVideo` Black Video… (File › New): {"seconds":f64}
- `file.newColorMatte` Color Matte… (File › New): {"color":"#rrggbb","seconds":f64}
- `file.newCountingLeader` Universal Counting Leader… (File › New)
- `file.newOfflineFile` Offline File… (File › New): {"name":str?,"fileName":str?,"tapeName":str?,"video":bool=true,"audio":bool=true,"width":u32?,"height":u32?,"fps":f64?,"sampleRate":u32=48000,"channels":u32=2,"timecode":"HH:MM:SS:FF"?,"seconds":f64=10,"description":str?}
- `file.newProject` Project… (File › New) [Cmd+Alt+N]: {"name":str}
- `file.newProjectFromTemplate` New Project from Template: {"template":name\|path,"name":str?}
- `file.newSearchBin` Search Bin (File › New): {"name":str?,"column":str?,"operator":str?,"text":str?,"rows":[..]?,"matchAll":bool?,"caseSensitive":bool?}
- `file.newSequence` Sequence… (File › New) [Cmd+N]: {"name":str,"width":u32=1920,"height":u32=1080,"fps":f64=23.976,"sampleRate":u32=48000,"video":n=3,"audio":n=3,"mix":"Stereo\|Mono\|5.1\|Adaptive"?,"trackType":"Standard\|Mono\|5.1\|Adaptive"?,"fromItem":itemId?}
- `file.newSequenceFromClip` Sequence From Clip (File › New): {"items":[id]?}
- `file.newTransparentVideo` Transparent Video… (File › New)
- `file.open` Open Project… (File) [Cmd+O]: {"path":str}
- `file.openDemoProject` Demo Project (File › New)
- `file.projectManager` Project Manager… (File): {"destination":str,"mode":"collect\|consolidate","sequences":[id]?,"excludeUnused":bool=true,"handles":frames=30,"preset":"prores_lt\|prores_hq\|h264\|…","includeProxies":bool,"includePreviews":bool=false,"projectName":str?,"dryRun":bool=false,"overwrite":bool=false,"wait":bool=false}
- `file.projectSettings.general` General… (File › Project Settings): {"renderer":"gpu\|software"?,"videoDisplay":"timecode\|feet35\|feet16\|frames"?,"audioDisplay":"samples\|milliseconds"?,"captureFormat":"DV\|HDV"?,"titleSafe":[h,v]?,"actionSafe":[h,v]?}
- `file.projectSettings.scratchDisks` Scratch Disks… (File › Project Settings): {"captured":path\|null?,"videoPreviews":path\|null?,"audioPreviews":path\|null?,"autoSave":path\|null?}
- `file.recover` Recover Unsaved Changes… (File): {"id":str?}
- `file.recoveryList` List Recoverable Sessions
- `file.replaceFonts` Replace Fonts in Projects… (Graphics and Titles): {"from":family\|{"family","style"?},"to":family\|{"family","style"?},"toStyle":str?}
- `file.revert` Revert (File)
- `file.save` Save (File) [Cmd+S]: {"path":str?}
- `file.saveAll` Save All (File)
- `file.saveAs` Save As… (File) [Cmd+Shift+S]: {"path":str}
- `file.saveAsTemplate` Save as Template… (File): {"name":str?,"path":str?}
- `file.saveCopy` Save a Copy… (File) [Cmd+Alt+S]: {"path":str}
- `file.templates` List Project Templates

## fonts

- `fonts.list` List Fonts: {"system":bool=true (scan the system font folders)}

## graphics

- `graphics.align` Align Layers: {"clip":id?,"layers":[n]?,"align":"left\|hcenter\|right\|top\|vcenter\|bottom","to":"frame\|group\|selection"="frame" (frame: each layer; group: the layers' union; one layer always aligns to the frame)}
- `graphics.alignFrame.bottom` Bottom (Graphics and Titles › Align to Video Frame): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignFrame.hcenter` Center Horizontally (Graphics and Titles › Align to Video Frame): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignFrame.left` Left (Graphics and Titles › Align to Video Frame): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignFrame.right` Right (Graphics and Titles › Align to Video Frame): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignFrame.top` Top (Graphics and Titles › Align to Video Frame): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignFrame.vcenter` Center Vertically (Graphics and Titles › Align to Video Frame): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignGroup.bottom` Bottom (Graphics and Titles › Align to Video Frame as Group): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignGroup.hcenter` Center Horizontally (Graphics and Titles › Align to Video Frame as Group): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignGroup.left` Left (Graphics and Titles › Align to Video Frame as Group): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignGroup.right` Right (Graphics and Titles › Align to Video Frame as Group): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignGroup.top` Top (Graphics and Titles › Align to Video Frame as Group): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignGroup.vcenter` Center Vertically (Graphics and Titles › Align to Video Frame as Group): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignSelection.bottom` Bottom (Graphics and Titles › Align to Selection): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignSelection.hcenter` Center Horizontally (Graphics and Titles › Align to Selection): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignSelection.left` Left (Graphics and Titles › Align to Selection): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignSelection.right` Right (Graphics and Titles › Align to Selection): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignSelection.top` Top (Graphics and Titles › Align to Selection): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignSelection.vcenter` Center Vertically (Graphics and Titles › Align to Selection): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.alignTextCenter` Center align text [Cmd+Shift+C]
- `graphics.alignTextLeft` Left align text [Cmd+Shift+L]
- `graphics.alignTextRight` Right align text [Cmd+Shift+R]
- `graphics.arrangeLayer` Arrange Graphic Layer: {"clip":id?,"layer":n?,"to":"front\|back\|forward\|backward"\|index}
- `graphics.bringForward` Bring Forward (Graphics and Titles › Arrange) [Cmd+]]: {"clip":id?,"layer":n?}
- `graphics.bringToFront` Bring to Front (Graphics and Titles › Arrange) [Cmd+Shift+]]: {"clip":id?,"layer":n?}
- `graphics.deleteLayer` Delete Graphic Layer: {"clip":id?,"layer":n?}
- `graphics.distribute` Distribute Layers: {"clip":id?,"layers":[n] (3 or more)?,"axis":"horizontal\|vertical","space":bool=false (equal gaps instead of equal centre spacing)}
- `graphics.distributeHorizontally` Distribute Horizontally (Graphics and Titles › Distribute): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.distributeSpaceHorizontally` Distribute Space Horizontally (Graphics and Titles › Distribute): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.distributeSpaceVertically` Distribute Space Vertically (Graphics and Titles › Distribute): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.distributeVertically` Distribute Vertically (Graphics and Titles › Distribute): {"clip":id?,"layers":[n]? (default: the selected layers)}
- `graphics.fontSizeDown` Decrease Font Size by One Unit [Cmd+Alt+Left]
- `graphics.fontSizeDown5` Decrease Font Size by Five Units [Cmd+Alt+Shift+Left]
- `graphics.fontSizeUp` Increase Font Size by One Unit [Cmd+Alt+Right]
- `graphics.fontSizeUp5` Increase Font Size by Five Units [Cmd+Alt+Shift+Right]
- `graphics.fonts.used` List Fonts Used
- `graphics.leadingDown` Decrease Leading by One Unit [Alt+Down]
- `graphics.leadingDown5` Decrease Leading by Five Units [Alt+Shift+Down]
- `graphics.leadingUp` Increase Leading by One Unit [Alt+Up]
- `graphics.leadingUp5` Increase Leading by Five Units [Alt+Shift+Up]
- `graphics.list` List Graphic Layers: {"clip":id?}
- `graphics.newEllipse` Ellipse (Graphics and Titles › New Layer) [Cmd+Alt+E]: {"position":[x,y]?,"size":[w,h]=[400,200],"clip":id?}
- `graphics.newFromFile` From file… (Graphics and Titles › New Layer): {"path":str,"time":ticks?,"track":index?} (imports the image or video and places it above the clips at the playhead)
- `graphics.newPolygon` Polygon (Graphics and Titles › New Layer): {"position":[x,y]?,"size":[w,h]=[300,300],"sides":n=6,"clip":id?}
- `graphics.newRectangle` Rectangle (Graphics and Titles › New Layer) [Cmd+Alt+R]: {"position":[x,y]?,"size":[w,h]=[400,200],"clip":id?}
- `graphics.newShape` Shape: {"shape":"rectangle\|ellipse\|polygon\|path","position":[x,y]?,"size":[w,h]=[400,200],"points":[[x,y],…]?,"clip":id?,"seconds":f64=5}
- `graphics.newText` Text (Graphics and Titles › New Layer) [Cmd+T]: {"text":str="New Text","position":[x,y]? (point text: its alignment point on the first baseline; with `box`: the box's top-left corner),"box":[w,h]? (paragraph text wrapped in a box this size),"clip":id?,"newClip":bool?,"vertical":bool=false,"size":px=100,"font":str?,"fontStyle":str?,"seconds":f64=5,"track":index?,"time":ticks?}
- `graphics.newVerticalText` Vertical Text (Graphics and Titles › New Layer): {"text":str="New Text","position":[x,y]?,"clip":id?,"size":px=100,"seconds":f64=5,"time":ticks?}
- `graphics.nudgeDown` Nudge Selected Object down by one
- `graphics.nudgeDown5` Nudge Selected Object down by five
- `graphics.nudgeLeft` Nudge Selected Object to left by one
- `graphics.nudgeLeft5` Nudge Selected Object to left by five
- `graphics.nudgeRight` Nudge Selected Object to right by one
- `graphics.nudgeRight5` Nudge Selected Object to right by five
- `graphics.nudgeUp` Nudge Selected Object up by one
- `graphics.nudgeUp5` Nudge Selected Object up by five
- `graphics.pin` Responsive Design - Position: {"clip":id?,"layer":n\|name?,"to":"frame"\|"none"\|layer index\|layer name,"edges":["left","top","right","bottom"]\|"all"="all"}
- `graphics.resetAllParameters` Reset All Parameters (Graphics and Titles): {"clip":id?,"layers":[n]? (default: the selected layers, else all)}
- `graphics.resetDuration` Reset Duration (Graphics and Titles): {"clip":id?,"seconds":f64=5 (the default graphic duration; limited by the next clip on the track)}
- `graphics.selectLayer` Select Graphic Layer: {"clip":id?,"layers":[n]}
- `graphics.selectNextGraphic` Select Next Graphic (Graphics and Titles › Select)
- `graphics.selectNextLayer` Select Next Layer (Graphics and Titles › Select) [Cmd+Alt+]]
- `graphics.selectPreviousGraphic` Select Previous Graphic (Graphics and Titles › Select)
- `graphics.selectPreviousLayer` Select Previous Layer (Graphics and Titles › Select) [Cmd+Alt+[]
- `graphics.sendBackward` Send Backward (Graphics and Titles › Arrange) [Cmd+[]: {"clip":id?,"layer":n?}
- `graphics.sendToBack` Send to Back (Graphics and Titles › Arrange) [Cmd+Shift+[]: {"clip":id?,"layer":n?}
- `graphics.set` Set Graphic Properties: {"clip":id?,"layer":n\|name?,"props":{"font":"Inter","font_style":"Bold","size":120,"align":"center","tracking":50,"leading":0,"fill_color":"#ffcc00","stroke":true,"stroke_width":6,"background":true,"shadow":true,"position":[x,y],"scale":100,"rotation":0,"opacity":100,…},"time":ticks?}
- `graphics.setCharStyle` Character Style: {"clip":id?,"layer":n\|name?,"start":char=0,"end":char=len,"style":{"font":str,"fontStyle":str,"size":px,"color":"#rrggbb","bold":bool,"italic":bool,"underline":bool,"tracking":n,"baselineShift":px,"caps":"normal\|all caps\|small caps"},"clear":bool? (remove styles from the range)}
- `graphics.setResponsiveTime` Responsive Design - Time: {"clip":id?,"introFrames":n?,"outroFrames":n? (or introSeconds / outroSeconds, or ticks as intro / outro)}
- `graphics.setRoll` Roll/Crawl Options: {"clip":id?,"mode":"off\|roll\|crawlLeft\|crawlRight"?,"startOffScreen":bool?,"endOffScreen":bool?,"prerollFrames":n?,"easeInFrames":n?,"easeOutFrames":n?,"postrollFrames":n? (or …Seconds, or ticks as preroll/easeIn/easeOut/postroll)}
- `graphics.setText` Edit Text: {"clip":id?,"layer":n\|name?,"text":str,"merge":bool? (coalesce with the previous Edit Text undo step)}
- `graphics.setTextType` Text Layer Type: {"clip":id?,"layer":n\|name?,"type":"point\|paragraph" (point: no box, handles scale the text; paragraph: the text wraps in a box that handles resize)}
- `graphics.template.apply` Apply Graphics Template: {"template":id\|name\|path,"values":{control id or name: value}?,"time":ticks?,"track":index?}
- `graphics.template.controls` List Template Properties: {"clip":id?}
- `graphics.template.export` Export As Motion Graphics Template… (Graphics and Titles): {"clip":id?,"name":str,"category":str="My Templates","description":str?,"controls":[{"layer":n\|name,"param":"text\|fill_color\|size\|font\|position\|enabled\|…","name":str?,"kind":"text\|color\|slider\|checkbox\|font\|position"?,"min":f64?,"max":f64?,"id":str?}]? (default: each text layer's text),"path":str? (default: the user templates folder),"embedFonts":bool=false,"fontLicense":str?}
- `graphics.template.install` Install Motion Graphics Template… (Graphics and Titles): {"path":str (a .fcgt file; Adobe .mogrt files are refused)}
- `graphics.template.list` List Graphics Templates: {"query":str? (search names, categories, descriptions, tags),"category":str?,"source":"builtin\|user"?}
- `graphics.template.remove` Remove Graphics Template: {"template":id\|name (a user template)}
- `graphics.template.set` Set Template Property: {"clip":id?,"control":id\|name,"value":any} or {"clip":id?,"values":{control: value}}
- `graphics.template.thumbnail` Graphics Template Thumbnail: {"template":id\|name\|path,"width":px=320,"path":str? (write a PNG there; else returned as pngBase64)}
- `graphics.upgradeCaption` Upgrade Caption to Graphic (Graphics and Titles): {"captions":[id]? (default: the selected captions, else the one under the playhead)}
- `graphics.upgradeToSourceGraphic` Upgrade to Source Graphic (Graphics and Titles): {"clip":id?}

## help

- `help.systemReport` System Compatibility Report

## history

- `history.list` List History

## jobs

- `jobs.cancel` Cancel Job: {"job":id}
- `jobs.list` List Jobs

## lumetri

- `lumetri.applyMatch` Apply Match: {"clip":id?,"referenceTime":ticks?\|"referenceFrame":n?\|"referenceTimecode":str?,"faceDetection":bool=true}
- `lumetri.applyPreset` Apply Lumetri Preset: {"name":str,"clips":[id]?}
- `lumetri.presetThumbnails` Lumetri Preset Thumbnails: {"folder":str?,"names":[str]?,"width":n=160,"columns":n=4,"path":str?}
- `lumetri.presets` List Lumetri Presets: {"folder":str?}
- `lumetri.setInputLut` Set Input LUT: {"clip":id?,"lut":"lib:<id>"\|"builtin:<id>"\|""?,"path":str?}
- `lumetri.setLook` Set Creative Look: {"clip":id?,"lut":"lib:<id>"\|"builtin:<id>"\|""?,"path":str?}
- `lumetri.setSection` Toggle Lumetri Section: {"clip":id?,"section":"basic"\|"creative"\|"curves"\|"wheels"\|"hsl"\|"vignette","on":bool?}

## lut

- `lut.export` Export LUT: {"lut":"lib:<id>"\|"builtin:<id>","path":str,"format":"cube"\|"3dl"?}
- `lut.import` Import LUT…: {"path":str,"name":str?}
- `lut.list` List LUTs
- `lut.remove` Remove LUT: {"id":str}

## markers

- `markers.add` Add Marker (Markers) [M]: {"time":ticks?,"name":str?,"comment":str?,"color":label?,"durationFrames":i64?}
- `markers.addChapter` Add Chapter Marker… (Markers): {"time":ticks?,"name":str?,"comment":str?,"color":label?}
- `markers.addFlashCue` Add Flash Cue Marker… (Markers): {"time":ticks?,"name":str?,"comment":str?,"color":label?}
- `markers.addRange` Add Range Marker (Markers) [Ctrl+Shift+M]: {"time":ticks?,"durationFrames":i64=1s,"duration":ticks?,"name":str?,"comment":str?,"color":label?}
- `markers.addRangeInOut` Add Range Marker to In and Out (Markers) [Ctrl+M]: {"name":str?,"comment":str?,"color":label?}
- `markers.clearAll` Clear Markers (Markers) [Cmd+Alt+Shift+M]
- `markers.clearCurrent` Clear Selected Marker (Markers) [Cmd+Alt+M]
- `markers.clearIn` Clear In (Markers) [Cmd+Shift+I]
- `markers.clearInOut` Clear In and Out (Markers) [Cmd+Shift+X]
- `markers.clearOut` Clear Out (Markers) [Cmd+Shift+O]
- `markers.copyPasteIncludesSequenceMarkers` Copy Paste Includes Sequence Markers (Markers): {"on":bool?}
- `markers.edit` Edit Marker…: {"marker":id,"name":str?,"comment":str?,"color":label?,"durationFrames":i64?}
- `markers.filterColors` Marker Colour Filter: {"hidden":[label]}\|{"color":label,"visible":bool?}
- `markers.goNext` Go to Next Marker (Markers) [Shift+M]
- `markers.goPrev` Go to Previous Marker (Markers) [Cmd+Shift+M]
- `markers.goToIn` Go to In (Markers) [Shift+I]
- `markers.goToOut` Go to Out (Markers) [Shift+O]
- `markers.goToSplitAudioIn` Audio In (Markers › Go to Split): {"target":"program\|source"}
- `markers.goToSplitAudioOut` Audio Out (Markers › Go to Split): {"target":"program\|source"}
- `markers.goToSplitVideoIn` Video In (Markers › Go to Split): {"target":"program\|source"}
- `markers.goToSplitVideoOut` Video Out (Markers › Go to Split): {"target":"program\|source"}
- `markers.markClip` Mark Clip (Markers) [X]
- `markers.markIn` Mark In (Markers) [I]: {"time":ticks?,"target":"program\|source"}
- `markers.markOut` Mark Out (Markers) [O]: {"time":ticks?,"target":"program\|source"}
- `markers.markSelection` Mark Selection (Markers) [/]
- `markers.markSplitAudioIn` Audio In (Markers › Mark Split): {"time":ticks?,"target":"program\|source"}
- `markers.markSplitAudioOut` Audio Out (Markers › Mark Split): {"time":ticks?,"target":"program\|source"}
- `markers.markSplitVideoIn` Video In (Markers › Mark Split): {"time":ticks?,"target":"program\|source"}
- `markers.markSplitVideoOut` Video Out (Markers › Mark Split): {"time":ticks?,"target":"program\|source"}
- `markers.rippleSequenceMarkers` Ripple Sequence Markers (Markers): {"on":bool?}
- `markers.showAllMarkerColors` Show All Marker Colors (Markers)

## masks

- `masks.add` Create Mask: {"clip":id?,"effect":index\|id?="opacity","shape":"ellipse"\|"polygon"\|"bezier","path":[[x,y]…]\|{vertices}?,"center":[x,y]?,"size":[w,h]?}
- `masks.addVertex` Add Mask Vertex: {"clip":id?,"effect":index\|id?,"mask":n?,"after":n,"at":[x,y]}
- `masks.list` List Masks: {"clip":id?,"time":ticks?}
- `masks.moveVertex` Move Mask Vertex: {"clip":id?,"effect":index\|id?,"mask":n?,"vertex":n,"handle":"point"\|"in"\|"out"?,"to":[x,y]?\|"delta":[dx,dy]?,"breakHandles":bool?,"merge":key?}
- `masks.remove` Delete Mask: {"clip":id?,"effect":index\|id?,"mask":n?}
- `masks.removeVertex` Delete Mask Vertex: {"clip":id?,"effect":index\|id?,"mask":n?,"vertex":n}
- `masks.select` Select Mask: {"clip":id,"effect":index\|id,"mask":n}\|{"none":true}
- `masks.set` Change Mask: {"clip":id?,"effect":index\|id?,"mask":n?,"name":str?,"inverted":bool?,"mode":"none\|add\|subtract\|intersect\|lighten\|darken\|difference"?,"trackMethod":"position\|positionRotation\|positionScaleRotation"?,"feather":px?,"opacity":pct?,"expansion":px?,"path":path?,"time":ticks?,"merge":key?}
- `masks.toggleVertexSmooth` Convert Mask Vertex: {"clip":id?,"effect":index\|id?,"mask":n?,"vertex":n}
- `masks.track` Track Selected Mask: {"clip":id?,"effect":index\|id?,"mask":n?,"direction":"forward"\|"backward"?,"frames":n?,"method":"position\|positionRotation\|positionScaleRotation"?,"wait":bool?}
- `masks.translate` Move Mask: {"clip":id?,"effect":index\|id?,"mask":n?,"delta":[dx,dy],"merge":key?}

## media

- `media.attachProxies` Attach Proxies… (Clip › Proxy): {"item":id,"path":str}\|{"items":[id],"paths":[str]},"force":bool=false
- `media.autoRelink` Relink Moved Media: {"from":str,"to":str}\|{"folder":str} + match options
- `media.colorInfo` Media Colour Info: {"item":id}
- `media.createProxies` Create Proxies… (Clip › Proxy): {"items":[id]?,"preset":"prores_proxy_quarter\|prores_proxy_half\|prores_lt_half\|h264_quarter\|h264_half","destination":str?,"attach":bool=true,"wait":bool=false}
- `media.detachProxies` Detach Proxies (Clip › Proxy): {"items":[id]?}
- `media.findMissing` Find Missing Media
- `media.linkMedia` Link Media… (File): {}  (opens the Link Media dialog; agents use media.relink / media.autoRelink)
- `media.makeOffline` Make Offline… (File): {"items":[id]?,"deleteFiles":bool=false}
- `media.offlineAll` Offline All: {}  (leave every missing file offline and close the Link Media dialog)
- `media.proxyPresets` Proxy Presets
- `media.reconnectFullRes` Reconnect Full Resolution Media… (Clip › Proxy): {"item":id,"path":str}
- `media.relink` Relink Media: {"item":id,"path":str,"force":bool=false,"relinkOthers":bool=true,"alignTimecode":bool=false,"match":{"fileName":bool,"extension":bool,"clipId":bool,"duration":bool,"mediaStart":bool,"metadata":bool}?}
- `media.replaceFootage` Replace Footage…: {"item":id,"path":str}
- `media.search` Search for Media: {"folder":str,"item":id?,"exactName":bool=true}
- `media.status` Media Status: {"item":id?}
- `media.toggleProxies` Toggle Proxies (View): {"enabled":bool?}

## mediaBrowser

- `mediaBrowser.clearRecent` Clear Recent Directories
- `mediaBrowser.favorite` Add to Favorites: {"path":str?,"remove":bool?}
- `mediaBrowser.import` Import: {"paths":[str]?,"bin":binId?,"imageSequence":bool?}
- `mediaBrowser.list` List Directory: {"path":str?,"fileTypes":str?}
- `mediaBrowser.navigate` Go to Directory: {"path":str} \| {"back":true} \| {"forward":true} \| {"up":true}
- `mediaBrowser.openInSource` Open In Source Monitor: {"path":str?}
- `mediaBrowser.probe` Media File Properties: {"path":str}
- `mediaBrowser.roots` Media Browser Locations
- `mediaBrowser.select` Select Files: {"paths":[str]}
- `mediaBrowser.settings` Media Browser Settings: {"fileTypes":"all\|video\|audio\|image\|project\|caption\|<ext>"?,"view":"list\|thumbnails"?,"columns":[str]?,"importAsImageSequence":bool?,"hoverScrub":bool?,"thumbnailSize":f32?}

## mediaCache

- `mediaCache.clean` Delete Media Cache Files: {"all":bool?}
- `mediaCache.info` Media Cache Info

## metadata

- `metadata.get` Get Metadata: {"item":id?,"clip":id?}
- `metadata.set` Edit Metadata: {"item":id?,"clip":id?,"field":"Name\|Label\|Description\|Scene\|Shot\|Log Note\|Comment\|Tape Name\|Client\|Camera Angle\|…","value":str} \| {"item":id?,"fields":{name:str}}

## mixer

- `mixer.addInsert` Add Track Effect: {"strip":"A1"\|"S1"\|"Mix"\|id,"effect":str,"slot":n?,"postFader":bool?}
- `mixer.addSend` Add Send: {"strip":"A1"\|"S1"\|id,"target":"S1"\|id,"levelDb":f64?,"preFader":bool?,"pan":f64?}
- `mixer.addSubmix` Add Audio Submix Track (Sequence): {"name":str?,"channels":"Mono\|Stereo\|5.1"?}
- `mixer.clearLane` Clear Track Keyframes: {"strip":"A1"\|"S1"\|"Mix"\|id,"lane":str?}
- `mixer.deleteKeyframe` Delete Track Keyframe: {"strip":"A1"\|"S1"\|"Mix"\|id,"lane":str?,"time":ticks}
- `mixer.deleteSubmix` Delete Submix Track: {"strip":"S1"\|id}
- `mixer.inspect` Inspect Audio Track Mixer: {"time":ticks?}
- `mixer.moveKeyframe` Move Track Keyframe: {"strip":"A1"\|"S1"\|"Mix"\|id,"lane":str?,"time":ticks,"newTime":ticks?,"value":f64?}
- `mixer.recordStart` Start Automation Pass: {"time":ticks?}
- `mixer.recordStop` Write Automation: {"time":ticks?}
- `mixer.release` Release Mixer Control: {"strip":"A1"\|"S1"\|"Mix"\|id,"lane":str?,"time":ticks?}
- `mixer.removeInsert` Remove Track Effect: {"strip":"A1"\|"S1"\|"Mix"\|id,"slot":n}
- `mixer.removeSend` Remove Send: {"strip":"A1"\|"S1"\|id,"send":n}
- `mixer.setInsert` Track Effect Settings: {"strip":"A1"\|"S1"\|"Mix"\|id,"slot":n,"enabled":bool?,"postFader":bool?,"params":{id:value}?}
- `mixer.setKeyframe` Add Track Keyframe: {"strip":"A1"\|"S1"\|"Mix"\|id,"lane":str?,"time":ticks?,"value":f64}
- `mixer.setSend` Send Settings: {"strip":"A1"\|"S1"\|id,"send":n,"levelDb":f64?,"pan":f64?,"preFader":bool?,"muted":bool?,"target":"S1"?}
- `mixer.setStrip` Track Mixer Settings: {"strip":"A1"\|"S1"\|"Mix"\|id,"name":str?,"volumeDb":f64?,"pan":f64?,"muted":bool?,"solo":bool?,"recordArm":bool?,"soloSafe":bool?,"mode":"Off\|Read\|Latch\|Touch\|Write"?,"output":"Mix"\|"S1"?,"inputMap":"Stereo\|Left\|Right\|Swap\|Mono"?,"channels":"Mono\|Stereo\|5.1"?}
- `mixer.setValue` Set Mixer Control: {"strip":"A1"\|"S1"\|"Mix"\|id,"lane":"volume\|pan\|mute\|send.<i>.level\|fx.<slot>.<param>","value":f64,"time":ticks?}
- `mixer.touch` Touch Mixer Control: {"strip":"A1"\|"S1"\|"Mix"\|id,"lane":"volume\|pan\|mute\|send.<i>.level\|fx.<slot>.<param>","value":f64,"time":ticks?}
- `mixer.writeAutomation` Write Automation Points: {"strip":"A1"\|"S1"\|"Mix"\|id,"lane":str?,"points":[[ticks,value]],"tolerance":f64?}

## multicam

- `multicam.audioFollowsVideo` Multi-Camera Audio Follows Video: {"enabled":bool?}
- `multicam.autoAdjustQuality` Auto-Adjust Multi-Camera Playback Quality: {"enabled":bool?}
- `multicam.cut` Cut to Camera: {"camera":1..16\|"angle":0-based,"time":ticks?,"videoOnly":bool?}
- `multicam.cutToCamera` Cut to Camera: {"camera":1..16\|"angle":0-based,"time":ticks?,"videoOnly":bool?}
- `multicam.cutToCamera1` Cut to Camera 1 [Ctrl+1]: {"videoOnly":bool?}
- `multicam.cutToCamera2` Cut to Camera 2 [Ctrl+2]: {"videoOnly":bool?}
- `multicam.cutToCamera3` Cut to Camera 3 [Ctrl+3]: {"videoOnly":bool?}
- `multicam.cutToCamera4` Cut to Camera 4 [Ctrl+4]: {"videoOnly":bool?}
- `multicam.cutToCamera5` Cut to Camera 5 [Ctrl+5]: {"videoOnly":bool?}
- `multicam.cutToCamera6` Cut to Camera 6 [Ctrl+6]: {"videoOnly":bool?}
- `multicam.cutToCamera7` Cut to Camera 7 [Ctrl+7]: {"videoOnly":bool?}
- `multicam.cutToCamera8` Cut to Camera 8 [Ctrl+8]: {"videoOnly":bool?}
- `multicam.cutToCamera9` Cut to Camera 9 [Ctrl+9]: {"videoOnly":bool?}
- `multicam.editCameras` Edit Cameras…: {"sequence":id?,"cameras":[{"angle":0-based,"name":str?,"enabled":bool?}]?,"audio":"camera1\|all\|switch"?}
- `multicam.grid` Multi-Camera Grid: {"time":ticks?,"playing":bool?,"cellPixels":f32?,"playbackScale":f32?}
- `multicam.gridLayout` Multi-Camera Layout: {"layout":"auto\|2x2\|3x3\|4x4"}
- `multicam.inspect` Inspect Multi-Camera: {"time":ticks?}
- `multicam.nextPage` Next Multi-Camera Page
- `multicam.page` Multi-Camera Page: {"page":0-based\|"next"\|"prev"}
- `multicam.prevPage` Previous Multi-Camera Page
- `multicam.recordStart` Start Multi-Camera Recording: {"time":ticks?}
- `multicam.recordStop` Stop Multi-Camera Recording: {"time":ticks?}
- `multicam.selectCamera1` Select Camera 1 [1]: {"videoOnly":bool?}
- `multicam.selectCamera2` Select Camera 2 [2]: {"videoOnly":bool?}
- `multicam.selectCamera3` Select Camera 3 [3]: {"videoOnly":bool?}
- `multicam.selectCamera4` Select Camera 4 [4]: {"videoOnly":bool?}
- `multicam.selectCamera5` Select Camera 5 [5]: {"videoOnly":bool?}
- `multicam.selectCamera6` Select Camera 6 [6]: {"videoOnly":bool?}
- `multicam.selectCamera7` Select Camera 7 [7]: {"videoOnly":bool?}
- `multicam.selectCamera8` Select Camera 8 [8]: {"videoOnly":bool?}
- `multicam.selectCamera9` Select Camera 9 [9]: {"videoOnly":bool?}
- `multicam.selectionTopDown` Multi-Camera Selection Top Down: {"enabled":bool?}
- `multicam.showPreviewMonitor` Show Multi-Camera Preview Monitor: {"enabled":bool?}
- `multicam.switchAngle` Switch Multi-Camera Angle: {"camera":1..16 (shown order)\|"angle":0-based,"clips":[id]?,"time":ticks?,"videoOnly":bool?,"audioOnly":bool?}
- `multicam.transmitView` Transmit Multi-Camera View: {"enabled":bool?}

## perf

- `perf.stats` Performance Statistics

## playhead

- `playhead.end` Go to Sequence End [End]
- `playhead.nextEdit` Go to Next Edit Point [Down]
- `playhead.nextEditAnyTrack` Go to Next Edit Point on Any Track [Shift+Down]
- `playhead.prevEdit` Go to Previous Edit Point [Up]
- `playhead.prevEditAnyTrack` Go to Previous Edit Point on Any Track [Shift+Up]
- `playhead.selectedClipEnd` Go to Selected Clip End [Shift+End]
- `playhead.selectedClipStart` Go to Selected Clip Start [Shift+Home]
- `playhead.set` Set Playhead: {"time":ticks\|"frame":i64\|"seconds":f64\|"timecode":str}
- `playhead.start` Go to Sequence Start [Home]
- `playhead.step` Step Frames: {"frames":i64}
- `playhead.stepBack` Step Back One Frame [Left]
- `playhead.stepBack5` Step Back Five Frames [Shift+Left]
- `playhead.stepForward` Step Forward One Frame [Right]
- `playhead.stepForward5` Step Forward Five Frames [Shift+Right]

## prefs

- `prefs.get` Get Preferences: {"key":str?}
- `prefs.reset` Reset Preferences: {"category":str?}
- `prefs.schema` Settings Schema: {"category":str?}
- `prefs.set` Set Preferences: {"key":str,"value":any}\|{"values":{key:value}}

## presets

- `presets.apply` Apply Preset: {"preset":str,"clips":[id]?}
- `presets.delete` Delete Preset: {"name":str}
- `presets.export` Export Presets: {"path":str,"names":[str]?}
- `presets.import` Import Presets: {"path":str}
- `presets.list` List Effect Presets
- `presets.rename` Rename Preset: {"name":str,"to":str}
- `presets.save` Save Preset: {"clip":id?,"effects":[index]?,"name":str,"description":str?,"keyframes":"scale"\|"anchorIn"\|"anchorOut"\|"none"?}

## project

- `project.columns.list` List Project Columns
- `project.columns.resize` Resize Column: {"column":str,"width":f32}
- `project.columns.set` Metadata Display: {"columns":[name\|{"name":str,"width":f32}]}
- `project.delete` Clear [Delete]: {"items":[id]?}
- `project.deleteSearchBin` Delete Search Bin: {"bin":id}
- `project.deselectAll` Deselect All Project Items
- `project.editSearchBin` Edit Search Bin: {"bin":id,"name":str?,"column":str?,"operator":str?,"text":str?,"rows":[..]?,"matchAll":bool?,"caseSensitive":bool?}
- `project.freeform.alignToGrid` Align to Grid: {"bin":binId?,"grid":f32?}
- `project.freeform.arrangements` List Arrangements: {"bin":binId?}
- `project.freeform.deleteArrangement` Delete Arrangement: {"name":str,"bin":binId?}
- `project.freeform.layout` Freeform Layout: {"bin":binId?,"width":f32?}
- `project.freeform.move` Move Clip Cards: {"items":[id]?,"x":f32,"y":f32,"snap":bool?} \| {"positions":{"<id>":[x,y]}}
- `project.freeform.options` Freeform View Options…: {"grid":f32?,"snap":bool?,"showNames":bool?,"showDurations":bool?,"cardSize":f32?}
- `project.freeform.reset` Reset to Grid: {"bin":binId?}
- `project.freeform.resize` Clip Size: {"items":[id]?,"size":f32?,"step":1\|-1?}
- `project.freeform.restoreArrangement` Restore Arrangement: {"name":str,"bin":binId?}
- `project.freeform.saveArrangement` Save Arrangement: {"name":str,"bin":binId?}
- `project.freeform.stack` Stack Clips: {"items":[id]?}
- `project.freeform.unstack` Unstack Clips: {"items":[id]?}
- `project.ingestSettings` Ingest Settings… (File › Project Settings): {"enabled":bool?,"action":"copy\|transcode\|createProxies\|copyAndCreateProxies"?,"destination":str?,"preset":str?}
- `project.inspect` Inspect Project
- `project.items` List Project Panel Rows: {"bin":binId?,"recursive":bool?}
- `project.matteColor` Color Matte Color…: {"item":id?,"color":"#rrggbb"}
- `project.moveToBin` Move to Bin: {"items":[id]?,"bin":binId\|null}
- `project.renameBin` Rename Bin: {"bin":binId,"name":str}
- `project.searchBinItems` Search Bin Contents: {"bin":id}
- `project.select` Select Project Items: {"items":[id]}
- `project.selectAll` Select All Project Items
- `project.setMarks` Set Source In/Out: {"item":id,"in":ticks?\|null,"out":ticks?\|null}
- `project.sort` Sort Project Items: {"column":str,"descending":bool?}
- `project.view.get` Project Panel View
- `project.view.set` Set Project Panel View: {"view":"list\|icon\|freeform"?,"iconSize":f32?,"fontSize":"small\|medium\|large\|extraLarge"?,"previewArea":bool?,"thumbnails":bool?,"thumbnailsShowEffects":bool?,"hoverScrub":bool?,"thumbnailControlsAllDevices":bool?,"iconSort":column\|{"column":str,"descending":bool}?}
- `project.viewPreset.delete` Delete View Preset: {"slot":1..10}
- `project.viewPreset.list` List View Presets
- `project.viewPreset.rename` Rename View Preset: {"slot":1..10,"name":str}
- `project.viewPreset.restore` Restore View Preset: {"slot":1..10}
- `project.viewPreset.save` Save Current View Preset: {"slot":1..10?,"name":str?}
- `project.viewPreset.saveAs` Save As New View Preset: {"name":str?,"slot":1..10?}

## scopes

- `scopes.read` Read Lumetri Scopes: {"scopes":["waveform","parade","histogram","vectorscopeYuv","vectorscopeHls"]?,"waveformType":"rgb\|luma\|yc\|ycNoChroma"?,"paradeType":"rgb\|yuv\|rgbWhite"?,"colorSpace":"auto\|601\|709\|2100"?,"clamp":bool=true,"columns":n=8,"peaks":n=8,"bins":bool=true,"scale":0.5,"time":ticks?\|"frame"\|"seconds"\|"timecode"}

## sequence

- `sequence.addEdit` Add Edit (Sequence) [Cmd+K]: {"time":ticks?}
- `sequence.addEditAllTracks` Add Edit to All Tracks (Sequence) [Cmd+Shift+K]: {"time":ticks?}
- `sequence.addTracks` Add Tracks… (Sequence): {"video":n=1,"audio":n=0,"submix":n=0,"videoAfter":"first"\|"V2"\|n?,"audioAfter":"first"\|"A2"\|n?,"submixAfter":"first"\|"S1"\|n?,"audioType":"standard\|5.1\|adaptive\|mono"?,"submixType":"stereo\|5.1\|adaptive\|mono"?}
- `sequence.applyAudioTransition` Apply Audio Transition (Sequence) [Cmd+Shift+D]: {"clip":id?,"effect":str?,"frames":i64?}
- `sequence.applyVideoTransition` Apply Video Transition (Sequence) [Cmd+D]: {"clip":id?,"effect":"cross_dissolve\|Cross Dissolve\|…"?,"frames":i64?,"edge":"in"\|"out"?,"params":{param:value}?,"reverse":bool?}
- `sequence.close` Close Sequence: {"item":id?}
- `sequence.closeGap` Close Gap (Sequence): {"track":"V1"\|id,"time":ticks}
- `sequence.closeOthers` Close Other Timeline Panels: {"item":id?}
- `sequence.colorSettings` Color Management… (Sequence): {"workingSpace":"rec709"\|"rec2100-pq"\|"rec2100-hlg"?,"wideGamut":bool?,"autoToneMap":bool?}
- `sequence.deleteRenderFiles` Delete Render Files (Sequence)
- `sequence.deleteRenderFilesInToOut` Delete Render Files In to Out (Sequence)
- `sequence.deleteTrack` Delete Track: {"track":"V3"\|id}
- `sequence.deleteTracks` Delete Tracks… (Sequence): {"video":"empty"\|"V2"\|id?,"audio":"empty"\|"A2"\|id?}
- `sequence.extract` Extract (Sequence) [']
- `sequence.goToNextGap` Next in Sequence (Sequence › Go to Gap) [Shift+;]
- `sequence.goToNextGapInTrack` Next in Track (Sequence › Go to Gap): {"track":"V1"\|id?}
- `sequence.goToPrevGap` Previous in Sequence (Sequence › Go to Gap) [Cmd+Shift+;]
- `sequence.goToPrevGapInTrack` Previous in Track (Sequence › Go to Gap): {"track":"V1"\|id?}
- `sequence.inspect` Inspect Sequence: {"item":id?}
- `sequence.joinThroughEdits` Join Through Edits: {"clips":[id]?,"all":bool?}
- `sequence.lift` Lift (Sequence) [;]
- `sequence.linkedSelection` Linked Selection (Sequence): {"on":bool?}
- `sequence.makeSubsequence` Make Subsequence (Sequence) [Shift+U]: {"name":str?}
- `sequence.matchFrame` Match Frame (Sequence) [F]
- `sequence.moveTab` Move Sequence Tab: {"item":id?,"index":int}
- `sequence.nestSequences` Insert and overwrite sequences as nests or individual clips: {"on":bool?}
- `sequence.normalizeMixTrack` Normalize Mix Track… (Sequence): {"db":f64=0}
- `sequence.open` Open in Timeline: {"item":id}
- `sequence.renderAudio` Render Audio (Sequence): {"wait":bool=false}
- `sequence.renderBar` Render Bar
- `sequence.renderEffectsInToOut` Render Effects In to Out (Sequence) [Enter]: {"wait":bool=false}
- `sequence.renderInToOut` Render In to Out (Sequence): {"wait":bool=false}
- `sequence.renderSelection` Render Selection (Sequence): {"wait":bool=false}
- `sequence.revealInProject` Reveal Sequence in Project: {"item":id?}
- `sequence.revealNested` Reveal Nested Sequence [Cmd+Alt+F]
- `sequence.reverseMatchFrame` Reverse Match Frame (Sequence) [Shift+R]
- `sequence.selectionFollowsPlayhead` Selection Follows Playhead (Sequence): {"on":bool?}
- `sequence.setTransition` Edit Transition Settings: {"transition":id,"params":{param:value}?,"reverse":bool?,"reset":bool?}
- `sequence.settings` Sequence Settings… (Sequence): {"width":u32?,"height":u32?,"fps":f64?,"name":str?,"sampleRate":u32?,"mix":"Stereo\|Mono\|5.1\|Adaptive"?}
- `sequence.showThroughEdits` Show Through Edits (Sequence): {"on":bool?}
- `sequence.simplify` Simplify Sequence… (Sequence): {"name":str?,"removeDisabled":bool=true,"removeEmptyTracks":bool=true,"closeGaps":bool=false,"moveClipsDown":bool=false,"removeVideoEffects":bool=false,"removeAudioEffects":bool=false,"removeText":bool=false,"keep":"both\|video\|audio"}
- `sequence.snap` Snap in Timeline (Sequence) [S]: {"on":bool?}
- `sequence.throughEdits` List Through Edits
- `sequence.transcribe` Transcribe Sequence… (Sequence): {"track":"mix"\|"A1"\|id?,"language":"en\|auto"?,"diarize":bool?,"maxSpeakers":n?,"model":str?}

## shortcuts

- `shortcuts.audit` Shortcut Audit
- `shortcuts.clear` Clear Shortcut: {"command":id,"keys":str?,"panel":str?}
- `shortcuts.conflicts` Shortcut Conflicts: {"platform":"mac\|windows\|linux"?}
- `shortcuts.deletePreset` Delete Shortcut Preset: {"name":str}
- `shortcuts.export` Export Keyboard Shortcuts: {"path":str}
- `shortcuts.forKey` Shortcuts on a Key: {"key":"K","platform":str?}
- `shortcuts.get` Get Shortcuts of a Command: {"command":id,"platform":str?}
- `shortcuts.import` Import Keyboard Shortcuts: {"path":str,"activate":bool=true}
- `shortcuts.list` List Keyboard Shortcuts: {"query":str?,"panel":str?,"assigned":bool?,"platform":"mac\|windows\|linux"?}
- `shortcuts.loadPreset` Load Shortcut Preset: {"name":str}
- `shortcuts.presets` Keyboard Shortcut Presets
- `shortcuts.redo` Redo Shortcut Change
- `shortcuts.resolve` Resolve Shortcut: {"keys":str,"panel":str?,"platform":str?}
- `shortcuts.savePreset` Save Shortcut Preset As: {"name":str}
- `shortcuts.set` Assign Shortcut: {"command":id,"keys":"Cmd+Shift+K","panel":str?,"add":bool?,"keepConflicts":bool?}
- `shortcuts.undo` Undo Shortcut Change

## source

- `source.insert` Insert (Clip) [,]
- `source.inspect` Inspect Source Monitor
- `source.open` Open in Source Monitor: {"item":id?}
- `source.overwrite` Overwrite (Clip) [.]
- `source.setPlayhead` Set Source Playhead: {"time":ticks\|"frame":i64\|"seconds":f64}

## state

- `state.inspect` Inspect Editor State

## timeline

- `timeline.move` Move Clips: {"moves":[{"clip":id,"track":id\|"V2","time":ticks}],"insert":bool,"linked":bool?}
- `timeline.moveAudioTargetsDown` Move All Audio Targets Down
- `timeline.moveAudioTargetsUp` Move All Audio Targets Up
- `timeline.moveVideoTargetsDown` Move All Video Targets Down
- `timeline.moveVideoTargetsUp` Move All Video Targets Up
- `timeline.nudgeDown` Nudge Clip Selection Down
- `timeline.nudgeLeft` Nudge Clip Selection Left One Frame
- `timeline.nudgeLeft5` Nudge Clip Selection Left Five Frames
- `timeline.nudgeRight` Nudge Clip Selection Right One Frame
- `timeline.nudgeRight5` Nudge Clip Selection Right Five Frames
- `timeline.nudgeUp` Nudge Clip Selection Up
- `timeline.place` Place Clip: {"item":id,"track":"V1"\|id\|"A1" (sound only)?,"audioTrack":"A1"\|id?,"time":ticks\|"frame":i64\|"seconds":f64,"insert":bool,"sourceIn":ticks?,"duration":ticks?}
- `timeline.rateStretch` Rate Stretch: {"clip":id,"edge":"in\|out","delta":ticks}
- `timeline.razor` Razor: {"time":ticks,"track":"V1"\|id?,"clip":id?}
- `timeline.roll` Rolling Edit: {"left":id,"right":id,"delta":ticks\|"deltaFrames":i64}
- `timeline.select` Select Clips: {"clips":[id],"add":bool,"toggle":bool}
- `timeline.selectClipAtPlayhead` Select Clip at Playhead [D]
- `timeline.selectNextClip` Select Next Clip [Cmd+Down]
- `timeline.selectPrevClip` Select Previous Clip [Cmd+Up]
- `timeline.setTargeting` Track Targeting: {"track":"V1"\|id,"targeted":bool?,"sourcePatch":bool?}
- `timeline.setTrack` Track Settings: {"track":"V1"\|id,"locked":bool?,"syncLock":bool?,"enabled":bool?,"muted":bool?,"solo":bool?,"name":str?,"volumeDb":f64?,"pan":f64?}
- `timeline.slide` Slide: {"clip":id,"delta":ticks\|"deltaFrames":i64}
- `timeline.slideLeft` Slide Clip Selection Left One Frame
- `timeline.slideLeft5` Slide Clip Selection Left Five Frames
- `timeline.slideRight` Slide Clip Selection Right One Frame
- `timeline.slideRight5` Slide Clip Selection Right Five Frames
- `timeline.slip` Slip: {"clip":id,"delta":ticks\|"deltaFrames":i64}
- `timeline.slipLeft` Slip Clip Selection Left One Frame
- `timeline.slipLeft5` Slip Clip Selection Left Five Frames
- `timeline.slipRight` Slip Clip Selection Right One Frame
- `timeline.slipRight5` Slip Clip Selection Right Five Frames
- `timeline.toggleAllAudioTargets` Toggle All Audio Targets [Cmd+9]
- `timeline.toggleAllSourceAudio` Toggle All Source Audio [Cmd+Alt+9]
- `timeline.toggleAllSourceVideo` Toggle All Source Video [Cmd+Alt+0]
- `timeline.toggleAllVideoTargets` Toggle All Video Targets [Cmd+0]
- `timeline.toggleMuteTargetedAudio` Toggle Mute for All Targeted Audio Tracks
- `timeline.toggleOutputTargetedVideo` Toggle Track Output for All Targeted Video Tracks
- `timeline.toggleSoloTargetedAudio` Toggle Solo for All Targeted Audio Tracks
- `timeline.toggleTargetA1` Toggle Target Audio 1
- `timeline.toggleTargetA2` Toggle Target Audio 2
- `timeline.toggleTargetA3` Toggle Target Audio 3
- `timeline.toggleTargetA4` Toggle Target Audio 4
- `timeline.toggleTargetA5` Toggle Target Audio 5
- `timeline.toggleTargetA6` Toggle Target Audio 6
- `timeline.toggleTargetA7` Toggle Target Audio 7
- `timeline.toggleTargetA8` Toggle Target Audio 8
- `timeline.toggleTargetV1` Toggle Target Video 1
- `timeline.toggleTargetV2` Toggle Target Video 2
- `timeline.toggleTargetV3` Toggle Target Video 3
- `timeline.toggleTargetV4` Toggle Target Video 4
- `timeline.toggleTargetV5` Toggle Target Video 5
- `timeline.toggleTargetV6` Toggle Target Video 6
- `timeline.toggleTargetV7` Toggle Target Video 7
- `timeline.toggleTargetV8` Toggle Target Video 8
- `timeline.trim` Trim Edit: {"clip":id,"edge":"in\|out","mode":"regular\|ripple","delta":ticks\|"deltaFrames":i64}

## transcript

- `transcript.createCaptions` Create Captions from Transcript… (Sequence › Transcript): {"maxChars":n?,"lines":1\|2?,"minSeconds":f?,"maxSeconds":f?,"gapFrames":n?,"format":str?,"name":str?}
- `transcript.delete` Delete Transcript (Sequence › Transcript): {"items":[id]?}
- `transcript.downloadModel` Download Speech Model: {"model":"whisper-base"?}
- `transcript.extract` Extract Selected Text: {"from":word,"to":word?}
- `transcript.generate` Transcribe… (Sequence › Transcript): {"items":[id]?,"model":"whisper-base"?,"language":"en\|auto"?,"diarize":bool?,"maxSpeakers":n?}
- `transcript.inspect` Inspect Transcript: {"paragraphGapSeconds":f?}
- `transcript.lift` Lift Selected Text: {"from":word,"to":word?}
- `transcript.models` List Speech Models
- `transcript.removeFillers` Remove Filler Words (Sequence › Transcript): {"fillers":[str]?}
- `transcript.removePauses` Remove Pauses (Sequence › Transcript): {"minSeconds":f?,"keepSeconds":f?}
- `transcript.renameSpeaker` Rename Speaker…: {"speaker":"Speaker 1"\|index,"name":str,"item":id?}
- `transcript.search` Search Transcript: {"query":str}
- `transcript.select` Mark Selected Text: {"from":word,"to":word?}
- `transcript.set` Import Transcript: {"item":id,"transcript":{"language":str,"speakers":[{"name":str}],"words":[{"text":str,"start":tick,"end":tick,"speaker":n?}]}}

## trim

- `trim.applyDefaultTransition` Apply Default Transitions to Selection (Sequence) [Shift+D]: {"clips":[id]?}
- `trim.backward` Trim Backward [Alt+Left]
- `trim.backwardMany` Trim Backward Many [Alt+Shift+Left]
- `trim.cancelDynamic` Cancel Dynamic Trim
- `trim.clear` Clear Edit Point Selection
- `trim.edit` Trim Edit (Sequence) [Shift+T]
- `trim.extendNextEdit` Extend Next Edit To Playhead [Shift+W]
- `trim.extendPreviousEdit` Extend Previous Edit To Playhead [Shift+Q]
- `trim.extendToPlayhead` Extend Selected Edit to Playhead [E]
- `trim.forward` Trim Forward [Alt+Right]
- `trim.forwardMany` Trim Forward Many [Alt+Shift+Right]
- `trim.monitor` Trim Monitor State
- `trim.next` Trim Next Edit to Playhead [Alt+W]
- `trim.nudge` Trim by Frames: {"frames":i64}
- `trim.playAround` Play Around Edit: {"clock":seconds,"loop":bool=true,"toggle":bool?}
- `trim.previous` Trim Previous Edit to Playhead [Alt+Q]
- `trim.rippleNext` Ripple Trim Next Edit to Playhead [W]
- `trim.ripplePrevious` Ripple Trim Previous Edit to Playhead [Q]
- `trim.selectEditPoint` Select Edit Point: {"clip":id,"edge":"in\|out","kind":"trim\|ripple\|roll","add":bool?}
- `trim.selectNearest` Select Nearest Edit Point: {"kind":"rippleIn\|rippleOut\|roll\|trimIn\|trimOut"}
- `trim.shuttle` Dynamic Trim (Shuttle): {"direction":"forward\|reverse","slow":bool?,"clock":seconds}
- `trim.shuttleStop` Dynamic Trim Stop: {"clock":seconds?}
- `trim.tick` Advance Trim Playback: {"clock":seconds}
- `trim.toggleType` Toggle Trim Type [Ctrl+T]
