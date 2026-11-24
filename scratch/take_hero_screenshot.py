from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 800})
    page.goto('https://boloupgoagency.com/?nocache=1', wait_until='networkidle')
    page.screenshot(path='scratch/live_hero.png', clip={'x': 0, 'y': 0, 'width': 1280, 'height': 750})
    browser.close()
    print("Screenshot saved to scratch/live_hero.png")

