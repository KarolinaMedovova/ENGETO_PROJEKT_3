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
badge_get_started = page.locator('text="Get started"')
badge_get_started.click()

print("7. Načtení stránky Writing tests")
page.click('text="Writing tests"')

"""
tady přichází zajímavost, že když jsem bod výše zkusila takto:
badge2 = page.locator('text="Writing tests"')
badge2.click()

hodilo to dlouhou chybu, končící  :Call log:
                                  - waiting for locator("text=\"Writing tests\"")
a tomu bych ráda porozuměla. stejný lokátor, jen jinak napsaný, a objeví se problém.
"""

assert page.url == "https://playwright.dev/docs/writing-tests", "❌ Nepodařilo se načíst stránku"
print("---2. mezitest, kontrola načtení URL proběhla v pořáku---")

print("8. Načtení stránky How to write the first test")
badge3 = page.locator('text="How to write the first test"')
badge3.click()

assert page.url == "https://playwright.dev/docs/writing-tests#first-test", "❌ Test neprošel!"
print("--- ✅ CELÝ TEST PROBĚHL ÚSPĚŠNĚ!=== ")