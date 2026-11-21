"""Write narration scripts and a synthetic preview of Book 1.

The preview is for editing. Read publishing/audio.md before you publish it.

    python tools\\build_audio.py
    python tools\\build_audio.py --text-only
"""

from __future__ import annotations

import argparse
import asyncio
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from booklib import ROOT, load_book


def speakable(text: str) -> str:
    text = text.replace("**", "")
    text = text.replace("`", "")
    text = text.replace("*", "")
    text = text.replace("YYYY-MM-DD", "year, month, day")
    text = re.sub(r"https?://\S+", "the link in the PDF", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def chapter_speech(chapter: dict, chapter_number: int) -> str:
    if chapter["kind"] == "chapter":
        parts = [f"Chapter {chapter_number}. {chapter['title']}."]
    else:
        parts = [f"{chapter['title']}."]
    for kind, payload in chapter["blocks"]:
        if kind == "callout":
            continue
        if kind in {"h2", "h3"}:
            parts.append(speakable(payload) + ".")
        elif kind == "p" or kind == "quote":
            parts.append(speakable(payload))
        elif kind == "ul":
            parts.extend(speakable(item) for item in payload)
        elif kind == "ol":
            for index, item in enumerate(payload, start=1):
                parts.append(f"{index}. {speakable(item)}")
        elif kind == "code":
            parts.append("The page reads as follows.")
            for line in payload.splitlines():
                cleaned = speakable(line)
                if cleaned:
                    parts.append(cleaned)
    return "\n\n".join(parts)


def slug(index: int, title: str) -> str:
    words = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return f"{index:02d}-{words[:48]}"


async def synthesize(text: str, audio_path: Path, voice: str, rate: str) -> None:
    from edge_tts import Communicate
    from edge_tts.exceptions import NoAudioReceived
    from edge_tts.submaker import SubMaker

    last_error: Exception | None = None
    for attempt in range(3):
        try:
            communicate = Communicate(text, voice, rate=rate, boundary="SentenceBoundary")
            maker = SubMaker()
            audio = bytearray()
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    audio.extend(chunk["data"])
                elif chunk["type"] == "SentenceBoundary":
                    maker.feed(chunk)
            if not audio:
                raise NoAudioReceived("No audio was received.")
            audio_path.write_bytes(audio)
            srt_path = audio_path.with_suffix(".srt")
            srt = maker.get_srt() if maker.cues else ""
            srt_path.write_text(srt, encoding="utf-8")
            return
        except Exception as exc:  # retry transient network and service errors
            last_error = exc
            await asyncio.sleep(2 * (attempt + 1))
    assert last_error is not None
    raise last_error


async def build(text_only: bool) -> None:
    series, book, chapters = load_book()
    out = ROOT / "dist" / "audio" / "01-the-agent-loop"
    out.mkdir(parents=True, exist_ok=True)
    intro = (
        f"{series['series_title']}. Book {book['book_number']}. {book['title']}. "
        f"{book['subtitle']}. Written by {series['author']}. "
        f"This is a private audio preview of edition {book['edition']}, dated {book['edition_date']}. "
        "The PDF contains the same words. "
        "This voice is synthetic, for editing the read-aloud. "
        "Publish the public audio in your own voice, or use a voice whose license allows you to share it."
    )
    pieces: list[tuple[str, str]] = [("00-introduction", intro)]
    number = 0
    for index, chapter in enumerate(chapters, start=1):
        if chapter["kind"] == "chapter":
            number += 1
        pieces.append((slug(index, chapter["title"]), chapter_speech(chapter, number)))

    full = []
    playlist = ["#EXTM3U"]
    for name, text in pieces:
        script_path = out / f"{name}.txt"
        script_path.write_text(text + "\n", encoding="utf-8")
        full.append(text)
        playlist.append(f"#EXTINF:-1,{name}")
        playlist.append(f"{name}.mp3")
        print(f"Script {script_path.name}", flush=True)

    (out / "full-narration.txt").write_text("\n\n".join(full) + "\n", encoding="utf-8")
    (out / "playlist.m3u").write_text("\n".join(playlist) + "\n", encoding="utf-8")
    (out / "PREVIEW.txt").write_text(
        "\n".join(
            [
                "PRIVATE PREVIEW. Do not upload this audio as the public edition.",
                "",
                "These files are a synthetic read-through so you can hear the book while you edit it.",
                "The voice is Microsoft Edge read-aloud, reached through the edge-tts library.",
                "That service is not a license to redistribute an audiobook.",
                "",
                "Before you publish audio:",
                "- Record it in your own voice, using full-narration.txt or the chapter scripts, or",
                "- Use a text-to-speech voice whose license explicitly allows redistribution.",
                "",
                "Captions, when generated, are sentence-level .srt files beside each mp3.",
                "The PDF is the accessible text of the same edition.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    if text_only:
        print(f"Wrote narration scripts in {out}")
        return

    voice = series.get("voice", "en-US-AndrewNeural")
    rate = series.get("voice_rate", "-8%")
    for name, text in pieces:
        audio_path = out / f"{name}.mp3"
        print(f"Audio {audio_path.name}", flush=True)
        await synthesize(text, audio_path, voice, rate)
    print(f"Wrote preview audio in {out}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Book 1 narration scripts and preview audio.")
    parser.add_argument("--text-only", action="store_true", help="Write scripts and skip speech synthesis.")
    args = parser.parse_args()
    try:
        asyncio.run(build(args.text_only))
    except Exception as exc:
        print(f"ERROR: audio preview failed: {exc}")
        print("Narration scripts were still written when the failure happened after that step.")
        print("Re-run with --text-only to export scripts without calling the speech service.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
