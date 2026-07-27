from pypdf import PdfReader
from pathlib import Path

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\_extract")


def dump(pdf: str, start: int, end: int, out_name: str) -> None:
    r = PdfReader(pdf)
    parts = []
    for i in range(start - 1, min(end, len(r.pages))):
        t = r.pages[i].extract_text() or ""
        parts.append(f"\n===== PAGE {i + 1} =====\n{t}")
    out = OUT / out_name
    out.write_text("".join(parts), encoding="utf-8")
    print(out_name, "chars", sum(len(p) for p in parts), "pages", start, "-", min(end, len(r.pages)))


dump(
    r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\runandgun.pdf",
    28,
    52,
    "rng_firearms.txt",
)
dump(
    r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\streetlethal.pdf",
    25,
    72,
    "sl_firearms.txt",
)

# Print RnG TOC firearm-ish lines
r = PdfReader(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\runandgun.pdf")
toc = (r.pages[1].extract_text() or "") + "\n" + (r.pages[2].extract_text() or "")
print("---TOC---")
for line in toc.splitlines():
    u = line.upper()
    keys = (
        "PISTOL",
        "SMG",
        "RIFLE",
        "SHOT",
        "MACHINE",
        "CANNON",
        "LASER",
        "FLAME",
        "TASER",
        "HOLD",
        "ASSAULT",
        "SNIPER",
        "SPECIAL",
        "SUBMACHINE",
        "HEAVY",
        "LIGHT",
        "LAUNCH",
        "GUN",
        "WEAPON",
    )
    if any(k in u for k in keys):
        print(line)
