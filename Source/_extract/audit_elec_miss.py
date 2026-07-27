import fitz
from pathlib import Path

OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")

# Dump likely miss pages
dumps = {
    "elec_kc_misc2.txt": (r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\killcode.pdf", list(range(68, 80))),
    "elec_rng_comm.txt": (r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\runandgun.pdf", [52, 53, 54, 90]),
    "elec_rf_packs.txt": (r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\runfaster.pdf", [247, 248, 249]),
    "elec_r5_sat.txt": (r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\rigger5.pdf", [168, 169, 170]),
    "elec_dt_voice.txt": (r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\datatrails.pdf", [175, 176, 177, 178, 179]),
    "elec_core_bne.txt": (r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\shadowrunfiftheditioncorerulebook_V2.pdf", [452, 453]),
}

for name, (path, pages) in dumps.items():
    doc = fitz.open(path)
    chunks = []
    for p in pages:
        chunks.append(f"\n\n===== {Path(path).name} p{p} =====\n")
        chunks.append(doc.load_page(p - 1).get_text("text"))
    (OUT / name).write_text("".join(chunks), encoding="utf-8")
    print("wrote", name)

# Search KC for any table item with Avail/Cost we might have missed in dips & chips
kc = fitz.open(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF\killcode.pdf")
print("\nKC chapter gear names with yen near ACCESSORIES or MISC:")
for i in range(48, 80):
    t = kc.load_page(i).get_text("text")
    if "AVAIL" in t and "COST" in t:
        # extract lines after ITEM or GRENADE or TYPE
        lines = t.splitlines()
        for j, line in enumerate(lines):
            if line.strip() in ("ITEM", "GRENADE", "TYPE", "DONGLE", "COMMLINK", "MODULES", "MISC. ITEMS", "AMMO") or "AVAIL" == line.strip():
                print(f"  p{i+1}: context around line {j}: {lines[j:j+15]}")
