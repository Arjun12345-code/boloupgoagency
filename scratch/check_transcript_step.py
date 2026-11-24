import json

with open('C:/Users/asus/.gemini/antigravity/brain/1d3a1ce6-2e32-4691-98c1-6222d711483f/.system_generated/logs/transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('step_index') in range(891, 915) and obj.get('source') == 'MODEL' and obj.get('content'):
            print(f"STEP {obj['step_index']}: {obj['content'][:300]}")

