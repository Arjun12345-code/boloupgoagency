with open('style.css', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if '255, 69, 0' in line or 'ff4500' in line.lower():
            print(f"{i+1}: {line.strip()[:100]}")

