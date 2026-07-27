# -*- coding: utf-8 -*-
out = r"c:\Users\admin\Desktop\Shadowrun\Encyclopedia\Identity and Documentation.md"

text = r'''# Identity and Documentation

Agent reference (SR5). LLM layout; full mechanical detail; no flavor.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `runfaster.pdf` · `stolensouls.pdf`
**Books:** Core · RF · SS
**Printed:** Core Identification (GM Advice) ~PDF 371-373 (print ~366-368); Core Street Gear ID and Credit ~PDF 447-448 (print ~442-443); Device Ratings ~PDF 239 (print ~234); Availability/licenses ~PDF ~419; SINner quality ~PDF 89 (print ~84); RF Pack Your Kit Core/Lifestyle PACKs ~PDF 230-231 / 246-247 (print ~228-229 / 244-245); SS Extractor's Toolkit disguises/mods tables ~PDF 188 (print ~186)
**See also:** `Encyclopedia/Commlinks and Electronics.md` (RFID, Device Ratings, commlink as SIN host) · `Encyclopedia/Tools Kits and Survival.md` (full Runner/Bug-Out PACK contents) · `Encyclopedia/Medical Gear.md` (Fake DocWagon wrist band) · `Encyclopedia/Lifestyles and Safehouses.md` (banking via Low+) · `Encyclopedia/Vehicle and Drone Modifications.md` (morphing plate / spoof chip / SS light bars: vehicle identity) · `Encyclopedia/Security and Surveillance.md` (keycards / access) · `Encyclopedia/Armor and Clothing.md` (SS uniforms)

**Scope:** Fake SINs, fake licenses, certified credsticks, credit-account rules, SIN verification/burn, legal-license framework, RF PACKs that bundle Fake SIN/credstick, SS forger services + Fake DocWagon band (ID/disguise).
**Not here:** SINner quality full chargen essay (summary only); DIY Forgery skill craft (pointer); passport/visa as separate SKUs (none printed); vehicle spoof/plates; RFID catalog (Electronics); DocWagon contracts (Medical); lifestyle month PACKs without SIN (Lifestyles / Tools).

## Inventory (completeness checklist)

**Core Credsticks (5):** Standard; Silver; Gold; Platinum; Ebony
**Core Identification (2 formulas):** Fake SIN (R1-6); Fake license (R1-6)
**Core procedures (not SKUs):** Real SIN issue; legal licenses (Item/Magic/Spell Weapon/Technomancy/Occupational); credit account; Fake SIN Rating attributes; SIN verification test + Rating 1-6 checker detail; burned SINs; multi-SIN ops
**Core related (pointer/summary):** SINner (Layered) quality; Device Ratings for checkers; Forgery skill vs bought fakes; Availability R needs license / F none
**RF PACKs with Fake SIN and/or credstick (4):** Intro Runner; Basic Runner; Advanced Runner; Bug-Out Bag
**SS (2 + service):** Fake DocWagon wrist band; Forger services; (Uniforms/Fixer listed as disguise, pointer)
**No local PDF shop SKU:** passport, visa, national ID card, legal license fee table, biometric-sample "extra fee" price

---

## Schema

| Col | Meaning |
| --- | --- |
| Src | Core / RF / SS |
| Cat | Credstick / FakeSIN / FakeLicense / Service / PACK / Quality / Procedure |
| Rating | Device/Fake Rating or `-` |
| Max | Credstick max capacity (nuyen) or `-` |
| Avail / Cost | Street Availability / nuyen (or Karma for PACK buy-with-Karma option) |
| Rules | Full mechanical notes |

---

## Common rules

### System Identification Number (Core ~366-367, 442-443)

- Legal life needs a SIN (country or AA/AAA corp citizenship). Issued at birth (or citizenship change). String encodes name, birth date, place of birth, issuing nation (readable with proper software). Biometrics (DNA, retina, fingerprints) logged with national registry + Corporate Court **Global SIN Registry (GSINR)**.
- No SIN: cannot legally work, buy, or walk "in the system"; SINless = outside.
- SINs are **digital** (commlink / PAN), not physical cards.
- Shadowrunners default SINless unless **SINner** quality. Bought **Fake SIN** is the shop product.

### Fake SIN operations (Core 367, 442-443)

- Rating 1-6 = craft quality vs verification.
- Using a Fake SIN for legitimate activity leaves a datatrail. Criminal use can be traced to that Fake SIN -> disposable.
- Typical loadout: one Fake SIN for legal/lifestyle, one for shady work, optional third for bug-out.
- High-Rating SINs may include matching organic samples (blood/skin/hair) "**if the extra fee is paid**." **No printed fee amount.**
- Street Gear price: Avail `(Rating x 3)F`, Cost `Rating x 2,500¥`.

### Fake SIN Rating attributes (Core Fake SIN Details table, print ~367)

| Rating | Attributes |
| --- | --- |
| 1 | Random anybody; age/nationality/sex may not match; no supporting data |
| 2 | Rough match; sex matches; age and nationality "pretty close"; no supporting data |
| 3 | Good match; sex, age, nationality match; supporting data but obviously fake |
| 4 | Casually plausible; sex/age/nationality match; supporting data valid only on cursory checks |
| 5 | Good fit; all statistics match; valid biometrics for another person (with samples); some supporting data and history |
| 6 | Alternate life; all statistics match; valid biometrics with samples; complete believable history |

### Checking a Fake SIN (Core 368)

- Checker sophistication = Rating (see SIN Verification Details).
- Test: **Simple Device Rating x 2**, threshold = Fake SIN Rating. Use Device Ratings (Core p.234 / PDF 239) for the verification system's Device Rating.
- Hits **under** threshold: no problem reported.
- Hits **equal** threshold: something "odd"; system recommends further investigation (operator's call whether to dig).
- Hits **over** threshold: SIN reported false; may notify authorities; Fake SIN is **burned**.
- Fake **license** uses the **same** verification procedure with the license's Rating (Core 443).

### SIN Verification Details (what Rating checks; Core 368)

| Checker Rating | What's checked |
| --- | --- |
| 1 | Do you have a SIN? |
| 2 | Basic redundancy check on the number and vital statistics |
| 3 | Redundancy check on number and statistics; query for external data attached to SIN |
| 4 | Verify all vital statistics; external data checked for obvious conflicts; biometric must be present |
| 5 | Full verification and consistency check; biometrics tested against sample |
| 6 | All possible verification; multiple biometric samples must match; random supporting data verified externally |

### Burned SINs (Core 368)

- On failed check (hits > threshold), connected verifier sends emergency report to the **SIN registry of the country where verification occurred**.
- Further use of that Fake SIN **automatically fails**. Abandon it.
- Instant burn is **country-local**. Cross-border data sharing may lag; GM may allow a burned SIN to still work in another country until sync.

### Legal licenses (Core 367; Availability ~419)

- Legal license: application, fee, SIN check, possible certification/training. Details = GM. **No Avail/Cost table.**
- Common legal license types (examples):

| License | Situation |
| --- | --- |
| Item | Any item with Availability **R** |
| Magic | Practice magic; registered Awakened |
| Spell Weapon | Knowledge/use of a **single** Combat spell |
| Technomancy | Registered technomancer; use Resonance abilities |
| Occupational | Registered professional (doctor, nurse, electrician, PI, etc.) |

- Street Gear fake licenses: only for **Restricted** items/activities. **Forbidden** = no license exists. Unmarked Avail = no license needed.
- Each item/activity type = separate license. Examples needing license: hunting (bow and rifle), firearm possession, **concealed carry** (separate from possession), spellcasting, Restricted gear/augs.
- Fake license lives on a Fake SIN and is **bound to that SIN**. If SIN or license is exposed, **the other becomes worthless** (Core Availability text + Street Gear).
- Verify with license Rating via Fake SIN check procedure.

### Credsticks vs credit account (Core 442-443)

- **Certified credstick:** Bearer cash. Not registered to a person. Not wireless: must **slot UDC** to move funds. Untraceable; can be physically stolen. Max Value = capacity ceiling, not loaded balance. Stick Device Rating example: Cutting Edge / **DR 5** (Device Ratings table).
- **Credit account:** Online bank via commlink; passcode or biometric. Hard to physically steal; leaves paper trail. Must be registered to a (usually fake) SIN unless anonymous underworld bank (own risks). Banking cost **included in Low lifestyle or better**; else keep money on sticks. **Not a priced SKU.**

### Forgery skill vs shop Fake SINs (Core Skills ~145)

- Forgery can craft documents/SINs/credsticks. **Data forgeries fail when used** (fund transfer, pass SIN check, etc.). Bought Fake SINs are the intended working syndicate product with Rating vs checkers. Do not treat Forgery Extended Tests as equivalent to purchased Fake SIN rows.

### Device Ratings reminder (Core 234; for checkers)

| Category | DR | Examples (excerpt) |
| --- | --- | --- |
| General purpose / consumer | 1-2 | Public terminals, cheap gear |
| ... | 3-4 | Security-grade |
| Cutting Edge | 5 | Deltaware, **credsticks**, black-ops vehicles/security |
| Bleeding Edge | 6 | Experimental |

GM picks verifier Device Rating by venue (Stuffer Shack vs border), not "always 5 because credsticks are 5."

---

## Credsticks (Core Street Gear)

| Name | Src | Cat | Max | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- |
| Standard certified credstick | Core | Credstick | 5,000¥ | - | 5¥ | Bearer; slot UDC; untraceable; stealable. Cost = stick only. |
| Silver certified credstick | Core | Credstick | 20,000¥ | - | 20¥ | As Standard. |
| Gold certified credstick | Core | Credstick | 100,000¥ | 5 | 100¥ | As Standard. |
| Platinum certified credstick | Core | Credstick | 500,000¥ | 10 | 500¥ | As Standard. |
| Ebony certified credstick | Core | Credstick | 1,000,000¥ | 20 | 1,000¥ | As Standard. |

---

## Identification gear (Core Street Gear)

| Name | Src | Cat | Rating | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- |
| Fake SIN | Core | FakeSIN | 1-6 | (R x 3)F | R x 2,500¥ | Digital ID on commlink/PAN. Rating vs SIN check (Device Rating x 2, threshold = Rating). Attributes per Fake SIN Details. Datatrail on use; disposable if burned. Optional organic samples at high Rating for unlisted extra fee. |
| Fake SIN (Rating 1) | Core | FakeSIN | 1 | 3F | 2,500¥ | Expanded buy row. Attributes: Rating 1 row above. |
| Fake SIN (Rating 2) | Core | FakeSIN | 2 | 6F | 5,000¥ | |
| Fake SIN (Rating 3) | Core | FakeSIN | 3 | 9F | 7,500¥ | |
| Fake SIN (Rating 4) | Core | FakeSIN | 4 | 12F | 10,000¥ | |
| Fake SIN (Rating 5) | Core | FakeSIN | 5 | 15F | 12,500¥ | Biometrics + samples (extra fee unlisted). |
| Fake SIN (Rating 6) | Core | FakeSIN | 6 | 18F | 15,000¥ | Full alternate life + samples (extra fee unlisted). |
| Fake license | Core | FakeLicense | 1-6 | (R x 3)F | R x 200¥ | Restricted only; Forbidden = none. One type per license; bind to one Fake SIN. Verify with license Rating (same check procedure). Linked: expose SIN or license -> other worthless. |
| Fake license (Rating 1) | Core | FakeLicense | 1 | 3F | 200¥ | Expanded buy row. |
| Fake license (Rating 2) | Core | FakeLicense | 2 | 6F | 400¥ | |
| Fake license (Rating 3) | Core | FakeLicense | 3 | 9F | 600¥ | |
| Fake license (Rating 4) | Core | FakeLicense | 4 | 12F | 800¥ | |
| Fake license (Rating 5) | Core | FakeLicense | 5 | 15F | 1,000¥ | |
| Fake license (Rating 6) | Core | FakeLicense | 6 | 18F | 1,200¥ | |

---

## Stolen Souls (Extractor's Toolkit)

| Name | Src | Cat | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Fake DocWagon wrist band | SS | FakeLicense/Disguise | 10F | 100¥ | Counterfeit DocWagon contract band for medic disguise ops. Also cataloged in Medical Gear. Pair with uniforms / medkits / gurney / counterfeit ambulance (Vehicles / Vehicle Modifications). |
| Forger services | SS | Service | - | 500¥+ | Per document; complexity and security features raise price. Open-ended. Matches SS prose "500¥ per document and up." |
| Uniforms | SS | Disguise | 16F | 2,000-15,000¥ | LE/medic/etc. costume. Not a SIN. Full kit sourcing often via Fixer. -> Armor and Clothing / Identity ops. |
| Fixer services (disguise) | SS | Service | - | 250¥/hour | Costume/badge/kit sourcing for authority disguises. |

---

## RF PACKs containing Fake SIN / credstick

Full PACK item lists -> `Encyclopedia/Tools Kits and Survival.md`. ID-relevant contents only here. Nuyen evenly divisible by 2,000; may buy with listed Karma at chargen.

| Name | Src | Cat | Cost / Karma | Avail | ID / cred contents | Rules |
| --- | --- | --- | --- | --- | --- | --- |
| Intro Runner PACK | RF | PACK | 4,000¥ / 2 Karma | - | Fake SIN (1); Standard credstick | Rookie bundle; SIN "barely functional" for pizza/dive, fails real scrutiny. |
| Basic Runner PACK | RF | PACK | 10,000¥ / 5 Karma | - | Fake SIN (3); Silver credstick | Professional baseline. |
| Advanced Runner PACK | RF | PACK | 20,000¥ | 12F | Fake SIN (4); Gold credstick | Veteran bundle. |
| Bug-Out Bag | RF | PACK | 4,000¥ / 2 Karma | 4F | Fake SIN (1); Standard credstick **pre-loaded 1,000¥**; 10 security tags | Dump-life bag; SIN for slum rent; tags -> Electronics RFID. |

Lifestyle-only PACKs (Street Rat, Lowlife, Success in the Shadows, High Life): no Fake SIN SKU -> Lifestyles / Tools.

---

## SINner quality (summary; Core p.84)

Not a shop SKU. Chargen negative quality **SINner (Layered)** 5-25 Karma:

| Tier | Karma | Notes (abbrev) |
| --- | --- | --- |
| National SIN | 5 | Citizen; vote/passport/military/gov eligible; **15%** gross income tax; biometrics in GSINR; always legally broadcast SIN |
| Criminal SIN | 10 | Replaces prior SIN; must broadcast Criminal SIN; felony to hide; social/legal penalties; questioning holds |
| Corporate Limited SIN | 15 | Megacorp outsider hire; often replaces National; in GSINR; may flag Awakened |
| Corporate Born | 25 | (see Core quality text for full Born rights/drawbacks) |

Legal purchases require a legal SIN (or working Fake SIN). Full writeup stays in chargen/qualities docs if present.

---

## Print gaps / conflicts

- **Biometric sample "extra fee"** for high Fake SINs: mentioned, no Cost.
- **Legal license fees / process:** GM only; no table.
- **Passport / visa SKUs:** none in local PDFs (National SIN grants passport *rights*).
- **Forgery skill DIY data** fails on use vs purchased Fake SIN Ratings that work until burned.
- **Fake DocWagon wrist band:** listed here and in Medical Gear (dual catalog by design).
- **CF DocWagon temporary/debt SIN:** narrative; not a Fake SIN buy row.
- **Device Rating:** credsticks listed DR 5; SIN checkers use venue-appropriate Device Rating, not automatic 5.

---

## Item index

Advanced Runner PACK; Basic Runner PACK; Bug-Out Bag; Certified credstick (Standard/Silver/Gold/Platinum/Ebony); Credit account (procedure); Fake DocWagon wrist band; Fake license (R1-6); Fake SIN (R1-6); Fixer services (SS disguise); Forger services; Intro Runner PACK; Legal licenses (Item/Magic/Spell Weapon/Technomancy/Occupational); SIN verification; SINner quality; Uniforms (SS).
'''

text = text.replace("\u2014", "-").replace("—", "-").replace("–", "-")
with open(out, "w", encoding="utf-8", newline="\n") as f:
    f.write(text)
print("wrote", out, "lines", text.count("\n") + 1)
