# -*- coding: utf-8 -*-
"""Create Source Texts folders + INDEX for newly added PDFs."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF_DIR = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF")
ST_DIR = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts")

# New complete PDFs only (skip .crdownload)
NEW = [
    ("better-than-bad-pdf.pdf", "Better Than Bad", "Hooding / runs with a conscience; Pretoria setting."),
    ("Book of the Lost.pdf", "Book of the Lost", "Sixth World Tarot campaign book: plot hooks and adventure seeds."),
    ("Shadowrun_5E_Aetherology.pdf", "Aetherology", "Metaplanes / astral exploration PDF."),
    ("Shadowrun_5E_Assassins_Primer.pdf", "Assassin's Primer", "Assassin character options and wetwork primer."),
    ("Shadowrun_5E_Bullets_&_Bandages.pdf", "Bullets and Bandages", "Medical / combat support gear and rules."),
    ("Shadowrun_5E_Cutting_Aces.pdf", "Cutting Aces", "Cons and social runs; Constantinople."),
    ("Shadowrun_5E_Gun_H(e)aven_3.pdf", "Gun Heaven 3", "Extra weapons catalog (dual-statted era PDF)."),
    ("shadowrun-lockdown-pdf.pdf", "Lockdown", "Boston quarantine / CFD plot sourcebook."),
    ("shadow-spells-pdf.pdf", "Shadow Spells", "Extra spells, adept powers, and rituals."),
]


def safe_filename(title: str, n: int) -> str:
    t = title.strip()
    t = re.sub(r'[<>:"/\\|?*]', "", t)
    t = re.sub(r"\s+", " ", t)
    t = t.replace(":", " -")
    if len(t) > 80:
        t = t[:77].rstrip() + "..."
    return f"{n:02d} - {t}.md"


def toc_entries(pdf_path: Path) -> list[tuple[str, int]]:
    doc = fitz.open(pdf_path)
    toc = doc.get_toc() or []
    pages = doc.page_count
    doc.close()
    # Prefer top-level (lvl 1) entries; if few, include lvl 2
    top = [(t, p) for lvl, t, p in toc if lvl == 1]
    if len(top) < 3:
        top = [(t, p) for lvl, t, p in toc if lvl <= 2]
    # Dedupe consecutive same titles
    out: list[tuple[str, int]] = []
    for title, page in top:
        title = re.sub(r"\s+", " ", title).strip()
        if not title:
            continue
        if out and out[-1][0].lower() == title.lower():
            continue
        out.append((title, page))
    return out, pages


def write_book(pdf_name: str, folder_name: str, blurb: str) -> None:
    pdf_path = PDF_DIR / pdf_name
    folder = ST_DIR / folder_name
    folder.mkdir(parents=True, exist_ok=True)

    entries, pages = toc_entries(pdf_path)

    lines = [
        f"# {folder_name}",
        "",
        blurb,
        "",
        f"**PDF:** `Source/PDF/{pdf_name}` ({pages} pages).",
        "",
        "## Sections",
        "",
    ]

    if not entries:
        lines.append("_No PDF outline/TOC detected. Add chapter stubs after extract._")
        lines.append("")
    else:
        for i, (title, page) in enumerate(entries, start=1):
            fname = safe_filename(title, i)
            # stub file
            stub = folder / fname
            if not stub.exists():
                stub.write_text(
                    f"# {title}\n\n"
                    f"**Source:** {folder_name} | `Source/PDF/{pdf_name}` | "
                    f"print page ~{page}\n\n",
                    encoding="utf-8",
                )
            link = fname.replace(" ", "%20")
            lines.append(f"{i}. [{title}]({link}) (p. {page})")
        lines.append("")

    lines += [
        "## Pipeline status",
        "",
        "- [ ] Extract",
        "- [ ] Format",
        "- [ ] Loss-check",
        "- [ ] Done-check",
        "",
    ]

    (folder / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"OK {folder_name}: {len(entries)} sections, {pages} pages")


def main() -> None:
    for pdf_name, folder, blurb in NEW:
        if not (PDF_DIR / pdf_name).exists():
            print("MISSING PDF", pdf_name)
            continue
        write_book(pdf_name, folder, blurb)

    # Note incomplete download
    cr = list(PDF_DIR.glob("*.crdownload"))
    if cr:
        print("SKIP incomplete:", ", ".join(c.name for c in cr))


if __name__ == "__main__":
    main()
