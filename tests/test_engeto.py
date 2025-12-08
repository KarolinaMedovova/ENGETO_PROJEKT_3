import pytest                                                     # je doporučováno pro případné další pokročilejší funkce
from playwright.sync_api import sync_playwright                   # import playwrighut
from playwright.sync_api import Page, Browser

# S Fixturou:
def test_engeto(page: Page):
    print("Otevírám stánku engeto.cz")
    page.goto("https://engeto.cz/")                                   # vložím URL adresu
    page.wait_for_selector("#cookiescript_badgetext")                   # křížek tam být musí. protože je to ID !!!!!
    badge1 = page.locator("#cookiescript_badgetext")
    badge1.click()
    page.wait_for_selector("#cookiescript_accept")    
    badge2 = page.locator("#cookiescript_accept")    
    badge2.click()
    print("Zobrazení přehledu kurzů")
    page.wait_for_selector('a[href="/prehled-kurzu/"]')
    badge3 = page.locator('a[href="/prehled-kurzu/"]')
    badge3.click()
    print("Zobrazení Testing akademie")
    page.wait_for_selector('a[href="https://engeto.cz/testovani-softwaru/"]')
    badge4 = page.locator('a[href="https://engeto.cz/testovani-softwaru/"]')
    badge4.click()
    print("Zobrazení termínů kurzu Testing Akademie")
    page.wait_for_selector('a[href="#terminy"]')                    #('text="Zobrazit termíny kurzu"')      
    badge5 = page.locator('a[href="#terminy"]')
    badge5.click()
    print("Zobrazení detailu termínu")    
    badge6 = page.locator('text="Detail termínu"').nth(0)
    badge6.click()
    print("počkáme na url")
    page.wait_for_url("https://engeto.cz/product/detail-terminu-testing-akademie-13-1-31-3-2026/")
    assert page.url == "https://engeto.cz/product/detail-terminu-testing-akademie-13-1-31-3-2026/", "❌ Špatné URL"  
    
    #page.url.endswith("/detail-terminu-testing-akademie-5-11-17-12-2025/"), "❌ Špatné URL"  

    #browser.close()                                              
    #p.stop()     


"""
Bez fixtury                                           
def test_engeto(page: Page):
    p = sync_playwright().start()                                     # zapnutí PW
    browser = p.chromium.launch()                                     # nastartuj chrom
    page = browser.new_page()                                         # otevři novou prázdnou stránku
"""

"""
def test_engeto(page: Page):
    p = sync_playwright().start()                                     # zapnutí PW
    browser = p.firefox.launch()                                     # nastartuj chrom
    page = browser.new_page()                                         # otevři novou prázdnou stránku
    print("Otevírám stánku engeto.cz")
    page.goto("https://engeto.cz/")                                   # vložím URL adresu
    badge1 = page.locator("#cookiescript_badgetext")
    badge1.click()
    badge2 = page.locator("#cookiescript_accept")
    badge2.click()


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

    browser.close()                                                # uzavřít test
    p.stop()
"""
