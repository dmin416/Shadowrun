import fitz
from pathlib import Path

OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")

def dump(path, pages, out_name):
    doc = fitz.open(path)
    chunks = []
    for p in pages:
        if 1 <= p <= doc.page_count:
            chunks.append(f"\n\n===== {Path(path).name} PDF {p} =====\n")
            chunks.append(doc.load_page(p - 1).get_text("text"))
    (OUT / out_name).write_text("".join(chunks), encoding="utf-8")
    print(out_name, len(pages))

core = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\shadowrunfiftheditioncorerulebook_V2.pdf"
dt = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\datatrails.pdf"
kc = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\killcode.pdf"
rng = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\runandgun.pdf"

# Find Core electronics start
doc = fitz.open(core)
for i in range(doc.page_count):
    t = doc.load_page(i).get_text("text")
    if "Meta Link" in t and "Fairlight Caliban" in t and "Sim module" in t:
        print("Core commlinks PDF", i + 1)
        dump(core, list(range(i, i + 12)), "elec_core.txt")
        break

# DT TOC-ish
doc = fitz.open(dt)
print("DT pages", doc.page_count)
toc = doc.get_toc()
for t in toc:
    print(t)

dump(dt, list(range(55, 70)), "elec_dt.txt")
dump(kc, list(range(49, 78)), "elec_kc.txt")
# RnG weapon-mounted commlink?
dump(rng, [52, 53, 54], "elec_rng_weapon.txt")
