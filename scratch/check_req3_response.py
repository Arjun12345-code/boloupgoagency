import json

with open(r'C:\Users\asus\.gemini\antigravity\brain\1d3a1ce6-2e32-4691-98c1-6222d711483f\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('step_index') in range(1210, 1240):
            c = str(obj.get('content'))
            if obj.get('source') == 'MODEL' and obj.get('type') == 'PLANNER_RESPONSE' and not obj.get('tool_calls'):
                print(f"STEP {obj.get('step_index')}: {c[:250]}")

