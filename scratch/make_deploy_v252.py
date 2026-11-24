with open('scratch/deploy_v2_5_1.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace version 2.5.1 with 2.5.2
code = code.replace('2.5.1', '2.5.2')
code = code.replace('sync_v251_boloupgo', 'sync_v252_boloupgo')

# Fix ecosystem map
code = code.replace(
    "'assets/images/boloup-ecosystem.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/boloup-ecosystem.png'",
    "'assets/images/boloup-ecosystem.png': 'https://boloupgoagency.com/wp-content/uploads/2026/11/BoloUp-Ecosystem.png'"
)

with open('scratch/deploy_v2_5_2.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Created deploy_v2_5_2.py successfully!")

