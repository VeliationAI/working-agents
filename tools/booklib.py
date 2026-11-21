"""Load series config and markdown manuscripts for any Working Agents book."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOKS_DIR = ROOT / "books"

BOOK_ORDER = [
    "01-the-agent-loop",
    "02-briefing-an-agent",
    "03-tools-and-permissions",
    "04-memory",
    "05-agents-at-work",
    "06-when-the-loop-goes-wrong",
    "07-more-than-one-agent",
    "08-shipping-an-agent",
]


def list_books() -> list[Path]:
    found = []
    for book_id in BOOK_ORDER:
        path = BOOKS_DIR / book_id
        if (path / "book.yaml").exists():
            found.append(path)
    return found


def resolve_book(book_id: str | None = None) -> Path:
    if book_id is None:
        return BOOKS_DIR / BOOK_ORDER[0]
    if book_id.isdigit():
        index = int(book_id) - 1
        if index < 0 or index >= len(BOOK_ORDER):
            raise SystemExit(f"Unknown book number: {book_id}")
        book_id = BOOK_ORDER[index]
    path = BOOKS_DIR / book_id
    if not (path / "book.yaml").exists():
        raise SystemExit(f"No book.yaml in {path}")
    return path


def load_yaml(path: Path) -> dict:
    data: dict = {}
    current_list: str | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        item = re.match(r"^\s+-\s+(.*)$", line)
        if item:
            if current_list is None:
                raise ValueError(f"List item without a key in {path}: {raw}")
            data.setdefault(current_list, []).append(item.group(1).strip())
            continue
        if ":" not in line:
            raise ValueError(f"Cannot parse line in {path}: {raw}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        if value == "":
            current_list = key
            data[key] = []
        else:
            current_list = None
            data[key] = value
    return data


def substitute(text: str, series: dict, book: dict) -> str:
    replacements = {
        "AUTHOR": series["author"],
        "CONTACT": series["contact"],
        "SERIES": series["series_title"],
        "BOOK": book["title"],
        "LICENSE_URL": series["license_url"],
        "EDITION": book["edition"],
    }
    for key, value in replacements.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def parse_markdown(text: str) -> dict:
    text = text.lstrip("\ufeff").replace("\r\n", "\n")
    meta = {"kind": "chapter", "title": "Untitled"}
    body = text
    if text.startswith("---\n"):
        end = text.find("\n---", 3)
        if end == -1:
            raise ValueError("Unclosed front matter")
        front = text[4:end]
        body = text[end + 4 :]
        for line in front.splitlines():
            if not line.strip() or ":" not in line:
                continue
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()

    blocks: list[tuple] = []
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            blocks.append(("p", " ".join(paragraph).strip()))
            paragraph.clear()

    lines = body.split("\n")
    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if stripped == "!!!":
            flush_paragraph()
            index += 1
            callout: list[str] = []
            while index < len(lines) and lines[index].strip() != "!!!":
                if lines[index].strip():
                    callout.append(lines[index].strip())
                index += 1
            index += 1
            blocks.append(("callout", " ".join(callout)))
            continue
        if stripped.startswith("```"):
            flush_paragraph()
            index += 1
            code: list[str] = []
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code.append(lines[index].rstrip())
                index += 1
            index += 1
            blocks.append(("code", "\n".join(code).rstrip()))
            continue
        if stripped.startswith("### "):
            flush_paragraph()
            blocks.append(("h3", stripped[4:].strip()))
            index += 1
            continue
        if stripped.startswith("## "):
            flush_paragraph()
            blocks.append(("h2", stripped[3:].strip()))
            index += 1
            continue
        if stripped.startswith("# "):
            flush_paragraph()
            meta["title"] = stripped[2:].strip()
            index += 1
            continue
        if stripped.startswith("> "):
            flush_paragraph()
            quote = [stripped[2:].strip()]
            index += 1
            while index < len(lines) and lines[index].strip().startswith("> "):
                quote.append(lines[index].strip()[2:].strip())
                index += 1
            blocks.append(("quote", " ".join(quote)))
            continue
        if stripped.startswith("- "):
            flush_paragraph()
            items: list[str] = []
            while index < len(lines) and lines[index].strip().startswith("- "):
                items.append(lines[index].strip()[2:].strip())
                index += 1
            blocks.append(("ul", items))
            continue
        if re.match(r"^\d+\. ", stripped):
            flush_paragraph()
            items = []
            while index < len(lines) and re.match(r"^\d+\. ", lines[index].strip()):
                items.append(re.sub(r"^\d+\. ", "", lines[index].strip()))
                index += 1
            blocks.append(("ol", items))
            continue
        if not stripped:
            flush_paragraph()
            index += 1
            continue
        paragraph.append(stripped)
        index += 1
    flush_paragraph()
    return {"kind": meta.get("kind", "chapter"), "title": meta.get("title", "Untitled"), "blocks": blocks}


def load_book(book_id: str | None = None) -> tuple[dict, dict, list[dict], Path]:
    book_dir = resolve_book(book_id)
    series = load_yaml(ROOT / "series.yaml")
    book = load_yaml(book_dir / "book.yaml")
    chapters = []
    manuscript = book_dir / "manuscript"
    for name in book["chapters"]:
        path = manuscript / name
        parsed = parse_markdown(substitute(path.read_text(encoding="utf-8"), series, book))
        parsed["source"] = name
        chapters.append(parsed)
    return series, book, chapters, book_dir


def word_count(chapters: list[dict]) -> int:
    total = 0
    for chapter in chapters:
        total += len(chapter["title"].split())
        for kind, payload in chapter["blocks"]:
            if kind in {"ul", "ol"}:
                total += sum(len(item.split()) for item in payload)
            else:
                total += len(str(payload).split())
    return total


def pdf_filename(book: dict) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "-", book["title"]).strip("-")
    return f"{slug}.pdf"
