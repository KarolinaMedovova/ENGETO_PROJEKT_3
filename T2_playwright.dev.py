# import pytest                                                     # je doporučováno pro případné další pokročilejší funkce

print("1. Import Playwrightu")
from playwright.sync_api import sync_playwright

print("2. Spuštění PW")
p = sync_playwright().start()               

print("3. Spuštění browseru")
browser = p.chromium.launch()

print("4. Otevření nové prázdné stránky")
page = browser.new_page()

print("5. Načtení web. stránky")
page.goto("https://playwright.dev")

assert page.url == "https://playwright.dev/", "❌ Nepodařilo se načíst stránku"
print("---1. mezitest, kontrola načtení URL proběhla v pořádku---")

print("6. Načteni Get started")
page.click('text="Get started"')

print("7. Načtení stránky Writing tests")
page.click('text="Writing tests"')

assert page.url == "https://playwright.dev/docs/writing-tests", "❌ Nepodařilo se načíst stránku"
print("---2. mezitest, kontrola načtení URL proběhla v pořáku---")

print("8. Načtení stránky How to write the first test")
page.click('text="How to write the first test"')

assert page.url == "https://playwright.dev/docs/writing-tests#first-test", "❌ Test neprošel!"
print("--- ✅ CELÝ TEST PROBĚHL ÚSPĚŠNĚ!=== ")