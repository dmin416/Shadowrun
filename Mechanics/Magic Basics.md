# Magic Basics

Agent reference (SR5). LLM layout; spellcasting, Drain, traditions, conjuring, astral, adepts, mana barriers; background-count pointer.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Magic chapter ~p.276-324 (basics, sorcery, conjuring, astral, barriers)
**Source Text:** `17 - Magic.md`
**See also:** [Dice and Tests](Dice%20and%20Tests.md) · [Healing and Injuries](Healing%20and%20Injuries.md) (Heal / Stabilize) · [Character Creation/Magic and Resonance](Character%20Creation/Magic%20and%20Resonance.md) · Encyclopedia Magical Goods · *Street Grimoire* / *Forbidden Arcana*

**Scope:** Force/Drain; hermetic vs shamanic Drain attrs + spirit affinities; Spellcasting steps; direct vs indirect combat; Summon / Bind / Banish; Astral Perception / Projection / Assensing; mana barriers; Power Points; noticing magic
**Out of scope:** Full spell/ritual/spirit-stat catalogs; initiation metamagics; detailed background count tables (Street Grimoire)

## Inventory (completeness checklist)

- [x] Spellcasting + Drain; traditions
- [x] Spirits summon/bind/banish; Edge (summoner)
- [x] Astral perception/projection; wards
- [x] Adepts PP; background count / mana issues

---

## Schema

| Token | Meaning |
| --- | --- |
| Force | Spell/spirit power; often the Limit |
| Drain | Stun (or Physical if overcast / high Force); resist with tradition attrs |
| Overcast | Hits (not net) after Limit > Magic → Physical Drain |
| Service | What a spirit owes; lost at sunrise/sunset if only summoned |

---

## Magical skills

| Group | Skills |
| --- | --- |
| Sorcery | Spellcasting, Counterspelling, Ritual Spellcasting |
| Conjuring | Summoning, Binding, Banishing |
| Enchanting | Alchemy, Artificing, Disenchanting |

**Force:** Choose up to **Magic × 2** for spells/spirits. Higher Force = stronger effect + worse Drain.

**Drain:** Cannot be healed by magic or medkits; only natural recovery. Minimum DV usually **2**.

**Astral Limit:** Inherent Limit for many astral tests.

---

## Traditions (Core)

| Tradition | Drain resist | Spirit affinities (category) |
| --- | --- | --- |
| Hermetic | Logic + Willpower | Combat Fire, Detection Air, Health Man, Illusion Water, Manipulation Earth |
| Shamanic | Charisma + Willpower | Combat Beasts, Detection Water, Health Earth, Illusion Air, Manipulation Man |

More traditions: Street Grimoire / Forbidden Arcana.

**Lodges:** Force × 500¥ materials; days = Force to raise. Acts as mana barrier keyed to you. Temporary lodge via reagents possible.

---

## Spellcasting

1. Choose spell (must know it).
2. Choose Force (Limit; ≤ Magic × 2).
3. Complex Action (or Reckless Simple: +3 Drain; two Simple spells in one Phase both get +3).
4. Spellcasting + Magic [Force] ± mods (wounds, sustained spells **-2 each**, visibility for LOS spells).
5. Resolve opposed/threshold per spell; effect applies even if Drain drops you.
6. Resist Drain (tradition pool).

**Multi-spell:** Split Spellcasting + Magic among spells (min 1 die each); modifiers after split; max spells = Magic.

**Targeting:** Natural vision / Essence-paid cybereyes OK. Digitized feeds (cameras, Matrix) cannot provide LOS for most spells. Indirect combat can be "fire and forget" with clear path.

**Physical Drain:** If hits (after Limit) **> Magic**, Drain is Physical.

### Combat spell patterns

| Type | Opposed | Damage |
| --- | --- | --- |
| Direct | Spellcasting + Magic [Force] vs Body (physical) or Willpower (mana) | Net hits boxes; no separate Damage Resistance |
| Indirect | Spellcasting + Magic [Force] vs Reaction + Intuition | DV = Force + net hits; AP = -(Force); resist Body + Armor |

### Noticing magic

Perception + Intuition [Mental]; threshold = caster Skill - Force (or 6 - Force if no skill), min 1. +2 if you have a magic Active/Knowledge skill. Obvious fireballs need no roll.

---

## Conjuring

### Summon (Complex)

1. Spirit type of your tradition; Force ≤ Magic × 2. Optional powers: 1 per 3 full Force.
2. Summoning + Magic [Force] vs Force. Net hits = services. Reagents can set Limit.
3. Drain DV = **2 × spirit's hits** (not net), min 2. Physical if Force > Magic.

Spirit hangs until services done or **sunrise/sunset**. One summoned spirit at a time.

**Team summon:** Teamwork; all resist same Drain; only leader commands.

### Bind

Already-summoned spirit; **1 hour × Force**; reagents **Force × 25** drams. Binding + Magic [Force] vs Force × 2. Drain = 2 × spirit hits, min 2. Extra net hits add services. Bound spirits resent long control (tradition flavor).

### Banish (Complex)

Banishing + Magic [Astral] vs Force (+ summoner's Magic if bound). Each net hit removes 1 service; at 0 the spirit leaves next action. Drain = 2 × defense hits, min 2; Physical if Force > Magic. You may try to re-Summon a free spirit before it goes.

**Edge:** Summoner's Edge can apply to conjuring tests like other Magician tests ([Edge](Edge.md)); spirits do not spend the summoner's Edge for free.

Disruption (filling a spirit Condition Monitor) sends it home and **loses remaining services**.

---

## Astral

### Astral Perception

Dual-natured while perceiving; **-2** to physical actions. Assensing + Intuition [Astral] for detail (Assensing Table: health/emotion at 1 hit through Exact Essence/Magic/Force at 4+). Magicians and adepts with Astral Perception power only (among metahumans).

### Astral Projection

Full Magicians only. Body comatose; astral form uses mental attributes. Fast travel blur vs "Walk" 100 m/Turn / "Run" 5 km/Turn. Earth is solid; high altitude dangerous. Mana spells affect astral; weapon foci need astral presence to hit astral forms. Manifest (Complex): ghostly visible/audible, no physical interaction / no physical spell targeting; Magic × 5 minutes per projection.

### Mana barriers / wards

Block spells and astral forms. Casting through: add barrier Force to defense/resistance (or oppose Force if no opposed pool). Lodge, Ward ritual, Mana Barrier spell, Circle of Protection. Creator passes freely. Adept innate powers generally ignore barriers.

---

## Adepts

**Power Points** = Magic at chargen (mystic adepts buy PP with Karma). +1 PP when Magic rises (adepts); or take PP instead of metamagic at initiation. Essence loss that drops Magic also drops PP (un-buy powers). Magic 0 → cut off from magic.

---

## Background count / mana issues

Core emphasizes **mana barriers**, lodge Force, and tradition/reagent flavor. Full **background count** (polluted/aspected domains penalizing Magic tests) is expanded in *Street Grimoire*. When BGC is in play: treat as a penalty/threshold on Magic-linked tests per that book's table; toxic/alchera domains escalate further.

---

## Quick cheat sheet

| Task | Pool |
| --- | --- |
| Cast | Spellcasting + Magic [Force] |
| Resist Drain | Tradition Drain attrs |
| Summon | Summoning + Magic [Force] vs Force |
| Bind | Binding + Magic [Force] vs Force × 2 |
| Banish | Banishing + Magic [Astral] vs Force (+ Magic if bound) |
| Assense | Assensing + Intuition [Astral] |
