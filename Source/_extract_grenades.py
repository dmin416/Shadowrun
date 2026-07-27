from pypdf import PdfReader
from pathlib import Path

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\_extract")


def dump(pdf: str, pages: list[int], name: str) -> None:
    r = PdfReader(pdf)
    parts = []
    for p in pages:
        t = r.pages[p - 1].extract_text() or ""
        parts.append(f"\n===== PAGE {p} =====\n{t}")
    path = OUT / name
    path.write_text("".join(parts), encoding="utf-8")
    print(name, "chars", sum(len(x) for x in parts))


dump(
    r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\runandgun.pdf",
    [100, 101, 102, 103, 104, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198],
    "rng_grenades.txt",
)
dump(
    r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\streetlethal.pdf",
    [43, 44, 64, 65, 66, 67, 74, 75, 76, 77, 132, 133],
    "sl_grenades.txt",
)
