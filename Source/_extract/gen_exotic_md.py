# -*- coding: utf-8 -*-
"""Generate Encyclopedia/Exotic Weapons.md"""
from pathlib import Path

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Encyclopedia\Exotic Weapons.md")

def E(**kw):
    return kw

ITEMS = []

# ========== EXOTIC MELEE ==========
ITEMS += [
E(name="Monofilament whip", cat="Melee", src="Core p.423 / Street Gear melee table; RnG tables p.202",
  skill="Exotic Melee Weapon (Monofilament Whip)",
  acc="5(7)", reach="2", dv="12P", ap="-8", mode="-", rc="-", ammo="-",
  avail="12F", cost="10,000¥",
  rules="Line extends to 2 m; retracts into handle. Glitch: weighted tip snags; disentangle before another proper attack. Crit glitch: hit self for base DV (resist normally). Wireless: Ready Weapon = Free; built-in safety auto-retracts on glitch (no snag); Acc +2 (5->7). Also in Melee Weapons.md."),
E(name="Garrote (standard)", cat="Melee", src="RnG p.20 / tables p.202",
  skill="Exotic Melee Weapon (Garrote)",
  acc="5", reach="0", dv="(STR+4)S", ap="-6", mode="-", rc="-", ammo="-",
  avail="-", cost="50¥",
  rules="Wire/cord + handles (or improvised). PLACE: attack with Called Shot Location; need >=1 net hit (like subduing). After placed, later Action Phase: deal weapon DV and/or improve hold with another Attack Test and/or knock down. Break free: Agility + Unarmed Combat [Physical], threshold = attacker net hits on all attacks so far; or Knock Out of Hands / grip-breaking attack. Also in Melee Weapons.md. Nunchaku choke may substitute Clubs for Exotic(Garrote) at -2 (SL; Clubs SKU)."),
E(name='Ares "Queen of Hearts" Monofilament Garrote', cat="Melee", src="RnG p.20 / tables p.202",
  skill="Exotic Melee Weapon (Garrote)",
  acc="5", reach="0", dv="(STR+6)P", ap="-8", mode="-", rc="-", ammo="-",
  avail="18F", cost="2,000¥",
  rules="Same Garrote placement/break procedures as standard. Dangerous to untrained users on mistakes. Also in Melee Weapons.md."),
E(name="Bullwhip", cat="Melee", src="RnG p.20-21 / tables p.202",
  skill="Exotic Melee Weapon (Whip)",
  acc="6", reach="2", dv="(STR+1)P", ap="+3", mode="-", rc="-", ammo="-",
  avail="6", cost="100¥",
  rules="Within 2 m: Blast Out of Hands called shot + Opposed Strength to yank item toward attacker instead of away (+2 dice to that Strength Test); or Knockdown called shot to trip. Attacker must be within 2 m. Also in Melee Weapons.md."),
E(name="Ash Arms Combat Chainsaw", cat="Melee", src="RnG p.21 / tables p.202",
  skill="Exotic Melee Weapon (Chainsaw)",
  acc="5", reach="1", dv="8P", ap="-4", mode="-", rc="-", ammo="-",
  avail="6R", cost="2,000¥",
  rules="Weaponized (safeties stripped for swinging). Also in Melee Weapons.md. See civilian/tool sibling entry."),
E(name="Ash Arms Combat Chainsaw (civilian/tool)", cat="Melee", src="RnG p.21",
  skill="Exotic Melee Weapon (Chainsaw)",
  acc="3", reach="1", dv="6P", ap="-4", mode="-", rc="-", ammo="-",
  avail="2", cost="150¥",
  rules="Non-combat tool version of Combat Chainsaw: Acc reduced to 3; DV reduced by 2 (8P->6P); Avail 2; Cost 150¥. Same Reach/AP as combat model unless GM rules otherwise."),
E(name="Ash Arms Monofilament Chainsaw", cat="Melee", src="RnG p.21 / tables p.202",
  skill="Exotic Melee Weapon (Chainsaw)",
  acc="5", reach="1", dv="12P", ap="-8", mode="-", rc="-", ammo="-",
  avail="8R", cost="7,500¥",
  rules="Weaponized monofilament chainsaw. Also in Melee Weapons.md. See civilian/tool sibling entry."),
E(name="Ash Arms Monofilament Chainsaw (civilian/tool)", cat="Melee", src="RnG p.21",
  skill="Exotic Melee Weapon (Chainsaw)",
  acc="3", reach="1", dv="10P", ap="-8", mode="-", rc="-", ammo="-",
  avail="6R", cost="1,500¥",
  rules="Non-combat tool version: Acc 3; DV -2 (12P->10P); Avail 6R; Cost 1,500¥. Flavor: cutting concrete / sculpting stone."),
E(name="Krime Stun Lance", cat="Melee", src="SL p.24-25",
  skill="Exotic Melee Weapon (Stun Lance)",
  acc="4", reach="2", dv="10S(e)", ap="-5", mode="-", rc="-", ammo="charges (stun baton rules)",
  avail="9R", cost="900¥",
  rules="~3 m stun baton/lance. Troll sizes only (Using Unadapted Gear, Core p.420). Charge rules as stun baton (10 charges; wall 1/10 sec; wireless induction 1/hour); SL table does not override recharge. Also in Melee Weapons.md."),
]

# ========== CORE SPECIAL / EXOTIC RANGED ==========
ITEMS += [
E(name="Ares S-III Super Squirt", cat="Ranged", src="Core p.429-430 Special Weapons",
  skill="Exotic Ranged Weapon (Special Weapons / Super Squirt)",
  acc="3", reach="-", dv="Chemical (no weapon DV)", ap="-", mode="SA", rc="-", ammo="20(c)",
  avail="7R", cost="950¥",
  rules="Fires DMSO gel packs. DMSO forces skin to absorb carried chemical as Contact-vector toxin into bloodstream (Core Toxins p.408); the attack itself causes no damage. Buy chemical/toxin separately. Light Pistol ranges. Top + underbarrel accessories. DMSO gel packs are not a separate ammo SKU in Core ammo table."),
E(name="Fichetti Pain Inducer", cat="Ranged", src="Core p.429-430",
  skill="Exotic Ranged Weapon (Special Weapons / Pain Inducer)",
  acc="3", reach="-", dv="Special (toxin-like)", ap="-", mode="SS", rc="-", ammo="Special (10 charges)",
  avail="11R", cost="5,000¥",
  rules="Microwave-like pain. Toxin attack Power 8, Immediate; resist Body + Willpower. If modified Power > Mental limit: next Action Phase must flee the pain. Attacker may hold beam with Complex Action (until GM says target dodged/covered). If trapped in beam: incapacitated; dice pool modifier equal to modified Power on all tests while held. SMG ranges; top + underbarrel accessories. 10 charges; wall recharge 1 charge / 10 seconds. Wireless: induction recharge 1 charge / hour."),
E(name="Parashield Dart Pistol", cat="Ranged", src="Core p.429-430",
  skill="Exotic Ranged Weapon (Special Weapons / Dart Gun)",
  acc="5", reach="-", dv="as Drug/Toxin", ap="-", mode="SA", rc="-", ammo="5(c)",
  avail="4R", cost="600¥",
  rules="Fires Injection Darts (Core p.433-434) with Narcoject or other payload (sold separate). Heavy Pistol ranges; top-mounted accessories only. Wireless: dart reports hit/inject success; may report gross tissue anomalies (Device Rating 1). See Injection Darts ammo entry."),
E(name="Parashield Dart Rifle", cat="Ranged", src="Core p.429-430",
  skill="Exotic Ranged Weapon (Special Weapons / Dart Gun)",
  acc="6", reach="-", dv="as Drug/Toxin", ap="-", mode="SA", rc="-", ammo="6(m)",
  avail="6R", cost="1,200¥",
  rules="Compressed-air Injection Darts. Includes top-mounted imaging scope. Sporting rifle ranges; top + underbarrel accessories. Same wireless dart reporting as pistol. See Injection Darts ammo entry."),
]

# ========== RNG EXOTIC RANGED ==========
ITEMS += [
E(name="Ares Screech Sonic Rifle", cat="Ranged", src="RnG p.26 / tables p.204",
  skill="Exotic Ranged Weapon (Sonic Rifle)",
  acc="6", reach="-", dv="7S", ap="*", mode="SS", rc="-", ammo="10(c) peak-discharge (1 PU/shot)",
  avail="16R", cost="8,000¥",
  rules="Variable beam uses shotgun rules (Core p.180) for targets affected, DV modifier, ranges. Damage Resistance: Willpower (not Body); ignores standard armor. Damper earware +2 to resist. Hush/Silence spell: -1 DV per Spellcasting hit. Hit: Disorientation + Nausea (Core p.409; use Damage Resistance in place of Toxin Resistance). Immune spirits (no standard biology). Peak-discharge packs; 1 PU/shot."),
E(name="Blowgun", cat="Ranged", src="RnG p.26 / tables p.204",
  skill="Exotic Ranged Weapon (Blowgun)",
  acc="8", reach="-", dv="1P", ap="-", mode="SS", rc="-", ammo="1(ml)",
  avail="4", cost="15¥",
  rules="Almost always toxin/drug on needle (sold separate). Deliver toxin via Called Shot Location to unarmored area; success delivers poison. Crit glitch: may inhale own dart; some modern mouthpieces have cross-guard safeguard. Taser ranges."),
E(name="Bolas (standard)", cat="Ranged", src="RnG p.26-27 / tables p.204",
  skill="Exotic Ranged Weapon (Bolas)",
  acc="Phys", reach="-", dv="(STR+3)S", ap="+4", mode="thrown", rc="-", ammo="-",
  avail="6", cost="75¥",
  rules="HIT for damage: Exotic Ranged (Bolas) Attack Test with listed DV/AP. WRAP Called Shot Location: target Agility + Gymnastics [Physical] vs attacker net hits or fall prone. Remove wrap: Agility + Escape Artist [Physical] (6, 1 Action Phase) Extended, or Complex Action with sharp knife. Shuriken ranges. Boom-bolas (grenade improvisation, no separate SKU): -2 Acc; miss scatter max distance direction 7; success = grenades at 0 distance (Multiple Simultaneous Blast Core p.183)."),
E(name="Nemesis Arms Suruchin Monofilament Bolas", cat="Ranged", src="RnG p.26-27 / tables p.204",
  skill="Exotic Ranged Weapon (Bolas)",
  acc="Phys", reach="-", dv="(STR+3)S / 12P", ap="+4 / -8", mode="thrown", rc="-", ammo="-",
  avail="18F", cost="4,000¥",
  rules="Hit use left slash stats; wrap also forces immediate Damage Resistance with right slash stats + Gymnastics test. While wrapped, Escape Artist or movement attempts each require another Damage Resistance Test. Shuriken ranges."),
E(name="FN-AAL Gyrojet Pistol", cat="Ranged", src="RnG p.26-27 / tables p.204",
  skill="Exotic Ranged Weapon (Gyrojet)",
  acc="5", reach="-", dv="10P", ap="-2", mode="SA", rc="-", ammo="10(c)",
  avail="12F", cost="2,000¥",
  rules="6mm mini-rockets explode on impact. Heavy pistol accessories + Heavy Pistol ranges. Underwater: +2 DV to standard munitions (plus other mods). Commentary: alternate munitions (jelly rockets etc.) exist; no separate SKU stats in RnG."),
E(name='Mortimer of London "Trafalger" Gun Cane', cat="Ranged", src="RnG p.27 / tables p.204",
  skill="Exotic Ranged Weapon (Gun Cane)",
  acc="6", reach="-", dv="7P", ap="-", mode="SS", rc="-", ammo="1(b)",
  avail="9R", cost="750¥",
  rules="Caseless only; no accessories. Taser ranges. Concealability: +0 whole cane; -6 to detect true nature (Core p.419)."),
E(name="Knockoff Gun Cane", cat="Ranged", src="RnG p.27 / tables p.204",
  skill="Exotic Ranged Weapon (Gun Cane)",
  acc="5", reach="-", dv="9P", ap="-", mode="SS", rc="-", ammo="1 (destroyed after fire)",
  avail="6R", cost="150¥",
  rules="Same cane rules as Trafalger. Destroyed after firing. Table Ammo column is blank for knockoff."),
E(name="SA Retiarus Net Gun (Basic)", cat="Ranged", src="RnG p.28 / tables p.204",
  skill="Exotic Ranged Weapon (Net Gun)",
  acc="5", reach="-", dv="-", ap="-", mode="SS", rc="-", ammo="4(b)",
  avail="9", cost="750¥ gun (ammo load separate)",
  rules="On hit: apply thrown Net subduing rules (RnG p.25). Light Pistol ranges; no accessories. Large net vs normal target: -2 Agility on break tests; large target vs normal net: +2 Agility. Full ammo load: see Net Gun ammo (Basic)."),
E(name="SA Retiarus Net Gun (XL)", cat="Ranged", src="RnG p.28 / tables p.204",
  skill="Exotic Ranged Weapon (Net Gun)",
  acc="5", reach="-", dv="-", ap="-", mode="SS", rc="-", ammo="2(b)",
  avail="9", cost="1,000¥ gun (ammo load separate)",
  rules="For trolls / larger creatures. Same net-gun procedures as Basic. Full ammo load: see Net Gun ammo (XL)."),
E(name='Tiffani "Elegance" Shooting Bracer', cat="Ranged", src="RnG p.28 / tables p.204",
  skill="Exotic Ranged Weapon (Shooting Bracer)",
  acc="5(6)", reach="-", dv="7P", ap="-", mode="SS", rc="-", ammo="1(b)",
  avail="10R", cost="1,250¥",
  rules="Caseless only; no accessories. Taser ranges. Acc 6 with laser sight on newest model. Concealability -5 to hide true function (Core p.419)."),
E(name="Net (thrown)", cat="Ranged", src="RnG p.24-25 / tables p.204",
  skill="Exotic Ranged Weapon (Net)",
  acc="Phys-2", reach="-", dv="-", ap="-", mode="thrown", rc="-", ammo="-",
  avail="6", cost="350¥",
  rules="Grazing Hit success: target in subduing combat (Core p.195). Attacker must move to target for Subduing actions. Break free: Agility + Unarmed Combat or Agility + Escape Artist Complex Action vs attacker net hits (Agility not Strength). Half Thrown Knife ranges (round up). Flavor variants without separate SKU rows: Terra Cotta ShredNet (barbed); Ares ShockNet (electrical) -> use ShockNet ammo when firing from Net Gun."),
]

# ========== LASERS ==========
ITEMS += [
E(name="Ares Redline", cat="Laser", src="RnG p.47-48 / tables p.208",
  skill="Exotic Ranged Weapon (Laser Weapons)",
  acc="9", reach="-", dv="5P", ap="-10", mode="SA", rc="-", ammo="10(c) power clip or external; 1 PU/shot",
  avail="14F", cost="7,500¥",
  rules="Laser basics (Common rules). Detachable power clip or external (usually satchel). SMG ranges. Top + underbarrel only; cannot otherwise modify."),
E(name="Ares Lancer MP Laser", cat="Laser", src="RnG p.48 / tables p.208",
  skill="Exotic Ranged Weapon (Laser Weapons)",
  acc="7", reach="-", dv="7P", ap="-10", mode="SA", rc="-", ammo="2x10(c) or external; 2 PU/shot",
  avail="18F", cost="16,000¥",
  rules="Laser basics. Twin power clips or satchel/backpack. Assault Rifle ranges. Note: RnG Lancer body text mislabels power line as Archon; table + Archon entry confirm Lancer = 2 PU, Archon = 4 PU."),
E(name="Ares Archon Heavy MP Laser", cat="Laser", src="RnG p.49 / tables p.208",
  skill="Exotic Ranged Weapon (Laser Weapons)",
  acc="7", reach="-", dv="10P", ap="-10", mode="SA", rc="-", ammo="External only; 4 PU/shot",
  avail="24F", cost="35,000¥",
  rules="Laser basics. Std upgrades: bipod; tripod or gyro stabilization mount; sound suppressor. Sniper rifle ranges. External pack (almost always backpack) or emplacement power link (unlimited while powered)."),
]

# ========== FLAMETHROWER ==========
ITEMS += [
E(name="Shiawase Blazer", cat="Flame", src="RnG p.49-50 / tables p.208",
  skill="Exotic Ranged Weapon (Flamethrowers)",
  acc="6", reach="-", dv="10P", ap="-6", mode="SA/BF/FA", rc="-", ammo="4(c)",
  avail="16F", cost="2,200¥",
  rules="See Flamethrower basics. Handheld modern package (fuel in weapon, not backpack tank). No accessories except biometric/advanced safety. Replace fuel tank: full Combat Turn."),
]

# ========== SL OTHER RANGED ==========
ITEMS += [
E(name="Narcoject Gas Gun", cat="Ranged", src="SL p.43-45",
  skill="Exotic Ranged Weapon (Gas Gun)",
  acc="5", reach="-", dv="As toxin", ap="-", mode="SS", rc="-", ammo="5x2(c)",
  avail="8R", cost="1,500¥",
  rules="Inhalation-vector toxin stream via compressed air mixing with separate toxin doses. Armor useless; respiratory protection helps (Core Toxin Protection table p.408). Single target or Complex Action vs up to 3 targets in 4 m spread (one Attack, separate Defense); multi consumes 2 toxin rounds. Cloud ~2 Combat Turns (GM: wind/confined). Enclosed space dangerous to everyone. Air tank refill with included electric pump: 3 minutes. Toxin doses separate. Taser ranges."),
E(name="Narcoject PEP", cat="Ranged", src="SL p.44-45",
  skill="Exotic Ranged Weapon (PEP)",
  acc="6", reach="-", dv="10S", ap="- / -5*", mode="SS", rc="-", ammo="2x10(c); 2 PU/shot",
  avail="12R", cost="7,500¥",
  rules="Pulsed Energy Projectile: short intense laser pulses vaporize surface -> plasma flash/bang/stun (non-lethal design). *AP none if armor can Chemical Seal; AP -5 if clothing/armor with gaps. Heavy Pistol ranges; top + underbarrel only. Peak-discharge packs (RnG p.52); typically 2 clips of 10 charges."),
E(name="Narcoject Trackstopper", cat="Ranged", src="SL p.44-46",
  skill="Exotic Ranged Weapon (Trackstopper / foam projector)",
  acc="5", reach="-", dv="-", ap="-", mode="SS", rc="-", ammo="6",
  avail="15R", cost="8,500¥",
  rules="Backpack foam stream (adapted from discontinued Ares Fogger Glop Cannon). Hardens in 1 Combat Round (not instant). Per net hit: -1 Agility; at Agility 0 cannot move or take limb actions. Hardened foam Structure 4, Armor 6; formulated to allow breathing. Dissolves in 1 hour or instantly with Narcoject solvent (free with foam refills). Light Pistol ranges. See Foam Refills ammo."),
E(name="Gunstock War Club (thrown mode)", cat="Ranged", src="SL p.22",
  skill="Exotic Ranged Weapon (when thrown); Clubs in melee",
  acc="Phys", reach="0 thrown", dv="(STR+2)P thrown", ap="-1", mode="thrown", rc="-", ammo="-",
  avail="10 (melee SKU)", cost="200¥ (same SKU)",
  rules="Melee profile is Clubs Acc 5 Reach 1 DV (STR+3)P AP -1 (see Melee Weapons.md). Thrown requires Exotic Ranged Weapon skill (no Clubs)."),
E(name="Shiawase/Nemesis Arms Man-Catcher", cat="Ranged", src="SL p.133 CorpSec Arsenal",
  skill="Exotic Ranged Weapon (Man-Catcher)",
  acc="4", reach="-", dv="Ammo", ap="-", mode="SS", rc="-", ammo="10(m)",
  avail="18F", cost="6,000¥",
  rules="~50 cm tube launcher; ~30 cm warhead of expanding rubber compound. Pre-program detonate: timer, proximity, or impact. Impact: 50% chance compound works (1D6, success on 4+; no Edge rerolls). Range table not listed in SL. See Man-Catcher ammo."),
]

# ========== AMMO / PAYLOADS ==========
ITEMS += [
E(name="Injection Darts", cat="Ammo", src="Core p.433-434 ammo table",
  skill="as dart gun",
  acc="-", reach="-", dv="as Drug/Toxin", ap="-", mode="-", rc="-", ammo="1 dose capacity each",
  avail="4R", cost="75¥",
  rules="For dart guns (Parashield pistol/rifle, etc.). Each dart carries +1 dose drug/toxin (sold separate). Deliver payload on >=1 net hit vs unarmored, or >=3 net hits vs armored. Injection-vector toxin attack. Also listed in Ammunition.md."),
E(name="Net Gun ammo load (Basic)", cat="Ammo", src="RnG p.28",
  skill="as Net Gun Basic",
  acc="as gun", reach="-", dv="-", ap="-", mode="as gun", rc="-", ammo="fills 4(b)",
  avail="9", cost="350¥ (full load)",
  rules="Full ammunition load for SA Retiarus Net Gun Basic. Cost is the right side of the 750/350¥ slash in RnG."),
E(name="Net Gun ammo load (XL)", cat="Ammo", src="RnG p.28",
  skill="as Net Gun XL",
  acc="as gun", reach="-", dv="-", ap="-", mode="as gun", rc="-", ammo="fills 2(b)",
  avail="9", cost="400¥ (full load)",
  rules="Full ammunition load for SA Retiarus Net Gun XL. Cost is the right side of the 1,000/400¥ slash in RnG."),
E(name="ShockNet (net-gun ammo)", cat="Ammo", src="RnG p.28 / tables p.204",
  skill="as Net Gun",
  acc="as gun", reach="-", dv="8S(e)", ap="-5", mode="as gun", rc="-", ammo="as gun",
  avail="10R", cost="+250¥",
  rules="Electrical net ammo for Net Gun. Two charges: one on contact, second at start of next Combat Turn. Otherwise as Net Gun hit/subdue rules (RnG p.25)."),
E(name="Narcoject Foam Refills", cat="Ammo", src="SL p.46",
  skill="as Trackstopper",
  acc="-", reach="-", dv="-", ap="-", mode="-", rc="-", ammo="6 charges",
  avail="15R", cost="500¥ (6 charges)",
  rules="Refills for Trackstopper. Purchase includes Narcoject solvent (free) that instantly dissolves hardened foam; foam otherwise dissolves in 1 hour."),
E(name="Man-Catcher ammo compound", cat="Ammo", src="SL p.133",
  skill="as Man-Catcher",
  acc="-", reach="-", dv="-", ap="-", mode="-", rc="-", ammo="10 shots per pack",
  avail="18", cost="200¥ (10 shots)",
  rules="Blast 10 m. Anyone/thing in blast: opposed grapple vs dice pool 12 or trapped/immobile as compound hardens and expands +1 m."),
]

# Peak discharge as support gear
ITEMS += [
E(name="Peak-discharge Power Clip", cat="Power", src="RnG p.52 / accessories table p.54",
  skill="n/a",
  acc="-", reach="-", dv="-", ap="-", mode="-", rc="-", ammo="10 power units",
  avail="14F", cost="400¥",
  rules="Fits like a clip. Charge 1 PU / 30 min. Not slot-using accessory. Not usable as IED."),
E(name="Peak-discharge Satchel Power Pack", cat="Power", src="RnG p.52",
  skill="n/a",
  acc="-", reach="-", dv="-", ap="-", mode="-", rc="-", ammo="20 power units",
  avail="16F", cost="900¥",
  rules="Canteen-sized belt pack. Cord attach Simple Action. Charge 1 PU / 30 min."),
E(name="Peak-discharge Power Backpack", cat="Power", src="RnG p.52",
  skill="n/a",
  acc="-", reach="-", dv="-", ap="-", mode="-", rc="-", ammo="30 power units",
  avail="20F", cost="2,500¥",
  rules="Backpack. Cord attach Simple Action. Charge 1 PU / 30 min."),
]

# Related underbarrel exotic launchers
ITEMS += [
E(name="Underbarrel Bola Launcher", cat="Accessory", src="RnG p.53 / tables p.209",
  skill="Exotic Ranged Weapon (Bola)",
  acc="as bola", reach="-", dv="as bola STR 5", ap="as bola", mode="-", rc="-", ammo="bola",
  avail="8R", cost="350¥",
  rules="Underneath slot; rifle-sized+. Launched bola as thrown bola with Strength 5. Heavy Pistol ranges. Full accessory install rules in Weapon Accessories.md."),
E(name="Underbarrel Chainsaw", cat="Accessory", src="RnG p.53 / tables p.209",
  skill="Exotic Melee Weapon (Chainsaw)",
  acc="as chainsaw", reach="-", dv="as chainsaw (x2 DV vs barriers)", ap="as chainsaw", mode="-", rc="-", ammo="-",
  avail="10R", cost="as chainsaw + 500¥",
  rules="Underneath; rifle+. Barrier: double DV. See Weapon Accessories.md."),
E(name="Underbarrel Flamethrower", cat="Accessory", src="RnG p.53 / tables p.209",
  skill="Exotic Ranged Weapon (Flamethrowers)",
  acc="as Blazer / FT rules", reach="-", dv="as flamethrower", ap="as flamethrower", mode="-", rc="-", ammo="as FT",
  avail="as flamethrower +2", cost="as flamethrower + 200¥",
  rules="Underneath; rifle+. Use flamethrower rules RnG p.49. See Weapon Accessories.md."),
]

header = """# Exotic Weapons

Agent reference (SR5). Structured field blocks for LLM parsing. Mechanical detail only.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `runandgun.pdf` · `streetlethal.pdf`
**Books:** Core · RnG · SL. CT has no separate exotic SKU list (no CT PDF in repo; INDEX cross-check only).
**See also:** `Encyclopedia/Melee Weapons.md` (shares exotic melee rows) · `Encyclopedia/Projectile Weapons.md` (Archery / Throwing skill gear) · `Encyclopedia/Firearms.md` · `Encyclopedia/Weapon Accessories.md` · `Encyclopedia/Ammunition.md` · `Encyclopedia/Drugs Toxins and Chemicals.md`
**Out of scope:** Archery skill weapons (harpoon gun, pistol crossbow, slingshot, bows, Krime Trollbow archery mode); Throwing skill weapons (boomerang, javelin, tomahawk) except when a SKU explicitly requires Exotic Ranged for a mode; tasers (Pistols skill); grenade/missile/torpedo launchers using Heavy Weapons (e.g. ArmTech PTL-02); cyber implant weapons; Narcoject Dazzler and Krime Stun-O-Net (Weapon Accessories, not Exotic skill weapons); flavor-only net variants without SKU rows (Terra Cotta ShredNet); gyrojet alternate munitions without SKU rows (jelly rockets).

## Schema

| Field | Meaning |
| --- | --- |
| Cat | Melee / Ranged / Laser / Flame / Ammo / Power / Accessory |
| Src | Book + page |
| Skill | Exact Exotic Melee / Exotic Ranged specialization required |
| Acc | Attack limit; `Phys` = Physical limit; `N(M)` wireless |
| Reach | Melee Reach only; `-` if ranged |
| DV / AP | Damage / Armor Penetration; `-` none |
| Mode / RC / Ammo | Fire mode / Recoil Comp / capacity (`PU` = power unit) |
| Avail / Cost | Street Availability / nuyen |
| Rules | Full mechanical notes |

## Common rules

### Skills

- Exotic Melee Weapon and Exotic Ranged Weapon are separate Active skills; each weapon subtype is a specialization / required specialty (Core Skills).
- Subtype must match the weapon (Monofilament Whip != Garrote != Blowgun).
- Core Special Weapons: use Exotic Ranged Weapon skill (Core p.429).

### Shock / electricity melee

- Unless a row overrides: 10 charges; wall recharge 1 / 10 seconds; wireless induction 1 / hour (Core stun baton family).

### Peak-discharge power (RnG p.52)

- Used by lasers, Screech, PEP, Thunderstruck (not exotic), etc.
- Power clip 10 PU Avail 14F 400¥; satchel 20 PU 16F 900¥; backpack 30 PU 20F 2,500¥.
- Recharge 1 PU / 30 minutes. Cord attach to satchel/backpack = Simple Action.
- Not usable as improvised explosives.

### Laser stack penalties (RnG p.47)

- No recoil.
- Range DV: Medium -1, Long -2, Extreme -3 (per category past Short).
- Visibility DV: Light -1, Moderate -2, Heavy -3 (Environmental Visibility Conditions, Core p.175).
- Range and Visibility modifiers stack.
- Top + underbarrel accessories only; cannot be modified otherwise.
- Require Exotic Ranged Weapon (Laser Weapons).

### Flamethrower basics (RnG p.49)

- Pilot light ready: Complex / Wireless Simple / DNI Free.
- Area Complex: up to 2 additional targets within 2 m of another; one Attack Test, separate Defense; DV -2 per additional target.
- Suppressive Fire consumes 4 shots; may use Flechette Suppressive Fire rules (RnG p.120).
- Fire damage (Core p.171); ignites items (GM).
- Taser ranges but only -1 at Extreme; no penalty at Long or closer.
- Exotic Ranged Weapon (Flamethrowers). No accessories except biometric/advanced safety.

### Cross-file exotic melee

- Full exotic melee SKUs are duplicated here for a single exotic lookup and also live in Melee Weapons.md.

## Catalog

"""

def render(d):
    lines = [
        f"### {d['name']}",
        f"- Cat: {d['cat']}",
        f"- Src: {d['src']}",
        f"- Skill: {d['skill']}",
        f"- Acc: {d['acc']} | Reach: {d['reach']} | DV: {d['dv']} | AP: {d['ap']}",
        f"- Mode: {d['mode']} | RC: {d['rc']} | Ammo: {d['ammo']}",
        f"- Avail: {d['avail']} | Cost: {d['cost']}",
        f"- Rules: {d['rules']}",
        "",
    ]
    return "\n".join(lines)

CAT_ORDER = ["Melee", "Ranged", "Laser", "Flame", "Ammo", "Power", "Accessory"]
CAT_HEAD = {
    "Melee": "EXOTIC MELEE",
    "Ranged": "EXOTIC RANGED",
    "Laser": "LASER WEAPONS (Exotic Ranged: Laser Weapons)",
    "Flame": "FLAMETHROWERS (Exotic Ranged: Flamethrowers)",
    "Ammo": "EXOTIC AMMO / PAYLOADS",
    "Power": "PEAK-DISCHARGE POWER PACKS",
    "Accessory": "RELATED UNDERBARREL EXOTIC ACCESSORIES",
}

parts = [header]
for cat in CAT_ORDER:
    group = [i for i in ITEMS if i["cat"] == cat]
    if not group:
        continue
    parts.append(f"## {CAT_HEAD[cat]}\n")
    for i in group:
        parts.append(render(i))

parts.append("## Inventory checklist\n")
parts.append(f"Total entries: {len(ITEMS)}\n\n")
parts.append("""Core Special Weapons (4): Super Squirt, Pain Inducer, Dart Pistol, Dart Rifle.

Core exotic melee (1): Monofilament whip.

Core ammo (1): Injection Darts.

RnG exotic melee (7): Garrote, Mono Garrote, Bullwhip, Combat Chainsaw, Combat Chainsaw civilian, Mono Chainsaw, Mono Chainsaw civilian.

RnG exotic ranged (11): Screech, Blowgun, Bolas, Mono Bolas, Gyrojet, Trafalger cane, Knockoff cane, Net Gun Basic/XL, Shooting Bracer, thrown Net.

RnG lasers (3): Redline, Lancer, Archon.

RnG flamethrower (1): Blazer.

RnG net ammo (3): Net Gun load Basic, Net Gun load XL, ShockNet.

RnG power packs (3): clip, satchel, backpack.

RnG underbarrel exotic accessories (3): bola, chainsaw, flamethrower.

SL exotic melee (1): Krime Stun Lance.

SL exotic ranged (5): Gas Gun, PEP, Trackstopper, Gunstock thrown mode, Man-Catcher.

SL ammo (2): Foam Refills, Man-Catcher ammo.
""")

text = "".join(parts)
text = text.replace("\u2014", "-").replace("\u2013", "-").replace("—", "-").replace("–", "-")
OUT.write_text(text, encoding="utf-8")
print("Wrote", OUT, "entries", len(ITEMS), "bytes", OUT.stat().st_size)
