import fitz
from pathlib import Path

OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")
OUT.mkdir(parents=True, exist_ok=True)

def dump(path, pages, out_name):
    doc = fitz.open(path)
    chunks = []
    for p in pages:
        i = p - 1
        if 0 <= i < doc.page_count:
            chunks.append(f"\n\n===== PDF page {p} =====\n")
            chunks.append(doc.load_page(i).get_text("text"))
    (OUT / out_name).write_text("".join(chunks), encoding="utf-8")
    print(out_name, "wrote", len(pages), "pages")

cf = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\chromeflesh.pdf"
r5 = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\rigger5.pdf"
rf = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\runfaster.pdf"
rng = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\runandgun.pdf"
core = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\shadowrunfiftheditioncorerulebook_V2.pdf"
ss = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\stolensouls.pdf"

# Find Core Biotech by searching printed page markers / text
doc = fitz.open(core)
for i in range(doc.page_count):
    t = doc.load_page(i).get_text("text")
    if "Disposable syringe" in t and "Medkit" in t and "Biomonitor" in t:
        print("Core biotech PDF page", i + 1)
        dump(core, list(range(i, i + 4)), "med_core_biotech.txt")
        break

dump(cf, list(range(27, 40)), "med_cf_docwagon.txt")
dump(cf, [83, 86, 87, 90, 155, 223, 225, 227, 237], "med_cf_gear.txt")
dump(r5, [142, 143, 144, 167], "med_r5_medicart.txt")
dump(rf, [42, 43, 44, 162, 163, 164, 192, 247, 248], "med_rf_refs.txt")
dump(rng, [81, 83, 84, 85, 87], "med_rng_refs.txt")
dump(ss, [133, 134, 174, 175], "med_ss_refs.txt")
