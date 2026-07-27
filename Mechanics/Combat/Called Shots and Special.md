# Combat - Called Shots and Special

Agent reference (SR5). LLM layout; Called Shots, suppression, Interrupts summary, knockdown, subdue, multi-attack.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Called Shots / Multiple Attacks / Dead Man's Trigger ~p.195-196; Suppressive Fire ~p.179; Interception / Knockdown / Subduing ~p.194-195; Defense Interrupts ~p.168, 190-191
**Source Text:** `11 - Combat.md`
**See also:** [Overview](Overview.md) · [Action Economy](Action%20Economy.md) · [Ranged Combat](Ranged%20Combat.md) · [Melee Combat](Melee%20Combat.md) · [Damage Armor and Wounds](Damage%20Armor%20and%20Wounds.md) · [Surprise](Surprise.md) · `../Edge.md`

**Scope:** Core called-shot options; suppression (Reaction+Edge; zone; Hit the Dirt); knockdown; Full Defense / Block / Parry / Dodge; Intercept; subduing; Multiple Attacks; Dead Man's Trigger
**Out of scope:** Run & Gun expanded called shots; full Barriers chapter; vehicle called shots depth (Vehicles)

## Inventory (completeness checklist)

- [x] Full Core called-shot table
- [x] Suppression (Reaction+Edge; zone; Hit the Dirt)
- [x] Knockdown; full defense; block/parry/dodge interrupts

---

## Schema

| Token | Meaning |
| --- | --- |
| Called Shot | Free Action + attack; -4 DP; pick effect |
| Suppression | Complex FA spray; zone; Reaction + Edge (threshold = hits) |
| Interrupt | Pay Init Score; act out of turn |

---

## Called Shots (Core)

All: **-4** dice pool + **Free Action** with Fire / Throw / Melee Attack. GM may disallow options.

| Option | Effect |
| --- | --- |
| **Blast out of Hands** | Disarm; target takes **no** damage. Item flies (net hits - 1) meters away from shooter |
| **Dirty Trick** | ≥1 net hit → target -4 DP on **next** action |
| **Harder Knock** | Stun weapon/attack deals **Physical** instead (DV otherwise unchanged) |
| **Knock Down** (melee only) | If more hits than defender: Str + net hits vs Physical Limit; exceed → prone, **no** damage. Attacker may Drop Prone free to follow (glitch: fall too; crit: you fall, they stay up) |
| **Shake Up** | Normal damage **and** target Init Score **-5** (even if all damage resisted). Score < 0 → lose last Phase this Pass |
| **Splitting the Damage** | Target must wear armor; attacker's AP must be **less** than that armor. Split remaining DV half P / half S (odd → more Stun). If modified DV < modified Armor after, half damage all Stun |
| **Trick Shot** | Not mid-brawl (needs setup). Hits = bonus dice on later Intimidation by you or known ally |
| **Vitals** | +**2** DV (aim brain/heart/etc.) |

Also: Harder Knock (S→P); Splitting the Damage when armored; vehicle components (Vehicles). Melee "transfer damage types" on armored targets points at Called Shots (Harder Knock / Splitting as applicable); unarmored lethal→nonlethal = club conversion ([Melee](Melee%20Combat.md)).

---

## Suppressive Fire

| Rule | Detail |
| --- | --- |
| Action | Complex; **20** rounds; **ignores recoil** |
| Zone | Triangle from firer to chosen distance (≤ weapon max range); **10 m** wide at far end, **2 m** high |
| Attack roll | Weapon Skill + Agility [Accuracy] (± smartlink/laser/tracer/GM); record **hits** |
| Duration | Until end of Combat Turn if firer does not move or take another action |
| Near zone | In or adjacent: -hits to all actions unless completely unaware of fire |
| Risk hit | Anyone in zone (not full cover / prone) who is there or moves in/out before end: Reaction + **Edge attribute** (± Full Defense) vs threshold = suppressor hits. Fail → hit for weapon **base DV** (+ ammo mods). Use full Edge rating (spent points OK; burned Edge no) |
| Avoid | Free Drop Prone, or **Hit the Dirt** Interrupt (-5 Init) if Free already used |
| Stay prone / full cover | Not at risk while suppressed (normal prone mods apply) |
| Stand/move again | Must test again if fire continues |
| Short ammo | Width -1 m per 2 bullets short |
| Overlap | Highest action penalty; separate Rea+Edge vs each zone; -1 DP per prior defense that Phase |

Vehicle notes: passengers get vehicle cover; Hit the Dirt may add vehicle Armor to Resistance; if weapon DV ≤ vehicle Armor, no penetrate; driver may Rea+Edge to exit zone with whole vehicle.

---

## Defense Interrupts (summary)

| Interrupt | Init | Effect |
| --- | --- | --- |
| **Dodge** | -5 | **Melee only:** + Gymnastics to one Defense [Physical] |
| **Parry** | -5 | **Melee only:** + melee weapon skill to one Defense [Physical] |
| **Block** | -5 | **Melee only:** + Unarmed to one Defense [Physical]; empty hands |
| **Full Defense** | -10 | + Willpower to Defense vs **any** attack for **rest of Combat Turn**; stacks with above |
| **Hit the Dirt** | -5 | Vs suppression without Free; go prone |
| **Intercept** | -5 | Melee out of turn (below) |

Ranged active defense options: free Rea+Int, or Full Defense only (Core Active Defenses).

Need enough Init Score; not if surprised. Details: [Action Economy](Action%20Economy.md) · [Melee](Melee%20Combat.md).

---

## Interception

| Rule | Detail |
| --- | --- |
| Trigger | Someone moves within **1 + interceptor's Reach** m and tries to pass without attacking, **or** leaves melee |
| Cost | Interrupt -5 Init; melee attack (weapon skill or Unarmed; firearm as club OK) |
| Stop | If after Resistance they take damage ≥ their **Body**, movement ends |
| Prone | Cannot intercept |
| Slip past | Complex + move: Agility + Gymnastics (1) [Physical]; each hit over threshold = pass one opponent |

---

## Knockdown

| Trigger | Effect |
| --- | --- |
| Boxes from one attack (after Resistance) **> Physical Limit** | Forced Drop Prone |
| ≥ **10** boxes after Resistance | Always knocked down |
| Gel rounds | Treat Physical Limit as **-2** for this comparison |
| Intentional | Melee Called Shot **Knock Down** (above) |

---

## Subduing (grapple)

| Step | Rule |
| --- | --- |
| Attack | Unarmed melee as normal |
| Grapple? | On hit: Strength + net hits vs defender Physical Limit; exceed → immobilized, **no** damage |
| Break free | Complex: Unarmed + Strength [Physical] vs threshold = attacker's grapple net hits |
| While held | No physical-movement actions; count as prone vs attacks |
| Maintainer | Each Phase: Complex to hold; optional: tighten (+2 Superior Position; adjust net hits), deal Stun = Strength (resist; Armor applies), or Called Shot Knock Down (+2) |

---

## Multiple Attacks

| Rule | Detail |
| --- | --- |
| Cost | Free Action + attack action(s) |
| Pool | Apply all mods (incl. full recoil of all shots) **then** split pool as evenly as possible; resolve each attack separately |
| Cap | Attacks ≤ half Combat Skill |
| Edge | Dice from Edge spend apply **before** split; one Second Chance can re-roll both pools |

---

## Dead Man's Trigger

One final action before death/unconsciousness if **all** of:

1. Initiative Score ≥ 1 this Turn
2. Spend 1 Edge (activates only; extra Edge can still boost tests)
3. Body + Willpower (3) succeeds

Then: one action of any kind (**no** movement); Free Actions may modify it.

---

## Coverage notes

- Core Called Shots list + suppression + Intercept/Knockdown/Subdue/Multi/DMT: complete for Core Combat specials.
- Expanded called shots: *Run & Gun* when sourced.
- Barriers / shooting through: Core Barriers (not expanded here).
