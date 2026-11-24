import json

with open('C:/Users/asus/.gemini/antigravity/brain/1d3a1ce6-2e32-4691-98c1-6222d711483f/.system_generated/logs/transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('step_index') in range(360, 420):
            c = str(obj.get('content'))
            if 'nobg' in c or 'rembg' in c or 'background' in c or 'remove' in c:
                print(f"STEP {obj['step_index']}: {c[:150]}")

