# -*- coding: utf-8 -*-
"""Debug deinterleave on Arsenal opening."""
from pathlib import Path
import importlib.util

spec = importlib.util.spec_from_file_location(
    "di", r"c:\Users\admin\Desktop\Shadowrun\Source\_extract\deinterleave_rng.py"
)
di = importlib.util.module_from_spec(spec)
spec.loader.exec_module(di)

path = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Run and Gun\05 - Arsenal.md")
lines = path.read_text(encoding="utf-8").splitlines()
# find heart / of an enemy
for i, ln in enumerate(lines[:60]):
    if "heart" in ln.lower() or ln.startswith("of an") or ln.strip() == "ACC":
        print(i, "inc", di.is_incomplete(ln), "cont", di.is_continuation(ln), "caps", di.is_allcaps_title(ln), "stat", di.is_statish(ln))
        print("   ", repr(ln[:100]))

# simulate scan at 'of an enemy'
idx = next(i for i, ln in enumerate(lines) if ln.startswith("of an enemy"))
print("continuation at", idx)
out = lines[:idx]
inc_idx = None
seen_stats = False
for j in range(len(out) - 1, -1, -1):
    s = out[j]
    flags = []
    if di.is_blank(s):
        continue
    if di.is_heading(s) or di.is_source(s):
        print("stop heading", j); break
    if di.is_statish(s) or di.is_allcaps_title(s):
        seen_stats = True
        print(j, "skip stat/caps", repr(s[:40]), "seen_stats", seen_stats)
        continue
    if di.is_comment_marker(s):
        print(j, "skip comment"); continue
    st = s.strip()
    if len(st) < 40 and st and st[0].isupper() and "." not in st and not di.is_incomplete(s):
        print(j, "skip handle", repr(st)); continue
    if di.is_incomplete(s):
        intervening = out[j + 1 :]
        print(j, "INCOMPLETE candidate", repr(s[-60:]), "interv_len", len(intervening), "seen", seen_stats, "looks", di.looks_like_interrupt(intervening))
        if intervening and (seen_stats or di.looks_like_interrupt(intervening)):
            inc_idx = j
        break
    if seen_stats:
        print(j, "complete-in-interrupt", repr(s[:50]))
        continue
    print(j, "STOP complete", repr(s[:50]))
    break
print("inc_idx", inc_idx)
