# -*- coding: utf-8 -*-
import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\Shadowrun_5E_Hard_Targets.pdf")
folder = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Hard Targets")
folder.mkdir(parents=True, exist_ok=True)

doc = fitz.open(PDF)
pages = doc.page_count
toc = doc.get_toc() or []
doc.close()
print("pages", pages, "toc", len(toc))
for lvl, title, page in toc[:40]:
    print(lvl, page, title)

top = [(t, p) for lvl, t, p in toc if lvl == 1]
if len(top) < 3:
    top = [(t, p) for lvl, t, p in toc if lvl <= 2]

entries = []
for title, page in top:
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
    "# Hard Targets",
    "",
    "Wetwork guide: assassination trade, Havana, wetwork gear and character options.",
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
            f"**Source:** Hard Targets | `Source/PDF/{PDF.name}` | print page ~{page}\n\n",
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
