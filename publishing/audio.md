# Audio

The book and the audio have to be the same edition. Readers switch between them. If you change a chapter, rebuild the PDF and re-record, or re-synthesize, that chapter.

## What to publish

Publish a voice you have the right to share.

The strongest version for LinkedIn is your own voice. People follow a person, and a ninety-second clip of you reading one page will do more for the series than a polished synthetic hour. The scripts are the manuscript, cleaned up for speech:

- `dist/audio/01-the-agent-loop/full-narration.txt` is the whole book
- the numbered `.txt` files are one file per chapter
- record anywhere quiet, one chapter at a time, and leave the file name as the chapter title

A text-to-speech voice is fine for the public edition when its license says you may redistribute the audio. Read that license for the specific voice, not the slogan on the download page. Keep the credit in the episode description: synthetic voice, voice name, license.

## What the preview in this folder is

`python tools\build_audio.py` writes the scripts, then reads them with a Microsoft Edge neural voice through the `edge-tts` library (`en-US-AndrewNeural` by default, slower by 8 percent, set in `series.yaml`). A full preview takes roughly fifteen to twenty minutes.

Use that audio to hear awkward sentences, repeated rhythms, and examples that do not survive being spoken. Then change the manuscript.

Do not upload those mp3 files as the public audiobook. The Edge read-aloud endpoint behind `edge-tts` is not a grant to redistribute a book. `dist/audio/01-the-agent-loop/PREVIEW.txt` says the same thing beside the files.

`--text-only` skips the network call and still writes the scripts.

## Captions

Each preview mp3 can have a sentence-level `.srt` next to it. For a public YouTube edition, use captions that match the words you actually released. YouTube can auto-caption your own recording. Listen once and fix names.

## A clip you can post before the full audio exists

You do not need the full audiobook to start. Read one of these, to camera or as a voice note, in under ninety seconds:

- The meeting test, from the chapter "A chatbot answers. An agent finishes."
- The weak goal and the finishable goal, from "Goals you can finish."
- The five lines of the handback, from "The check."

Point people at the PDF for the rest.
