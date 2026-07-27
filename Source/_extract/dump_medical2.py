import fitz
from pathlib import Path

OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")
cf = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\chromeflesh.pdf"
r5 = r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\rigger5.pdf"
doc = fitz.open(cf)

# trauma control system pages
for i in range(doc.page_count):
    t = doc.load_page(i).get_text("text")
    if "trauma control" in t.lower() or "Trauma Control" in t:
        print("trauma control on PDF", i+1)

# Valkyrie cost table in R5
doc2 = fitz.open(r5)
for i in range(doc2.page_count):
    t = doc2.load_page(i).get_text("text")
    if "Valkyrie" in t:
        print("Valkyrie on R5 PDF", i+1)

# dump CF trauma + clinics end + competitor contracts
chunks = []
for p in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 148, 149, 150]:
    chunks.append(f"\n\n===== PDF page {p} =====\n")
    chunks.append(doc.load_page(p-1).get_text("text"))
(OUT / "med_cf_docwagon2.txt").write_text("".join(chunks), encoding="utf-8")

# dump Valkyrie table pages
chunks = []
for i in range(doc2.page_count):
    t = doc2.load_page(i).get_text("text")
    if "Valkyrie" in t and ("AVAIL" in t or "COST" in t or "Avail" in t or "Cost" in t or "Modification" in t):
        chunks.append(f"\n\n===== PDF page {i+1} =====\n")
        chunks.append(t)
(OUT / "med_r5_valkyrie.txt").write_text("".join(chunks), encoding="utf-8")
print("done")
