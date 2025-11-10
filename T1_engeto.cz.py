## [co_testuji]_[kdy_nebo_za_jakých_podmínek]_[co_očekávám]


import pytest                                                     # je doporučováno pro případné další pokročilejší funkce

from playwright.sync_api import sync_playwright                   # import playwrighut

p = sync_playwright().start()                                     # zapnutí PW

browser = p.chromium.launch()                                     # nastartuj chrom
page = browser.new_page()                                         # otevři novou prázdnou stránku
print("Otevírám stánku engeto.cz")
page.goto("https://engeto.cz/")                                   # vložím URL adresu

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
page.click('text="Přehled IT kurzů"')

# tohle tam dneska nevidim '''#page.click('a[href="#terminy"]')                            # kliknout na "Zobrazit termíny kurzů"

print("Zobrazení Testing akademie")
page.click('text="Testing Akademie"')
#page.click('a[href="https://engeto.cz/testovani-softwaru/"]')      # kliknout na "Testing akademie"

print("Zobrazení termínů kurzu Testing Akademie")
page.click('text="Zobrazit termíny kurzu"')                          

print("Zobrazení detailu termínu")                                          
page.click('text="Detail termínu"')

print("počkáme na url")
assert page.url.endswith("/detail-terminu-testing-akademie-5-11-17-12-2025/"), "❌ Špatné URL"  

browser.close()                                                   # uzavřít test
p.stop()                                                    # zavřít web.prohlížeč

