import pytest
from playwright.sync_api import sync_playwright
from engine.healer import suggest_new_selector

def test_smart_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")

        broken_selector = "button.not-real-class"
        
        try:
            page.click(broken_selector, timeout=3000)
        except Exception:
            print(f"\n[!] Selector failed. Healing...")
            html_snapshot = page.content()[:2000]
            new_selector = suggest_new_selector(broken_selector, html_snapshot)
            
            print(f"[+] AI suggested: {new_selector}")
            if new_selector and "Error" not in new_selector:
                page.click(new_selector)
                print("[✓] SUCCESS: Test healed!")
            else:
                raise Exception(f"Healing failed: {new_selector}")
        browser.close()