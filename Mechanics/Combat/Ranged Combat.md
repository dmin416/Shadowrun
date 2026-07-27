# Combat - Ranged Combat

Agent reference (SR5). LLM layout; firearms, projectiles, mods, recoil, ranges.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Ranged ~p.173-185; Fire modes ~p.178-180; Range Table p.185; Defense mods ~p.189
**Source Text:** `11 - Combat.md`
**See also:** [Overview](Overview.md) · [Action Economy](Action%20Economy.md) · [Damage Armor and Wounds](Damage%20Armor%20and%20Wounds.md) · [Melee Combat](Melee%20Combat.md) · [Called Shots and Special](Called%20Shots%20and%20Special.md) · Encyclopedia firearms

**Scope:** Attack/defense pools; fire modes + defense mods; progressive recoil; environmental / situational / defense tables; Take Aim; cover; blind fire; Range Table; shotgun choke; grenade/scatter pointer
**Out of scope:** Full blast/scatter geometry depth (summary only); full suppression play (Called Shots); ammo types (Encyclopedia)

## Inventory (completeness checklist)

- [x] Attack pool / Accuracy Limit; Defense Rea+Int
- [x] Fire modes (SS/SA/BF/FA/LB/SB) + recoil progression
- [x] Range / environmental / attacker / defender mods tables
- [x] Take Aim; called shots pointer; cover; blind fire

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

## Shotguns (flechette choke)

Slug = listed DV. Shot = flechette ammo rules on weapon DV. Change choke: Simple (Free if smartlink).

| Choke | Summary |
| --- | --- |
| Narrow | Target -1 Defense all ranges |
| Medium | DV and multi-target by range; Defense -3; **no** Called Shots |
| Wide | Heavier DV penalties; Defense -5; wider spreads; **no** Called Shots |

(Exact DV/-Accuracy by range: Core shotgun choke section.)

---

## Grenades / launchers (pointer)

| Type | Hit test | Scatter |
| --- | --- | --- |
| Thrown grenade | Throwing + Agility [Physical] (3) | Miss → Scatter Table; net hits reduce scatter |
| Launched grenade/rocket/missile | Heavy Weapons + Agility [Accuracy] (3) | Same; then blast |

Detonation: timer (next Turn, Score -10), motion (dangerous), wireless (DNI Free / else Simple). Blast effects: Damage / Street Gear.

---

## Coverage notes

- Core ranged attack engine + Range Table + mode/recoil tables: complete for this page.
- Shotgun choke: Defense mods on this page; per-range DV/Accuracy/spread widths remain in Core choke section.
- Suppression zone / Reaction+Edge: Called Shots and Special.
- Full scatter diagram / blast: Damage or Vehicles when expanded.
