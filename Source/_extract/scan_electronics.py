import fitz
from pathlib import Path
from collections import defaultdict

PDF_DIR = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\PDF")
OUT = Path(r"C:\Users\admin\Desktop\Shadowrun\Source\_extract")
OUT.mkdir(parents=True, exist_ok=True)

TERMS = [
    "commlink", "Commlink", "cyberdeck", "Cyberdeck", "sim module", "simrig",
    "trodes", "Trodes", "datajack", "Datajack", "RFID", "tag eraser",
    "jammer", "Jammer", "white noise", "bug scanner", "micro-transceiver",
    "micro transceiver", "transceiver", "datatap", "data tap", "datapocket",
    "AR gloves", "AR gloves", "electronics", "Electronics", "Device Rating",
    "Meta Link", "Sony Emperor", "Renraku Sensei", "Erika Elite", "Hermes Ikon",
    "Transys Avalon", "Fairlight Caliban", "hot-sim", "cold-sim", "simsense",
    "PAN", "noise", "Noise", "signal scrub", "firewall", "Firewall",
    "credstick", "Credstick", "certified credstick", "fake SIN",
    "sequencer", "maglock", "keycard", "passkey", "electronics kit",
    "satellite link", "Satellite Link", "retrans", "area jammer",
    "directional jammer", "headjammer", "stealth tag", "security tag",
    "sensor tag", "datachip", "optical chip", "holographic", "printer",
    "scanner", "biometric", "cyberware scanner", "MAD", "millimeter",
    "camera", "microphone", "subvocal", "earbuds", "contacts", "glasses",
    "goggles", "monocle", "binoculars", "vision enhancement", "audio enhancement",
    "image link", "smartlink", "low-light", "thermographic", "ultrasound",
    "drone",  # skip mostly
]

# Focus search for electronics chapter markers
FOCUS = [
    "commlink", "sim module", "trodes", "RFID", "jammer", "tag eraser",
    "bug scanner", "micro-transceiver", "data tap", "AR gloves",
    "credstick", "electronics", "Device Rating", "white noise generator",
    "satellite link", "sequencer", "Meta Link", "Fairlight", "Hermes Ikon",
    "headjammer", "stealth tags", "security tags", "sensor tags",
]

for pdf in sorted(PDF_DIR.glob("*.pdf")):
    doc = fitz.open(pdf)
    hits = defaultdict(list)
    tableish = []
    for i in range(doc.page_count):
        t = doc.load_page(i).get_text("text")
        low = t.lower()
        medical = False
        for term in FOCUS:
            if term.lower() in low:
                hits[term].append(i + 1)
                medical = True
        if medical and (("AVAIL" in t or "Avail" in t) and ("COST" in t or "Cost" in t or "¥" in t)):
            # further filter: electronics-ish
            if any(x in low for x in ["commlink", "jammer", "trode", "rfid", "sim module", "electronics", "credstick", "tag eraser", "bug scanner", "transceiver", "data tap", "ar gloves", "noise", "sequencer", "satellite"]):
                tableish.append(i + 1)
    interesting = {k: v for k, v in hits.items() if v}
    if not interesting:
        continue
    print(f"\n=== {pdf.name} tableish={tableish[:40]} ===")
    for k, v in sorted(interesting.items(), key=lambda x: -len(x[1]))[:25]:
        print(f"  {k}: {v[:20]}")
