# Kill Code per-chapter sweep report

Checked 2026-07-26 vs `Source/PDF/killcode.pdf`.

**Method:** size ratio vs PDF page span; landmark presence (TOC gear/rules/critters); JackPoint handle order (`> **Handle**` then `> body`); em/en dash + ellipsis scan; table/cost spot checks; no next-chapter bleed.

**Fix this pass:** Ch13 Null Sign had all 44 JackPoint comments inverted (body before handle). Flipped to project convention.

| # | Chapter | Loss | Notes |
| --- | --- | --- | --- |
| 01 | Contents and Credits | PASS | Summary TOC + credits (detailed TOC lives in PDF only, matching Chrome Flesh style) |
| 02 | Introduction | PASS | |
| 03 | Double Decker | PASS | Fiction; intentional OCR cleanups (lorries, pierced, etc.) |
| 04 | So You Want To Be A Hacker | PASS | JP 57/57; all 11 new Matrix actions; Patrol IC OS paragraph present; Denial of Service print test mismatch noted |
| 05 | Dips & Chips | PASS | JP 91/91; Zapper/Datajack costs match; summary tables present |
| 06 | Disk Jockeys & Lightstream Riders | PASS | Qualities + Life Modules; intro mentions complex forms but none on pp.76-81 (noted) |
| 07 | Parallel Processing | PASS | Amy Veeres fiction |
| 08 | Data Streams | PASS | Sourcerers/Sourcerors spelling split preserved; stream CFs present |
| 09 | In the Flow | PASS | CFs, qualities, sprites, echoes, paragons |
| 10 | A Million Icons Bloom | PASS | Strictures + sample tribes + flash tribes |
| 11 | Diving Under | PASS | |
| 12 | Infinite Realms | PASS | Realms + Dissonant streams rules |
| 13 | Null Sign | PASS | JP order fixed this sweep (44 comments) |
| 14 | Into the Wild | PASS | |
| 15 | The Core of Consciousness | PASS | All critter landmarks; Power Munger W20/C30 print paste quirk preserved |
| 16 | Rule Index | PASS | Category tables; decks under Gear (print has no separate Cyberdecks heading); Force Heuristics matches print index spelling |

**Book verdict:** No chapter is missing substantial body text. Residual work is optional polish only (more heading promotions inside long ch04/ch05 blocks), not content recovery.

Scripts: `Source/_extract/killcode_sweep.py`, `Source/_extract/killcode_landmark_sweep.py`.
