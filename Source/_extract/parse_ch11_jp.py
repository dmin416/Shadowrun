# -*- coding: utf-8 -*-
with open('ch11_raw.txt', encoding='utf-8') as f:
    raw = f.read()

lines = raw.split('\n')

def is_delim(line):
    return line.strip() == '>'

delim_positions = [i for i, l in enumerate(lines) if is_delim(l)]

chunks = []
for a, b in zip(delim_positions, delim_positions[1:]):
    seg = lines[a+1:b]
    chunks.append((a+2, seg))  # a+2 -> 1-indexed line number of first content line

out_lines = []
for idx, (start_ln, seg) in enumerate(chunks):
    label = 'TEXT' if idx % 2 == 0 else 'HANDLE'
    joined = ' '.join(s.strip() for s in seg if s.strip() != '')
    out_lines.append(f'[{idx}] line~{start_ln} {label}: {joined}')

with open('ch11_jp_chunks.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))

print('total chunks:', len(chunks))
print('wrote ch11_jp_chunks.txt')
