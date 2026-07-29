# Combat - Called Shots and Special

Agent reference (SR5). LLM layout; Called Shots, suppression, Interrupts summary, knockdown, subdue, multi-attack.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `Source/PDF/runandgun.pdf`
**Printed:** Core Called Shots ~p.195-196; RnG Killshots ~p.105-126; Suppression ~p.179; Interception / Knockdown / Subduing ~p.194-195
**Source Text:** `11 - Combat.md` · `08 - Killshots and More.md` · `Run and Gun Condensed.md`
**See also:** [Overview](Overview.md) · [Action Economy](Action%20Economy.md) · [Ranged Combat](Ranged%20Combat.md) · [Melee Combat](Melee%20Combat.md) · [Martial Arts](Martial%20Arts.md) · [Damage Armor and Wounds](Damage%20Armor%20and%20Wounds.md) · [Surprise](Surprise.md) · [Barriers](../Barriers.md) · `../Edge.md`

**Scope:** Core + RnG called shots (location, ammo-specific, MA-only); suppression + Enhanced/Flechette; knockdown; defense interrupts; intercept; subduing; multiple attacks; DMT
**Out of scope:** Full Barriers chapter ([Barriers](../Barriers.md)); deep vehicle combat (Vehicles); RG1-RG6 optional combat options (RnG GM options only)

## Inventory (completeness checklist)

- [x] Full Core called-shot table
- [x] RnG martial-arts Called Shots (Disarm, Break Weapon, Feint, etc.)
- [x] Location Called Shots (Specific Target) full table
- [x] Ammo Whammy shots + by-ammo index
- [x] Suppression (+ Enhanced / Flechette)
- [x] Knockdown; defense interrupts; intercept; subdue; multi-attack; DMT

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

## Run & Gun Called Shots (expanded)

RnG shots use **variable** modifiers (not always -4). Many double as [Martial Arts](Martial%20Arts.md) techniques (trained users get -1 to the listed penalty where noted in Martial Arts).

| Called Shot | Modifier | Notes |
| --- | --- | --- |
| **Blast out of Hand** | -4 (Core) | No damage; disarm. Some ammo adds damage (Ammo Whammy) |
| **Break Weapon** | -4 | Close combat only; **MA training required**. Weapon resists as barrier. If Accuracy >3: -1 Accuracy (repeat until 3). If Reach >0: -1 Reach (repeat until 0) |
| **Dirty Trick** | -4 (Core) | No damage; target -4 DP next action. Ammo may enhance |
| **Disarm** | -4 | Unarmed only; **MA required**. Str + net hits > target Physical Limit: snatch weapon (Ready Weapon to use). Else: -net hits if they use that weapon next Phase. Fail: opponent +2 with that weapon this Phase |
| **Entanglement** | -4 | Exotic whip/rope weapons only; **MA required**. Net hits reduce Agility this Phase instead of damage; cannot move farther than weapon range. Agi 0 = only break free. Escape Artist + Agility [Physical] Complex vs net hits |
| **Feint** | -4 | Close combat; **MA required**. No damage; next Phase target -net hits Defense vs your real attack. Only most recent Feint counts |
| **Knock Down** | -4 (Core) | Melee; no damage if successful (Core rules) |
| **Pin** | -4 | Archery/thrown; **MA required**. If DV > clothing Armor (not dermal plating), pin to surface. -2 Defense while pinned. Break: Body + Strength Simple vs net hits; or Free rip free for 1P/box per net hit (failed Simple adds gap to rip damage) |
| **Reversal** | -4 | Unarmed; **MA required**. In clinch without Superior Position: reverse roles; if was grapple, may Subdue next Phase |
| **Shake Up** | -4 (Core) | Normal damage + Init -5 |
| **Splitting the Damage** | -4 (Core) | Half P / half S on armored target |
| **Specific Target** | varies | See Location table below |
| **Trick Shot** | -4 (Core) | Net hits add to Intimidation vs target |
| **Vitals** | -4 (Core) | +2 DV |
| **Harder Knock** | -4 (Core) | Stun attack deals Physical |

---

## Location Called Shots (Specific Target)

Replaces standard -4 modifier. After Attack Test, **before** Resistance: spend net hits **after the first** to pick effects (hits do **not** add DV). If Resistance leaves **no** damage, **no** extra effects. Effects from different locations stack new effects but do not double same effect; durations extend with repeat hits to same location.

| Location | Mod | DV Limit | Effects |
| --- | --- | --- | --- |
| **Ankle** | -8 | 1 | Slowed (half Walk/Run, no Sprint); Winded (no Complex Actions for turns = original DV) |
| **Ear** | -10 | 1 | Deafened (-2 one ear / -4 both, no hearing Perception for turns = original DV); Stunned (Body+Will 2 or -10 Init). Twice = both ears |
| **Eye** | -10 | 1 | Blinded (-4 one / -8 both); Stunned (Body+Will 3 or -10 Init). Twice = both eyes |
| **Foot** | -8 | 1 | Stunned (Body+Will 3 or -5 Init); Slowed; Winded |
| **Forearm** | -6 | 2 | Broken Grip (drop item, -1/clinch per injured arm for turns = DV); Weak Side (-1 melee Defense) |
| **Genitals** | -10 | 4 | Stunned (Body+Will 4 or -10 Init); Nauseous (Body+Will 4, each miss = 1 turn vomiting, -4 all actions); Buckled (Body(DV) or prone for (DV-hits) turns) |
| **Gut** | -6 | 8 | Stunned (Body+Will 2 or -5 Init); Nauseous; Slow Death (**Physical piercing only**: 2S/min internal bleed until Medicine/First Aid (16, 1 min) Extended or Heal removes 1+ box) |
| **Hand** | -8 | 1 | Stunned (Body+Will 2 or -5 Init); Broken Grip; Weak Side |
| **Hip** | -6 | 3 | Knockdown (Strength+Agility (DV+3) or prone); Slowed |
| **Jaw** | -8 | 2 | Stunned (Body+Will 2 or -5 Init); Unable to Speak (1 hour x DV) |
| **Knee** | -8 | 1 | Stunned (Composure 2 or -10 Init); Knockdown; Slowed; Winded |
| **Neck** | -8 | 10 | Stunned (Body+Will 3 or -10 Init); Bleedout (1P unresisted per action that is not First Aid until Logic+First Aid (4) or Heal removes 1+ box) |
| **Shin** | -6 | 2 | Knockdown; Slowed; Winded |
| **Shoulder / Upper Arm** | -6 | 3 | Stunned (Body+Will 1 or -5 Init); One-Armed Bandit (limb useless for turns = DV, -6 dice); Weak Side (-2 melee Defense) |
| **Sternum** | -10 | 10 | Stunned (Body+Will 3 or -10 Init); Fatigued (Body-only resist vs half DV Stun); Winded |
| **Thigh** | -6 | 3 | Slowed; Winded |

### Vehicle Called Shots (RnG)

| Location | Mod | DV Limit | Effect |
| --- | --- | --- | --- |
| Engine block | -4 | None | Disables vehicle |
| Fuel tank / battery | -6 | None | Disables; leak |
| Axle | -6 | - | Speed to 1 |
| Antenna | -8 | - | No comms/wireless |
| Door lock | -6 | - | Door stuck |
| Window motor | -4 | - | Window stuck |

Effects apply only if damage remains after vehicle Resistance.

---

## Ammo Whammy (ammo-specific Called Shots)

Extra shots keyed to ammunition. Modifier replaces standard Called Shot mod where listed. See effect names in Location / Core sections for full effect text.

| Shot | Mod | DV Limit | Effect | Ammo |
| --- | --- | --- | --- | --- |
| **Bellringer** | -8 | 4 | Stunned (-10 Init) | Gel |
| **Bulls-Eye Double-Tap/Burst** | -4 | None | AP x bullets in burst (max x3 base AP) | APDS |
| **Down the Gullet** | -8 | 2 | +2 Toxin Power | Capsule |
| **Extreme Intimidation!** | -4 | 0 | Composure (net hits) or -10 Init | Assault Cannon |
| **Finger Popper** | -4 | 2 | Enhanced Blast out of Hands: base DV resisted with Body, max 2; +1 m thrown | Explosive, Gel, Hollow Points |
| **Flame On!** | -6 | 1 | Light 'em Up (ignite flammables) | Tracer |
| **Flash Blind** | -6 | 2 | Blinded (-8 next Action Phase; no vision Perception 10 Combat Turns) | Flare |
| **Here's Muck in Your Eye!** | -4 | 0 | Enhanced Dirty Trick (-5 next action) | Explosive, Frangible, Hollow Points |
| **Hit 'em Where It Counts** | -6 | 1 | +2 Toxin Power; Speed -1 category | Injection Dart |
| **Light 'em Up** | -10 | 1 | Ignite flammables | Flare, Gyrojet |
| **More Muck, Better Duck!** | -4 | 0 | Enhanced Dirty Trick (-6) | EX-Explosive |
| **Nasty Finger Prick** | -4 | 2 | Enhanced Blast out of Hands (max 2 DV) | Flechette |
| **On Pins and Needles** | -4 | 0 | Rough Terrain (1 shot/m², half Move; barefoot 3P vs Body) | Flechette |
| **Ricochet Shot** | -6 | None | Intimidating Strike: Composure (2) or -1 shaken | Gel, Gyrojet |
| **Shake, Rattle, and BOOM!** | -4 | 0 | Enhanced Shake Up (-8 Init) | EX-Explosive |
| **Shake, Rattle, and Pop!** | -4 | 0 | Enhanced Shake Up (-6 Init) | Explosive |
| **Shredded Flesh** | -4 | 10 | Bleedout (1P unresisted per non-FA action until FA (4) or Heal) | Flechette |
| **Spinner** | -4 | 2 | Dirty Trick (-4 next Phase) | Gel, Gyrojet |
| **Tag!** | -4 | 0 | No damage; embeds in armor | Tracker |
| **That Hit the Spot!** | varies | varies | Localized: Eye Blinded; Ear Deafened; Arm/Hand drop item; Leg/Foot Agility (2) or prone | AV, Gyrojet Taser, Stick'n'Shock, Taser Dart |
| **Through and Through ... and Into** | -(Armor + 1/2 Body of front target) | 1 front / none rear | Rear target takes all but 1 DV; both defend | APDS, Gauss Rifle |
| **Troll Finger Popper** | -4 | 3 | Enhanced Blast out of Hands (max 3; +2 m thrown) | EX-Explosive |
| **Up the Ante** | varies | varies | Doubles location DV Limit | Assault Cannon, AV |
| **Warning Shot** | -6 | 1 | Intimidating Strike: Composure (4) or attitude shift | Injection Dart |

### Called Shots by ammo type (index)

| Ammo | Shots available |
| --- | --- |
| APDS | Bulls-Eye Double-Tap/Burst, Through and Through ... and Into |
| Assault Cannon | Extreme Intimidation!, Up the Ante |
| AV | That Hit the Spot!, Up the Ante |
| AV Assault Cannon | Up the Ante |
| Capsule | Down the Gullet |
| Explosive | Finger Popper, Here's Muck in Your Eye!, Shake Rattle and Pop! |
| EX-Explosive | More Muck Better Duck!, Shake Rattle and BOOM!, Troll Finger Popper |
| Flechette | Nasty Finger Prick, On Pins and Needles, Shredded Flesh |
| Flare | Flash Blind, Light 'em Up |
| Frangible | Here's Muck in Your Eye! |
| Gauss Rifle | Through and Through ... and Into |
| Gel | Bellringer, Finger Popper, Spinner, Ricochet Shot |
| Gyrojet | Light 'em Up, Ricochet Shot, Spinner |
| Gyrojet Plus | Finger Popper, Here's Muck, Shake Rattle and Pop! |
| Gyrojet Taser | That Hit the Spot! |
| Gyrojet Tracker | Tag! |
| Hollow Points | Finger Popper, Here's Muck in Your Eye! |
| Injection Dart | Hit 'em Where It Counts, Warning Shot |
| Stick'n'Shock | That Hit the Spot! |
| Taser Dart | That Hit the Spot! |
| Tracer | Flame On! |
| Tracker | Tag! |

**Miracle Shot** (1 Edge): remove 4 points of Called Shot penalties. See `../Edge.md`.

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

### Enhanced Suppression (RnG)

Complex Action variant. Zone end width **5 m** (not 10). Targets **cannot** use Free Drop Prone to avoid the Reaction+Edge test (Lucky Cover Edge still works). Normal suppress penalties still apply.

### Flechette Suppressive Fire (RnG)

Complex; no width loss; Drop Prone cannot avoid. Choke tables modify DV, Accuracy, Defense, and extra width by range:

**Medium spread**

| Range | DV adj | Acc adj | Def adj | Extra width |
| --- | --- | --- | --- | --- |
| Short | -1 | - | -3 | 4 m |
| Medium | -3 | - | -3 | 8 m |
| Long | -5 | -1 | -3 | 12 m |
| Extreme | -7 | -1 | -3 | 16 m |

**Wide spread**

| Range | DV adj | Acc adj | Def adj | Extra width |
| --- | --- | --- | --- | --- |
| Short | -3 | - | -5 | 6 m |
| Medium | -5 | - | -5 | 12 m |
| Long | -7 | -1 | -5 | 18 m |
| Extreme | -9 | -1 | -5 | 24 m |

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

- Core Called Shots + RnG location/ammo/MA shots + suppression variants: complete for agent use.
- Martial Arts technique discounts: [Martial Arts](Martial%20Arts.md).
- New combat actions (Clinch, Finishing Move, etc.): [Action Economy](Action%20Economy.md).
- Barriers / shooting through: [Barriers](../Barriers.md).
