import json

with open('C:/Users/asus/.gemini/antigravity/brain/1d3a1ce6-2e32-4691-98c1-6222d711483f/.system_generated/logs/transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('step_index') in [370, 375]:
            print(f"STEP {obj['step_index']}: {str(obj.get('tool_calls'))[:300]}")

