# -*- coding: utf-8 -*-
import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\pdfcoffee.com_shadowrun-5e-splintered-state-pdf-free.pdf")
folder = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Splintered State")
folder.mkdir(parents=True, exist_ok=True)

doc = fitz.open(PDF)
pages = doc.page_count
toc = doc.get_toc() or []
doc.close()
print("pages", pages, "toc", len(toc))

entries = []
for lvl, title, page in toc:
    if lvl != 1:
        continue
    title = re.sub(r"\s+", " ", title).strip()
    if not title:
        continue
    if entries and entries[-1][0].lower() == title.lower():
        continue
    entries.append((title, page))
print("sections", len(entries))


def safe(title: str, n: int) -> str:
    t = re.sub(r'[<>:"/\\|?*]', "", title.strip())
    t = re.sub(r"\s+", " ", t).replace(":", " -")
    if len(t) > 80:
        t = t[:77].rstrip() + "..."
    return f"{n:02d} - {t}.md"


lines = [
    "# Splintered State",
    "",
    "Adventure: Seattle politics, Project Daybreak, and competing interests around Seth Dietrich.",
    "",
    f"**PDF:** `Source/PDF/{PDF.name}` ({pages} pages).",
    "",
    "## Sections",
    "",
]
for i, (title, page) in enumerate(entries, 1):
    fname = safe(title, i)
    stub = folder / fname
    if not stub.exists():
        stub.write_text(
            f"# {title}\n\n"
            f"**Source:** Splintered State | `Source/PDF/{PDF.name}` | print page ~{page}\n\n",
            encoding="utf-8",
        )
    lines.append(f"{i}. [{title}]({fname.replace(' ', '%20')}) (p. {page})")

lines += [
    "",
    "## Pipeline status",
    "",
    "- [ ] Extract",
    "- [ ] Format",
    "- [ ] Loss-check",
    "- [ ] Done-check",
    "",
]
(folder / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
print("wrote", folder)
print("md files", len(list(folder.glob("*.md"))))
