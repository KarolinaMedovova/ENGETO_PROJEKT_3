## [co_testuji]_[kdy_nebo_za_jakých_podmínek]_[co_očekávám]


import pytest                                                     # je doporučováno pro případné další pokročilejší funkce

from playwright.sync_api import sync_playwright                   # import playwrighut

p = sync_playwright().start()                                     # zapnutí PW

browser = p.firefox.launch()                                     # nastartuj chrom
page = browser.new_page()                                         # otevři novou prázdnou stránku

print("Otevírám stánku engeto.cz")
page.goto("https://engeto.cz/")                                   # vložím URL adresu

badge1 = page.locator("#cookiescript_badgetext")
badge1.click()

badge2 = page.locator("#cookiescript_accept")
badge2.click()
"""
# Počkej, až se objeví tlačítko pro otevření cookie lišty
page.locator('#cookiescript_badgetext').wait_for(state="visible", timeout=30000)
page.locator('#cookiescript_badgetext').click()

# Počkej, až se objeví tlačítko pro přijetí cookies
page.locator('#cookiescript_accept').wait_for(state="visible", timeout=30000)
page.locator('#cookiescript_accept').click()

print("Otevření cookies")
page.locator('#cookiescript_badgetext').click()         #page.click('text="Nastavení souborů cookies"') - nefunguje. nechápu proč.

print("Odsouhlasení cookies")
page.locator('cookiescript_accept').click()             # page.click('text="Chápu a přijímám!"')
"""
"""
print("Zobrazení a kliknutí na lištu s cookies")
try:
    page.wait_for_selector('text="Nastavení souborů cookies"', timeout=10000)
    page.click('text="Nastavení souborů cookies"')
except Exception as e:
    print("❌ Nepodařilo se kliknout na lištu cookies", e)                   # kliknou na cookies

print("Čekání,až se zobrazí tlačítka k přijmutí/odmítnutí cookies")
try:
    page.wait_for_selector('text="Chápu a přijímám!"', timeout=10000)                # počká, až se zobrazí text "Chápu a přijímám"
    page.click('text="Chápu a přijímám!"')
except Exception as e:
    print("❌ Nepodařilo se zobrazit a kliknout na tlačítko 'CHÁPU A PŘIJÍMÁM!'")
"""

print("Zobrazení přehledu kurzů")
#page.click('a[href="/prehled-kurzu/"]')                           # kliknout na "Přehled IT kurzů"
badge3 = page.locator('text="Přehled IT kurzů"')
badge3.click()

# tohle tam dneska nevidim '''#page.click('a[href="#terminy"]')     # kliknout na "Zobrazit termíny kurzů"

print("Zobrazení Testing akademie")
page.click('a[href="https://engeto.cz/testovani-softwaru/"]')
#badge4 = page.locator('a[href="https://engeto.cz/testovani-softwaru/"]')    # kliknout na "Testing akademie"
#badge4.click()

#page.click('a[href="https://engeto.cz/testovani-softwaru/"]')
print("Zobrazení termínů kurzu Testing Akademie")
page.click('text="Zobrazit termíny kurzu"')                          

print("Zobrazení detailu termínu")    
badge5 = page.locator('text="Detail termínu"')
badge5.click()

print("počkáme na url")
assert page.url.endswith("/detail-terminu-testing-akademie-5-11-17-12-2025/"), "❌ Špatné URL"  

browser.close()                                                   # uzavřít test
p.stop()                                                    # zavřít web.prohlížeč

