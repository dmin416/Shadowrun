import fitz
from pathlib import Path

# Extract trauma control system full text around p149 CF
cf = fitz.open(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\chromeflesh.pdf")
chunks = []
for p in range(147, 152):
    chunks.append(f"\n\n===== PDF page {p} =====\n")
    chunks.append(cf.load_page(p-1).get_text("text"))
Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract\med_cf_trauma.txt").write_text("".join(chunks), encoding="utf-8")

# Valkyrie cost from R5 page 168
r5 = fitz.open(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\rigger5.pdf")
chunks = []
for p in [167, 168, 169, 170]:
    chunks.append(f"\n\n===== PDF page {p} =====\n")
    chunks.append(r5.load_page(p-1).get_text("text"))
Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract\med_r5_valkyrie2.txt").write_text("".join(chunks), encoding="utf-8")

# Search all PDFs for unique medical SKUs we might have missed
pdfs = {
    "core": r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\shadowrunfiftheditioncorerulebook_V2.pdf",
    "cf": r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\chromeflesh.pdf",
    "r5": r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\rigger5.pdf",
    "rf": r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\runfaster.pdf",
    "rng": r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\runandgun.pdf",
    "sl": r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\streetlethal.pdf",
    "ss": r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\stolensouls.pdf",
    "ht_missing": None,
}
keys = [
    "Savior medkit", "Valkyrie module", "MediCart", "CrashCart",
    "CodeBlue", "WagonWheel", "PharmaFarm", "Aesculapius",
    "HolePatcher", "DroneRx", "Prosperity", "QuetzalCare", "BluSix",
    "BuMoNa", "street doc", "cyberclinic", "body shop",
    "First Aid kit", "paramedic kit", "surgical kit", "autodoc",
    "stabilizer", "defibrillator", "blood pack", "IV drip",
    "medical supplies", "Medkit supplies", "trauma control",
]
for label, path in pdfs.items():
    if not path:
        continue
    doc = fitz.open(path)
    found = {}
    for i in range(doc.page_count):
        t = doc.load_page(i).get_text("text")
        for k in keys:
            if k.lower() in t.lower():
                found.setdefault(k, []).append(i+1)
    print(f"\n== {label} ==")
    for k,v in found.items():
        print(f"  {k}: {v[:15]}")
