# Barriers

Agent reference (SR5). Structure/Armor barriers, shooting through, destroying, body-as-cover, fence toppers.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Barriers ~p.197-198; security fencing ~p.363
**Source Text:** `11 - Combat.md` · security devices in GM/Security chapter
**See also:** [Combat/Ranged Combat](Combat/Ranged%20Combat.md) · [Combat/Damage Armor and Wounds](Combat/Damage%20Armor%20and%20Wounds.md) · [Combat/Called Shots and Special](Combat/Called%20Shots%20and%20Special.md) · [Security and Surveillance](../Encyclopedia/Security%20and%20Surveillance.md)

**Scope:** Barrier ratings; Condition Monitor; shooting through; destroying; penetration weapons; body barriers; fence-top damage
**Out of scope:** Full facility sensor suite procedures (Encyclopedia / GM chapter depth)

## Inventory

- [x] Barrier Ratings table
- [x] Shooting through / Blind Fire interaction
- [x] Destroying Barriers + Damaging Barriers table
- [x] Penetration Weapons multi-bullet
- [x] Body Barriers
- [x] Fence toppers (barbed / concertina / monowire / electrified)

---

## Schema

| Token | Meaning |
| --- | --- |
| Structure | Barrier "Body"; boxes per ~1 m² × ~10 cm thickness = Structure |
| Armor | Barrier armor; compared to modified DV for pierce |
| Penetration weapon | Firearm / pointed blade: barrier takes few boxes; rest transfers |

Barriers ignore **Stun** damage.

---

## Barrier Ratings

| Barrier | Structure | Armor | Examples |
| --- | --- | --- | --- |
| Fragile | 1 | 2 | Standard glass |
| Cheap Material | 2 | 4 | Drywall, plaster, door, regular tire |
| Average Material | 4 | 6 | Furniture, plastiboard, ballistic glass |
| Heavy Material | 6 | 8 | Tree, hardwood, dataterm, light post, chain link |
| Reinforced Material | 8 | 12 | Densiplast, security door, armored glass, Kevlar wallboard |
| Structural Material | 10 | 16 | Brick, plascrete |
| Heavy Structural Material | 12 | 20 | Concrete, metal beam |
| Armored/Reinforced Material | 14 | 24 | Reinforced concrete |
| Hardened Material | 16+ | 32+ | Blast bunkers |

Condition Monitor: Structure boxes per square meter (~10 cm thick).

---

## Shooting Through Barriers

| Situation | Rule |
| --- | --- |
| Cover | Defender using barrier as cover gets cover defense bonus |
| Fully hidden | Attacker −6 Blind Fire; defender unaware of attack |
| Transparent (e.g. ballistic glass) | No cover/sight block, but must penetrate |
| Pierce check | Modified DV must **≥** barrier Armor (after AP). Else attack fails vs barrier |
| Barrier resists first | Structure + Armor vs damage; unresisted damage to Structure |
| Excess | If damage exceeds Structure, remainder transfers to target behind |

---

## Penetration Weapons

Firearms and pointed blades (GM: primarily penetrating):

| Bullets in attack | Boxes to barrier (unresisted) |
| --- | --- |
| 1 | 1 (or 0 at GM discretion) |
| 3 | 2 |
| 6 | 3 |
| 10 | 4 |

Subtract those boxes from DV passed to the target behind. Only if modified DV ≥ barrier Armor; else stopped cold.

---

## Destroying Barriers

| Step | Rule |
| --- | --- |
| Attack | Unopposed (barriers don't dodge). Hits add to DV; 0 hits = base DV only. Critical glitch = miss the barn |
| Demolitions | May use Demolitions with time + materials |
| DV adjust | See Damaging Barriers table before Resistance |
| Resist | Structure + Armor (ignore Stun) |
| Hole | Remaining DV ≥ Structure → hole **1 m²** per Structure increment (e.g. 30 damage vs Structure 15 = 2 m²) |

### Damaging Barriers

| Weapon | DV Modifier |
| --- | --- |
| Melee or unarmed | No change |
| Projectiles and bullets | Use Penetration Weapons |
| Explosive in contact | Base DV × 2 |
| AV rocket/missile | Base DV × 2 |
| Combat spell | No change |

Confined grenade blast: if walls hold (this section), channel blast; else normal blast (grenade/launcher blast resolution: [Ranged Combat](Combat/Ranged%20Combat.md)).

---

## Body Barriers

Living/dead body as cover: **Body** replaces Structure; Armor normal. Damage applies to the body first. Carrier: −Agility and −Reaction equal to (shield Body − carrier Strength) while carrying.

---

## Fence toppers

Climbing past fence-top wiring: Climbing + Agility **(3)**; fail → take damage (Body + Armor). Mats over wire/electric fence allow climb without that damage.

| Type | Perception threshold to spot | Damage on fail |
| --- | --- | --- |
| Barbed | 1 | 4P |
| Concertina | 1 | 5P |
| Electrified | 2 | 6S (electricity rules) |
| Monowire | 3 | 8P |
