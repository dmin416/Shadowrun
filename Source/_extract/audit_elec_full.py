import fitz
from pathlib import Path
from collections import defaultdict

PDF_DIR = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")

# Names / phrases that indicate purchasable electronics SKUs
NEEDLES = [
    "Meta Link", "Sony Emperor", "Renraku Sensei", "Erika Elite", "Hermes Ikon",
    "Transys Avalon", "Fairlight Caliban", "Sim module", "hot-sim",
    "EvoTech Himitsu", "Evotech Himitsu", "Blue Defender", "Sekretär", "Sekretar",
    "Liebesekretär", "Attack dongle", "Stealth dongle", "Stun dongle", "Cable tap",
    "Receiver", "AR Gloves", "Biometric reader", "Electronic paper", "Satellite link",
    "Simrig", "Subvocal", "Trid projector", "Trodes", "Trode Patch",
    "Bug scanner", "Data tap", "Headjammer", "Jammer, area", "Jammer, directional",
    "Micro-transceiver", "Tag eraser", "White noise", "Security Tags", "Stealth Tags",
    "Sensor Tags", "Datachip", "Standard Tags", "Datasoft", "Mapsoft", "Shopsoft",
    "Tutorsoft", "Activesoft", "Knowsoft", "Linguasoft",
    "Faceless", "Booster cloud", "Booster Chip", "MOS", "DumDum", "Douser",
    "CoS", "Fuzzy grenade", "Fuzzy", "PANICBUTTON", "Theme Music", "Ticker",
    "Diagnostics", "P2.1", "AR Games", "electronic parts", "Persona Firmware",
    "Fairlight Paladin", "Radio Shack PCD", "credstick", "Fake SIN",
    "sequencer", "maglock", "passkey", "keycard", "guncam", "commlink",
    "weapon form factor", "Non-standard Form Factor",
    "Patch Cover", "Custom Case", "Brute Force", "Data Spike",
    "Induction Receiver", "Vectored Signal Filter", "Program Carrier",
    "Overwatch Mask", "Hardening", "Self-Destruct", "Multidimensional",
    "datajack plus", "Datajack Plus", "Biolink", "retrans", "Retrans",
    "signal scrub", "Signal Scrub", "browse", "Browse",
    "Agent (Rating", "Cyberprogram",
]

for pdf in sorted(PDF_DIR.glob("*.pdf")):
    doc = fitz.open(pdf)
    found = defaultdict(list)
    for i in range(doc.page_count):
        t = doc.load_page(i).get_text("text")
        for n in NEEDLES:
            if n.lower() in t.lower():
                found[n].append(i + 1)
    if not found:
        continue
    # only print if has table-ish pages with yen near electronics
    print(f"\n=== {pdf.name} ===")
    for k, v in sorted(found.items(), key=lambda x: -len(x[1]))[:30]:
        print(f"  {k}: {v[:15]}")
