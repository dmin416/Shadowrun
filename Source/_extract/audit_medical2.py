import fitz
from pathlib import Path

OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")

dumps = {
    "med_ss_tables.txt": (r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\stolensouls.pdf", [133, 134, 173, 174, 175, 176, 177, 178, 187, 188, 198]),
    "med_r5_more.txt": (r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\rigger5.pdf", [14, 23, 76, 77, 78, 95, 128, 141, 142, 147, 190]),
    "med_cf_implantmedic.txt": (r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\chromeflesh.pdf", [147, 148, 149, 154, 155]),
    "med_kc_med.txt": (r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\killcode.pdf", [67, 74, 83]),
    "med_rng_space.txt": (r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\runandgun.pdf", [80, 81, 82, 83, 87]),
    "med_fa_valk.txt": (r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\forbiddenarcana.pdf", [69, 84]),
    "med_se_clinic.txt": (r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\serratededge.pdf", [12, 13, 14]),
    "med_core_index_med.txt": (r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\shadowrunfiftheditioncorerulebook_V2.pdf", [474, 475, 476, 477, 490, 493]),
}

for name, (path, pages) in dumps.items():
    doc = fitz.open(path)
    chunks = []
    for p in pages:
        chunks.append(f"\n\n===== {Path(path).name} PDF page {p} =====\n")
        chunks.append(doc.load_page(p - 1).get_text("text"))
    (OUT / name).write_text("".join(chunks), encoding="utf-8")
    print("wrote", name)

# Search for purchasable-looking medical names across all PDFs
needles = [
    "Savior medkit", "MediCart", "Valkyrie", "implant medic",
    "DocWagon Basic", "trauma control", "built-in medkit",
    "CodeBlue", "Aesculapius", "HolePatcher", "Dustoff",
    "Chariot", "ambulance", "paramedic kit", "trauma bag",
    "First Aid kit", "surgical kit", "cyberware kit",
    "cybertechnology kit", "biotech kit", "Medicine shop",
    "autodoc", "MedWagon", "CrashCart",
]
for pdf in sorted(Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF").glob("*.pdf")):
    doc = fitz.open(pdf)
    found = {}
    for i in range(doc.page_count):
        t = doc.load_page(i).get_text("text")
        for n in needles:
            if n.lower() in t.lower():
                found.setdefault(n, []).append(i + 1)
    if found:
        print(f"\n{pdf.name}")
        for k, v in found.items():
            print(f"  {k}: {v[:20]}")
