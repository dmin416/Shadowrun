import fitz
from pathlib import Path
from collections import defaultdict

PDF_DIR = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")

# Broad medical-related terms that often sit near gear tables
TERMS = [
    "medkit", "biomonitor", "slap patch", "stim patch", "trauma patch",
    "antidote patch", "tranq patch", "chem patch", "disposable syringe",
    "DocWagon", "CrashCart", "Savior", "Valkyrie", "MediCart", "autodoc",
    "CodeBlue", "First Aid", "paramedic", "resuscitat", "stabiliz",
    "surgical", "clinic", "ambulance", "defibrill", "tourniquet",
    "bandage", "stretcher", "gurney", "IV ", "blood pack", "plasma",
    "morphine", "antibiotic", "disinfectant", "anesthetic", "scalpel",
    "sutur", "trauma bag", "medical kit", "medical gear", "biotech",
    "HolePatcher", "Aesculapius", "WagonWheel", "PharmaFarm",
    "auto-injector", "auto injector", "injector", "syringe",
    "Doc Wagon", "Crash Cart", "Medi Cart", "trauma control",
    "built-in medkit", "builtin medkit", "medical supplies",
    "medkit supplies", "Savior medkit", "nanite medic", "implant medic",
]

pdfs = sorted(PDF_DIR.glob("*.pdf"))
print("PDFs:", [p.name for p in pdfs])

# For each PDF, find pages with AVAIL/COST tables near medical terms
for pdf in pdfs:
    doc = fitz.open(pdf)
    hits = defaultdict(list)
    tableish = []
    for i in range(doc.page_count):
        t = doc.load_page(i).get_text("text")
        low = t.lower()
        medical = False
        for term in TERMS:
            if term.lower() in low:
                hits[term].append(i + 1)
                medical = True
        if medical and (("AVAIL" in t or "Avail" in t) and ("COST" in t or "Cost" in t or "¥" in t or "nuyen" in low)):
            tableish.append(i + 1)
    interesting = {k: v for k, v in hits.items() if v}
    if not interesting:
        continue
    print(f"\n=== {pdf.name} ({doc.page_count}p) tableish={tableish} ===")
    for k, v in sorted(interesting.items(), key=lambda x: -len(x[1])):
        print(f"  {k}: {v[:25]}{'...' if len(v)>25 else ''}")
