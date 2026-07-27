# Character Creation - Skills

Agent reference (SR5). LLM layout; Priority skill spend + Knowledge/Language + groups.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Chargen Step Five ~p.88-90; Skills chapter groups/links ~p.128-151
**Source Text:** `08 - Creating A Shadowrunner.md` · `09 - Skills.md`
**See also:** [Priority System](Priority%20System.md) · [Overview](Overview.md) · [Attributes](Attributes.md) · `../Dice and Tests.md`

**Scope:** Priority individual/group points; max ratings; specializations; Knowledge free formula; categories; skill groups; Active skills by linked Attr; Mag/Res free skills note
**Out of scope:** Full per-skill Default/specialization lists (Skills chapter / future Skills Reference); use-in-play social/stealth procedures

## Inventory (completeness checklist)

- [x] Priority skill/group points; buy rules; max 6 (7 Aptitude)
- [x] Free Knowledge/Language (Int+Log)×2; native N; Bilingual
- [x] Knowledge categories + linked Attr
- [x] Full skill groups list; Active skills by linked Attr
- [x] Specializations (+2; not on groups); no group+same skill duplicate
- [x] Restricted skills / default italic pointer (explicit Default: No list)

---

## Schema

| Token | Meaning |
| --- | --- |
| Skill points | Priority Skills first number (individual) |
| Group points | Priority Skills second number |
| Rating | 1-6 at chargen (7 skill with Aptitude) |
| N | Native language (no numeric rating) |

---

## Priority Skills column

| Pri | Individual / Groups |
| --- | --- |
| A | 46 / 10 |
| B | 36 / 5 |
| C | 28 / 2 |
| D | 22 / 0 |
| E | 18 / 0 |

| Rule | Detail |
| --- | --- |
| Individual buy | 1 point → gain skill at 1 **or** +1 to a skill |
| Group buy | 1 group point → +1 to a skill group rating (all skills in group = group rating) |
| No convert | Group points ≠ individual points |
| Spend all | Must spend all skill and group points at creation |
| Max | Skill or group ≤ **6**; skill ≤ **7** with Aptitude. Groups never 7 |
| Post-chargen max | 12 (skill 13 with Aptitude) |
| Mag/Res free skills | From Mag/Res Priority: **already paid**; do not spend these points on them |
| Duplicate ban | Do not buy an individual skill already covered by a purchased group |

### Specializations (Step Five)

| Rule | Detail |
| --- | --- |
| Cost | **1** skill point |
| Effect | +2 DP when specialization applies |
| Cap | One specialization per skill from points at chargen |
| Groups | **Cannot** specialize a skill group. Specializing a skill **inside** a group **breaks** the group permanently (only allowed in leftover Karma Step 7, not Step Five) |

---

## Knowledge and Language (free)

| Rule | Detail |
| --- | --- |
| Free points | **(Intuition + Logic) × 2** using **unaugmented** attrs |
| Spend | 1 free point = 1 rank Knowledge or Language |
| Native | One Language at **N** free. Bilingual quality → second native free |
| Max at chargen | Knowledge / Language rating ≤ **6** |
| Extra | May also spend Priority individual skill points on Knowledge/Language |

### Knowledge categories

| Category | Linked Attr | Examples |
| --- | --- | --- |
| Academic | Logic | Biology, History, Magic Theory, Politics |
| Interests | Intuition | Sports, music, hobbies, trideo |
| Professional | Logic | Law, Business, Journalism, Military Service |
| Street | Intuition | Gangs, fixers, Mr. Johnsons, smuggling |

Language linked Attr: **Intuition**.

---

## Skill groups (complete Core list)

| Skill Group | Skills |
| --- | --- |
| Acting | Con, Impersonation, Performance |
| Athletics | Gymnastics, Running, Swimming |
| Biotech | Biotechnology, Cybertechnology, First Aid, Medicine |
| Close Combat | Blades, Clubs, Unarmed Combat |
| Conjuring | Banishing, Binding, Summoning |
| Cracking | Cybercombat, Electronic Warfare, Hacking |
| Electronics | Computer, Hardware, Software |
| Enchanting | Alchemy, Artificing, Disenchanting |
| Engineering | Aeronautics Mechanic, Automotive Mechanic, Industrial Mechanic, Nautical Mechanic |
| Firearms | Automatics, Longarms, Pistols |
| Influence | Etiquette, Leadership, Negotiation |
| Outdoors | Navigation, Survival, Tracking |
| Sorcery | Counterspelling, Ritual Spellcasting, Spellcasting |
| Stealth | Disguise, Palming, Sneaking |
| Tasking | Compiling, Decompiling, Registering |

---

## Active skills by linked attribute

Exotic skills are specific (taken per weapon / vehicle type).

| Attr | Skills |
| --- | --- |
| Agility | Archery, Automatics, Blades, Clubs, Escape Artist, Exotic Melee Weapon (Specific), Exotic Ranged Weapon (Specific), Gunnery, Gymnastics, Heavy Weapons, Locksmith, Longarms, Palming, Pistols, Sneaking, Throwing Weapons, Unarmed Combat |
| Body | Diving, Free-Fall |
| Reaction | Pilot Aerospace, Pilot Aircraft, Pilot Exotic Vehicle (Specific), Pilot Ground Craft, Pilot Walker, Pilot Watercraft |
| Strength | Running, Swimming |
| Charisma | Animal Handling, Con, Etiquette, Impersonation, Instruction, Intimidation, Leadership, Negotiation, Performance |
| Intuition | Artisan, Assensing, Disguise, Navigation, Perception, Tracking |
| Logic | Aeronautics Mechanic, Arcana, Armorer, Automotive Mechanic, Biotechnology, Chemistry, Computer, Cybertechnology, Cybercombat, Demolitions, Electronic Warfare, First Aid, Forgery, Industrial Mechanic, Hacking, Hardware, Medicine, Nautical Mechanic, Software |
| Willpower | Astral Combat, Survival |
| Magic | Alchemy, Artificing, Banishing, Binding, Counterspelling, Disenchanting, Ritual Spellcasting, Spellcasting, Summoning |
| Resonance | Compiling, Decompiling, Registering |

Knowledge/Language also use Intuition or Logic as above (not Active).

### Cannot default (Core Default: No)

No roll if untrained (Attr−1 default not allowed). From skill writeups:

| Category | Skills |
| --- | --- |
| Combat / physical | Exotic Ranged Weapon (Specific); Palming |
| Magic | Alchemy, Arcana, Artificing, Assensing, Astral Combat, Banishing, Binding, Counterspelling, Disenchanting, Ritual Spellcasting, Spellcasting, Summoning |
| Resonance | Compiling, Decompiling, Registering |
| Technical | Aeronautics Mechanic, Automotive Mechanic, Industrial Mechanic, Nautical Mechanic, Biotechnology, Chemistry, Cybertechnology, Electronic Warfare, Hardware, Locksmith, Medicine, Software, Artisan |
| Vehicles | Pilot Aerospace, Pilot Aircraft, Pilot Walker, Pilot Exotic Vehicle (Specific) |

All other Active skills on the list above: Default **Yes** (pool = Attr − 1). Default math: `../Dice and Tests.md`.

**Note:** Exotic Melee Weapon writeup is Default **Yes** in Core; Exotic Ranged is Default **No**.

---

## Path restrictions (reminder)

| Path | Restriction |
| --- | --- |
| Adept | No Sorcery / Conjuring / Enchanting skills |
| Aspected | Only the chosen Magical skill group; never the other two |
| Assensing | Adepts/mystic adepts need Astral Perception power first |

---

## Leftover Karma (skills)

Leftover Karma costs: Active new Rating × 2; Knowledge/Language × 1; specialization **7** Karma; skill group × 5. May break groups / add specs in Step 7. Details: Finishing Touches.

---

## Coverage notes

- Chargen buy engine complete vs Core Step Five.
- Per-skill specialization lists: use Core Skills chapter until Skills Reference exists.
- Default: No list above matched to Core skill Default lines (PDF); Active Skill List italics in some printings can disagree with writeups (use writeups).
- Defaulting math: `../Dice and Tests.md`.
