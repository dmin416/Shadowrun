# Combat - Ranged Combat

Agent reference (SR5). LLM layout; firearms, projectiles, mods, recoil, ranges.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Ranged ~p.173-185; Fire modes ~p.178-180; Range Table p.185; Defense mods ~p.189
**Source Text:** `11 - Combat.md`
**See also:** [Overview](Overview.md) · [Action Economy](Action%20Economy.md) · [Damage Armor and Wounds](Damage%20Armor%20and%20Wounds.md) · [Melee Combat](Melee%20Combat.md) · [Called Shots and Special](Called%20Shots%20and%20Special.md) · Encyclopedia firearms

**Scope:** Attack/defense pools; fire modes + defense mods; progressive recoil; environmental / situational / defense tables; Take Aim; cover; blind fire; Range Table; full shotgun choke DV/Accuracy/Defense/spread table; grenade & launcher Scatter Table + blast resolution procedure
**Out of scope:** Per-model grenade/rocket/missile DV/AP/Blast numbers (Encyclopedia); full suppression play (Called Shots); ammo types (Encyclopedia)

## Inventory (completeness checklist)

- [x] Attack pool / Accuracy Limit; Defense Rea+Int
- [x] Fire modes (SS/SA/BF/FA/LB/SB) + recoil progression
- [x] Range / environmental / attacker / defender mods tables
- [x] Take Aim; called shots pointer; cover; blind fire
- [x] Shotgun choke DV/Accuracy/Defense/spread by range band
- [x] Grenade/launcher Scatter Table + blast resolution procedure (falloff, confined space, multiple blasts)

---

## Schema

| Token | Meaning |
| --- | --- |
| Attack | Weapon Skill + Agility [Accuracy] |
| Defense | Reaction + Intuition (or Full Defense / etc.) |
| Recoil RC | Free 1 + Str/3 (up) + weapon RC of ready guns |
| Progressive recoil | Accumulates across Phases until non-shoot Simple/Complex |

---

## Basic Opposed Test

```
Attacker: Weapon Skill + Agility ± mods [Accuracy]
vs
Defender: Reaction + Intuition ± mods  (no Limit unless skill added)
```

| Result | Effect |
| --- | --- |
| Attacker more hits | Hit; net hits → +DV (or reduce scatter for thrown/launched) |
| Tie | Grazing hit ([Overview](Overview.md)) |
| Defender more | Miss |

Then Damage Resistance ([Damage Armor and Wounds](Damage%20Armor%20and%20Wounds.md) / Overview DADA).

---

## Fire modes

| Mode | Action | Rounds | Defense mod | Notes |
| --- | --- | --- | --- | --- |
| SS | Simple | 1 | 0 | No progressive recoil (unless Multiple Attacks) |
| SA | Simple | 1 | 0 | Progressive recoil |
| Semi-Auto Burst (SB) | Complex | 3 | -2 | SA weapons; Multi-Attack OK |
| Burst Fire (BF) | Simple | 3 | -2 | Multi-Attack OK |
| Long Burst (LB) | Complex | 6 | -5 | Multi-Attack OK |
| FA (Simple) | Simple | 6 | -5 | |
| FA (Complex) | Complex | 10 | -9 | |
| Suppressive Fire | Complex | 20 | Duck/cover | **Ignores recoil**; zone rules → [Called Shots and Special](Called%20Shots%20and%20Special.md) |

| Rule | Detail |
| --- | --- |
| One attack Simple | Cannot combine with another attack Simple same Phase |
| Dual wield | Multiple Attacks Free; off-hand -2; bullets from **both** count for recoil |
| Short ammo | Reduce each defense mod by 1 per missing bullet (FA Complex short 3 → -6 not -9) |
| Suppress short | Width -1 m per 2 bullets short |

---

## Progressive recoil

| Step | Rule |
| --- | --- |
| RC pool | **1 free** (when you start firing) + **Strength ÷ 3** (round up) + RC of each **ready** gun (loaded, in hand) |
| This Phase | RC - (bullets about to fire). If negative → that many dice off attack pool |
| Multi-attack same Phase | Total bullets first; apply penalty **before** splitting pools |
| Accumulate | Keeps building across Phases/Turns while you keep shooting |
| Reset | Take (or are forced into) a Simple or Complex that is **not** shooting → RC resets |
| Take Aim | Non-shoot → resets progressive recoil |
| SS mode | No progressive recoil between SS shots |
| Vehicle mount | Mount RC = vehicle Body + weapon RC |

Two-gun: add RC of both ready guns; bullets from both add to the same progressive total (on the character).

---

## Environmental modifiers

Take the **worst** single category (Visibility, Light/Glare, Wind, Range). If **two or more** tied at that worst severity → bump one category worse. Two+ at -6 row → **-10**.

| Severity | Visibility | Light/Glare | Wind | Range | Mod |
| --- | --- | --- | --- | --- | --- |
| None | Clear | Full / no glare | None/light breeze | Short | 0 |
| Mild | Light rain/fog/smoke | Partial / weak glare | Light winds | Medium | -1 |
| Bad | Moderate rain/fog/smoke | Dim / moderate glare | Moderate winds | Long | -3 |
| Severe | Heavy rain/fog/smoke | Total dark / blinding glare | Strong winds | Extreme | -6 |
| Extreme combo | Two+ conditions at -6 row | | | | -10 |

Apply vs what the **shot** experiences (e.g. target in dark cave → darkness even if shooter stands in sun).

### Compensation (shift rows up / reduce)

| Gear / effect | Helps |
| --- | --- |
| Flare compensation | Glare 2 rows up |
| Image magnification | Range 1 category better (**needs Take Aim** to enable) |
| Low-light | Partial/Dim as Full Light |
| Thermographic | Visibility + Light 1 row up (not thermal smoke for Visibility) |
| Tracer rounds (FA) | Wind below Light and Range below Short: 1 row up |
| Smartlink | Wind 1 row up |
| Sunglasses | Glare 1 up / Light 1 **down** |
| Ultrasound | Visibility 1 up; ignore Light within 50 m |

---

## Situational modifiers (attacker)

| Situation | Attacker DP |
| --- | --- |
| Firing from cover with imaging device | -3 |
| Firing from moving vehicle (unmounted) | -2 |
| Attacker in melee | -3 |
| Attacker running | -2 |
| Off-hand weapon | -2 |
| Wounded | -wound |
| Blind fire | -6 (not cum. with Total Darkness; extra -4 if also strong wind or extreme range) |
| Called shot | -4 (+ Free Action) |
| Take Aim (each) | +1 DP **or** +1 Accuracy (choose one per Aim); wireless smartgun Aim: **both** |
| Wireless smartgun | +1 gear / +2 implanted (attack bonus; separate from Aim) |

### Take Aim (Simple)

| Rule | Detail |
| --- | --- |
| Cumulative | Stack over Phases/Turns |
| Lost if | Any other action before attack (**including Free**) |
| Cap | Bonus (to pool **or** Accuracy track) ≤ half Willpower (round up) |
| Image mag / scope | First Take Aim enables mag; that first Aim gives **no** extra +1 beyond enabling |

Called shot effects: [Called Shots and Special](Called%20Shots%20and%20Special.md).

---

## Defense modifiers (ranged-relevant)

| Situation | Defense DP |
| --- | --- |
| Inside moving vehicle | +3 |
| Prone | -2 (ranged: only if attacker ≤5 m) |
| Unaware / surprised | **No defense** (Success Test); cover may still give cover dice |
| Wounded | -wound |
| Defended vs prior attack since last Phase | -1 per extra defense |
| Flechette shotgun narrow / medium / wide | -1 / -3 / -5 |
| FA Complex (10) | -9 |
| LB or FA Simple (6) | -5 |
| BF or SA Burst (3) | -2 |
| In melee, targeted by ranged | -3 |
| Running | +2 |
| Good Cover | +4 |
| Partial Cover | +2 |
| Area-effect attack | -2 |
| Full Defense | +Willpower (Interrupt -10 Init; whole Turn) |

| Cover | Rule |
| --- | --- |
| Partial | >25% up to 50% obscured → +2 Defense (ranged + Indirect Combat spells with Defense) |
| Good | Better cover → +4 |
| Take Cover | Simple Action (not if surprised) |
| Tie vs cover | Tie on Opposed Test hits target **through** cover if attack penetrates the barrier (Barriers) |

### Shooting into melee

If defender **wins** the Opposed Test, attacker's **allies in that melee** must Defense vs the attacker's hits (same penalties, incl. -3 in melee). Someone may eat the round.

---

## Range Table (meters)

Range env mods: Short 0, Medium -1, Long -3, Extreme -6 (after compensation).

### Pistols

| Weapon | Short | Medium | Long | Extreme |
| --- | --- | --- | --- | --- |
| Taser | 0-5 | 6-10 | 11-15 | 16-20 |
| Hold-Out / Light Pistol | 0-5 | 6-15 | 16-30 | 31-50 |
| Heavy Pistol | 0-5 | 6-20 | 21-40 | 41-60 |

### Automatics

| Weapon | Short | Medium | Long | Extreme |
| --- | --- | --- | --- | --- |
| Machine Pistol | 0-5 | 6-15 | 16-30 | 31-50 |
| SMG | 0-10 | 11-40 | 41-80 | 81-150 |
| Assault Rifle | 0-25 | 26-150 | 151-350 | 351-550 |

### Longarms

| Weapon | Short | Medium | Long | Extreme |
| --- | --- | --- | --- | --- |
| Shotgun (flechette) | 0-15 | 16-30 | 31-45 | 45-60 |
| Shotgun (slug) | 0-10 | 11-40 | 41-80 | 81-150 |
| Sniper Rifle | 0-50 | 51-350 | 351-800 | 801-1,500 |

### Heavy

| Weapon | Short | Medium | Long | Extreme |
| --- | --- | --- | --- | --- |
| LMG | 0-25 | 26-200 | 201-400 | 401-800 |
| MMG/HMG | 0-40 | 41-250 | 251-750 | 751-1,200 |
| Assault Cannon | 0-50 | 51-300 | 301-750 | 751-1,500 |
| Grenade Launcher | 5-50* | 51-100 | 101-150 | 151-500 |
| Missile Launcher | 20-70* | 71-150 | 151-450 | 451-1,500 |

\* Launcher minimum range rules apply (Core).

### Projectiles / thrown

| Weapon | Short | Medium | Long | Extreme |
| --- | --- | --- | --- | --- |
| Bow | 0-STR | to STR×10 | to STR×30 | to STR×60 |
| Light / Med / Heavy Crossbow | 0-6 / 0-9 / 0-15 | 7-24 / 10-36 / 16-45 | 25-60 / 37-90 / 46-120 | 61-120 / 91-150 / 121-180 |
| Thrown Knife | 0-STR | to STR×2 | to STR×3 | to STR×5 |
| Shuriken | 0-STR | to STR×2 | to STR×5 | to STR×7 |
| Grenade (standard) | 0-STR×2 | to STR×4 | to STR×6 | to STR×10 |
| Grenade (aerodynamic) | 0-STR×2 | to STR×4 | to STR×8 | to STR×15 |

Ready Agility÷2 knives or shuriken per Ready Weapon.

---

## Shotguns (choke settings)

Slug rounds use the weapon's listed DV. Shot (flechette) rounds apply the flechette ammunition rules to that DV. Changing choke: **Simple Action** (**Free Action** if smartlinked, or via Change Linked Device Mode Free Action with DNI).

DV/Accuracy mods apply to the **shooter's** roll; Defense mod applies to **each** target's Defense. "Max targets / spread" = that many targets within a spread of that width can be attacked with the **same** roll (compare the attacker's hits vs each target's modified Defense separately). Only Narrow Spread may be used with Called Shots.

### Narrow Spread

Single target only, all ranges.

| Range | DV mod | Accuracy mod | Target Defense mod |
| --- | --- | --- | --- |
| Any | 0 | 0 | -1 |

### Medium Spread (no Called Shots)

| Range | DV mod | Accuracy mod | Target Defense mod | Max targets | Spread width |
| --- | --- | --- | --- | --- | --- |
| Short | -1 | 0 | -3 | 2 | 2 m |
| Medium | -3 | 0 | -3 | 3 | 4 m |
| Long | -5 | -1 | -3 | 4 | 6 m |
| Extreme | -7 | -1 | -3 | 6 | 8 m |

### Wide Spread (no Called Shots)

| Range | DV mod | Accuracy mod | Target Defense mod | Max targets | Spread width |
| --- | --- | --- | --- | --- | --- |
| Short | -3 | 0 | -5 | 2 | 3 m |
| Medium | -5 | 0 | -5 | 3 | 6 m |
| Long | -7 | -1 | -5 | 4 | 9 m |
| Extreme | -9 | -1 | -5 | 6 | 12 m |

---

## Grenades and launched explosives

### Throwing / launching

| Type | Action | Hit test | Result |
| --- | --- | --- | --- |
| Thrown grenade | Throw Weapon (Simple) | Throwing + Agility [Physical] (3), modified for range/conditions | Meet/beat threshold (3 net hits) → lands exactly where aimed. Short of threshold → scatters (below); a low scatter roll can still land it close |
| Launched grenade / rocket / missile | Fire Weapon (Simple) | Heavy Weapons + Agility [Accuracy] (3), modified for range/conditions | Same success/scatter logic, then resolve Blast Effects |

**Launcher minimum range:** 5 m (grenades) / 10 m (rockets, missiles) - the projectile does not arm until it has traveled that far (safety feature). Disable with Armorer + Logic [Mental] (4, 5-10 minutes) Extended Test.

### Determine Scatter

If the throw/launch misses its landing spot, roll **2D6** for direction (7 = continues straight past the target away from the thrower; 2 or 12 = bounces straight back toward the thrower; other results scatter to that clock-position side). Then roll the dice below for **distance**, reducing the roll by the attacker's hits on the attack roll. Distance ≤ 0 = direct hit on the intended spot.

#### Scatter Table

| Type | Scatter distance |
| --- | --- |
| Standard grenade | (1D6 - hits) m |
| Aerodynamic grenade | (2D6 - hits) m |
| Grenade Launcher | (3D6 - hits) m |
| Missile Launcher | (4D6 - hits) m |
| Rocket Launcher | (5D6 - hits) m |

### Detonation triggers

| Trigger | Rule |
| --- | --- |
| Built-in Timer | Detonates on the thrower's/firer's own Initiative Score in the **next** Combat Turn, at (Score when thrown/fired) **- 10**, regardless of later Score changes |
| Motion Sensor | Arms ~1 second after activation (thrown) or after traveling 5 m (launched). Explodes on any sudden stop/impact. If the attack roll **missed** (no net hits): roll full Scatter distance, then it explodes immediately at that spot. **Glitch** on the attack roll → does not detonate on impact; scatter distance is **doubled**, then it explodes. **Critical Glitch** → detonates immediately at the thrower/firer |
| Wireless Link | Thrower/firer (or anyone with a mark on it) can detonate remotely. With DNI: Change Wireless Device Mode Free Action, and this **reduces scatter**. Without DNI: Change Linked Device Mode Simple Action on this or a later Action Phase; scatter is **not** reduced |

### Blast Effects

1. Determine the blast point (direct hit or scattered landing spot, above).
2. The item's base **DV** and **Blast** rating (DV lost per meter from the blast point) come from its stat line - see [Encyclopedia/Grenades and Explosives](../../Encyclopedia/Grenades%20and%20Explosives.md) for per-model numbers (frag, HE, AV, flash-bang, gas/smoke, etc.). Some items instead print a flat **"X m Radius"**: full listed effect anywhere inside that radius, none beyond it.
3. For a per-meter Blast rating: **DV at range r = base DV - (Blast x r)**, minimum 0.
4. Everyone caught in the blast resists the DV at their distance with **Body + Armor** ([Damage Armor and Wounds](Damage%20Armor%20and%20Wounds.md)) as a normal Damage Resistance Test. Blast is **not** an Opposed Test - there is no Defense roll and no cover Defense bonus against it, though physical barriers between the target and the blast point still apply their own rules (below).

#### Blasts in a confined space

If the surrounding walls/barriers **hold** against the blast (Barriers), the shockwave reflects back rather than escaping. A character caught by both the outbound and the rebounding wave takes the **combined** DV of both hits; repeated bounces off multiple surfaces in a small room can stack further ("chunky salsa effect").

#### Multiple simultaneous blasts

If two or more blasts hit the same character on the **same Initiative Score**, add **half** the value of the lower DV(s) to the highest DV and resist that as one modified DV. For AP, use the **best** AP among them, improved by **1** per additional explosion.

#### Explosive vs. barriers

Placed/bulk explosive Blast falloff: circular blast **-2/m**, directional (up to 60 degree arc) **-1/m** (default AP -2, halved target Armor if charge is in contact). See [Barriers](../Barriers.md) for Structure/Armor resolution and [Encyclopedia/Grenades and Explosives](../../Encyclopedia/Grenades%20and%20Explosives.md) for the full explosives formula and per-item stats.

---

## Coverage notes

- Core ranged attack engine + Range Table + mode/recoil tables: complete for this page.
- Shotgun choke: full per-range DV/Accuracy/Defense/spread table above (Core-complete).
- Grenade/launcher Scatter Table + detonation triggers + blast falloff/resistance/confined-space/multi-blast procedure: complete above. Per-model DV/AP/Blast numbers live in Encyclopedia (not duplicated here to avoid drift).
- Suppression zone / Reaction+Edge: [Called Shots and Special](Called%20Shots%20and%20Special.md).
