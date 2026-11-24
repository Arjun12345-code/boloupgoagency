import re

with open('index.html', 'r', encoding='utf-8') as f:
    raw = f.read()

# Strip HTML tags
text_only = re.sub(r'<[^>]+>', ' ', raw)

def norm(t):
    return re.sub(r'\s+', ' ', t).strip().replace('’', "'").replace('–', '-').replace('&amp;', '&').replace(' ', ' ')

norm_text = norm(text_only)

items_to_check = {
    'benefits_headline': 'Why Build Your Own BoloUp Go Agency?',
    'earnings_headline': 'How Can a BoloUp Go Agency Earn?',
    'reg_headline': 'How to Join BoloUp Go Agency',
    'step_1_desc': 'Install BoloUp Go using this link and create your account using one of the available sign-up methods.',
    'faqs_headline': 'Frequently Asked Questions',
    'cta_headline': 'Become a BoloUp Go Agent',
}

for k, v in items_to_check.items():
    found = norm(v) in norm_text
    print(f"{k}: found={found}")
    if not found:
        # Find partial
        words = norm(v).split()[:3]
        sample = ' '.join(words)
        idx = norm_text.find(sample)
        if idx != -1:
            print(f"   Context in text: ...{norm_text[idx:idx+80]}...")
        else:
            print(f"   Could not find start: {sample}")

