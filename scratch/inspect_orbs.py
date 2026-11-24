with open('style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '.orb-' in l or 'ambient-glow-orb' in l:
        print(f"Line {i+1}:")
        print(''.join(lines[i:i+20]))

