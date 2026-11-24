import json

with open('C:/Users/asus/.gemini/antigravity/brain/1d3a1ce6-2e32-4691-98c1-6222d711483f/.system_generated/logs/transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('step_index') in range(345, 360):
            print(f"STEP {obj['step_index']} [{obj.get('source')}]: {str(obj.get('content'))[:200]}")

