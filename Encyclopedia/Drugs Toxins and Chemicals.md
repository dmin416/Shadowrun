# Drugs Toxins and Chemicals

Agent reference (SR5). LLM layout; full mechanical detail from local PDFs.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `chromeflesh.pdf` · `stolensouls.pdf`
**Printed:** Core Toxins/Drugs/BTLs/Addiction ~p.408-415; Industrial Chemicals ~p.448; CF Quick & Dirty drugs ~p.169-193 + tables p.188-189 / 234-235; SS Extractor’s Toolkit drugs ~p.188-191
**See also:** `Encyclopedia/Medical Gear.md` · `Encyclopedia/Nanotech and Geneware.md` (Narco / Anti-tox / carcerands) · `Encyclopedia/Ammunition.md` (capsule/toxin rounds) · `Encyclopedia/Grenades and Explosives.md` (gas grenades) · `Encyclopedia/Security and Surveillance.md` · `Encyclopedia/Magical Goods.md` (primary CF magical compounds + SG/FA alchemy; this file also reprints CF compound dose rows) · **Play:** [Mechanics/Toxins and Drugs Play](../Mechanics/Toxins%20and%20Drugs%20Play.md)

**Scope:** toxins, street/combat/social drugs, BTLs/PsychChips, Awakened drugs, magical compounds, DMSO/carriers, extraction sedatives, industrial chemicals with buy stats, CF grades/custom/interactions/PCI/everyday pharma.
**Out of scope:** critter Venom power templates (use toxin framework); Howling Shadows critter-only venoms without buy SKUs. HT commercial venoms and B&B/Lockdown/BTB drugs are cataloged below.

## Inventory (completeness checklist)

**Core toxins (9):** CS/Tear Gas; Gamma-Scopolamine; Narcojet; Nausea Gas; Neuro-Stun VIII / IX / X; Pepper Punch; Seven-7  
**Core drugs (10):** Bliss; Cram; Deepweed; Jazz; Kamikaze; Long Haul; Nitro; Novacoke; Psyche; Zen (+ Alcohol / Soykaf addiction rows)  
**Core BTLs (4 types):** Dreamchip; Moodchip; Personafix; Tripchip (+ downloads)  
**Core industrial (3):** Glue solvent; Glue sprayer; Thermite burning bar  
**SS chemicals (11):** Caldwell lily (+ concentrate); Chloral hydrate; Chloroform; DMSO; Gamma-scopolamine (reprint); Laés / Leél / Laésal wine; Liquid nutrients; Narcoject (reprint); Normal saline; Slab  
**CF:** full street/Awakened/magical/BTL catalog + grades/custom/interactions/PCI/everyday pharma (sections below)  

---

## Schema

| Field | Meaning |
| --- | --- |
| Src | Core / CF / SS |
| Vector / Speed / Duration | Delivery and timing |
| Pen / Power | Toxin Penetration / Power (DV or effect strength) |
| Add Type | Physiological / Psychological / Both / n/a |
| Add R / Th | Addiction Rating / Threshold |
| Avail / Cost | Per dose unless noted |
| Effects / Crash | On-drug effects and wear-off |

---

## Common rules (Core p.408-415 + CF overlays)

### Toxin attributes

- **Vector:** Contact (skin; melee coat OK even if 0 damage; chem seal = immunity unless breached; chem protection +Rating dice); Ingestion (eat/drink; toxin extractor helps); Inhalation (aerosol/gas; gas mask / chem seal / active internal air tank = immunity; respirator/chem protection +Rating); Injection (bloodstream; dart/needle/edged melee that deals damage).
- **Speed:** Effects apply end of Combat Turn. Immediate = end of exposure turn; 1 CT = end of next CT; etc.
- **Power:** DV for damaging toxins; for non-damage toxins, Power still opposed. Reduce to 0 → no effects.
- **Effect:** Damage and/or Disorientation / Nausea / Paralysis / special. Unless noted, all effects occur if Power remains after resistance.
- **Penetration:** Like AP vs protective systems’ ratings.

### Toxin Resistance Test

Body + Willpower + protection ratings; each hit −1 Power. At 0, no effect.

### Concentration / prolonged exposure

+1 Power per extra dose at once (duration may increase, GM). Still exposed when Speed interval elapses → another Resistance Test; each subsequent test +1 Power cumulative.

### Antidotes

Must be taken **before** effects kick in to block damage; after, may reduce other effects. Some toxins (esp. neurotoxins) have no antidote. Physical overflow from toxin: correct antidote auto-stabilizes.

### Named toxin conditions (Core p.409)

- **Disorientation:** −2 all actions **10 minutes**.
- **Nausea:** If Power after resist > Willpower → incapacitated vomiting **3 CT**. Either way, **double** wound modifiers for **10 minutes**.
- **Paralysis:** If Power after resist > Reaction → no physical actions **1 hour**. Else −2 dice **1 hour**.

### Protection table (Core)

| Gear | Against | Protection |
| --- | --- | --- |
| Chemical seal | Contact, Inhalation | Immunity |
| Chemical protection | Contact | +Rating |
| Digestive expansion | Ingestion | +2 |
| Dwarf natural resistance | All toxins, diseases | +2 |
| Gas mask | Inhalation | Immunity |
| Internal air tank (active) | Inhalation | Immunity |
| Pathogenic defense | Diseases | +Rating |
| Respirator | Inhalation | +Rating |
| Toxin extractor | All toxins | +Rating |
| Tracheal filter | Inhalation | +Rating |

### Drug attributes

Same Vector/Speed/Power framework as toxins where applicable, plus **Duration**, **Addiction Type**. Attribute boosts count toward +4 augmented max (Core p.94).

### Addiction Tests (Core p.414)

Every (11 − Addiction Rating) weeks of use in a row → Addiction Test. Skip weeks still count; each abstaining week −1 Threshold (to 0 clears until reuse). Psych: Logic + Willpower; Phys: Body + Willpower; Both: two tests. Fail → gain Addiction quality (no Karma) or worsen one step. At Burnout fail: permanently −1 Body or Willpower (higher; tie by type) and max; 0 → coma + overflow.

### Withdrawal / staying clean

Need fix per Addiction quality severity. Resist craving: Withdrawal Test (Addiction Test rules). Stay clean weeks = Addiction Rating then Addiction Test; success → may buy off quality with Karma.

### Overdose (Core p.415)

Take substance while already on it **or** one sharing an effect (e.g. cram + novacoke both Reaction): Stun DV = sum of Addiction Ratings of overlapping drugs; resist Body + Willpower.

### CF overlays (full detail in CF common rules below)

Speedballing: +1 Addiction Rating to all drugs in mix. Interaction table when stacking/crash-recovering. Grades (Street/Standard/Pharma/Designer). Custom drug builder. Aisa multi-dose 4S per extra dose.

---

## Core sample toxins (p.409-410)

| Name | Src | Vector | Speed | Pen | Power | Effect | Avail | Cost | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CS / Tear Gas | Core | Contact, Inhalation | 1 CT | 0 | 8 | Disorientation, Nausea, Stun | 4R | 20¥ | Eyes/skin/mucus burn; panic response. Soap/water ends nausea early. Inert after **2 min** air. Outdoor wind may disperse. |
| Gamma-Scopolamine | Core/SS | Injection | Immediate | 0 | 12 | Paralysis, Truth Serum | 14F | 200¥ | Nightshade NM blocker. ~1 hour full effects; then 1 hour truth serum: Willpower **−3** (min 1). SS reprints with Duration lines. |
| Narcoject | Core/SS | Injection | Immediate | 0 | 15 | Stun Damage | 8R | 50¥ | Common dart tranquilizer; no side effects. |
| Nausea Gas | Core | Inhalation | 3 CT | 0 | 9 | Disorientation, Nausea | 6R | 25¥ | Riot agent. Inert after **2 min** air. |
| Neuro-Stun VIII | Core | Contact, Inhalation | 1 CT | 0 | 15 | Disorientation, Stun | 12R | 60¥ | Colorless/odorless knockout. Inert after **10 min** air. |
| Neuro-Stun IX | Core | Contact, Inhalation | 1 CT | 0 | 15 | Disorientation, Stun | 13R | 60¥ | Inert after **1 min** air. |
| Neuro-Stun X | Core | Contact, Inhalation | 1 CT | −2 | 15 | Disorientation, Stun | 14R | 100¥ | Pen −2; inert after **1 min** air. |
| Pepper Punch | Core | Contact, Inhalation | 1 CT | 0 | 11 | Nausea, Stun | - | 5¥ | CS + oreocapsicum spray; often RFID/dye tagged. Intense burn; eyes/nose/mouth worst. |
| Seven-7 | Core | Contact, Inhalation | 1 CT | −2 | 12 | Physical, Disorientation, Nausea | 20F | 1,000¥ | Bypasses chem protection focus. Cramp/nausea/double vision. Inert after **10 min** air. |

---

## Core street drugs (p.410-412)

| Name | Src | Vector | Speed | Duration | Add Type | Add R/Th | Avail | Cost | Effects | Crash / notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bliss | Core | Inhalation, Injection | 1 CT | (6−Body) h, min 1 | Both | 5 / 3 | 3F | 15¥ | −1 Reaction; +1 all thresholds; −1 all Limits; High Pain Tolerance 3 | Opiate tranquilizer |
| Cram | Core | Ingestion, Inhalation | 10 min | (12−Body) h, min 1 | Psych | 4 / 3 | 2R | 10¥ | +1 Reaction; +1D6 Initiative | Crash: **6S** unresisted |
| Deepweed | Core | Ingestion, Inhalation | Immediate | (6−Body) h, min 1 | Phys | (table: not listed; use GM/CF if any) | 8F | 400¥ | +1 Wil; +1 Mental limit; −1 Physical limit; **forces astral perception** (even non-perceiving adepts) | After: −1 all dice pools and −1 all limits for same duration as effect. Caribbean Awakened kelp |
| Jazz | Core | Inhalation | Immediate | 10×1D6 min | Both | 8 / 3 | 2R | 75¥ | +1 Reaction; +1 Physical limit; +2D6 Initiative | Crash: Disorientation for equal duration |
| Kamikaze | Core | Inhalation | Immediate | 10×1D6 min | Phys | 9 / 3 | 4R | 100¥ | +1 Bod, +1 Agi, +2 Str, +1 Wil, +2 Physical limit, +2D6 Init, HPT 3 | Crash: −1 Rea, −1 Wil, −2 all Limits equal duration; **6S** unresisted. Overdose risk escalates to death |
| Long Haul | Core | Injection | 10 min | 4 days | Psych | 2 / 1 | - | 50¥ | No sleep need; no fatigue mods for 4 days | Then sleep 8D6 h or Disorientation if kept awake. 2nd dose: +1D6÷2 days then **10S** unresisted + crash sleep. No further doses work past that |
| Nitro | Core | Inhalation | 1 CT | 10×1D6 min | Both | 9 / 3 | 2R | 50¥ | +2 Str, +2 Wil, +2 Perception, +2 Physical limit, HPT 6 | Crash: −2 all limits; **9S** unresisted equal duration |
| Novacoke | Core | Inhalation, Injection | 1 CT | (10−Body) h, min 1 | Both | 7 / 2 | 2R | 10¥ | +1 Rea, +1 Cha, +1 Perception, +1 Social limit, HPT 1 | Crash: Cha and Wil = **1**; −1 all limits equal duration |
| Psyche | Core | Ingestion | 10 min | (12−Body) h, min 1 | Psych | 6 / 2 | - | 200¥ | +1 Int, +1 Log, +1 Mental limit; Awakened: −1 per sustained spell (vs −2) | Designer stimulant |
| Zen | Core | Inhalation | 5 min | 10×1D6 min | Psych | 3 / 1 | 4R | 5¥ | −2 Reaction; +1 Willpower; −1 physical action dice | Hallucinogen |

**Also on Addiction Table (no full drug blocks):** Alcohol 3/2; Soykaf 1/2; Hot-Sim Simsense 3/1; Legal-Strength Simsense 2/1; Skillwires 5/2; Focus Addiction (total Force active foci)/2; Essence Drain (critter Magic)/2.

**Deepweed Addiction:** not on Core Addiction Table; still has Addiction Type Physiological in drug block.

---

## Better-Than-Life (Core p.412-413)

Shared: Speed Immediate; Duration typically 10×1D6 min; Addiction Psychological. Auto-erase after one use; bypass: Hardware + Logic (10, 1 hour) Extended. Downloads need hot-sim module.

| Type | Avail | Cost | Add R/Th | Notes |
| --- | --- | --- | --- | --- |
| Dreamchip | 4F | 20¥ | 6 / 1 | Modified simsense (heroic/crime/porn/snuff themes). Dreamdeck (hot-sim deck) or direct-input (skilljack/datajack). |
| Moodchip | 4F | 50¥ | 6 / 2 | Emotive track; crash opposite emotion 1-2 hours. Most common. RAS often disabled. |
| Personafix | 4F | 200¥ | 7 / 2 | Behavior overwrite (historical/pop icons; bunraku). RAS often disabled. |
| Tripchip | 4F | 100¥ | 8 / 3 | Sensory flood / synaesthesia; RAS often disabled. |

CF expands PsychChips and specialized BTLs (see CF sections).

---

## Stolen Souls chemicals (p.188-191)

| Name | Src | Vector | Speed | Pen | Power | Duration | Avail | Cost | Effects / notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Caldwell lily extract | SS | Ingestion (hallucinogen); Contact (local); Injection (general) | 1 CT | 0 | 4 hall / 4 local / 8 inject | (6−Body) h, min 1 | 10R | 600¥ | Stun Damage. Local numbness for minor medical. Inject may need multiple doses to KO. |
| Caldwell lily, concentrated | SS | as above | 1 CT | 0 | 14 | as above | 12R | 1,000¥ | Usually KO in one dose. |
| Chloral hydrate | SS | Ingestion | 2 CT | 0 | 12 (15 if +alcohol or other drowsy meds) | (14−Body) h; (18−Body) if mixed | 6R | 50¥ | Stun. Insomnia treatment / spiked drinks. |
| Chloroform | SS | Inhalation | 1 CT | 0 | 7 | (10−Body) h | 4R | 75¥ | Stun. Poor vs trolls/orks; **dwarfs immune**. |
| DMSO | SS | (carrier) | Instant absorb | - | - | - | 5R | 50¥ | Forces Contact vector for any compound dissolved with it (Core p.408). Soluble in acetone/alcohol/ether/water. |
| Gamma-Scopolamine | SS | = Core | | | | | 14F | 200¥ | Same as Core; SS adds explicit Duration lines. |
| Laés / Laésal wine | SS/CF | Ingestion, Injection (CF also Inhalation) | 1 CT | 0 | 12 | 20×1D6 min | 12F | 750¥ | **SS:** any Stun damage (even conscious) → erase last **(12−Body, min 1) h**. **CF:** “resist 12S or fall unconscious … with memories erased” (+ cigarette vector). Wine = same. Prefer SS wipe wording for play; see Awakened entry. |
| Leél | SS/CF | Ingestion, Injection | 1 CT | 0 | 10 | 5×1D6 min | 10F | 400¥ | Drowsiness not full KO; if ≥1 Stun box: lose last **(120−Body, min 100) minutes**. |
| Liquid nutrients | SS | NG tube or stomach shunt | - | - | - | - | 4R | 75¥ | Nourish unconscious long-haul. Medicine + Logic (2) to administer (tube already in); **no** First Aid default. |
| Narcoject | SS | = Core | | | | | 8R | 50¥ | Same as Core. |
| Normal saline | SS | IV | - | - | - | - | - | 30¥ | Hydration. Safe with medkit/biomonitor. Critical glitch on Medicine + Logic administer → metabolic acidosis risk (coma/death). |
| Slab | SS/CF | Injection | 2 CT | 0 | 16 | (10−Body) h, min 1 | 8R | 250¥ | Stun + suspended animation (near hibernation). Detect alive without proper gear: Perception + Intuition (6) or Medicine + Logic (4); medkit insufficient. After: −4 Reaction for half duration (round down). CF adds Reaper variant (−8 Assensing). |

**SS table also lists** Laés/Leél costs matching CF. Delivery gear (SS p.187/189 table): **Stimtouch hosiery** Dam 8S(e), AP −5, Reach 0, Avail 6R, 250¥; **laced lipstick** Avail 10F, cost (Drug+DMSO)+50¥.

---

## Industrial chemicals (Core p.448)

| Name | Src | Avail | Cost | Rules |
| --- | --- | --- | --- | --- |
| Glue solvent | Core | 2 | 90¥ | Dissolves ~1 m² fast aerosol glue. |
| Glue sprayer | Core | 2 | 150¥ | ~1 m² glue; hardens 1 CT; Body/Strength 5 to force (Opposed Body + Strength). |
| Thermite burning bar | Core | 16R | 500¥ | Fire DV **30P** vs barriers (iron/steel/plasteel). Not a normal weapon (tied/unconscious only). **Wireless:** activate. |

---

## CF common rules

### Overdose (Core; CF references)

CF does not rewrite overdose. **Core p.415:** whenever you take a substance while already on that substance **or** one that shares an effect (e.g. cram + novacoke both affect Reaction), take Stun DV = sum of Addiction Ratings of the overlapping drugs, resist Body + Willpower.

**Aisa (CF p.179):** in addition to standard overdose, more than one dose at a time: **4S per additional dose**.

### Speedballing / cocktailing (CF p.176)

Characters who mix drugs add **+1 to the Addiction Ratings of all drugs involved**.

### Drug interactions (CF p.178 narrative; full procedure p.193)

Trigger: take a drug while still under another drug **or** recovering from a crash.

1. Roll **1D6 per drug beyond the first**; sum the dice.  
2. Modifiers: **+1** per street-cooked drug in the mix (cumulative); **−1** if **all** drugs are designer grade.  
3. Consult Drug Interactions Table (below).

| Roll | Effect |
| --- | --- |
| 1 | Double duration of all drugs |
| 2-4 | No side effect |
| 5-6 | Duration of all crash effects doubled |
| 7-9 | Crash effects occur immediately |
| 10 | Immediately take 3S unresisted |
| 11-13 | Crash effect damage is Physical instead of Stun |
| 14+ | Immediately resist 10P by Body only |

Narrative (p.178): interactions unpredictable (harder crash, immediate crash, headache/cramps, nothing, or death). Impurities raise bad-reaction chance. Clinical zero under a trained doctor: no mixing penalties (Zero entry).

### Grades of drugs (CF p.190)

| Grade | Cost | Crash duration | Addiction / interaction notes |
| --- | --- | --- | --- |
| Street cooked | ×0.5 Standard | ×2 | Interaction rolls **+1** per street-cooked drug (cumulative) |
| Standard | listed | listed | Default |
| Pharmaceutical | ×2 | ×0.5 | Addiction Threshold **−1**; minimum grade for customized drugs |
| Designer | ×3 of pharmaceutical (= ×6 Standard) | ×0.25 | Cook must keep user’s DNA on file; if **all** drugs designer: interaction rolls **−1**. Used by wrong person: treat as Street cooked |

### Customizing drugs (CF p.190-192)

1. Choose **one foundation**.  
2. Add **blocks** (levels) respecting restrictions.  
3. Optional **enhancers**.  
4. Base: Duration **10 × 1D6 minutes**; Vector **Ingestion**; Speed **3 Combat Turns**.  
5. Acquire: chemist/dealer Connection **≥5**; raw ingredients = half normal drug price; Chemistry + Logic Extended (threshold Avail × 2, interval 8 hours). Glitch: restart with no hits; critical glitch: ingredients destroyed.

**Restrictions:** Initiative dice from all sources ≤ **+4D6**; any one Attribute bonus ≤ **+4** from all sources; no Attribute below 1 (else paralyzed until wear-off); if foundation negatively mods an Attribute, max positive block level for that Attribute is **Level 2**; crash Stun unresisted; overflow Stun→Physical at 1P per 2S (or portion).

#### Foundations

| # | Name | Effects |
| --- | --- | --- |
| 1 | Tank | Body +2, Willpower +1, Pain Resistance 3, Charisma −2 |
| 2 | Defender | Agility +1, Reaction +1, Intuition +1, Strength −1, Logic −1 |
| 3 | Genius | Logic +2, Intuition +2, Willpower −1, Reaction −1 |
| 4 | Charmer | Charisma +1, Social limit +1, Agility −1 |
| 5 | Warrior | Strength +1, Agility +1, Body +1, Willpower −1 |

#### Blocks 1-9

| Block | L1 | L2 | L3 |
| --- | --- | --- | --- |
| 1 Crush | Str +1, Int −1 | Str +2, Int −1; crash 2S | Str +3, Int −1, Low Pain Tolerance; crash 2S |
| 2 Brute | Bod +1, Log −1 | Bod +2, Log −1; crash 2S | Bod +3, Log −1, Int −1; crash 2S |
| 3 Strike | Agi +1, Str −1 | Agi +2, Str −1; crash 2S | Agi +3, Str −1, Unsteady Hands; crash 2S |
| 4 Lightning | Rea +1, Log −1 | Rea +2, Log −1, Wil −1 | Rea +3, Log −1, Wil −1; crash 2S |
| 5 Einstein | Log +1, Wil −1 | Log +2, Wil −1, Int −1 | Log +3, Wil −1, Int −1; crash −1D6 Initiative Dice |
| 6 Gut Check | Int +1, Str −1 | Int +2, Str −1, Rea −1 | Int +3, Str −1, Rea −1; crash 2S |
| 7 Stonewall | Wil +1, Bod −1 | Wil +2, Bod −1, Agi −1 | Wil +3, Bod −1, Agi −1, Str −1 |
| 8 Smoothtalk | Cha +1, Str −1 | Cha +2, Str −1; crash 2S | Cha +3, Str −1, Uncouth; crash 2S |
| 9 Shock&Awe | +1D6 Init; crash 4S | +2D6 Init, −1 all limits; crash 4S | +3D6 Init, −2 all limits; crash 8S |

#### Advanced blocks 10-13 (2 levels)

| Block | L1 | L2 |
| --- | --- | --- |
| 10 Razor Mind | Int +1, Log +1, Cha −1; crash 1S | Int +2, Log +2, Cha −2; crash 2S |
| 11 The General | Cha +1, Wil +1, Str −1; crash 2S | Cha +2, Wil +2, Str −1, Agi −1; crash 2S |
| 12 Resist | Bod +1, Wil +1, Log −1; crash 1S | Bod +2, Wil +2, Log −1, Rea −1; crash 2S |
| 13 Speed Demon | Agi +1, Rea +1, Str −1; crash 1S | Agi +2, Rea +2, Str −1, Int −1; crash 2S |

#### Enhancers

| Enhancer | Effect |
| --- | --- |
| Ingestion | Adds Ingestion vector |
| Inhalation | Adds Inhalation vector |
| Speed | −1 Combat Turn Speed; up to 3 times |
| Duration | +1D6 to duration roll; up to 3 times (max duration **10 × 4D6**) |

#### Customized drugs cost (per dose)

| Component | Avail | Cost | Add R | Add Th |
| --- | --- | --- | --- | --- |
| Foundations 1-5 | 4R | 75¥ | 6 | 2 |
| Blocks 1-8 (per level) | +1 | +20¥ | * | * |
| Block 9 (per level) | +2 | +40¥ | * | * |
| Blocks 10-13 (per level) | +2 | +30¥ | * | * |
| Enhancer | +1 | +50¥ | +1 | +1 |

\* Block addiction stacking not given as a closed formula beyond enhancers’ +1/+1; use foundation base and listed enhancer mods as printed.

**Note:** Wrecker example (p.192-193) misstates Foundation 2 as Reaction +2 and Block 2 L3 as Charisma −1; use foundation/block tables above.

### Portable Chemical Injector (CF p.176)

External auto-injector; button or wireless. No chemicals included.

| Model | Doses | Cost |
| --- | --- | --- |
| Wrist | 3 | 500¥ |
| Thigh | 5 | 750¥ |
| Harness | 20 | 2,500¥ |

### Everyday pharma (CF p.176)

OTC / lifestyle chemicals (limited or no combat stats):

| Name | Notes |
| --- | --- |
| Versaception | Birth control (women) |
| Contrax | Birth control (men) |
| Alphasprin | Extra-strength analgesics |
| EZBreathe | Lozenges; +1 dice vs pollution-based fatigue while in use (RnG p.147) |
| VitaMax / VitaBombs | Multivitamin; kids’ gummy size of a fist |
| ComaDoze | Extra-strength sleeping pills |
| Trimline | Appetite suppressant; extends time before starvation penalties by **50%** |
| Beta Inhibitors | Popular sex drug; also mixed with downers vs drowsiness |

### Flavor-only / no CF game block (do not invent stats)

Compliance, zombie dust (flavor; **Zombie Dust** has later stats), bottled spells, wake up, Resonator, Salvatol (rumored), TrimLine marketing (Trimline has everyday entry).

---

## CF drugs (prose + tables)

### AEXD  - CF p.179

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | Immediate |
| Duration | 10 × 2D6 minutes |
| Add Type | Physiological |
| Add R / Th | 1 / 1 |
| Avail / Cost | 4 / 80¥ |
| Effects | +3 dice to Body + Willpower tests to resist TLE-x seizures (quality CF p.59) while drug active |
| Crash / side |  - |

### Aisa (Eau de Vivre, Tex-Mex Tea)  - CF p.179

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | Immediate |
| Duration | 20 + 2D6 minutes |
| Add Type | Psychological |
| Add R / Th | 5 / 2 |
| Avail / Cost | 4 / 25¥ |
| Effects | Disorientation; blot paper/plastic; giddiness, lassitude, mild hallucinations |
| Crash / side | 2S unresisted when wears off. Extra doses: **+4S per additional dose** beyond standard overdose |

### Betameth (Buzz, Rigger’s Cocktail)  - CF p.180

| | |
| --- | --- |
| Vector | Inhalation |
| Speed | 1 minute |
| Duration | (9 − Body) hours, min 1 hour |
| Add Type | Both |
| Add R / Th | 9 / 3 |
| Avail / Cost | 5F / 30¥ |
| Effects | +2 Reaction, +1 Intuition; appetite suppressant; energetic/jumpy |
| Crash / side | 6S unresisted. Habitual: malnutrition / oral infections (GM) |

### Betel (Corpcandy, Jaw)  - CF p.180

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | Immediate |
| Duration | 10 × 1D6 minutes |
| Add Type | Physiological |
| Add R / Th | Special / 2 |
| Avail / Cost | 4 / 5¥ |
| Effects | +1 Perception; mild stimulant |
| Crash / side | **No Addiction Test:** even one use → Mild addiction; addiction never worse than Mild. Bonus dice to toxin resistance: immune to instant Mild if toxin resistance test succeeds |

### Cereprax (Brain Boost, Egghead)  - CF p.180

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | 1D6 minutes |
| Duration | (12 − Body) hours, min 1 hour |
| Add Type | Both |
| Add R / Th | 9 / 3 |
| Avail / Cost | 14F / 800¥ |
| Effects | +2 Intuition, +3 Logic, +2 Mental limit; Analytical Mind (Core p.72) |
| Crash / side | −2 all limits, −2 Logic, 5S unresisted. GM secretly rolls Intuition + Edge; if used again before (8 − hits) hours: **1D6 permanent Intuition** damage (repurchase with Karma) |

### Dopadrine (Bitter, Werden)  - CF p.180

| | |
| --- | --- |
| Vector | Contact |
| Speed | Immediate |
| Duration | 10 × 1D6 minutes |
| Add Type | Both |
| Add R / Th | 3 / 2 |
| Avail / Cost | 8 / 45¥ |
| Effects | Cancels Berserk / prevents going berserk for duration; −1 die all physical actions; −2 Social limit; patch form |
| Crash / side |  - |

### eX (Eros)  - CF p.180

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | 1D6 minutes |
| Duration | (8 − Body) hours, min 1 hour |
| Add Type | Psychological |
| Add R / Th | 5 / 2 |
| Avail / Cost | 3R / 20¥ |
| Effects | +1 Charisma, −1 Logic, +1 Perception, −1 Willpower; aphrodisiac / open to suggestion |
| Crash / side | Disorientation for like period; −2 Mental limit for (Body) hours |

### Galak  - CF p.180 (Awakened; under eX)

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | 1D6 minutes (same block as eX) |
| Duration | (9 − Body) hours, **min 3 hours** |
| Add Type | Psychological |
| Add R / Th | 6 / 3 |
| Avail / Cost | 4R / 45¥ |
| Effects | Same printed Attribute mods as **eX**: +1 Charisma, −1 Logic, +1 Perception, −1 Willpower; aphrodisiac / open to suggestion. CF: Awakened orchid pollen, “similar to, though more potent than, eX” (only Duration differs in the printed block) |
| Crash / side | Disorientation for like period; −2 Mental limit for (Body) hours (as eX) |

### Forget-Me-Not  - CF p.180-181

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | 1 Combat Turn |
| Duration | (12 − Body) hours, min 1 hour |
| Add Type | Psychological |
| Add R / Th | **not on CF Addiction Table** |
| Avail / Cost | 10F / 400¥ |
| Effects | While active: laés / similar memory drugs do not affect user; +3 dice to resist Alter Memory spells. Check drug interactions (p.178/193) if memory-altering drug enters system while active |
| Crash / side |  - |

### G3 (Gerilixir, Vitalite)  - CF p.181

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | 1 hour |
| Duration | (15 − Body) hours, min 1 hour |
| Add Type | Physiological |
| Add R / Th | 2 / 1 |
| Avail / Cost | 2 / 15¥ |
| Effects | +1 Body when resisting Fatigue; Longevity: GM discretion, daily use may lessen old-age effects |
| Crash / side |  - |

### Guts (Nofear, Brass Balls)  - CF p.181

| | |
| --- | --- |
| Vector | Inhalation |
| Speed | Immediate |
| Duration | (12 − Body) hours, min 1 hour |
| Add Type | Both |
| Add R / Th | 5 / 3 |
| Avail / Cost | 8R / 60¥ |
| Effects | Immunity to Fear (incl. negative Composure results) and fear-based powers/attacks |
| Crash / side | Reckless: GM may call Logic + Willpower (3) to avoid foolish/dangerous/inappropriate acts |

### Hurlg (Fomorian Usquebaugh, Orkstaff’s XXX)  - CF p.181

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | 2D6 minutes |
| Duration | (12 − Body) hours, min 1 hour |
| Add Type | Both |
| Add R / Th | 4 / 3 |
| Avail / Cost | 2R / 10¥ |
| Effects | −1 Logic, +1 Willpower; 160-180 proof ale + nutmeg; inflammable |
| Crash / side | 9S resisted by Body. Humans/elves: Disorientation for duration unless implant/magic grants toxin-resistance bonus dice (then ignore disorientation) |

### K-10 (Blood of Kali)  - CF p.181

| | |
| --- | --- |
| Vector | Injection |
| Speed | Immediate |
| Duration | 5 × 1D6 minutes |
| Add Type | Both |
| Add R / Th | 11 / 3 |
| Avail / Cost | 16F / 900¥ |
| Effects | +3 Body, +3 Agility, +4 Strength, +1 Willpower, +5 Initiative Score, High Pain Tolerance 3, Berserk (as Bear shaman when wounded). Attributes still capped at +4 over natural unaugmented |
| Crash / side | 18S unresisted. While berserk: Edge (1) Test or **stay berserk permanently** |

### Memory Fog  - CF p.181-182

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | 1 minute |
| Duration | (14 − Body) hours, min 2 hours |
| Add Type | Both |
| Add R / Th | **not on CF Addiction Table** |
| Avail / Cost | 6R / 100¥ |
| Effects | After effects end: Memory Test (Core p.152) at −2 to recall events while on drug. While on drug: Memory Test at −2 to recall times **not** on drug. Same altered state every time: recalling prior doses’ events does **not** take the −2 (CF PDF truncates mid-sentence after “previous”; this completes that rule) |
| Crash / side |  - |

### Nightwatch (Animu, Beggar’s Gaze)  - CF p.182

| | |
| --- | --- |
| Vector | Contact (eyedrops) |
| Speed | Immediate |
| Duration | 20 × 1D6 minutes |
| Add Type | Psychological |
| Add R / Th | 1 / 2 |
| Avail / Cost | 3R / 25¥ |
| Effects | Grants low-light vision |
| Crash / side | All Glare environmental modifiers one category worse while active |

### NoPaint (Numb, PBG)  - CF p.182

| | |
| --- | --- |
| Vector | Contact |
| Speed | Immediate |
| Duration | 1D6 hours |
| Add Type | Both |
| Add R / Th | 3 / 1 |
| Avail / Cost | 3 / 15¥ |
| Effects | High Pain Tolerance 3; lose tactile perception on covered areas; First Aid + Logic (2) to judge injury severity while active. 1 dose covers dwarf/human/elf; ork/troll need 2 for full coverage |
| Crash / side |  - |

### Oxygenated Fluorocarbons (Blue Blood, P4MO)  - CF p.182

| | |
| --- | --- |
| Vector | See below (IV / blood substitute treatment) |
| Speed | 1D6 hours |
| Duration | 1 week |
| Add Type | Physiological |
| Add R / Th | 2 / 1 |
| Avail / Cost | 12R / 2,000¥ |
| Effects | +1 Agility; double breath-holding time. Five-liter treatment + carcerands that clear OFCs by end of duration |
| Crash / side | Second treatment while first active: embolism **15P unresisted**. When wears off: −1 Physical limit and −1 Body for (Body) days. (Text typo “PM40” = P4MO.) |

### Push (Nanohi, Rush)  - CF p.182

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | 1 minute |
| Duration | (15 − Body) minutes, min 1 minute |
| Add Type | Both |
| Add R / Th | 4 / 3 |
| Avail / Cost | 4F / 25¥ |
| Effects | Mild euphoria (theobromine + cathinone); no numeric Attribute mods printed |
| Crash / side | Long-term / burnout-level addicts: GM may use Essence loss + violent mood swings |

### Red Mescaline (Manashrooms, Vertigo)  - CF p.182-183

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | 1 hour |
| Duration | (18 − Body) hours, min 1 hour |
| Add Type | Both |
| Add R / Th | 5 / 3 |
| Avail / Cost | 4R / 50¥ |
| Effects | +1 Charisma, −2 Reaction, +2 Perception, +1 Willpower, Disorientation. Combines with psyche: **no** Drug Interaction roll; combo called **loco** |
| Crash / side | Charisma and Willpower reduced to **1** for an equivalent duration |

### Ripper (J-H, Roidpatch)  - CF p.182-183

| | |
| --- | --- |
| Vector | Injection, Contact |
| Speed | Immediate |
| Duration | 10 × 1D6 minutes |
| Add Type | Both |
| Add R / Th | 5 / 3 |
| Avail / Cost | 6F / 60¥ |
| Effects | +1 Strength, −1 Willpower. Regular use (≥3×/day for 3-6 weeks): Strength improvement Karma cost **−1** |
| Crash / side | 2 boxes Stun unresisted (fatigue). Prolonged: sterility, baldness, libido loss, secondary sex characteristics of opposite sex, cancer (flavor/GM) |

### Slab (Coeur d’Hiver, Ghulpille)  - CF p.183

| | |
| --- | --- |
| Vector | Injection |
| Speed | 2 Combat Turns |
| Duration | (10 − Body) hours, min 1 hour |
| Power | 16 |
| Add Type | n/a |
| Add R / Th |  - |
| Avail / Cost | 8R / 250¥ |
| Effects | Near hibernation; breathing/HR almost imperceptible. Without proper medical gear (medkit insufficient): Perception + Intuition (6) **or** Medicine + Logic (4) to tell still alive |
| Crash / side | −4 Reaction for hours = half duration (round down). Shakes, chills, appetite |

**Reaper** (Awakened slab variant, same entry): mana-rich myotoxins; aura appears dormant/dead: **−8** dice to Assensing the aura. **No separate Avail/Cost/Addiction row.**

### Snuff (Aztech Chew, Indian Tobacco)  - CF p.183

| | |
| --- | --- |
| Vector | Ingestion, Inhalation |
| Speed | 1 minute |
| Duration | 10 × 1D6 minutes |
| Add Type | Both |
| Add R / Th | 2 / 2 |
| Avail / Cost | 1R / 10¥ |
| Effects | +1 Reaction, Pain Resistance 1 |
| Crash / side | −1 Intuition for twice original duration. Long-term: GM may increase Fatigue/cancer susceptibility |

### Sober Time  - CF p.183-184

| | |
| --- | --- |
| Vector | Contact |
| Speed | 1 Combat Turn |
| Duration | 10 × 1D6 minutes |
| Add Type | Both |
| Add R / Th | **not on CF Addiction Table** |
| Avail / Cost | 6F / 125¥ |
| Effects | Removes up to **6 dice** of existing penalties among Charisma, Intuition, Reaction, and/or Willpower. If total penalties > 6: apply evenly across penalized attrs, leftovers as desired. Only affects penalties already in effect; new penalties after dosing apply normally |
| Crash / side | When wears off: all **reduced** penalties return at **2×** for their **whole original** duration (even if time already passed). Attr reduced below 1 → immobile trance until effect ends. See printed example p.183-184 |

### Soothsayer  - CF p.184

| | |
| --- | --- |
| Vector | Contact |
| Speed | 1 minute |
| Duration | (12 − Body) hours, min 1 hour |
| Add Type | Addiction Test: **None** |
| Add R / Th |  - |
| Avail / Cost | 12F / 150¥ |
| Effects | 8S resisted with Body only. Unless all damage resisted: Willpower −3 and Social limit −1. Each additional application: DV −1 (resistance builds), regardless of time since last dose |
| Crash / side | Interrogation pain gel (gympie gympie hairs) |

### Woad (Bozoku, Frenitico)  - CF p.184

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | 1 Combat Turn |
| Duration | 5 × 1D6 minutes |
| Add Type | Both |
| Add R / Th | 5 / 2 |
| Avail / Cost | 3R / 15¥ |
| Effects | +2 Agility; auto-berserk when wounded (as Bear, Core p.321); +2 Agility while berserk |
| Crash / side | −2 all Social tests for original duration × 10. Frothing, fever, urge to bite |

### Zero (Cybertram, Doctor Bob’s Allergy Elixir)  - CF p.184

| | |
| --- | --- |
| Vector | Ingestion, Injection |
| Speed | 1 hour |
| Duration | (20 − Body) hours, min 1 |
| Add Type | Physiological |
| Add R / Th | 1 / 3 |
| Avail / Cost | 8R / 150¥ |
| Effects | No allergy **penalties** (Severe still deal damage, Core p.78); treat Addictions as one level lower; −2 Disease Resistance and Toxin Resistance Tests. Clinical use under trained doctor: **no** mixing penalties (p.178) |
| Crash / side | Immunosuppressant side as Effects |

### Zone (SSRIs)  - CF p.184-185

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | 1 hour |
| Duration | (12 − Body) hours, min 1 hour |
| Add Type | Both |
| Add R / Th | **not on CF Addiction Table** |
| Avail / Cost | **not on CF Cost or Compiled tables** |
| Effects | Ignore Mild to Moderate Phobias (Run Faster p.157) |
| Crash / side | While active: Mild Allergy to light (Core p.78); −1 Perception tests; Glare penalties +1 |

---

## Awakened drugs (BADs)  - CF p.184-186

### Ayao’s Will  - CF p.184-185

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | 2 Combat Turns |
| Duration | 10 × 1D6 minutes |
| Add Type | Psychological |
| Add R / Th | 5 / 2 |
| Avail / Cost | 14F / 750¥ |
| Effects | +2 dice to resist Manipulation spells (harmful or beneficial) |
| Crash / side |  - |

### Crimson Orchid (H-Red, Scarlet Bliss)  - CF p.184-185

| | |
| --- | --- |
| Vector | Injection |
| Speed | 1 Combat Turn |
| Duration | (12 − Body) hours, min 1 hour |
| Add Type | Both |
| Add R / Th | 9 / 3 |
| Avail / Cost | 6F / 300¥ |
| Effects | −3 Reaction, +1 to all thresholds, Pain Resistance 6; amplifies opiates (bliss/heroin). Distinctive red aura tint; Astral Beacon (Core p.78) for duration |
| Crash / side |  - |

### Hecate’s Blessing  - CF p.185

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | Immediate |
| Duration | 10 × 1D6 minutes |
| Add Type | Both |
| Add R / Th | 4 / 2 |
| Avail / Cost | 12F / 500¥ |
| Effects | +1 die on drain rolls |
| Crash / side | Magic −1 for twice original duration |

### Laés (Leäl, Laésal Wine)  - CF p.185 / SS p.188

| | |
| --- | --- |
| Vector | Ingestion, Injection; **CF also Inhalation** (incl. prepared cigarettes) |
| Speed | 1 Combat Turn |
| Duration | 20 × 1D6 minutes (Leäl: 5 × 1D6 minutes) |
| Power | Laés/Laésal **12**; Leäl **10** (SS) |
| Pen | 0 (SS) |
| Add Type | n/a |
| Add R / Th |  - |
| Avail / Cost | Laés 12F / 750¥; Leäl 10F / 400¥ |
| Effects | **Wipe (SS, preferred combat wording):** resist Power as Stun; if **any** Stun damage (even if still conscious), erase last **(12 − Body, min 1) hours** backward from dosing; memories chemically altered, unrecoverable by tech/magic. **Wipe (CF):** “resist 12S or fall unconscious for the duration, with … memories … erased” (ambiguous whether wipe requires KO). Laésal wine = Laés. CF: can be rolled into cigarettes |
| Crash / side | Leäl: drowsiness (not full KO); if ≥1 Stun: lose last **(120 − Body, min 100) minutes**. SS Duration for Leäl is 5 × 1D6 minutes |

### Oneiro (Dreamsage, Delphi)  - CF p.186

| | |
| --- | --- |
| Vector | Inhalation |
| Speed | Immediate |
| Duration | 3D6 minutes |
| Add Type | Psychological |
| Add R / Th | 6 / 3 |
| Avail / Cost | 6F / 1,250¥ |
| Effects | Paralysis; may use Divination via Logic + Intuition (threshold Street Grimoire p.125). With Augury and Sortilege ritual: interpret as normal. Without: Disoriented for duration equal to drug duration after |
| Crash / side | Addiction from prophetic tantalization; long-term indecision/paranoia (flavor/GM) |

### Overdrive (X-Cyte)  - CF p.186

| | |
| --- | --- |
| Vector | Inhalation |
| Speed | 1 Combat Turn |
| Duration | (10 − Body) hours, min 1 hour |
| Add Type | Both |
| Add R / Th | 5 / 3 |
| Avail / Cost | 10F / 800¥ |
| Effects | +1 Reaction, +1 to all Logic-linked skills |
| Crash / side | 8S unresisted. Long-term: possible Poor Self-Control: Braggart or Paranoia (RF p.158) |

### Pixie Dust (Bleeder, Neverland)  - CF p.186

| | |
| --- | --- |
| Vector | Inhalation |
| Speed | Immediate |
| Duration | 1D6 minutes |
| Add Type | Both |
| Add R / Th | 10 / 4 |
| Avail / Cost | 8F / 800¥ |
| Effects | +1 Charisma, +1 Perception, High Pain Tolerance 1; lose memory of past **1D6 minutes** after onset (forget taking it; high remains). Cocaine cut with leäl (± other cuts) |
| Crash / side | Nosebleeds common; overdoses common because use is forgotten |

### Trance (Toadstone, Zuvembie Powder)  - CF p.186

| | |
| --- | --- |
| Vector | Inhalation |
| Speed | 1 Combat Turn |
| Duration | (6 − Body) hours, min 1 hour |
| Add Type | Both |
| Add R / Th | 6 / 3 |
| Avail / Cost | 10F / 1,100¥ |
| Effects | +1 Intuition, +2 to all Logic-linked skills, Paralysis (voluntary muscles only; breathing OK) |
| Crash / side | Remain paralyzed (Core p.409) for an equivalent duration after |

---

## Magical compounds  - CF p.186-187

Shared pattern: Duration **Essence + 1D6 hours, max 12 hours** unless noted. Exotic ingredients listed.

### Animal Tongue  - CF p.186

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | 3D6 minutes |
| Duration | Essence + 1D6 hours, max 12 hours |
| Add Type | Psychological |
| Add R / Th | 3 / 2 |
| Avail / Cost | 6R / 1,500¥ |
| Effects | Critter power Animal Control. Ingredient: manzana cactus pulp radical (Aztlan) |
| Crash / side | Fear of animals for equal duration (animals exude Fear; spirits ≠ animals) |

### Immortal Flower  - CF p.186-187

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | 16 Combat Rounds |
| Duration | Essence + 1D6 hours, max 12 hours |
| Add Type | Both |
| Add R / Th | 8 / 3 |
| Avail / Cost | 14R / 2,500¥ |
| Effects | Critter power Regeneration. Ingredient: immortal flower petals (Mojave) |
| Crash / side | Per 20 boxes damage sustained while active: Essence −0.1 permanent. Cyber/bioware users: **2D6 Physical unresisted** when wears off (regen “repairs” implants) |

### Little Smoke  - CF p.187

| | |
| --- | --- |
| Vector | Inhalation |
| Speed | 2D6 minutes |
| Duration | Essence + 1D6 hours, max 12 hours |
| Add Type | Psychological |
| Add R / Th | 6 / 3 |
| Avail / Cost | 12F / 1,800¥ |
| Effects | Concealment + Confusion critter powers. Ingredient: three units natural herbal refined Great Plains grasses |
| Crash / side | Perception and Willpower to **1** for equal duration |

### Rock Lizard Blood  - CF p.187

| | |
| --- | --- |
| Vector | Ingestion |
| Speed | 30 minutes |
| Duration | Essence + 1D6 hours, max 12 hours |
| Add Type | Physical (table: Physical) |
| Add R / Th | 6 / 3 |
| Avail / Cost | 10R / 1,700¥ |
| Effects | Immunity to Diseases and Toxins. Ingredient: North American weeping tree pulp radical |
| Crash / side | 2P unresisted; −4 dice all disease/toxin resistance for equal duration |

### Shade  - CF p.187

| | |
| --- | --- |
| Vector | Inhalation |
| Speed | Immediate |
| Duration | Essence + 1D6 hours, max 12 hours |
| Add Type | Psychological |
| Add R / Th | 7 / 3 |
| Avail / Cost | 6R / 1,000¥ |
| Effects | Forces astral projection (even mundanes); metaplanes if with spirit guide or initiate. Awakened: add drug duration to normal astral time. Ingredient: SE Asian red orchid pollen radical |
| Crash / side | 10S unresisted. Must return to body before duration ends or die |

### Wudu’aku  - CF p.187

| | |
| --- | --- |
| Vector | Ingestion, Inhalation |
| Speed | 2D6 minutes |
| Duration | Essence + 1D6 hours, max 12 hours |
| Add Type | Psychological |
| Add R / Th | 4 / 1 |
| Avail / Cost | 12F / 2,350¥ |
| Effects | +2 Conjuring skill group; +2 effective Charisma vs spirits of man. Ingredient: powdered Australian Outback fossils |
| Crash / side | After ingest: −2 Conjuring and −2 Charisma when summoning **any other** spirit type for **24 hours** |

### Zombie Dust  - CF p.187

| | |
| --- | --- |
| Vector | Contact, Injection |
| Speed | 2 Combat Turns |
| Duration | Essence + 1D6 hours, max 12 hours |
| Add Type | Physiological |
| Add R / Th | 2 / 3 |
| Avail / Cost | 12F / 1,500¥ |
| Effects | Instantly prepares target for possession (still Intuition + Willpower to resist). Ingredient: exotic metahuman remains (+ traditional animal powders in flavor) |
| Crash / side |  - |

---

## Chips / BTLs  - CF p.187-193

### PsychChips  - CF p.187

| | Legal | Illegal (BTL) |
| --- | --- | --- |
| Speed | Immediate | Immediate |
| Duration | 48 hours | 48 hours |
| Add Type | Psychological | Psychological |
| Add R / Th | 3 / 2 | 6 / 3 |
| Avail / Cost | 4R / 350¥ | 6F / 500¥ |
| Effects | No penalties from psychological negative qualities treated. Legal: Mild/Moderate only. BTL: can handle Severe |
| Side | −1 Reaction while active. If Addiction develops and user stops: counteracted quality worsens by one degree |

### Common BTL chips (moodchips)  - CF p.193

Count as moodchips (Core p.413): Avail **4F**, Cost **50¥**, Add R **6**, Add Th **2**.

| Chip | Effect |
| --- | --- |
| Downer BTL | Reaction −1, Intuition +1 |
| Upper BTL | Intuition −1, Reaction +1 |
| Hyper BTL | Reaction +1, Agility +1, Intuition −1, Charisma −1 |
| Chill BTL | Charisma +1, Intuition +1, Logic −1, Willpower −1 |

### Specialized BTLs  - CF p.193

Avail **8F**, Cost **200¥**, Add R **6**, Add Th **2**.

| Chip | Effect |
| --- | --- |
| Berserker BTL | Strength +1, Body +1, Logic −1, Willpower −1. Always Full Offense in fights (RnG p.121); no martial arts needed |
| Bodyguard BTL | Body +1, Logic −1. Protecting the Principal (RnG p.125) without Edge. Assigned protectee when slotted; protect above all else |
| Infiltrator | Agility +2, Strength +1, Charisma −2; Gymnastics 2, Locksmith 2, Palming 1. Greed: Willpower (3) to not steal unattended valuables. Thrill of the Heist: Willpower (2) to stop mid-job. If Cha < 1 and regain consciousness while running: Uncouth until p-fix stopped |
| Pacifier | Reaction −1, Intuition −1, Willpower −1, Charisma −1. Passive/compliant extraction control; slurred speech, glassy eyes |

---

## CF Addiction Table (p.188)  - complete

| Substance | Add R | Add Th |
| --- | --- | --- |
| AEXD | 1 | 1 |
| Aisa | 5 | 2 |
| Betel | Special (see entry) | 2 |
| Betameth | 9 | 3 |
| Cereprax | 9 | 3 |
| Dopadrine | 3 | 2 |
| eX | 5 | 2 |
| Galak | 6 | 3 |
| G3 | 2 | 1 |
| Guts | 5 | 3 |
| Hurlg | 4 | 3 |
| K-10 | 11 | 3 |
| Nightwatch | 1 | 2 |
| NoPaint | 3 | 1 |
| Oxygenated Fluorocarbons | 2 | 1 |
| Push | 4 | 3 |
| Red Mescaline | 5 | 3 |
| Ripper | 5 | 3 |
| Snuff | 2 | 2 |
| Woad | 5 | 2 |
| Zero | 1 | 3 |
| Ayao’s will | 5 | 2 |
| Crimson Orchid | 9 | 3 |
| Hecate’s blessing | 4 | 2 |
| Overdrive | 5 | 3 |
| Oneiro | 6 | 3 |
| Pixie Dust | 10 | 4 |
| Trance | 6 | 3 |
| Animal Tongue | 3 | 2 |
| Immortal Flower | 8 | 3 |
| Little Smoke | 6 | 3 |
| Rock Lizard Blood | 6 | 3 |
| Shade | 7 | 3 |
| Wudu’aku | 4 | 1 |
| Zombie Dust | 2 | 3 |
| Psych Chips (legal) | 3 | 2 |
| Psych Chips (illegal) | 6 | 3 |

**Prose drugs with no Addiction Table row:** Forget-Me-Not, Memory Fog, Sober Time, Zone; Slab/Laés/Leäl (n/a); Soothsayer (Addiction Test None).

---

## CF Drug Costs (p.189) + Compiled Drugs (p.234-235)

Every compiled-table name. CF-prose entries: effects above. Core/SS: Avail/Cost from CF table only; effects not in CF.

| Drug | Avail | Cost | Ref (CF compiled) | Effects source |
| --- | --- | --- | --- | --- |
| AEXD | 4 | 80¥ | CF p.179 | CF (above) |
| Aisa | 4 | 25¥ | CF p.179 | CF |
| Animal Tongue | 6R | 1,500¥ | CF p.186 | CF |
| Ayao’s Will | 14F | 750¥ | CF p.184 | CF |
| Betameth | 5F | 30¥ | CF p.180 | CF |
| Betel | 4 | 5¥ | CF p.180 | CF |
| Bliss | 3F | 15¥ | Core p.411 | Core (not CF prose) |
| Caldwell lily extract | 10R | 600¥ | SS p.181 | Stolen Souls |
| Caldwell lily extract, concentrated | 12R | 1,000¥ | SS p.188 | Stolen Souls |
| Cereprax | 14F | 800¥ | CF p.180 | CF |
| Chloral hydrate | 6R | 50¥ | SS p.188 | Stolen Souls |
| Chloroform | 4R | 75¥ | SS p.188 | Stolen Souls |
| Cram | 2R | 10¥ | Core p.411 | Core |
| Crimson Orchid | 6F | 300¥ | CF p.184 | CF |
| Deepweed | 8F | 400¥ | Core p.411 | Core |
| DMSO | 5R | 50¥ | SS p.188 | Stolen Souls (utility chem / contact carrier) |
| Dopadrine | 8 | 45¥ | CF p.180 | CF |
| eX | 3R | 20¥ | CF p.180 | CF |
| Forget-Me-Not | 10F | 400¥ | CF p.180 | CF |
| Galak | 4R | 45¥ | CF p.180 | CF |
| Gamma-scoplomine | 14F | 200¥ | SS p.188 | Stolen Souls (spelling as printed) |
| G3 | 2 | 15¥ | CF p.181 | CF |
| Guts | 8R | 60¥ | CF p.181 | CF |
| Hecate’s Blessing | 12F | 500¥ | CF p.185 | CF |
| Hurlg | 2R | 10¥ | CF p.181 | CF |
| Immortal Flower | 14R | 2,500¥ | CF p.186 | CF |
| Jazz | 2R | 75¥ | Core p.411 | Core |
| K-10 | 16F | 900¥ | CF p.181 | CF |
| Kamikaze | 4R | 100¥ | Core p.412 | Core |
| Laés | 12F | 750¥ | CF p.185 | CF |
| Leäl | 10F | 400¥ | CF p.185 | CF |
| Liquid nutrients | 4R | 75¥ | SS p.189 | Stolen Souls / Medical Gear |
| Little Smoke | 12F | 1,800¥ | CF p.187 | CF (compiled ref p.187; prose p.187) |
| Long haul |  - | 50¥ | Core p.412 | Core |
| Memory Fog | 6R | 100¥ | CF p.181 | CF |
| Narcoject | 8R | 50¥ | SS p.189 | Stolen Souls |
| Nightwatch | 3R | 25¥ | CF p.182 | CF |
| Nitro | 2R | 50¥ | Core p.412 | Core |
| NoPaint | 3 | 15¥ | CF p.182 | CF |
| Normal saline |  - | 30¥ | SS p.189 | Stolen Souls / Medical Gear |
| Novacoke | 2R | 10¥ | Core p.412 | Core |
| Oneiro | 6F | 1,250¥ | CF p.186 | CF |
| Oxygenated Fluorocarbons | 12R | 2,000¥ | CF p.182 | CF |
| Overdrive | 10F | 800¥ | CF p.186 | CF |
| Pixie Dust | 8F | 800¥ | CF p.186 | CF |
| PsychChips (illegal) | 6F | 500¥ | CF p.187 | CF |
| PsychChips (legal) | 4R | 350¥ | CF p.187 | CF |
| Psyche |  - | 200¥ | Core p.412 | Core |
| Push | 4F | 25¥ | CF p.182 | CF |
| Red Mescaline | 4R | 50¥ | CF p.182 | CF |
| Ripper | 6F | 60¥ | CF p.182 | CF |
| Rock Lizard Blood | 10R | 1,700¥ | CF p.187 | CF |
| Shade | 6R | 1,000¥ | CF p.187 | CF |
| Slab | 8R | 250¥ | CF p.183 | CF |
| Snuff | 1R | 10¥ | CF p.183 | CF |
| Sober Time | 6F | 125¥ | CF p.183 | CF |
| Soothsayer | 12F | 150¥ | CF p.184 | CF |
| Trance | 10F | 1,100¥ | CF p.186 | CF |
| Woad | 3R | 15¥ | CF p.184 | CF |
| Wudu’aku | 12F | 2,350¥ | CF p.187 | CF |
| Zen | 4R | 5¥ | Core p.412 | Core |
| Zero | 8R | 150¥ | CF p.184 | CF |
| Zombie Dust | 12F | 1,500¥ | CF p.187 | CF |

**On CF prose but not compiled table:** Zone (no Avail/Cost printed); Reaper (Slab variant); Galak listed; common/specialized BTL chips (separate cost lines above); everyday pharma; PCI.

---

## Toxins / chemicals note

- Core sample toxins + Core drugs + BTLs + addiction + industrial chemicals: filled above.
- SS extraction chems (DMSO, Caldwell, chloral, chloroform, saline, liquid nutrients, Slab, Laés/Leél): filled above; Gamma/Narcoject reprint Core.
- CF: no replacement sample-toxin block; adds street/Awakened/magical/BTL catalog + grades/custom/interactions.
- Core overdose + Addiction Tests apply unless a CF entry overrides (Betel, Soothsayer, Zero clinical mixing, redmesc+psyche no interaction roll).

---

## Inventory checklist

**Core toxins (9):** CS/Tear Gas; Gamma-Scopolamine; Narcoject; Nausea Gas; Neuro-Stun VIII/IX/X; Pepper Punch; Seven-7  
**Core drugs (10):** Bliss; Cram; Deepweed; Jazz; Kamikaze; Long Haul; Nitro; Novacoke; Psyche; Zen  
**Core BTLs:** Dreamchip; Moodchip; Personafix; Tripchip  
**Core industrial:** Glue solvent; Glue sprayer; Thermite burning bar  
**SS:** Caldwell lily (+ concentrate); Chloral hydrate; Chloroform; DMSO; Laés/Leél/Laésal; Liquid nutrients; Normal saline; Slab (+ Gamma/Narcoject reprints)  
**CF street:** AEXD; Aisa; Betameth; Betel; Cereprax; Dopadrine; eX; Galak; Forget-Me-Not; G3; Guts; Hurlg; K-10; Memory Fog; Nightwatch; NoPaint; Oxygenated Fluorocarbons; Push; Red Mescaline; Ripper; Slab (+ Reaper); Snuff; Sober Time; Soothsayer; Woad; Zero; Zone  
**CF Awakened:** Ayao’s Will; Crimson Orchid; Hecate’s Blessing; Laés; Leäl; Oneiro; Overdrive; Pixie Dust; Trance  
**CF magical compounds:** Animal Tongue; Immortal Flower; Little Smoke; Rock Lizard Blood; Shade; Wudu’aku; Zombie Dust  
**CF chips:** PsychChips legal/illegal; Downer/Upper/Hyper/Chill; Berserker; Bodyguard; Infiltrator; Pacifier  
**CF support:** grades; custom foundations/blocks/enhancers; interaction table; PCI; everyday pharma  

## Coverage notes

- **Complete** for Core Toxins/Drugs/BTLs/Addiction tables + Industrial Chemicals; SS Extractor drug list + prose; CF Quick & Dirty full prose + compiled drug tables.
- Magical compounds: each entry includes Duration **Essence + 1D6 hours, max 12** (also stated in section intro).
- Deepweed: Addiction Type Physiological in Core drug block but **absent** from Core Addiction Table (no R/Th printed).
- Zone: CF effects, no Avail/Cost in cost/compiled tables.
- Forget-Me-Not, Memory Fog, Sober Time: no CF Addiction Table rows.
- Memory Fog: CF PDF truncates after “previous”; entry completes same-altered-state recall without the −2.
- Laés: SS vs CF wipe wording differs (any damage vs “or fall unconscious”); both recorded; SS preferred for combat toxin use.
- Critter Venom power defaults (Core p.401) point to toxin framework; species-specific buyable venoms not cataloged without SKUs.

## Hard Targets toxins

**Verified from:** `Shadowrun_5E_Hard_Targets.pdf`.

| Name | Vector | Speed | Power | Avail | Cost/Dose | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Aconite | Inj/Ing | 1 CT | 5 | 11F | 200¥ | P dmg, Nausea; forces shapeshifters to natural form (Will+Magic vs Power). |
| Atropine | Inj | Immediate | 5 | 10F | 150¥ | P dmg, Disorientation. |
| Dog Asp Venom | Inj | 1 min | 10 | 12F | 350¥ | P dmg (necrosis). |
| Ekyelebenie Venom | Contact | 1 CT | 8 | 16F | 575¥ | P dmg + vision −Power; −6+ = blind 24 hr. |
| Naga Venom | Inj | Immediate | =Naga Magic | Power×3 F | Power×100¥ | Power scales with source naga Magic. |
| Nova Scorpion Venom | Inj | 1 hr | 12 | 14F | 600¥ | Pen −2; slow-acting. |
| Tetrodotoxin | Inj/Ing | 1 CT / 10 min | 7 | 18F | 1,000¥ | Paralysis; Power>Rea = paralyzed 1 hr. |

## Bullets & Bandages drugs / toxins / pathogens

**Verified from:** `Shadowrun_5E_Bullets_&_Bandages.pdf`.

| Name | Type | Avail | Cost/Dose | Notes |
| --- | --- | --- | --- | --- |
| Crash | Drug | 3 | 800¥ | Injectable trauma-patch Stabilization (Care Under Fire compatible). |
| Cryo | Drug | 8R | 1,000¥ | Rapid-infuser only; suspended animation (30−Body) min. |
| HemoSynth | Drug | 4 | 2,000¥ | Rapid-infuser; removes Progressive/Overflow over Body×2 CT after Body CT infusion. |
| NanoScan | Drug | 5 | 500¥ | Soft-nanite biomonitor 24 hr (or hive Rating days). |
| Neostigmine | Drug | 2 | 100¥ | vs Paralysis: double Reaction; Paralysis duration halved. |
| Ondansetron | Drug | 2 | 50¥ | vs Nausea: double Willpower; Nausea duration halved. |
| Sugammadex | Drug | 6 | 100¥ | vs Rocuronium: −2 remaining Power per CT. |
| Dread | Toxin | 12R | 1,000¥ | Inj; Speed 1 CT; Pen 1; Power 8; Disorientation, Panic. |
| Picrotoxin | Toxin | 8R | 250¥ | Ing; Speed 1 CT; Power 8; Agony, Physical. |
| Retro | Toxin | 10F | 500¥ | Inh; Speed 1 CT; Power 6; Agony, Paralysis, Physical. |
| Rocuronium | Toxin | 6R | 50¥ | Inj; Speed 1 CT; Power 10; Paralysis ("Rock"). |
| Cypher | Pathogen | 16R | 5,000¥ | Inh/Inj; Speed 12 hr (10); Power 4; genome data encoding + memory loss. |
| Cryptococcus Metaformans | Pathogen | - | - | Astral-contact fungal; temp Essence loss = Power. No street Avail/Cost. |
| Red Masque | Pathogen | - | - | Inhaled viral; drains STR/LOG/WIL. No street Avail/Cost. |

## Lockdown drugs

**Verified from:** `shadowrun-lockdown-pdf.pdf`.

| Name | Avail | Cost/Dose | Notes |
| --- | --- | --- | --- |
| Pinpoint | 6R | 75¥ | +2 Intuition, +1 Mental limit; Perception without Observe in Detail −10; crash −3 INT/−2 Mental. |
| Numb | 6R | 150¥ | High Pain Tolerance (14); −2 tactile Perception, −1 Agility. |
| Buffout | 6R | 100¥ | +6 STR Lift/Carry/Grapple; −4 STR melee DV; crash self-damage. |
| Accelerator | 6R | 200¥ | +3d6 Initiative dice (cap 5d6 with R1 init aug); −2 Body DR; bleeding 2P/round. |

## Better Than Bad toxin

| Name | Vector | Speed | Power | Avail | Cost/Dose | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Blight | Inj / Special | Immediate | 12 | 8F | 250¥ | Awakened lose manasphere [12 − (Body or Magic, higher)] hours (min 1). Dual-natured −4 all actions. +DMSO: contact; Awakened resist with Drain Resistance vs Power (Stun Drain). |

## Cutting Aces tailored perfume / cologne

All last ~4 hr or until washed unless noted.

| Name | Avail | Cost | Notes |
| --- | --- | --- | --- |
| Aztec Fly | 6 | 100¥ | +1 Con (Seduction) vs metahumans. |
| Black Panther | 8R | 250¥ | +1 Social vs metahumans. |
| Lion's Roar | 4 | 75¥ | +1 Intimidate vs metahumans. |
| Tanake Tiger | 5 | 100¥ | As Critter Spook (RF). |
| Tracking Hound | 3 | 75¥ | +2 Tracking with Olfactory Sensors or Scent. |
| Winter Wolf | 3 | 50¥ | +2 Intimidate vs animals. |
| Genemarked Pheromones | 8F | 300¥ | +2 Social vs one individual (needs genetic sample). |

