# Toxins and Drugs (Play)

Agent reference (SR5). LLM layout; toxin/drug **procedures** in play. Item stats live in Encyclopedia.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Toxins, Drugs, and BTLs ~p.408-415
**Source Text:** Core Condensed / Street Gear chapter (toxins block)
**See also:** [Encyclopedia/Drugs Toxins and Chemicals](../Encyclopedia/Drugs%20Toxins%20and%20Chemicals.md) · [Healing and Injuries](Healing%20and%20Injuries.md) · [Combat/Damage Armor and Wounds](Combat/Damage%20Armor%20and%20Wounds.md) · [Character Creation/Qualities](Character%20Creation/Qualities.md) (Addiction levels) · [Advancement](Advancement.md) (buy off Addiction)

**Scope:** Toxin/drug procedures; **Chrome Flesh** custom drug creation
**Out of scope:** Per-substance catalogs (Encyclopedia); full BTL chip SKUs; disease rules beyond Pathogenic Defense note

## Inventory

- [x] Vector / Speed / Power / Effect / Penetration
- [x] Toxin Resistance Test + protection table
- [x] Concentration / continuous exposure
- [x] Antidotes
- [x] Disorientation / Nausea / Paralysis
- [x] Drugs Duration + Addiction Type
- [x] Custom drug creation (Chrome Flesh)

---

## Schema

| Token | Meaning |
| --- | --- |
| Vector | How the toxin enters (Contact / Ingestion / Inhalation / Injection) |
| Speed | When Effect applies (end of Combat Turn clock) |
| Power | DV for damaging toxins; gate for non-damage effects |
| Penetration | Like AP vs protective systems' ratings |
| Toxin Resistance | Body + Willpower + protection; each hit −1 Power |

---

## Toxin attributes

| Attribute | Rule |
| --- | --- |
| **Vector** | Delivery method (below) |
| **Speed** | Immediate = end of **same** Combat Turn exposed; **N** Combat Turns = end of the Nth Turn after exposure |
| **Power** | Damaging toxins: Power = DV. Non-damage: effects only if Power remains after resistance |
| **Effect** | Damage type and/or listed statuses. Usually all apply unless Power → 0 |
| **Penetration** | Reduces rating of protective systems like weapon AP |

### Vectors

| Vector | Notes |
| --- | --- |
| Contact | Skin; liquid coat on weapon applies on successful melee (damage not required). Chemical seal = immunity (unless breached). Chemical protection = +Rating to Resistance |
| Ingestion | Must eat/drink; usually slower. Toxin extractor helps all toxins including ingested |
| Inhalation | Gas/aerosol. Gas mask / chemical seal / active internal air tank = immunity. Chemical protection / respirator / tracheal filter = +Rating |
| Injection | Bloodstream (dart, hypo, damaging edged melee). Coat edged weapon → needs damaging melee hit |

### Toxin and Drug Protection

| Gear / trait | Protects | Bonus |
| --- | --- | --- |
| Chemical seal | Contact, Inhalation | Immunity |
| Chemical protection | Contact (+ Inhalation per Core table note for chem prot on inhalation) | +Rating to Resistance |
| Digestive expansion | Ingestion | +2 |
| Dwarf natural resistance | All toxins, diseases | +2 |
| Gas mask | Inhalation | Immunity |
| Internal air tank (active) | Inhalation | Immunity |
| Pathogenic defense | Diseases | +Rating |
| Respirator | Inhalation | +Rating |
| Toxin extractor | All toxins | +Rating |
| Tracheal filter | Inhalation | +Rating |

Penetration reduces the effective rating of applicable protective systems.

---

## Toxin Resistance Test

1. Note exposure and toxin's **Speed**.
2. At end of the appropriate Combat Turn, roll:

```
Body + Willpower + protective ratings [vs Power]
```

Each hit reduces Power by 1. Power 0 → no damage and no other effects. Remaining Power → apply Effect (DV = remaining Power for damage toxins).

Damage from toxins uses normal injury tracks ([Healing and Injuries](Healing%20and%20Injuries.md)).

### Concentration

| Situation | Effect |
| --- | --- |
| Multiple doses at once | Power +1 per extra dose; Duration may increase (GM) |
| Still exposed when Speed interval elapses | New Resistance Test; Power +1 cumulative each subsequent interval |

### Antidotes

Must be taken **before** effects kick in to prevent damage. After effects start: may reduce non-damage effects; does not undo damage already applied. Some toxins (esp. neurotoxins) have no useful antidote. If Physical **overflow** from a toxin, correct antidote **auto-stabilizes**.

---

## Common Effects

| Effect | Rule |
| --- | --- |
| Disorientation | −2 all actions for **10 minutes** |
| Nausea | If remaining Power > Willpower → incapacitated (no actions) **3 Combat Turns**. Always: **double** wound modifiers for **10 minutes** |
| Paralysis | If remaining Power > Reaction → no physical actions for **1 hour**. Else −2 DP for 1 hour |
| Stun / Physical Damage | As normal damage with DV = remaining Power |

Outdoor gas: wind/environment may disperse (GM).

---

## Drugs (play)

Same Vector / Speed / Power / Effect / Penetration framework as toxins, plus:

| Extra | Meaning |
| --- | --- |
| Duration | How long beneficial / side effects last |
| Addiction Type | Physiological, Psychological, or both |
| Attr boosts | Subject to augmented max (**natural +4**) |

Roleplay mood/behavior changes. Catalog: Encyclopedia.

---

## Addiction Tests

Each addictive substance has **Addiction Rating** and **Addiction Threshold**.

| Rule | Detail |
| --- | --- |
| Trigger window | Use during **(11 − Addiction Rating)** weeks in a row → Addiction Test |
| Skip weeks | Clock keeps running; each week without use −1 Addiction Threshold (floors at 0 = off hook until next use) |
| Psychological | Logic + Willpower vs Addiction Threshold |
| Physiological | Body + Willpower vs Addiction Threshold |
| Both | Two separate tests |
| Multiple substances | Test each when due |
| Fail | Gain Addiction quality (no Karma) **or** raise severity one step (Mild → Moderate → Severe → Burnout) |
| Fail at Burnout | Permanently −1 higher of Body or Willpower (and that attr max). Tie: Body if phys, Willpower if psych; both → coin flip. Attr 0 → coma: fill Stun+Physical, then overflow |

### Core Addiction Table (sample)

| Substance | Addiction Rating | Addiction Threshold |
| --- | --- | --- |
| Alcohol | 3 | 2 |
| Bliss | 5 | 3 |
| Cram | 4 | 3 |
| Jazz | 8 | 3 |
| Kamikaze | 9 | 3 |
| Long Haul | 2 | 1 |
| Nitro | 9 | 3 |
| Novacoke | 7 | 2 |
| Psyche | 6 | 2 |
| Soykaf | 1 | 2 |
| Zen | 3 | 1 |
| BTL Dreamchip | 6 | 1 |
| BTL Moodchip | 6 | 2 |
| BTL Personafix | 7 | 2 |
| BTL Tripchip | 8 | 3 |
| Hot-Sim | 3 | 1 |
| Legal-strength sim | 2 | 1 |
| Skillwires | 5 | 2 |
| Focus Addiction | total Force of all active foci | 2 |
| Essence Drain | critter Magic | 2 |

### Craving / Withdrawal / Clean

| Step | Rule |
| --- | --- |
| Fix schedule | Per Addiction quality severity ([Qualities](Character%20Creation/Qualities.md)) |
| Resist craving | Withdrawal Test (same pools as Addiction Test) + severity mods |
| Fail craving | Need fix or enter withdrawal (quality penalties) |
| Stay clean | Weeks without = Addiction Rating → Addiction Test; success → may **buy off** Addiction with Karma ([Advancement](Advancement.md) ×2 listed bonus) |

### Overdose

Take substance while already on it **or** on another sharing an effect (e.g. Cram + Novacoke both Reaction): Stun DV = sum of overlapping Addiction Ratings; resist Body + Willpower.

---

## Custom drug creation (*Chrome Flesh*)

**Verified from:** `Chrome Flesh Condensed.md` Ch. 11.

### General rules

| Rule | Detail |
| --- | --- |
| Speedballing | Mixing drugs adds **+1 Addiction Rating** to **all** drugs involved |
| Drug interactions | Roll **1D6 per drug beyond the first** (modify by grade); consult interaction table |
| Grades | Street cooked: half cost, double crash, +1 interaction. Standard: default. Pharmaceutical: 2x cost, half crash, Threshold -1; **required for custom**. Designer: 6x standard (3x pharma), quarter crash, DNA on file |
| Creation test | **Chemistry + Logic Extended** (Threshold = Avail x 2, 8 hr interval). Glitch = restart; crit glitch = destroy ingredients |
| Supplier | Contact Connection **5+** for custom drugs and raw materials (raw = half drug price) |

### Custom foundations (pick one)

| # | Name | Effect |
| --- | --- | --- |
| 1 | Tank | Body +2, Wil +1, Pain Resistance 3, Cha -2 |
| 2 | Defender | Agi +1, Rea +1, Int +1, Str -1, Log -1 |
| 3 | Genius | Log +2, Int +2, Wil -1, Rea -1 |
| 4 | Charmer | Cha +1, Social limit +1, Agi -1 |
| 5 | Warrior | Str +1, Agi +1, Body +1, Wil -1 |

### Custom blocks (levels 1-3; incompatible pairs per source)

| Block | L1 (examples) | L3 extras |
| --- | --- | --- |
| Crush | STR +1, INT -1 | STR +3, INT -1, Low Pain Tolerance, crash 2S |
| Brute | BOD +1, LOG -1 | BOD +3, LOG -1, INT -1, crash 2S |
| Strike | AGI +1, STR -1 | AGI +3, Unsteady Hands, crash 2S |
| Lightning | REA +1, LOG -1 | REA +3, LOG -1, WIL -1, crash 2S |
| Einstein | LOG +1, WIL -1 | LOG +3, crash -1D6 Init dice |
| Shock & Awe | +1D6 Init, crash 4S | +3D6 Init, -2 all limits, crash 8S |

Full blocks 6-13: *Chrome Flesh* condensed §11.

### Restrictions and base stats

- Max **+4D6 Initiative** total; max **+4** to any one attribute; no attribute below 1 (0 = paralyzed until drug ends).
- Base duration **10 x 1D6 min**; base vector Ingestion; base Speed **3 Combat Turns**.

### Enhancers (each +50¥, +1 Avail, +1 Rating, +1 Threshold)

Ingestion, Inhalation, Speed (-1 CT each, x3 max), Duration (+1D6, x3 max, max 10 x 4D6).

### Cost per dose (components)

| Component | Avail | Cost | Addiction |
| --- | --- | --- | --- |
| Foundation 1-5 | 4R | 75¥ | Rating 6, Threshold 2 |
| Blocks 1-8 / level | +1 | +20¥ | per interaction roll |
| Block 9 / level | +2 | +40¥ | |
| Blocks 10-13 / level | +2 | +30¥ | |
| Enhancer | +1 | +50¥ | +1 Rating, +1 Threshold |

Catalog SKUs: [Encyclopedia/Drugs Toxins and Chemicals](../Encyclopedia/Drugs%20Toxins%20and%20Chemicals.md).
