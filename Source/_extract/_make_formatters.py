# -*- coding: utf-8 -*-
from pathlib import Path

base = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\_extract")
src = (base / "format_forbiddenarcana.py").read_text(encoding="utf-8")

# Find OUT line and replace
specs = [
    ("format_runfaster.py", "Run Faster", "RUN FASTER", r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Run Faster"),
    ("format_streetlethal.py", "Street Lethal", "STREET LETHAL", r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Street Lethal"),
    ("format_howlingshadows.py", "Howling Shadows", "HOWLING SHADOWS", r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Howling Shadows"),
]

for fname, title, banner, out in specs:
    t = src.replace("Forbidden Arcana", title).replace("FORBIDDEN ARCANA", banner)
    lines = []
    for ln in t.splitlines():
        if ln.startswith("OUT = Path("):
            lines.append(f'OUT = Path(r"{out}")')
        else:
            lines.append(ln)
    (base / fname).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote", fname)
