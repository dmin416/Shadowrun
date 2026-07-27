import fitz
from pathlib import Path

OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")

def search_pdf(path, keys):
    doc = fitz.open(path)
    hits = {k: [] for k in keys}
    for i in range(doc.page_count):
        t = doc.load_page(i).get_text("text")
        low = t.lower()
        for k in keys:
            if k.lower() in low:
                hits[k].append(i + 1)
    return doc.page_count, hits

def dump_pages(path, pages, out_name):
    doc = fitz.open(path)
    chunks = []
    for p in pages:
        i = p - 1
        if 0 <= i < doc.page_count:
            chunks.append(f"\n\n===== PDF page {p} =====\n")
            chunks.append(doc.load_page(i).get_text("text"))
    Path(OUT / out_name).write_text("".join(chunks), encoding="utf-8")

core = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\shadowrunfiftheditioncorerulebook_V2.pdf"
cf = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\chromeflesh.pdf"
r5 = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\rigger5.pdf"
rf = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\runfaster.pdf"
rng = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\runandgun.pdf"
sl = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\streetlethal.pdf"
ss = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\stolensouls.pdf"

keys = [
    "DocWagon", "CrashCart", "CodeBlue", "Savior", "medkit", "biomonitor",
    "MediCart", "autodoc", "slap patch", "trauma patch", "stim patch",
    "antidote patch", "tranq patch", "chem patch", "disposable syringe",
    "Aesculapius", "HolePatcher", "paramedic", "resuscitation",
    "High Threat Response", "built-in medkit", "auto-injector",
]

for label, path in [
    ("CF", cf),
    ("R5", r5),
    ("RF", rf),
    ("RnG", rng),
    ("SL", sl),
    ("SS", ss),
]:
    n, hits = search_pdf(path, keys)
    print(f"\n=== {label} ({n} pages) ===")
    for k, v in hits.items():
        if v:
            print(f"  {k}: {v}")
