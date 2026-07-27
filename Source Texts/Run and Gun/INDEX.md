# Run & Gun

Combat core book: weapons, armor, tactics, martial arts, demolitions.

**PDF:** `Source/PDF/runandgun.pdf` (216 pages; print page ≈ PDF page for body text)

Source Texts extracted via `Source/_extract/extract_run_and_gun.py` (pymupdf).

**Pipeline (every chapter):** extract → format → loss-check → done-check

## Chapters

| # | File | PDF idx |
| --- | --- | --- |
| 01 | [Contents and Credits](01%20-%20Contents%20and%20Credits.md) | 1-4 |
| 02 | [Catspaw](02%20-%20Catspaw.md) | 5-8 |
| 03 | [Fight for Your Life](03%20-%20Fight%20for%20Your%20Life.md) | 9-9 |
| 04 | [What You Don't Know Kills You](04%20-%20What%20You%20Don't%20Know%20Kills%20You.md) | 10-16 |
| 05 | [Arsenal](05%20-%20Arsenal.md) | 17-54 |
| 06 | [Armor and Protection](06%20-%20Armor%20and%20Protection.md) | 55-86 |
| 07 | [Tactics and Tools](07%20-%20Tactics%20and%20Tools.md) | 87-104 |
| 08 | [Killshots and More](08%20-%20Killshots%20and%20More.md) | 105-126 |
| 09 | [Martial Arts](09%20-%20Martial%20Arts.md) | 127-141 |
| 10 | [Fixin' All the Broken Drek](10%20-%20Fixin%20All%20the%20Broken%20Drek.md) | 142-142 |
| 11 | [Staying Alive](11%20-%20Staying%20Alive.md) | 143-168 |
| 12 | [Blow Up Good](12%20-%20Blow%20Up%20Good.md) | 169-196 |
| 13 | [Hostile Extraction](13%20-%20Hostile%20Extraction.md) | 197-200 |
| 14 | [Run and Gun Tables](14%20-%20Run%20and%20Gun%20Tables.md) | 201-212 |

Page index 0 is cover art. Pages 213-215 (idx) are copyright / blank; credits live in chapter 01.

## Related

- Encyclopedia gear from RnG is already filled (Firearms, Melee, Armor, Ammo, Accessories, Grenades, etc.)
- Mechanics combat options / martial arts still need these Source Texts

## Pipeline status

- [x] Extract (raw chapter markdown from PDF)
- [x] Format (headings, JackPoint comments, tables; strip leftover headers)
- [x] Loss-check vs PDF (deep audit + one-by-one chapter checks)
- [x] Done-check (see `Source/_extract/rng_chapter_check_report.md`)
