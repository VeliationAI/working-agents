# Working Agents

Free field guides on AI agents that do real work. PDF and audio, same words, shared under Creative Commons.

Book 1 is a complete public draft: **The Agent Loop**. It is about 7,000 words, an evening's read, and a commute if you listen. The next seven books are outlined so the series has a direction. You do not need them to publish this one.

LinkedIn is the distribution. The book is the asset people keep. Each chapter is already a post, a document, or a newsletter issue. You can start teaching in public this week, while your name and your own opening paragraph go onto the draft.

## This weekend

1. Open `series.yaml`. Put your name and your LinkedIn URL in `author` and `contact`.
2. Open `books/01-the-agent-loop/manuscript/00-preface.md`. Replace the yellow-box note with two or three sentences only you can write. Read the book once and change any sentence you would not say out loud.
3. Build the PDFs:

```powershell
python tools\build_pdf.py
```

4. Hear a private preview, and export the scripts you can record yourself:

```powershell
python tools\build_audio.py
```

5. Post from `publishing/linkedin/`. Upload `dist/pdf/The-One-Page-Agent-Brief.pdf` as a LinkedIn document. Put `dist/pdf/The-Agent-Loop.pdf` in your Featured section.
6. Share the PDFs from the GitHub release (or from this OneDrive folder while you are still editing).

The builder will warn you if the cover still says "Your Name", if the contact link is still a placeholder, or if the preface note is still there.

## What is in the folder

| Path | What it is |
| --- | --- |
| `series.yaml` | Your name, series title, license, contact link, preview voice |
| `books/01-the-agent-loop/manuscript/` | The book. Edit this. The PDF is generated. |
| `books/UPCOMING.md` | Books 2 through 8, outlined |
| `dist/pdf/` | The book and the one-page handout, after you build |
| `dist/audio/` | Narration scripts, captions, and a private voice preview |
| `publishing/linkedin/` | Profile text, a six-post launch, and the first newsletter |
| `publishing/where-to-publish.md` | Where a free PDF and audio edition can live |
| `publishing/audio.md` | What you may publish as audio |
| `SERIES.md` | Who the series is for, and the rules that keep it short |

## License, choose it once

The default is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Anyone may copy and adapt the books, including commercially, if they credit you and note changes. That is the right default if you want the work to travel and your name to travel with it.

If you do not want other people selling the books, change the license in `series.yaml` and `LICENSE` to CC BY-NC 4.0 before the first public post. People who already received a version can keep sharing that version on the terms you used at the time.

## Build tools

Python 3.12 is enough. Fonts come from Windows (Georgia, Calibri, Consolas).

```powershell
python -m pip install -r requirements.txt
python tools\build_pdf.py
python tools\build_audio.py
```

`Build-PDF.ps1` and `Build-Audio.ps1` do the same thing.

Audio synthesis needs a network connection. `python tools\build_audio.py --text-only` writes the scripts and skips the voice.
