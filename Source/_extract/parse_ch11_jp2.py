# -*- coding: utf-8 -*-
with open('ch11_raw.txt', encoding='utf-8') as f:
    raw = f.read()

lines = raw.split('\n')

def is_delim(line):
    return line.strip() == '>'

HANDLES = {
    "Slamm-0!", "Pistons", "Bull", "Turbo Bunny", "Butch", "Nephrine",
    "Baka Dabora", "Aufheben", "Sticks", "KAM", "Thorn", "Whippet", "Red",
    "The Smiling Bandit", "Lyran", "Picador", "/dev/grrl", "Hard Exit",
    "Man-of-Many-Names", "Snopes", "Ecotope", "Kia", "Marcos", "Netcat",
    "2XL", "Hannibelle", "Clockwork", "Kat o’ Nine Tales", "Kat o' Nine Tales",
    "Goat Foot", "Jimmy No", "Frosty", "Kane", "Haze", "Arete", "Glitch",
    "Cosmo", "Mr. Bonds", "Rigger X", "Glasswalker", "Cayman", "Plan 9",
    "Ethernaut", "Winterhawk", "Dr. Spin", "Kay St. Irregular", "Mika",
    "Am-mut", "Balladeer",
}

delim_positions = [i for i, l in enumerate(lines) if is_delim(l)]

chunks = []
for a, b in zip(delim_positions, delim_positions[1:]):
    seg = lines[a+1:b]
    # strip trailing/leading blank lines
    while seg and seg[0].strip() == '':
        seg = seg[1:]
    while seg and seg[-1].strip() == '':
        seg = seg[:-1]
    chunks.append((a+2, seg))

out_lines = []
for idx, (start_ln, seg) in enumerate(chunks):
    stripped_lines = [s.strip() for s in seg if s.strip() != '']
    joined = ' '.join(stripped_lines)
    is_single_line = len(stripped_lines) == 1
    label = 'HANDLE' if (is_single_line and joined in HANDLES) else 'TEXT'
    flag = ''
    if is_single_line and joined not in HANDLES:
        flag = '  <-- single line, NOT in whitelist (check manually)'
    out_lines.append(f'[{idx}] line~{start_ln} {label}{flag}: {joined}')

with open('ch11_jp_chunks2.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))

print('total chunks:', len(chunks))
