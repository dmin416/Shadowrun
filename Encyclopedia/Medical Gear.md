# Medical Gear

Agent reference (SR5). Compact; full mechanical detail; no flavor.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `chromeflesh.pdf` · `rigger5.pdf` · `stolensouls.pdf` · `runandgun.pdf` (spacesuit refill only)
**Books:** Core · CF · R5 · SS · RnG (one refill line)
**Printed:** Core Biotech 450-451; healing/medkit 205-209; CF DocWagon 26-33; nanoware TCS/implant medic 147-148; Savior 154; R5 MediCart 142-143; Valkyrie 166-167; SS Extractor's Toolkit 172-186
**See also:** `Encyclopedia/Drugs Toxins and Chemicals.md` · `Encyclopedia/Cyberware.md` · `Encyclopedia/Nanotech and Geneware.md` · `Encyclopedia/Armor Modifications.md` · `Encyclopedia/Drones.md` · `Encyclopedia/Vehicle and Drone Modifications.md` · `Encyclopedia/Tools Kits and Survival.md` · `Mechanics/Healing and Injuries.md`

**Scope:** purchasable medical devices, supplies, contracts, clinical/extraction medical tools, medical drones/mods, medical nanoware, and medical cyber installs that are first-aid / monitoring / clinic systems.
**Not here:** street drugs/toxins as combat consumables (except saline + liquid nutrients as Houdini medical feeds); street-doc setting essays (CF 33-40, no shop SKUs). B&B biotech gear and Dustoff/CAD-7 drones are cataloged (see below / Drones.md).

## Schema

| Col | Meaning |
| --- | --- |
| Src | Core / CF / R5 / SS / RnG |
| Avail / Cost | Street Availability / nuyen. `-` = none |
| Rules | Full mechanical notes |

## Common rules

### Medkits (Core 450; combat 208-209)

- Contents: drug supplies, bandages, tools, doctor expert system (fractures, gunshot, chemical wounds, poisoning, shock, blood loss, resuscitation).
- Add Rating to **limit** on First Aid tests.
- Size: Rating 1-3 pocket; Rating 4+ handheld case.
- Restock after every (Rating) uses. One **Medkit supplies** = one restock.
- First Aid requires a medkit even if supplies empty.
- Combat: Complex Action to apply/hook up medkit or autodoc, then treat.
- **Wireless on:** +Rating dice to First Aid + Logic; OR unattended pool = Rating x 2, limit = Rating.
- Untrained + wireless medkit: Logic - 1; use device Rating in place of First Aid skill.
- Remote care via Matrix: -2 dice.
- Remotely accessible/controllable via wireless/Matrix.
- Natural recovery can be bolstered by medkits or autodoc drones.

### Autodocs (Core 208-209)

- Autodoc drones rival trained paramedics; same apply/remote rules as medkits.
- Dice pool aid = autodoc First Aid or Medicine **autosoft** (not medkit Rating).
- No Core Street Gear SKU named "Autodoc." Concrete items: MediCart, Valkyrie. Core examples Aesculapius / HolePatcher4000 = ordinary medkits, not separate SKUs.

### Slap patches (Core 450-451)

- Adhesive dermal dispensers; apply to exposed skin.
- Unwilling: melee attack, **no** damage (Called Shots if little skin, Core 195).
- Trauma wireless bonus only while wireless on.

### Disposable syringe (Core 450)

- Single use; injection-vector delivery. Uncooperative: immobilize/grapple first.

### Stabilization (Core 209)

- Dying (Physical overflow): +1 box every (Body) minutes until stabilized or dead (overflow > Body = dead).
- Stabilize: First Aid + Logic [Mental] (3) or Medicine + Logic [Mental] (3); medkits/autodocs may assist.
- Fail: keep dying; retry at cumulative -2 dice per prior attempt.
- Trauma patch wireless off: immediate stabilize test with **Body**.
- Trauma patch wireless on: auto-stabilize, no test.
- Savior (nanites active, bleeding out): acts as trauma control system for duration (see TCS).
- Stabilize spell works; Heal spell does not stabilize.

### Healing Modifiers (medical-gear rows; Core 208)

| Situation | Mod |
| --- | --- |
| Wireless medkit/autodoc | +Rating |
| Care remotely through medkit/autodoc | -2 |
| No medical supplies | -3 |
| Improvised medical supplies | -1 |

### Nanoware medical systems (CF 146-148)

- Nanoware: no Essence; no grades. Rating degrades 1/week without nanohive; -1 Rating per 3 Physical boxes taken while active (nanohive can replenish). Rating 0 = destroyed.
- Soft vs hard and reprogramming: see Nanotech file; not required for TCS/implant medic base use.

## Shared procedures

### DocWagon contract (Core 450; CF 30-33)

1. Tissue samples on file (secure vault).
2. Biomonitor RFID implant **or** wristband: activate for help; homing beacon; band rupture alerts DocWagon.
3. Armed trauma team in **<10 min** or emergency care **free**.
4. Resuscitation: 5,000¥ unless free under tier.
5. HTR: 5,000¥ unless waived/discounted; death compensation **20,000¥ per dead DocWagon employee** when charged.
6. No response on extraterritorial gov/corp property without permission.
7. Competitors (CrashCart, BluSix, Wuxing Prosperity, QuetzalCare, etc.): CF setting; no Core buy table. Use DocWagon costs unless GM prices rival.

**Core tier mechanics:**

| Tier | Cost/year (Core) | Free resus/year | HTR | Extended care | Death comp |
| --- | --- | --- | --- | --- | --- |
| Basic | 5,000¥ | 0 | pay 5,000¥ | full | charged when applicable |
| Gold | 25,000¥ | 1 | 50% off | 10% off | charged |
| Platinum | 50,000¥ | 4 | free | 50% off | still charged |
| Super-platinum | 100,000¥ | 5 | free | (CF: clinic covered) | not charged |

**Conflict:** CF Super-Platinum narrative = **500,000¥**/year. Core table = **100,000¥**. Basic/Gold/Platinum match. Prefer Core buy price unless using CF-era pricing; keep both.

**CF extras:**
- Basic: AR ID card; optional bracelet/RFID/biometric (nominal fee); out-of-pocket heavy; may be deprioritized vs premium.
- Gold: photo ID + **CodeBlue biomonitor bracelet** (activate; damage auto-triggers). HTR "some areas" only. Unlimited urgent care/ER; secure in closest clinic after alert or treatment covered. Need ≥1 extra SIN as emergency contact.
- Platinum: basic medical needs covered; free RFID health chip (opt-out; later install costs); RFID can prompt alert via commlink. Legal cyberware install/maintenance included. Long-term care 50% off. No SP clinics.
- Super-Platinum: on-call personal staff; free biometric algorithm; out-of-range → 60s reply window else alarm; dying biometrics → HTR. Clinic/HTR covered per CF annual fee.

**CF non-subscriber:** SIN required (temp SIN often criminal-flagged); subscribers first; 1 ER visit / 6 months if valid SIN + current account, pay in full, forfeit malpractice recourse; Docs Around the Clock fees; PharmaFarm OTC.

**SS fake DocWagon ops:** spoof call + uniforms + medkits + gurney (+ fake wristband) to enter as medics. Counterfeit ambulance chassis: DocWagon SRT ≈ **GMC Endurance**; CrashCart ≈ **S-K LT-21** (vs MuBoNA Rettungswagen). Vehicle mods (lights, sirens, chameleon coat): Vehicles / Vehicle Modifications / SS Extractor tables, not duplicated here.

### Houdini machine (SS 172-173)

- Two external (non-implant) auto-injectors as IV drips, one per arm; each has expanded reservoir (**6 doses**).
- Typical load: injector A = sedatives; injector B = saline + liquid nutrients.
- Drugs/saline into veins (basic First Aid). Liquid nutrients into stomach via NG tube or temporary shunt (auto-injector can shunt); needs formal medical training (Medicine), not First Aid alone. Hydration-only is OK without medic.
- **I (commlink + biomonitor):** auto-dose from biomonitor prompts; most metahumans unconscious up to **2 days** before refill. Trolls/dwarfs: dosage may fail (wake early); double sedatives (halves duration) or use II.
- **II (medkit computer):** better dosing; unconscious up to **3 days** before refill; better for troll/dwarf physiology.
- Cost excludes drugs/saline/nutrients.

### MediCart (R5 143)

- Deploy medkit within **2 m**; Pilot Rating replaces medkit Rating; **20 uses**; drone-locked; refill with normal medkit supplies.
- Rescue tools: Strength+Body-style tests use **3 x Body**; carry **270 kg** no test.

### Valkyrie module (R5 166-167)

- Auto-stabilize occupant. = Rating 6 medkit. Operates as autodoc (remote OK).

### Trauma control system (CF 148)

- Nanites gather on vital organs; electro-stim heart/respiration; regulate blood flow.
- While dying from overflow: every **1 minute**, Stabilization Test using **Rating in place of First Aid and Logic**.
- Avail 12F; Cost Rating x 4,000¥; Rating 1-6.

### Implant medic (CF 147-148)

- Installed with a **specific** cyberware implant; monitors/repairs that implant.
- On Matrix damage to that implant: next Combat Turn starts repair; pool = Rating x 2 (Hardware + Logic), limit = Rating (Core Matrix repair 228).
- Cost = **10% of that implant's cost**; Avail 12F; Rating 1-6.

### Built-in medkit (CF 86-89)

- Cyberlimb (partial/full) compartment + parts; **buy medkit separately**; refill as normal medkit supplies.
- Ess 0.45, Cap [10], Avail 8, Cost 1,000¥ + medkit.

### Cyber biomonitor (CF 82-85)

- Implanted biomonitor; accounts for augments in readings.
- Ess 0.1, Cap [1], Avail 2, Cost 500¥.
- **Wireless:** healthcare-provider link; vitals as Free Action via PAN.

## Catalog

### Handheld / worn biotech (Core)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Biomonitor | Core | 3 | 300¥ | Armband/wristband or integrate clothing/commlink. Vitals; blood/sweat/skin analysis. **Wireless:** share with designated devices; auto-alert DocWagon/ambulance at thresholds. |
| Disposable syringe | Core | 3 | 10¥ | Single-use injection. See Common rules. |
| Medkit (Rating 1-6) | Core | Rating | Rating x 250¥ | See Common rules → Medkits. |
| Medkit supplies | Core | - | 100¥ | One restock after (Rating) uses. |

### Slap patches (Core)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Antidote patch (1-6) | Core | Rating | Rating x 50¥ | +Rating toxin resistance for **20 min** after apply. |
| Chem patch | Core | 6 | 200¥ | Blank; load 1 dose chemical/toxin. |
| Stim patch (1-6) | Core | Rating x 2 | Rating x 25¥ | Clear Rating Stun boxes for Rating x 10 min; then Rating+1 unresisted Stun. No rest while active. Addiction Rating 2 / Threshold 1 if frequent. |
| Tranq patch (1-10) | Core | Rating x 2 | Rating x 20¥ | Stun = Rating; resist Body only. |
| Trauma patch | Core | 6 | 500¥ | Dying: Body stabilize test. **Wireless:** auto-stabilize. |
| Spacesuit emergency slap patch | RnG | (with suit) | 50¥ each | Spacesuits include **5**; extras 50¥. Specialty-armor refill, not a Core patch type. |

### DocWagon contracts (Core)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| DocWagon Basic | Core | - | 5,000¥/year | Shared procedures → DocWagon. |
| DocWagon Gold | Core | - | 25,000¥/year | +1 free resus; 50% HTR; 10% extended care. CF: CodeBlue bracelet. |
| DocWagon Platinum | Core | - | 50,000¥/year | +4 free resus; HTR free; 50% extended care; death comp still applies. |
| DocWagon Super-platinum | Core | - | 100,000¥/year | +5 free resus; HTR free; no death comp. **CF: 500,000¥/year** conflict. |

### CF nanotech medkits

| Name | Src | Type | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Savior medkit | CF | - | 6 | 2,000¥ | Activate: nanites **5 min**. Acts as Rating 6 medkit. If bleeding out, nanites act as **TCS** for duration. Restock every use. |
| Savior medkit supplies | CF | Hard | 4 | 300¥ | Restock Savior. |

### Medical nanoware (CF)

| Name | Src | Rating | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Trauma control system | CF | 1-6 | 12F | Rating x 4,000¥ | Shared procedures → TCS. Hard nanoware. |
| Implant medic | CF | 1-6 | 12F | 10% of linked implant cost | Shared procedures → Implant medic. Hard nanoware. Linked to one cyber implant. |

### Medical cyberware (CF; also in Cyberware.md)

| Name | Src | Ess | Cap | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- | --- |
| Biomonitor (implant) | CF | 0.1 | [1] | 2 | 500¥ | Shared procedures → Cyber biomonitor. Grades apply as cyberware. |
| Built-in medkit | CF | 0.45 | [10] | 8 | 1,000¥ + medkit | Shared procedures → Built-in medkit. Limb only. |
| Auto-injector (reusable, 1 dose) | CF | 0.05 | - | 2 | 500¥ + contents | Implant injector; refill via port or chemical gland. **Wireless:** drug-effect DB + duration countdown. |
| Auto-injector expanded reservoir | CF | 0.05 | - | 4 | 250¥ + contents | +5 doses (separate implant option). |
| Auto-injector killswitch | CF | 0.05 | - | 8F | 750¥ + contents | Single-use mental-trigger lethal injector; not designed to refill. |

### Armor medical installs (RnG; also Armor Modifications)

| Name | Src | Cap | Avail | Cost | Rules |
| --- | --- | --- | --- | --- | --- |
| Auto-Injector (armor) | RnG | [2] | 4 | 1,500¥ + chem | Usually linked to biomonitor. Holds **5 doses** any mix. Fire on command or preset (Simple Logic + Computer [Mental] (1) to program). Refill 1 min/dose. **Wireless:** inject Free Action. |
| Biomonitor (in armor) | Core/RnG | [1] | (buy biomonitor) | (biomonitor cost) | Capacity to mount handheld biomonitor. |
| Medkit (in armor) | Core/RnG | [5] | (buy medkit) | (medkit cost) | Capacity to mount medkit. |

### SS clinical / extraction medical devices

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Houdini Machine I | SS | 12F | 8,500¥ | Commlink + biomonitor control. Drugs not included. See Shared procedures → Houdini. |
| Houdini Machine II | SS | 12F | 12,000¥ | Medkit-computer control. Drugs not included. See Houdini. |
| Ambulance gurney | SS | 8 | 2,000¥ | Transport patient/target; DocWagon disguise kit staple. |
| Body bag | SS | 6 | 50¥ | Coroner-van fake-death: often with hidden O2 + slab (drug separate). |
| Fake DocWagon wrist band | SS | 10F | 100¥ | Counterfeit contract band for DocWagon disguise. |

### SS medical feeds (Houdini; also usable clinically)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Normal saline | SS | - | 30¥ / dose | IV hydration for Houdini / clinical use. |
| Liquid nutrients | SS | 4R | 75¥ / dose | Stomach delivery (NG/shunt); needs Medicine-trained setup for Houdini nutrient function. |

(Other SS Extractor drugs: Narcoject, Slab, DMSO, Caldwell lily, etc. → Drugs Toxins and Chemicals.)

### Medical drones / vehicle systems

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| CrashCart MediCart | R5 | 6 | 10,000¥ | Large drone, Pilot Ground Craft. Handl 5, Speed 5G, Accel 1, Body 6(2), Armor 5, Pilot 4, Sensor 4. Tracked; hydraulic rescue tools + medkit. See MediCart procedure. DocWagon announced similar with Valkyrie + 300 kg lift (no stats). |
| Valkyrie module | R5 | 8 | 2,000¥ | Vehicle Body mod: Slots 4, Threshold 6, Shop, Hardware. See Valkyrie procedure. |

### MediCart profile (quick copy)

```
CrashCart "MediCart" | Large drone | Pilot Ground Craft
Handl 5 / Speed 5G / Accel 1 / Body 6(2) / Armor 5 / Pilot 4 / Sensor 4
Avail 6 / 10,000¥
Tracked; specialized tools (hydraulic rescue, medkit)
Medkit: ≤2 m; Pilot = medkit Rating; 20 uses; drone-locked; normal supplies refill
Rescue: 3x Body for Str+Body tests; 270 kg carry no test
```

### Clinical tool kits (Core generic tools; buy for skill)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Kit (Medicine / Cybertechnology / etc.) | Core | 2 | 500¥ | Portable; skill-specific. Needed for many repairs/installs (GM). |
| Shop | Core | 8 | 5,000¥ | Van-back; advanced build/repair. |
| Facility | Core | 12 | 50,000¥ | Building; advanced constructions/mods. |

### RF PACK note (composition, not unique shop SKU)

Medical Patches PACK (RF): 2,000¥ / 1 Karma, Avail 10 = 5x antidote (4) + 4x tranq (5) + stim (4) + trauma. Component stats above.

## Item index

1. Biomonitor (Core handheld)
2. Disposable syringe
3. Medkit (1-6)
4. Medkit supplies
5. Antidote patch (1-6)
6. Chem patch
7. Stim patch (1-6)
8. Tranq patch (1-10)
9. Trauma patch
10. Spacesuit emergency slap patch (RnG refill)
11. DocWagon Basic
12. DocWagon Gold
13. DocWagon Platinum
14. DocWagon Super-platinum
15. Savior medkit
16. Savior medkit supplies
17. Trauma control system
18. Implant medic
19. Biomonitor (cyber implant)
20. Built-in medkit (cyberlimb)
21. Auto-injector reusable (cyber)
22. Auto-injector expanded reservoir (cyber)
23. Auto-injector killswitch (cyber)
24. Auto-Injector (armor)
25. Biomonitor armor Capacity mount
26. Medkit armor Capacity mount
27. Houdini Machine I
28. Houdini Machine II
29. Ambulance gurney
30. Body bag
31. Fake DocWagon wrist band
32. Normal saline
33. Liquid nutrients
34. CrashCart MediCart
35. Valkyrie module
36. Kit / Shop / Facility (Medicine or Cybertechnology)

## Bullets & Bandages biotech gear

**Verified from:** `Shadowrun_5E_Bullets_&_Bandages.pdf`.

| Name | Avail | Cost | Notes |
| --- | --- | --- | --- |
| MD-9 Autoinjection Gun | 4 | 1,000¥ | Inject as Simple; 9-dose single reservoir. |
| MD-3X Autoinjection Gun | 6 | 1,500¥ | Inject as Simple; 3×3-dose reservoirs. |
| Rapid Infuser | 4 | 1,000¥ | Required for HemoSynth/Cryo; any drug/toxin Speed = Instant. |
| HemostatiX Dressing | 6 | 500¥ | First Aid+Logic (2); Progression/Overflow interval → (Body+2) CT. |
| GE STATscan | 8 | 2,500¥ | +2 Diagnosis; cyberhand install Cap 2. |
| PAG Suit | 6 | 500¥ | Armor 3, Cap 4; pneumatic anti-shock (see Armor Modifications). |

