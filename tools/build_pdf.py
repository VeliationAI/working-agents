"""Build the Book 1 PDF and the LinkedIn handout.

    python tools\\build_pdf.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from fpdf import FPDF
from fpdf.enums import MethodReturnValue

from booklib import ROOT, load_book, parse_markdown, substitute, word_count

NAVY = (16, 28, 48)
INK = (34, 36, 40)
MUTED = (100, 106, 116)
GOLD = (168, 124, 52)
CREAM = (245, 240, 230)
PAPER = (244, 241, 234)
NOTE = (248, 240, 220)


def use_fonts(pdf: FPDF) -> None:
    windir = Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts"
    required = {
        ("Georgia", ""): "georgia.ttf",
        ("Georgia", "B"): "georgiab.ttf",
        ("Georgia", "I"): "georgiai.ttf",
        ("Georgia", "BI"): "georgiaz.ttf",
        ("Calibri", ""): "calibri.ttf",
        ("Calibri", "B"): "calibrib.ttf",
        ("Consolas", ""): "consola.ttf",
    }
    for (family, style), filename in required.items():
        path = windir / filename
        if not path.exists():
            raise SystemExit(f"Missing font: {path}")
        pdf.add_font(family, style, str(path))


def write_paragraph(pdf: FPDF, text: str, *, size=11, leading=5.7, font="Georgia", style="", color=INK, markdown=False, after=2.2) -> None:
    pdf.set_font(font, style, size)
    wrapped = pdf.multi_cell(
        0,
        leading,
        text,
        align="L",
        markdown=markdown,
        dry_run=True,
        output=MethodReturnValue.LINES,
    )
    line_count = len(wrapped)
    room = pdf.page_break_trigger - pdf.get_y()
    lines_that_fit = int(room // leading) if leading else 0
    spill = line_count - lines_that_fit
    if line_count > lines_that_fit and 0 < spill <= 2 and line_count <= 16:
        pdf.add_page()
    pdf.set_x(pdf.l_margin)
    pdf.set_font(font, style, size)
    pdf.set_text_color(*color)
    pdf.multi_cell(0, leading, text, align="L", markdown=markdown, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(after)


def write_heading(pdf: FPDF, text: str, *, level: int) -> None:
    if pdf.get_y() > pdf.h - 40:
        pdf.add_page()
    pdf.ln(1.5 if level == 3 else 2.5)
    size = 12.5 if level == 3 else 14.5
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Georgia", "B", size)
    pdf.set_text_color(*NAVY)
    pdf.multi_cell(0, 6.6 if level == 3 else 7.2, text, align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1.4)


def write_items(pdf: FPDF, items: list[str], *, ordered: bool) -> None:
    width = pdf.epw
    for index, item in enumerate(items, start=1):
        if pdf.get_y() > pdf.h - 24:
            pdf.add_page()
        marker = f"{index}." if ordered else "\u2022"
        pdf.set_text_color(*INK)
        pdf.set_font("Georgia", "", 11)
        pdf.set_x(pdf.l_margin)
        pdf.cell(7, 5.7, marker, new_x="RIGHT", new_y="TOP")
        pdf.multi_cell(width - 7, 5.7, item, align="L", markdown=True, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(1.0)
    pdf.ln(1.4)


def write_code(pdf: FPDF, text: str) -> None:
    line_count = text.count("\n") + 1
    needed = line_count * 4.05 + 14
    content_height = pdf.page_break_trigger - pdf.t_margin
    room = pdf.page_break_trigger - pdf.get_y()
    if needed < content_height and room < needed:
        pdf.add_page()
    pdf.ln(0.6)
    pdf.set_fill_color(*PAPER)
    pdf.set_text_color(28, 36, 48)
    pdf.set_font("Consolas", "", 8)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(0, 4.05, text, align="L", fill=True, padding=3.2, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)


def write_callout(pdf: FPDF, text: str) -> None:
    pdf.set_font("Calibri", "", 10.5)
    wrapped = pdf.multi_cell(
        0,
        5.15,
        text,
        align="L",
        dry_run=True,
        output=MethodReturnValue.LINES,
    )
    needed = 12 + len(wrapped) * 5.15
    content_height = pdf.page_break_trigger - pdf.t_margin
    room = pdf.page_break_trigger - pdf.get_y()
    if needed < content_height and room < needed:
        pdf.add_page()
    pdf.ln(1)
    pdf.set_fill_color(*NOTE)
    pdf.set_text_color(110, 72, 28)
    pdf.set_font("Calibri", "B", 8.5)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(
        0,
        4.4,
        "BEFORE YOU PUBLISH",
        align="L",
        fill=True,
        padding=(3.0, 3.2, 1.0, 3.2),
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.set_fill_color(*NOTE)
    pdf.set_text_color(62, 46, 24)
    pdf.set_font("Calibri", "", 10.5)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(
        0,
        5.15,
        text,
        align="L",
        fill=True,
        padding=(0.4, 3.2, 3.2, 3.2),
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.ln(3)


def write_quote(pdf: FPDF, text: str) -> None:
    y0 = pdf.get_y()
    pdf.set_text_color(45, 50, 60)
    pdf.set_font("Georgia", "I", 11)
    pdf.set_x(pdf.l_margin + 4)
    pdf.multi_cell(pdf.epw - 4, 5.7, text, align="L", markdown=True, new_x="LMARGIN", new_y="NEXT")
    y1 = pdf.get_y()
    pdf.set_draw_color(*GOLD)
    pdf.set_line_width(0.5)
    pdf.line(pdf.l_margin + 0.4, y0, pdf.l_margin + 0.4, y1)
    pdf.ln(3)


def write_blocks(pdf: FPDF, blocks: list[tuple]) -> None:
    for kind, payload in blocks:
        if kind == "p":
            write_paragraph(pdf, payload, markdown=True)
        elif kind == "h2":
            write_heading(pdf, payload, level=2)
        elif kind == "h3":
            write_heading(pdf, payload, level=3)
        elif kind == "ul":
            write_items(pdf, payload, ordered=False)
        elif kind == "ol":
            write_items(pdf, payload, ordered=True)
        elif kind == "code":
            write_code(pdf, payload)
        elif kind == "callout":
            write_callout(pdf, payload)
        elif kind == "quote":
            write_quote(pdf, payload)
        else:
            raise ValueError(f"Unknown block: {kind}")


class BookPDF(FPDF):
    def __init__(self, book_title: str) -> None:
        super().__init__(orientation="P", unit="mm", format=(152.4, 228.6))
        self.book_title = book_title
        self.front_pages = 3
        self.set_margins(18, 18, 18)
        self.set_auto_page_break(auto=True, margin=16)
        use_fonts(self)

    def header(self) -> None:
        if self.page <= self.front_pages:
            return
        self.set_font("Calibri", "", 8.5)
        self.set_text_color(*MUTED)
        self.set_xy(self.l_margin, 8)
        self.cell(self.epw / 2, 4, "Working Agents", align="L", new_x="RIGHT", new_y="TOP")
        self.set_xy(self.l_margin + self.epw / 2, 8)
        self.cell(self.epw / 2, 4, self.book_title, align="R", new_x="LMARGIN", new_y="TOP")
        self.set_draw_color(220, 216, 208)
        self.set_line_width(0.2)
        self.line(self.l_margin, 14, self.w - self.r_margin, 14)
        self.set_xy(self.l_margin, self.t_margin)

    def footer(self) -> None:
        if self.page <= self.front_pages:
            return
        self.set_y(-12)
        self.set_font("Calibri", "", 9)
        self.set_text_color(*MUTED)
        self.cell(0, 5, str(self.page - self.front_pages), align="C")


def toc_title(chapter: dict, number: int) -> str:
    if chapter["kind"] == "chapter":
        return f"{number}.   {chapter['title']}"
    return chapter["title"]


def draw_contents(pdf: BookPDF, chapters: list[dict], page_map: dict[int, int] | None) -> None:
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Georgia", "B", 22)
    pdf.set_text_color(*NAVY)
    pdf.multi_cell(0, 10, "Contents", align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.set_draw_color(*GOLD)
    pdf.set_line_width(0.45)
    rule = pdf.get_y()
    pdf.line(pdf.l_margin, rule, pdf.l_margin + 18, rule)
    pdf.ln(8)
    number = 0
    for index, chapter in enumerate(chapters):
        if chapter["kind"] == "chapter":
            number += 1
        title = toc_title(chapter, number)
        page = "" if page_map is None else str(page_map[index])
        pdf.set_text_color(*INK)
        pdf.set_font("Georgia", "", 11)
        pdf.set_x(pdf.l_margin)
        pdf.cell(pdf.epw - 14, 7.4, title, align="L", new_x="RIGHT", new_y="TOP")
        pdf.set_font("Calibri", "", 11)
        pdf.set_text_color(*MUTED)
        pdf.cell(14, 7.4, page, align="R", new_x="LMARGIN", new_y="NEXT")


def add_cover(pdf: BookPDF, series: dict, book: dict) -> None:
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)
    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, pdf.w, pdf.h, "F")
    pdf.set_fill_color(*GOLD)
    pdf.rect(18, 40, 24, 1.3, "F")
    pdf.set_text_color(*GOLD)
    pdf.set_font("Calibri", "", 11)
    pdf.set_xy(18, 48)
    pdf.cell(0, 6, f"WORKING AGENTS    /    BOOK {book['book_number']}", align="L")
    pdf.set_text_color(*CREAM)
    pdf.set_font("Georgia", "B", 34)
    pdf.set_xy(18, 72)
    pdf.multi_cell(116, 15, book["title"], align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(214, 208, 196)
    pdf.set_font("Georgia", "I", 13)
    pdf.set_xy(18, 118)
    pdf.multi_cell(112, 6.6, book["subtitle"], align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.set_fill_color(*GOLD)
    pdf.rect(18, 168, 24, 0.7, "F")
    pdf.set_text_color(*CREAM)
    pdf.set_font("Calibri", "", 13)
    pdf.set_xy(18, 178)
    pdf.cell(0, 6, series["author"], align="L")
    pdf.set_text_color(186, 180, 168)
    pdf.set_font("Calibri", "", 10)
    pdf.set_xy(18, 196)
    pdf.cell(0, 5, f"Edition {book['edition']}   /   {book['edition_label']}", align="L")
    pdf.set_xy(18, 203)
    pdf.cell(0, 5, "Free PDF and audio", align="L")
    pdf.set_xy(18, 214)
    pdf.set_font("Calibri", "", 9.5)
    pdf.multi_cell(112, 4.6, series["series_tagline"], align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.set_auto_page_break(auto=True, margin=16)


def add_copyright(pdf: BookPDF, series: dict, book: dict) -> None:
    pdf.add_page()
    write_paragraph(pdf, book["title"], size=18, leading=8, font="Georgia", style="B", color=NAVY, after=2)
    write_paragraph(pdf, book["subtitle"], size=11, leading=5.6, font="Georgia", style="I", color=MUTED, after=6)
    year = book["edition_date"][-4:]
    paragraphs = [
        f"{series['series_title']}, Book {book['book_number']}.",
        f"Copyright {year} {series['author']}.",
        (
            f"Edition {book['edition']}, {book['edition_label'].lower()}, {book['edition_date']}. "
            "This draft is public so the ideas can be used while the sentences are still open to argument."
        ),
        (
            "The text is licensed under the Creative Commons Attribution 4.0 International License "
            "(CC BY 4.0). You may share and adapt it, including commercially, if you give credit, "
            "link the license, and indicate changes."
        ),
        series["license_url"],
        f"Credit line: {book['title']}, by {series['author']}. {series['series_title']}, CC BY 4.0.",
        f"Corrections and the current edition: {series['contact']}",
        (
            "The synthetic audio in the project folder is a private preview for editing the read-aloud. "
            "Publish audio in your own voice, or with a voice whose license allows redistribution."
        ),
    ]
    for paragraph in paragraphs:
        write_paragraph(pdf, paragraph, size=10.5, leading=5.3, after=3.2)


def open_chapter(pdf: BookPDF, chapter: dict, number: int) -> None:
    pdf.add_page()
    if chapter["kind"] == "chapter":
        label = f"CHAPTER {number}"
        outline = f"{number}. {chapter['title']}"
    elif chapter["kind"] == "preface":
        label = "PREFACE"
        outline = chapter["title"]
    else:
        label = "SERIES"
        outline = chapter["title"]
    pdf.start_section(outline, level=0)
    pdf.set_text_color(*GOLD)
    pdf.set_font("Calibri", "", 10)
    pdf.set_x(pdf.l_margin)
    pdf.cell(0, 5, label, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    pdf.set_text_color(*NAVY)
    pdf.set_font("Georgia", "B", 22)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(0, 9.4, chapter["title"], align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.set_draw_color(*GOLD)
    pdf.set_line_width(0.45)
    rule = pdf.get_y()
    pdf.line(pdf.l_margin, rule, pdf.l_margin + 18, rule)
    pdf.ln(7)


def render(series: dict, book: dict, chapters: list[dict], page_map: dict[int, int] | None) -> tuple[BookPDF, dict[int, int]]:
    pdf = BookPDF(book["title"])
    pdf.set_title(f"{book['title']} - {series['series_title']}")
    pdf.set_author(series["author"])
    pdf.set_subject(book["subtitle"])
    pdf.set_creator("Working Agents")
    pdf.set_keywords("AI agents, field guide, Working Agents")
    pdf.set_lang("en-US")
    add_cover(pdf, series, book)
    add_copyright(pdf, series, book)
    pdf.add_page()
    draw_contents(pdf, chapters, page_map)
    found: dict[int, int] = {}
    number = 0
    for index, chapter in enumerate(chapters):
        if chapter["kind"] == "chapter":
            number += 1
        open_chapter(pdf, chapter, number)
        found[index] = pdf.page - pdf.front_pages
        write_blocks(pdf, chapter["blocks"])
    return pdf, found


class HandoutPDF(FPDF):
    def header(self) -> None:
        if self.page == 1:
            return
        self.set_font("Calibri", "", 9)
        self.set_text_color(*MUTED)
        self.set_xy(self.l_margin, 8)
        self.cell(self.epw / 2, 4, "The one-page agent brief", align="L", new_x="RIGHT", new_y="TOP")
        self.set_xy(self.l_margin + self.epw / 2, 8)
        self.cell(self.epw / 2, 4, "Working Agents", align="R", new_x="LMARGIN", new_y="TOP")
        self.set_xy(self.l_margin, self.t_margin)

    def footer(self) -> None:
        self.set_y(-12)
        self.set_font("Calibri", "", 9)
        self.set_text_color(*MUTED)
        self.cell(0, 5, str(self.page), align="C")


def build_handout(series: dict, book: dict) -> Path:
    source = ROOT / "publishing" / "handout-the-one-page-brief.md"
    text = source.read_text(encoding="utf-8")
    chapter = parse_markdown(substitute(text, series, book))
    pdf = HandoutPDF(orientation="P", unit="mm", format="letter")
    pdf.set_margins(18, 18, 18)
    pdf.set_auto_page_break(auto=True, margin=16)
    use_fonts(pdf)
    pdf.set_title("The one-page agent brief")
    pdf.set_author(series["author"])
    pdf.set_subject("A one-page brief for an AI agent, from Working Agents")
    pdf.set_lang("en-US")
    pdf.add_page()
    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, pdf.w, 34, "F")
    pdf.set_text_color(*GOLD)
    pdf.set_font("Calibri", "", 10)
    pdf.set_xy(18, 8)
    pdf.cell(0, 5, f"WORKING AGENTS    /    BOOK {book['book_number']}", align="L")
    pdf.set_text_color(*CREAM)
    pdf.set_font("Georgia", "B", 20)
    pdf.set_xy(18, 16)
    pdf.cell(0, 8, "The one-page agent brief", align="L")
    pdf.set_y(42)
    write_blocks(pdf, chapter["blocks"])
    pdf.ln(2)
    write_paragraph(
        pdf,
        f"{book['title']}, by {series['author']}. {series['series_title']}, CC BY 4.0. {series['license_url']}",
        size=9,
        leading=4.4,
        font="Calibri",
        color=MUTED,
        after=0,
    )
    out = ROOT / "dist" / "pdf" / "The-One-Page-Agent-Brief.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(out))
    return out


def warnings_for(series: dict, chapters: list[dict]) -> list[str]:
    notes = []
    if series["author"].strip().lower() == "your name":
        notes.append("Cover still says Your Name. Edit series.yaml before you share the PDF.")
    if "your-handle" in series["contact"]:
        notes.append("Contact link is still a placeholder. Edit series.yaml.")
    if any(kind == "callout" for chapter in chapters for kind, _ in chapter["blocks"]):
        notes.append("The preface still has a BEFORE YOU PUBLISH note. Replace it with your own words, then rebuild.")
    return notes


def main() -> int:
    series, book, chapters = load_book()
    print(f"Manuscript words: {word_count(chapters)}")
    _, page_map = render(series, book, chapters, None)
    pdf, confirmed = render(series, book, chapters, page_map)
    if confirmed != page_map:
        print("WARNING: contents page numbers shifted between passes. Rebuild layout before sharing.")
    out = ROOT / "dist" / "pdf" / "The-Agent-Loop.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(out))
    handout = build_handout(series, book)
    print(f"Wrote {out}")
    print(f"Wrote {handout}")
    for note in warnings_for(series, chapters):
        print(f"WARNING: {note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
