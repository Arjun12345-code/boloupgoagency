import json

p = r'C:\Users\asus\.gemini\antigravity\brain\12e6acbf-bb62-4e5d-9ccc-0989f445e732\.system_generated\logs\transcript.jsonl'
with open(p, 'r', encoding='utf-8') as f:
    for line in f:
        if 'no-hero' in line or 'emang ada minta gambar' in line:
            obj = json.loads(line)
            print(f"STEP {obj.get('step_index')}: {obj.get('source')} - {str(obj.get('content'))[:200]}")

