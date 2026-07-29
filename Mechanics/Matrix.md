# Matrix

Agent reference (SR5). LLM layout; full Core Matrix play for deckers and technomancers: ASDF, Noise, modes, marks, grids, Matrix Perception/Search, full Matrix Actions list, Programs, hosts/IC, cybercombat, dumpshock/bricking, technomancer Living Persona + full complex-form library, sprites.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Matrix chapter ~p.214-259 (attrs, damage, modes, Noise, OS, PAN, marks, actions, programs, hosts/IC, technomancers, Resonance, sprites)
**Source Text:** `13 - The Matrix.md` (primary, full write-ups) · `Core Rulebook Condensed.md` (Matrix section, cross-check)
**See also:** [Dice and Tests](Dice%20and%20Tests.md) · [Rigging](Rigging.md) · [Combat/Initiative](Combat/Initiative.md) · [CFD](CFD.md) · Encyclopedia Cyberdecks · *Data Trails* Foundations (§19 below) · *Kill Code* Reckless Hacking and streams (§20)

**Scope:** Core-complete Matrix plus **Data Trails** Foundations/UV/AI overview and **Kill Code** Reckless Hacking, new Matrix Actions, Resonant/Dissonant streams.
**Out of scope:** Full DT/KC gear catalogs (Encyclopedia); every echo/sprite/CF (see condensed sources).

## Inventory (completeness checklist)

- [x] Persona / device attrs; device ratings; cyberdecks + deck config
- [x] Noise; grids + grid hopping; Overwatch Score + convergence
- [x] Marks; PAN/WAN; Matrix Perception/spotting/running silent; Matrix Search
- [x] Full Matrix Actions list (type/marks/test/opposed/illegal/effect)
- [x] Programs (Common + Hacking) + Agents
- [x] Matrix damage; bricking; repair; biofeedback; dumpshock; link-lock
- [x] Cybercombat quick reference
- [x] Hosts (rating, IC launch rules, sample ratings); Foundation pointer
- [x] Full core IC list with effects
- [x] Technomancer Living Persona; Resonance actions; Fading
- [x] Full core complex-form library
- [x] Submersion/echoes overview (Core sample)
- [x] Data Trails Foundations + node actions (§19)
- [x] Kill Code Reckless Hacking, new actions, streams (§20)

---

## Schema

| Token | Meaning |
| --- | --- |
| ASDF | Attack, Sleaze, Data Processing, Firewall |
| Mark | Matrix authentication recognition key; access token on an icon (max 3 unless owner, who counts as 4) |
| OS | Overwatch Score; illegal-activity trail tracked by GOD |
| Convergence | OS 40: 12 DV Matrix damage, forced reboot, location reported |
| Dumpshock | Forced VR disconnect: 6S cold-sim / 6P hot-sim biofeedback |
| Link-lock | Can't Switch Interface Mode / Enter-Exit Host / Reboot until you Jack Out |
| IC | Intrusion Countermeasures; host-run attack/defense programs |
| GOD / demiGOD | Grid Overwatch Division (global) / per-grid branch that tracks illegal activity |
| Living Persona | A technomancer's device-free Matrix presence, built from Mental attributes |
| Fading | Technomancer's Resonance-use drain, resisted with Resonance + Willpower |

---

## 1. Matrix attributes (ASDF) and devices

| Attr | Role |
| --- | --- |
| Attack | Illegal offense / brute-force code; Limit for Attack actions; harsh backlash on failure |
| Sleaze | Stealth / probing / subtle edits; Limit for Sleaze actions; harsh backlash on failure |
| Data Processing | Legal computing; Limit for most non-illegal actions; VR Initiative component |
| Firewall | Defense; virtual armor vs Matrix damage |

Commlinks: usually **Data Processing + Firewall** only (both equal to commlink rating unless custom). Cyberdecks and hosts: all four. Files have no rating of their own; they defend with their **owner's** ratings (or the host's, if archived there).

### Device ratings

| Type | Rating | Examples |
| --- | --- | --- |
| Simple | 1 | Appliances, public terminals, entertainment systems |
| Average | 2 | Personal electronics, basic cyberware, vehicles, drones, weapons |
| Smart | 3 | Security vehicles, alphaware, corporate security devices |
| Advanced | 4 | Betaware, military vehicles/security devices |
| Cutting Edge | 5 | Deltaware, credsticks, black-ops gear |
| Bleeding Edge | 6 | Experimental, billion-nuyen gear |

### Cyberdecks

| Deck | DR | Attribute Array | Programs | Avail | Cost |
| --- | --- | --- | --- | --- | --- |
| Erika MCD-1 | 1 | 4/3/2/1 | 1 | 3R | 49,500¥ |
| Microdeck Summit | 1 | 4/3/3/1 | 1 | 3R | 58,000¥ |
| Microtronica Azteca 200 | 2 | 5/4/3/2 | 2 | 6R | 110,250¥ |
| Hermes Chariot | 2 | 5/4/4/2 | 2 | 6R | 123,000¥ |
| Novatech Navigator | 3 | 6/5/4/3 | 3 | 6R | 205,750¥ |
| Renraku Tsurugi | 3 | 6/5/5/3 | 3 | 9R | 214,125¥ |
| Sony CIY-720 | 4 | 7/6/5/4 | 4 | 12R | 345,000¥ |
| Shiawase Cyber-5 | 5 | 8/7/6/5 | 5 | 15R | 549,375¥ |
| Fairlight Excalibur | 6 | 9/8/7/6 | 6 | 18R | 823,250¥ |

**Deck config:** At boot, assign the Attribute Array to ASDF (any order). **Reconfigure (Free Action, your Action Phase only, not a Matrix action):** swap two Matrix attributes, OR swap a running program for a stored one, OR load/unload a program into an open slot.

---

## 2. User modes

| Mode | Initiative | Init dice | Notes |
| --- | --- | --- | --- |
| AR | Physical (Reaction + Intuition) | Physical (1D6) | No biofeedback; -2 Perception if focused on AR display |
| Cold-sim VR | Data Processing + Intuition | 3D6 | Biofeedback = Stun |
| Hot-sim VR | Data Processing + Intuition | 4D6 | +2 dice pool to all Matrix actions; biofeedback = Physical; illegal |

Max 5D6 total Initiative Dice from any combination of bonuses. Switching VR to AR loses the VR Initiative dice; can't switch modes while link-locked.

---

## 3. Noise and connections

Noise = distance band + situations - Noise Reduction. Leftover positive Noise = **dice pool penalty on your Matrix actions only** (never on defense/resistance tests).

### Distance

| Physical distance to target | Noise |
| --- | --- |
| Directly connected (any distance) | 0 |
| Up to 100 m | 0 |
| 101-1,000 m (1 km) | 1 |
| 1,001-10,000 m (10 km) | 3 |
| 10,001-100,000 m (100 km) | 5 |
| Greater than 100 km | 8 |

### Situations (add)

| Situation | Noise |
| --- | --- |
| Dense foliage | 1 per 5 m |
| Faraday cage | No signal, action blocked |
| Fresh water | 1 per 10 cm |
| Jamming | 1 per hit on Jam Signals |
| Metal-laced earth/wall | 1 per 5 m |
| Salt water | 1 per cm |
| Spam zone / static zone | Zone Rating (see below) |
| Wireless negation (paint, wallpaper, etc.) | Rating |

### Spam / static zone ratings

| Spam zone | Static zone | Rating |
| --- | --- | --- |
| City downtown | Abandoned building | 1 |
| Sprawl downtown | Abandoned neighborhood, barrens | 2 |
| Major event / ad blitz | Rural, abandoned underground, heavy rain/snow | 3 |
| Commercial city area | Wilderness, severe storm | 4 |
| Commercial sprawl area | Remote (satellite access only) | 5 |
| Mass gathering / emergency | Remote enclosed (cave, desert ruin) | 6 |

**Direct connection** (jacked in with a cable): ignore all Noise and cross-grid/public-grid penalties entirely. Devices without wireless ("throwbacks") can only be hacked via direct connection.

---

## 4. Grids and grid hopping

| Grid | Access | Penalty |
| --- | --- | --- |
| Public | Global | -2 all Matrix actions, even inside hosts |
| Local | Physical service area only | Normal (cross-grid penalty if targeting elsewhere) |
| Global (Big Ten) | Worldwide to 2,000 km orbit | Normal |

**Cross-grid:** -2 dice pool when your action targets an icon on a different grid than you (doesn't apply inside a host; doesn't stack with the public grid penalty beyond the two -2's that can both apply).

**Grid Hop (Complex Action, no test):** Move to a grid you have legitimate access to. Must leave a host before hopping grids. Without legitimate access, use **Brute Force** or **Hack on the Fly** instead: defense pool is a flat 4 dice (local grid) or 6 dice (global grid); success moves you to the grid immediately instead of placing a mark. Illegal Brute Force grid-hops don't alert the grid; illegal Hack on the Fly grid-hops that fail don't add to your OS the way a normal failed Sleaze action would.

**Lifestyle default grid:** Low or lower = public; Middle = local; High = global (pick a mega); Luxury = any.

---

## 5. Marks and recognition keys

Get marks by **invite** (Invite Mark), **Brute Force** (loud, Attack), or **Hack on the Fly** (quiet, Sleaze). Max **3** marks on an icon from any one persona; the **owner** counts as having 4 (owners never need marks on their own stuff). Marks last until reboot or convergence wipes them; only personas can place marks.

**Control Device marks needed by action type:** 1 for Free Actions, 2 for Simple Actions, 3 for Complex/Standard Actions.

---

## 6. PANs and WANs

Slave up to (Device Rating x 3) devices to a commlink/deck (PAN) or unlimited devices to a host (WAN). A slaved device defends with **either its own or its master's rating, whichever is higher**, for each rating needed in a test. Direct-connection attacks on a slave can't borrow the master's ratings.

**Mark propagation:** A mark placed on a slave (even via direct connection) also marks the master. This doesn't run the other way: a failed Sleaze action against a slave only marks the device's own owner, not the master too. Inside a host's WAN, you're treated as directly connected to every device in that WAN.

Only devices can be slaves/masters/PAN members; in a WAN the master must be a host.

---

## 7. Matrix Perception, spotting, and Search

### Spotting

| Target is... | Not running silent | Running silent |
| --- | --- | --- |
| Within 100 m (physical distance to you) | Automatic | Opposed Computer + Intuition [Data Processing] v. Logic + Sleaze |
| Beyond 100 m | Simple Computer + Intuition [Data Processing] | (same Opposed Test once you know something's there) |
| A host | Automatic | n/a |

You always spot icons you have a mark on, no test needed, any distance. Once spotted, you keep spotting an icon until it Hides against you successfully, reboots, or jacks out.

**Running silent:** Simple Action, own device/persona only. -2 dice pool to all your Matrix actions while active. Marks themselves can't run silent. To find a silent icon you don't already know is there, you first need a Matrix Perception hit noting "an icon is running silent nearby/in this host," then the Opposed Test above (tie or better for the hider = they stay hidden; if several silent icons are present, pick one at random to roll against).

### Matrix Perception (Complex Action)

**Test:** Computer + Intuition [Data Processing], Opposed by Logic + Sleaze only if the target is running silent. One fact per net hit (or per hit if silent, per net hit after that). Facts you can ask for include: spot the target; a file's edit date; Matrix damage boxes; presence of a Data Bomb; running programs; device rating; commcode; a specific Matrix attribute's rating; icon type (if disguised); file protection/rating; grid in use; presence of silent runners nearby/in-host; last Matrix action taken and when; marks on an icon (count only, unless you recognize them).

### Matrix Search (Special Action)

**Test:** Simple Computer + Intuition [Data Processing]. Net hits beyond threshold halve remaining time (repeatedly). Failing still costs the full base time.

| Information is... | Threshold | Time |
| --- | --- | --- |
| General/public | 1 | 1 minute |
| Limited interest / not publicized | 3 | 30 minutes |
| Hidden / actively hunted and erased | 6 | 12 hours |
| Protected / secret | N/A (must find and enter the host first) | N/A |

Modifiers: intricate/specialized info -1, obscure -2, searching on another grid -2. Once inside the right host, a Matrix Search there uses a flat 1-minute base time regardless of info type (unless archived, which needs deeper host access, Data Trails).

### Noticing hackers

Succeed with an **Attack**: target knows it's under attack (usually alerts owner / launches IC) but doesn't automatically spot you. Fail an Attack: no detection, but you eat the backlash damage (below). Succeed with a **Sleaze**: no extra visibility. Fail a Sleaze: target gets a free mark on you immediately (spotting you) and alerts/launches IC as above.

---

## 8. Illegal actions and Overwatch

All **Attack** and **Sleaze** actions (per their bracketed Limit) are illegal; Control Device is illegal only when it uses Sleaze as its limit.

| Fail | Result |
| --- | --- |
| Attack | 1 unresisted Matrix damage per net hit the target got on defense |
| Sleaze | Target (or its owner, for devices) gets a free mark on you; owner alerted; host launches IC |

**Overwatch Score (OS):** Starts on your first illegal action after a fresh boot. Each Attack/Sleaze action adds the **defender's hits** to your OS. OS also climbs **+2D6 every 15 minutes** (GM secret). **Check Overwatch Score** (Simple, Sleaze, EW + Logic [Sleaze] v. 6) or the Baby Monitor program reveal your current OS.

### Convergence (OS reaches 40, on a grid)

1. 12 DV Matrix damage (resist normally).
2. Forced reboot: lose all your marks (and marks others had on you); dumpshock if in VR.
3. Physical location reported to the grid owner and to the host you were in (if any).

**Inside a host:** OS still climbs the same way, but at 40 the host places **3 marks** on you and deploys IC instead of the grid dumping you. Leaving the host after host-convergence triggers immediate grid convergence; jacking out from inside the host is safer.

Sanctioned spiders, G-men, and IC never accrue an Overwatch Score, no matter how illegal their actions.

---

## 9. Matrix damage

| Rule | Detail |
| --- | --- |
| Monitor | 8 + (Device Rating / 2) boxes |
| Resist | Device Rating + Firewall |
| No penalty until full | Unlike other damage tracks, no dice penalty until the Matrix Condition Monitor is completely filled |
| Full = bricked | Device shuts down (sparks/smoke/pops); dead until repaired |
| Persona hit | Damage goes to the device running the persona (technomancers take Stun to themselves instead) |
| Non-devices | Hosts and files can't take Matrix damage (no monitor); IC/sprites have a monitor but can't be repaired, just lose all damage when they stop running / return to Resonance |

**Repair:** Toolkit + 1 hour + Hardware + Logic [Mental] Test. Each hit removes 1 box OR halves remaining time (min 1 Combat Turn). Device is offline during repair. Critical glitch = permanently bricked; normal glitch = restored but glitchy.

**Biofeedback:** VR only. Cold-sim = Stun, hot-sim = Physical (unless the source says otherwise). Resist with Willpower + Firewall.

**Dumpshock:** Forced VR drop without a graceful Switch Interface Mode first. DV **6S** cold-sim / **6P** hot-sim, resisted Willpower + Firewall (use Firewall 0 if your deck just got bricked). Also **-2 to all actions for (10 - Willpower) minutes**.

**Link-lock:** Another icon's keep-alive signal blocks you from Switch Interface Mode, Enter/Exit Host, or Reboot Device on the locked device. Escape with **Jack Out** (usually costs you dumpshock). Unconscious + link-locked = stuck in VR, can't defend.

---

## 10. Matrix Actions (full list)

Legend: **Test** shows Skill + Attribute [Limit]; where the Limit is Attack or Sleaze the action is **illegal** (accrues OS on a fail per the rules above). "Opposed by" is the defender's dice pool. Marks are **required to attempt** the action, not a cost of the roll itself.

| Action | Type | Marks | Test | Opposed by | Illegal? | Effect |
| --- | --- | --- | --- | --- | --- | --- |
| Brute Force | Complex | 0 | Cybercombat + Logic [Attack] | Willpower + Firewall | Yes | Place 1 mark (max 3); optional 1 DV Matrix dmg/2 net hits; +1 mark attempts: -4 (2 marks) / -10 (3 marks); can illegally grid-hop (4 dice local / 6 global defense, no alert) |
| Change Icon | Simple | Owner | none [Data Processing] | - | No | Change your or a device's icon appearance; doesn't fool Matrix Perception |
| Check Overwatch Score | Simple | 0 | Electronic Warfare + Logic [Sleaze] | 6 | Yes | Learn your OS as it was before this test's defense hits are added |
| Control Device | Variable | 1/2/3 (Free/Simple/Complex) | Normal skill+attr for the action [that action's limit or Data Processing]; or EW + Intuition [Sleaze] v. Intuition + Firewall if no normal test exists | As above | If Sleaze used | Remotely perform an action through a device you control, using its own dice pool/limit or DP, whichever is lower |
| Crack File | Complex | 1 | Hacking + Logic [Attack] | Protection Rating x 2 | Yes | Strip a file's protection so it can be read/edited/copied |
| Crash Program | Complex | 1 | Cybercombat + Logic [Attack] | Intuition + Firewall | Yes | Named running program crashes; can't restart until reboot |
| Data Spike | Complex | 0 | Cybercombat + Logic [Attack] | Intuition + Firewall | Yes | Matrix damage = Attack rating + 1/net hit + 2/mark on target |
| Disarm Data Bomb | Complex | 0 | Software + Intuition [Firewall] | Data Bomb Rating x 2 | No | Net hits remove and delete a detected Data Bomb; fail = it triggers |
| Edit File | Complex | 1 | Computer + Logic [Data Processing] | Intuition + Firewall (file owner or host) | No | Create/change/copy/delete/protect one detail of a file per use; copying makes you the new owner |
| Enter/Exit Host | Complex | 1 (to enter) | none | - | No | Enter a host you hold a mark on, or leave one you're in (returns you to the grid you entered from) |
| Erase Mark | Complex | 3 on target icon | Computer + Logic [Attack] | Willpower + Firewall | Yes | Erase 1 mark (from same icon/target); +1 attempts: -4 (2) / -10 (3) |
| Erase Matrix Signature | Complex | 0 | Computer + Resonance [Attack] | Signature Rating x 2 | Yes | Erase a Resonance signature (technomancer/sprite trace); needs a Resonance rating to attempt |
| Format Device | Complex | 3 | Computer + Logic [Sleaze] | Willpower + Firewall | Yes | Device permanently shuts down on next reboot until reformatted (Extended Software + Logic [Mental] 12, 1 hr) |
| Full Matrix Defense | Interrupt | Owner | none [Firewall] | - | No | +Willpower to all your defense tests this Combat Turn; -10 Initiative Score |
| Grid Hop | Complex | none (legit access) | none [Data Processing] | - | No | Move to a grid you have legitimate access to; must exit host first |
| Hack on the Fly | Complex | 0 | Hacking + Logic [Sleaze] | Intuition + Firewall | Yes | Place 1 mark (max 3); every 2 net hits = 1 Matrix Perception hit; multi-mark -4/-10; can illegally grid-hop |
| Hide | Complex | 0 | Electronic Warfare + Intuition [Sleaze] | Intuition + Data Processing | Yes | Target loses its spot on you; can't Hide from an icon with a mark on you |
| Invite Mark | Simple | Owner | none [Data Processing] | - | No | Offer another icon a mark on your icon (count, duration, offer window your choice); they mark you with a Free Action |
| Jack Out | Simple | Owner | Hardware + Willpower [Firewall] (only if link-locked) | Logic + Attack (the locker's) | No | Disconnect and reboot your device; dumpshock if you were in VR |
| Jam Signals | Complex | Owner | Electronic Warfare + Logic [Attack] | - | Yes | Your device becomes a jammer; hits add Noise within 100 m while it keeps jamming (no other Matrix actions) |
| Jump Into Rigged Device | Complex | 3 (or owner/permission = no test) | Electronic Warfare + Logic [Data Processing] | Willpower + Firewall | No | Merge persona with a rigger-adapted device; needs VR + Control Rig; device must be vacant |
| Matrix Perception | Complex | 0 | Computer + Intuition [Data Processing] | Logic + Sleaze (only if target running silent) | No | 1 fact per net hit; see facts list above |
| Matrix Search | Special | n/a | Simple Computer + Intuition [Data Processing] | - | No | Find info; threshold/time per Matrix Search table |
| Reboot Device | Complex | 3 (or owner = no test) | Computer + Logic [Data Processing] | Willpower + Firewall | No | Device shuts down, comes back at end of next Combat Turn; resets your OS and all marks on your icon; dumpshock if VR; can't target hosts, living beings, or Resonance constructs |
| Send Message | Simple | n/a (or 1) | none [Data Processing] | - | No | Send a short message/image/file, or open a live feed, to a known commcode |
| Set Data Bomb | Complex | 1 | Software + Logic [Sleaze] | Device Rating x 2 | Yes | Attach a Data Bomb (rating up to net hits) to a file; choose delete-on-trigger and passcode |
| Snoop | Complex | 1 | Electronic Warfare + Intuition [Sleaze] | Logic + Firewall | Yes | Intercept/record target's Matrix traffic for as long as you hold the mark |
| Spoof Command | Complex | 1 on impersonated icon | Hacking + Intuition [Sleaze] | Logic + Firewall (target's) | Yes | Issue a command that a device/agent thinks came from its own owner; doesn't work on IC, sprites, hosts, or personas |
| Switch Interface Mode | Simple | Owner | none [Data Processing] | - | No | Swap AR &lt;-&gt; VR for yourself only; can't while link-locked |
| Trace Icon | Complex | 2 | Computer + Intuition [Data Processing] | Willpower + Sleaze | No | Learn target's physical location as long as you hold at least 1 mark; doesn't work on hosts or IC |

### Resonance actions (technomancer only, not Matrix actions)

No Overwatch Score, no marks needed, no VR init bonus. Almost all cause **Fading** (see Section 14).

| Action | Type | Test |
| --- | --- | --- |
| Call/Dismiss Sprite | Simple | none |
| Command Sprite | Simple | none |
| Compile Sprite | Complex | Compiling + Resonance [Level] v. Sprite Level |
| Decompile Sprite | Complex | Decompiling + Resonance [Social] v. Sprite Level (+ compiler's Resonance if registered) |
| Register Sprite | Complex | Registering + Resonance [Level] v. Sprite Level x 2 |
| Thread Complex Form | Complex | Software + Resonance [Level] v. special (per form) |
| Kill Complex Form | Complex | Software + Resonance [Mental] v. target form's Level + threader's Resonance |

---

## 11. Programs and Agents

Load one of each program type at a time; running programs use your deck's program slots (base slots per the Cyberdecks table, plus any bonuses).

### Common programs

| Program | Effect |
| --- | --- |
| Browse | Matrix Search time halved |
| Configurator | Store a full alternate deck config; swap to it wholesale on your next Reconfigure |
| Edit | +2 Data Processing limit on Edit File tests |
| Encryption | +1 Firewall |
| Signal Scrub | Rating 2 Noise Reduction |
| Toolbox | +1 Data Processing |
| Virtual Machine | +2 program slots; +1 unresisted Matrix damage whenever your persona is hit |

### Hacking programs (illegal)

| Program | Effect |
| --- | --- |
| Armor | +2 dice pool to resist Matrix damage |
| Baby Monitor | Always know your current Overwatch Score |
| Biofeedback | Your Matrix attacks (and failed-Attack backlash against you) also deal equal biofeedback (Stun cold-sim / Physical hot-sim) to biological targets |
| Biofeedback Filter | +2 dice pool to resist biofeedback |
| Blackout | Like Biofeedback, but Stun-only even vs hot-sim |
| Decryption | +1 Attack |
| Defuse | +4 dice pool to resist Data Bomb damage |
| Demolition | +1 to the rating of any Data Bomb you set |
| Exploit | +2 Sleaze on Hack on the Fly |
| Fork | One test hits two targets at once (each defends separately) |
| Guard | -1 DV per mark from extra mark damage taken |
| Hammer | +2 DV to Matrix damage you cause (not on failed-Attack backlash) |
| Lockdown | Anyone you damage stays link-locked until you stop running this or they Jack Out |
| Mugger | +1 DV per mark bonus damage you deal |
| Shell | +1 dice pool to resist Matrix **and** biofeedback damage (stacks with similar programs) |
| Sneak | +2 dice pool vs Trace Icon; convergence doesn't reveal your physical location |
| Stealth | +1 Sleaze |
| Track | +2 Data Processing on Trace Icon tests, OR negates a target's Sneak bonus (pick one benefit) |
| Wrapper | Disguise any icon as anything via Change Icon; Matrix Perception can see through it |

| Programs | Availability | Cost |
| --- | --- | --- |
| Common program | - | 80¥ |
| Hacking program | 4R | 250¥ |
| Agent (Rating 1-3) | Rating x 3 | Rating x 1,000¥ |
| Agent (Rating 4-6) | Rating x 3 | Rating x 2,000¥ |

### Agents

Autonomous programs, Rating 1-6, one program slot each. Use the host device's Matrix attributes; have Computer, Hacking, and Cybercombat at their own Rating. Run their own persona/icon alongside yours. Any attack on an agent damages the device it runs on (shares that device's Matrix Condition Monitor), not the agent as a separate target.

---

## 12. Cybercombat (quick reference)

| Piece | Pointer |
| --- | --- |
| Basic attack | Data Spike (Complex, Attack) |
| Crash a program | Crash Program (Complex, Attack) |
| Full Defense | Full Matrix Defense (Interrupt); +Willpower to all defense this Turn, -10 Initiative Score |
| Loud mark | Brute Force |
| Quiet mark | Hack on the Fly |
| Escape a lock | Jack Out (dumpshock likely) |
| Link-lock | See Section 9 |

Fighting IC/spiders: a host's IC shares marks and spotting with the host and with each other. A host launches **at most 1 IC program per Combat Turn** (start of turn), can run up to its **Rating** in IC at once, and never runs more than one of a given IC type simultaneously. Crashed IC just relaunches next Combat Turn if the host wants it back.

---

## 13. Hosts

Rating 1-12. Attributes are usually (Rating), (Rating+1), (Rating+2), (Rating+3) in any order, shared by the host and all its IC.

| Examples | Host Rating |
| --- | --- |
| Personal sites, pirate archives, public education | 1-2 |
| Low-end commercial, private business, public libraries, small policlubs | 3-4 |
| Social media, small colleges, local police, international policlubs | 5-6 |
| Matrix games, local corp hosts, large universities, low-level government | 7-8 |
| Affluent groups, regional corp hosts, major government, secure sites | 9-10 |
| Megacorp HQ, military command, clandestine head office | 11-12 |

**Archives:** Files not in active use sit in a host's archive, inaccessible until someone with a mark on them brings them out.

**Host convergence:** OS still climbs while you're inside, but hitting 40 gets you 3 marks + IC deployment instead of a grid dump; leaving right after triggers immediate grid convergence (jack out instead).

**Foundation:** Deeper host architecture (grid of nodes, GridGuide, deep archive diving) is a *Data Trails* mechanic. Core hosts above are enough for most runs.

---

## 14. Intrusion Countermeasures (IC)

IC rolls **Host Rating x 2** on its attack (Complex Action), limited by the host's Attack rating; a failed IC attack damages the IC itself like any failed Attack action. IC is always legal (no OS). One host runs at most one of each IC type at a time.

| IC | Opposed by | Effect |
| --- | --- | --- |
| Acid | Willpower + Firewall | 1+ net hit: -1 Firewall (cumulative until reboot); at Firewall 0, 1 DV Matrix dmg/net hit instead |
| Binder | Willpower + Data Processing | 1+ net hit: -1 Data Processing (cumulative); at DP 0, 1 DV Matrix dmg/net hit instead |
| Black IC | Intuition + Firewall | Link-locks on hit; (Attack) DV Matrix dmg (+1/net hit, +2/mark) plus equal biofeedback |
| Blaster (Grey IC) | Logic + Firewall | Link-locks on hit; (Attack) DV Matrix dmg (+1/net hit, +2/mark) plus Stun-only biofeedback |
| Crash | Intuition + Firewall | If host already has a mark on you and hits: one of your running programs crashes at random, unusable until reboot |
| Jammer | Willpower + Attack | 1+ net hit: -1 Attack (cumulative); at Attack 0, 1 DV Matrix dmg/net hit instead |
| Killer | Intuition + Firewall | (Attack) DV Matrix dmg per hit (+1/net hit, +2/mark) |
| Marker | Willpower + Sleaze | 1+ net hit: -1 Sleaze (cumulative); at Sleaze 0, 1 DV Matrix dmg/net hit instead |
| Patrol | n/a (no attack) | Matrix Perception on everyone in host, shares findings; runs 24/7 harmlessly |
| Probe | Intuition + Firewall | Each hit = 1 more mark for the host/IC on you (max 3) |
| Scramble | Willpower + Firewall | If host already has 3 marks on you and this hits: forced reboot (dumpshock if VR) |
| Sparky ("Psycho Killer") | Intuition + Firewall | Killer's damage plus biofeedback |
| Tar Baby | Logic + Firewall | Link-locks on hit; if already locked, adds a mark instead (max 3) |
| Track | Willpower + Sleaze | If host has 2+ marks on you and this hits: your physical location is reported |

---

## 15. Technomancers

No deck required. Skills come from the **Resonance skill group** (Compiling, Decompiling, Registering, Software as used for threading, etc.).

**Resonance attribute:** Max = Essence rounded down; lost Essence lowers current and max Resonance. Resonance 0 = lose the Technomancer quality.

### Living Persona

| Matrix attr | From |
| --- | --- |
| Device Rating | Resonance |
| Attack | Charisma |
| Sleaze | Intuition |
| Data Processing | Logic |
| Firewall | Willpower |

Not a device: cannot slave/master, join a PAN/WAN, reconfigure attrs, or run deck programs. Natural **hot-sim only** in the living persona (cold-sim needs a commlink/deck persona instead, which then can't use Resonance abilities). +2 dice pool to all Matrix Perception Tests. Matrix damage converts to **Stun** on the technomancer directly (no separate Matrix Condition Monitor), still resisted with Device Rating + Firewall. "Rebooting" the living persona works like Reboot Device (though it isn't a Matrix action).

**Resonance actions** (Section 10 table): no OS, no marks required, no VR init bonus; almost all cause Fading. You can still take ordinary Matrix actions on your living persona with all their usual rules (including OS).

### Fading

Resist with **Resonance + Willpower**. Minimum Fading DV 2 in all cases.

| Source | Fading DV | Physical if... |
| --- | --- | --- |
| Threading a complex form | Per the form's FV entry (min 2) | Your threading hits exceed your Resonance |
| Compiling / Decompiling / Registering a sprite | 2 x the sprite's hits (not net hits) on the Opposed Test, min 2 | Sprite's Level/Rating exceeds your Resonance |
| Kill Complex Form | Same as if you'd threaded the targeted form | Same rule as threading |

### Threading

Choose a Level up to **3 x Resonance**. Subject to Noise, other-grid, and public-grid modifiers like any Matrix effect; can only target icons you've spotted. Sustaining a complex form costs **-2 dice pool per sustained form** on all your actions (Simple Resonance + Willpower (2) Test to keep sustaining if concentration is challenged). You may know up to **Resonance x 2** complex forms (learn via Software + Intuition [Mental]; 12 / hits = days to learn, then spend Karma).

---

## 16. Resonance Library (full core complex-form list)

Target types: Persona / Device / File / Sprite / Self. Duration: **I** = Immediate, **S** = Sustained, **P** = Permanent (if sustained for its Level in Combat Turns). **FV** = Fading Value (L = the Level you choose).

| Complex form | Target | Dur | FV | Test | Effect |
| --- | --- | --- | --- | --- | --- |
| Cleaner | Persona | P | L-2 | Simple Software + Resonance [Level] | Each hit reduces target's Overwatch Score by 1 |
| Diffusion of [Matrix Attribute] | Device | S | L-2 | Software + Resonance [Level] v. Willpower + Firewall | Net hits reduce the named attribute (min 1); one of four attribute-specific forms |
| Editor | File | P | L-1 | Software + Resonance [Level] v. Intuition + Data Processing (file owner) | Net hits = Edit File-equivalent changes to the file |
| Infusion of [Matrix Attribute] | Device | S | L-2 | Software + Resonance [Level] (Level must equal/exceed the attribute) | Hits raise the named attribute, up to 2x its normal rating; one of four attribute-specific forms; ends if that attribute is swapped via Reconfigure |
| Pulse Storm | Persona | I | L-3 | Software + Resonance [Level] v. Logic + Data Processing | Net hits add that much Noise to the target |
| Puppeteer | Device | I | L+1 | Software + Resonance [Level] v. Willpower + Firewall; threshold 1/2/3 by Free/Simple/Complex | Forces the target to perform a chosen Matrix action next |
| Resonance Channel | Device | S | L-3 | Simple Software + Resonance [Level] | Net hits reduce distance-based Noise to that device |
| Resonance Spike | Device | I | L-3 | Software + Resonance [Level] v. Willpower + Firewall | 1 box Matrix damage per net hit, no resistance roll for target |
| Resonance Veil | Device | S | L-3 | Software + Resonance [Level] v. Intuition + Data Processing | Convincing Matrix illusion; target needs a Matrix Perception threshold = your net hits to see through it |
| Static Bomb | Self | I | L-1 | Software + Resonance [Level] v. Intuition + Data Processing (each spotter) | Beaten spotters lose their spot on you (marks are unaffected) |
| Static Veil | Persona | S | L-3 | Simple Software + Resonance [Level]; threshold 1 public grid / 2 other | While sustained (and not grid-hopping), target's OS doesn't rise from time, only from illegal actions |
| Stitches | Sprite | P | L-3 | Simple Software + Resonance [Level] | Each hit heals 1 box of Matrix damage on the target sprite |
| Tattletale | Persona | P | L-3 | Simple Software + Resonance [Level] | Each hit raises target's OS by 1 (only works if target has an OS) |
| Transcendent Grid | Self | I | L-3 | Simple Software + Resonance [Level] | No cross-grid or public-grid penalties for or against you, all grids at once, for 1 minute per hit |

---

## 17. Sprites

Personas without devices, compiled from the Resonance. Device Rating and Resonance = their **Level**. Matrix Condition Monitor: 8 + (Level / 2) boxes. Initiative: (Level x 2) + a fixed bonus per type, 4D6 Initiative Dice always. Owner = the technomancer who compiled them; carry that technomancer's Resonance signature. Cannot be part of a PAN/WAN. Compiling starts a sprite's own OS immediately, even before it does anything; convergence just deletes the sprite.

### Compiling and registering

**Compile Sprite** (Complex, Resonance action): choose a Level up to **2x Resonance**. Test: Compiling + Resonance [Level] v. Sprite Level. Net hits = tasks owed. Only **one compiled sprite** at a time. Fading = 2 DV per hit (not net) the sprite rolls, min 2, Stun unless sprite Level > your Resonance (then Physical).

**Register Sprite** (Complex): takes hours equal to the sprite's Level (OS frozen, no other actions for either of you); Opposed Registering + Resonance [Level] v. Sprite Level x2. 1+ net hit = registered (OS erased, restarts only if it acts illegally again); net hits add to tasks owed. Registered limit = your **Charisma**; doesn't count against the one-compiled-sprite cap.

**Decompile Sprite** (Complex): Opposed Decompiling + Resonance [Social] v. Level (+ compiler's Resonance if registered). Net hits reduce owed tasks; hits 0 owed = sprite returns to the Resonance on its next action. Same Fading formula as compiling.

**Tasks:** One task = one sprite power use, one Combat Turn of related Matrix actions, or cybercombat until the fight ends/you escape. Registered sprites can also Aid Study, Assist Threading, take a Loaned Task, a Remote Task (returns to you instead of the Resonance), Re-register, go on Standby, or Sustain a Complex Form for you.

### Sprite types

| Type | Attack | Sleaze | DP | Firewall | Init | Skills | Powers |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Courier | L | L+3 | L+1 | L+2 | 2L+1 | Computer, Hacking | Cookie, Hash |
| Crack | L | L+3 | L+2 | L+1 | 2L+2 | Computer, EW, Hacking | Suppression |
| Data | L-1 | L | L+4 | L+1 | 2L+4 | Computer, EW | Camouflage, Watermark |
| Fault | L+3 | L | L+1 | L+2 | 2L+1 | Computer, Cybercombat, Hacking | Electron Storm |
| Machine | L+1 | L | L+3 | L+2 | 2L+3 | Computer, EW, Hardware | Diagnostics, Gremlins, Stability |

(Init shown +1D6 to +4D6 flavor already folded in; all sprites roll 4D6 Initiative Dice on top.)

### Sprite powers

| Power | Effect |
| --- | --- |
| Camouflage | Hide a file inside another file, invisible to Matrix Search until specifically hunted for |
| Cookie | Hacking + Resonance [Sleaze] v. Intuition + Firewall to plant a tracking file that logs a persona's Matrix activity |
| Diagnostics | Teamwork-assist a repair/use of a device: hits give +1 limit and +1 die each to the helped character |
| Electron Storm | Cybercombat + Resonance [Attack] v. Intuition + Firewall; sustained Matrix damage each action plus 2 Noise; ends if the sprite takes Matrix damage |
| Gremlins | Hardware + Level [Attack] v. Device Rating + Firewall; causes a glitch (critical glitch at 4+ net hits) |
| Hash | Protect a carried file so only the sprite can unprotect it; up to Level x 10 Combat Turns; destroyed sprite = file permanently corrupted |
| Stability | On a marked target: ignore standard glitches, downgrade critical glitches to standard |
| Suppression | While active in a host, delays that host's next IC launch by (Level / 2) Combat Turns |
| Watermark | Invisible Resonance-only tag on an icon; erasable with Erase Matrix Signature |

---

## 18. Submersion (overview)

Grade-based, Karma cost **10 + (Grade x 3)**; grade can't exceed Resonance. Raises natural Resonance max to **6 + Grade**. Grants access to the Resonance Realms (deep-dive content in *Data Trails*) and one **echo** per grade. Sample echoes: Attack/Sleaze/Data Processing/Firewall Upgrade (+1 to that Living Persona attr, most twice), Mind over Machine (Control Rig equivalent), NeuroFilter (+1 resist biofeedback), Overclocking (+1D6 hot-sim), Resonance Link (empathic bond to another technomancer), Resonance [Program] (mimic one common/hacking program).

---

## Programs and IC cross-reference

For a live fight: check **Section 12** for the attack/defense flow, **Section 14** for what each IC type actually does, and **Section 9** for what happens if you get bricked or dumped mid-run.

---

## 19. Foundations (*Data Trails*)

**Verified from:** `Data Trails Condensed.md` Ch. 13.

### Entering a Foundation

| Rule | Detail |
| --- | --- |
| Who | Metahumans, metasapients, sprites, AIs (not agents/pilots) |
| How | Mark gateway via Brute Force or Hack on the Fly; **hot-sim VR**; Complex Action enter. Or via **Anchor** |
| Attributes | Body=Firewall, Agility=Sleaze, Reaction=Data Processing, Strength=Attack. Mental unchanged |
| Skills | Combat→Cybercombat, Physical→Hacking, Social→Software (or real Social), Technical→EW, Vehicle→Computer |
| Magic | Does not work in Foundation paradigm. **Resonance works**; Fading always Physical |
| Limits | No Matrix actions / **no OS**; link-locked; exit only via **Portal** |

### Damage and addiction

Physical CM → biofeedback. Matrix CM only → Matrix damage. Foundation addiction: Rating 5, Threshold 1.

### Nodes (all Complex Actions; fail = **variance**)

| Node | Key actions |
| --- | --- |
| Archive | Find/Copy/Fetch/Edit/Delete files (Comp/Hack vs host attrs) |
| Master Control | Alter Reality, Map, Calm Beast, Destroy Host (Extended), Grow Host, Configure Attr |
| Null | No known actions |
| Portal | Create Anchor; Exit to AR + reboot |
| Scaffolding | Observe; Edit sculpt; Reboot host (dump scaffolding personas) |
| Security | Target/Launch/Recall/Configure IC |
| Slave | Control Device; Brick; Perma-Mark (persists reboot, max 3) |

### Variance and alert

Minor variance: Firewall vs threshold 4. Severe: Rating+Firewall vs 4. Secret **Variance Tally** per intruder; at **40** → alerted. Separate from OS. Alert: everything attacks; escape via Portal.

### Hitchhikers (*Hitchhiker* program)

Hot-sim followers at gateway; physical attrs = leader's Foundation attrs; keep own skills; no Magic/Resonance as hitchers.

### Data Trails, extra Matrix actions

| Action | Type | Effect |
| --- | --- | --- |
| Garbage In/Garbage Out | Complex | 3 marks; remap one input↔output on device; reboot clears |
| Trackback | Special | Owner only; Extended Comp+Int find marker vicinity |

### Data Trails, sample complex forms and echoes

| CF | FV | Effect summary |
| --- | --- | --- |
| Derezz | L+2 | Matrix dmg; -1 Firewall until reboot |
| FAQ | L | Obscure info on device |
| IC Tray | L-2 | List deployable IC |
| Redundancy | L | Temp Matrix CM boxes |

Echoes (sample): FFF, Mathemagics, MMRI, Quiet (-2 Noise 10m x Res), Resonance Riding, Skinlink, Sleepwaker.

Full UV hosts, AI PC creation, advanced programs: *Data Trails* Ch. 15.

---

## 20. Kill Code supplements

**Verified from:** `Kill Code Condensed.md`

### Reckless Hacking

On one Matrix Action, take one or more **-5 dice pool** penalties. Each -5 acts as **+1 mark** beyond what you have. **Max 3** (-15). Critical glitch: device reboots immediately; dumpshock is **Physical** regardless of mode.

### New Matrix Actions

| Action | Type | Marks | Test | Effect |
| --- | --- | --- | --- | --- |
| Calibration | Simple | 1/persona | EW + Logic [DP] | +1 Init Score per 2 hits to marked personas (max = DP) |
| Denial of Service | Simple | See text | Computer + Intuition [DP] vs Wil + Firewall | Net hits x2 as -dice to wireless device tests until next CT; per PAN mark affects 2 slaved devices |
| I Am the Firewall | Complex / Int -5 | None | Computer + Intuition [DP] | Hits = Defense bonus to allies on AR feed (max allies = DP) |
| Haywire | Complex | None | Cybercombat + Logic [Attack] vs Wil + Firewall | Disable all PAN wireless until Extended fix or reboot |
| Intervene | Int -5 | None | Computer + Intuition [DP] | Hits add to ally Defense vs wireless attacks |
| Masquerade | Complex | 2+2 | Hacking + Intuition [Sleaze] vs Logic + Firewall | Fool target 1 min/net hit; not owner |
| Popup | Simple | 1 | Hacking or Cybercombat vs Wil + Firewall | AR spam -net hits to actions; optional Matrix dmg |
| Squelch | Simple | None | EW + Logic [Attack] vs Sleaze + Intuition | Block messaging net hits minutes |
| Subvert Infrastructure | Complex | 1 (host) | EW + Intuition [Sleaze] vs Intuition + Firewall | Control simple devices/net hit; sustain Complex/CT |
| Tag | Simple | None | Computer + Logic [DP] vs Sleaze + Intuition | Tag PAN targets; allies -Visibility/Light vs tagged |
| Watchdog | Complex | None | EW + Logic [Sleaze] vs Logic + Firewall | 1 mark; know target's Matrix actions; enables Haywire/Popup/Squelch as Interrupts |

### Variant host types (summary)

| Type | Notes |
| --- | --- |
| Industry | Non-Patrol IC launches at **end** of CT |
| Destination | DP +3; IC per persona per Combat Round; Running Silent disabled |
| Nested | Max nested = floor(parent Rating/3); shared Foundation |
| Outdated | DP -3, Firewall -2; no Foundation; OS only if >=50 inside |
| Offline | Direct connection only; no OS |
| Rogue | ±3 any attribute if sum unchanged; optional Foundation |

### Resonant Streams (20 Karma each; one stream; exclusive)

| Stream | Daemon benefit | Signature power |
| --- | --- | --- |
| Cyberadepts | Restore Res lost to cyberware = ceil(Submersion/2) | **Overdrive:** boost cyberware rating; drop = Matrix dmg |
| Machinists | Living persona as RCC; Noise Reduction = Willpower | **LOTO:** disable device/Pilot net hits CT |
| Sourcerors | Sustain floor(Submersion/2) CFs with no penalty | **Hyperthreading:** merge CFs; combined FV |
| Technoshamans | Great form sprites (double Fade) | **Sprite Pet:** Karma = Level; unlimited tasks; one at a time |

### Dissonant Streams (20 Karma; exclusive with Resonant)

| Stream | Daemon | Power |
| --- | --- | --- |
| Morphinae | Ignore 1 Noise/Submersion Grade | **Forced Heuristics:** -1 host/IC Matrix attr/net hit |
| Apophenians | +ceil(Sub/2) Sleaze | **Causal Nexus:** target glitches easier while sustained |
| Erisians | +ceil(Sub/2) Firewall | **Dissonance Spike:** 2 Matrix + 1 biofeedback boxes/hit (unresistable) |

### New IC (*Kill Code*)

| IC | Effect |
| --- | --- |
| Flicker | Link-lock + mark; 2 marks → disconnect (dumpshock); avatar persists [DR] rounds |
| Sleuther | +2 Search/Perception involving you |
| Blue Goo | Matrix-damage it → explodes vs attacker |

Full technocritters, Null forms, tribes, qualities: *Kill Code* condensed catalog.
