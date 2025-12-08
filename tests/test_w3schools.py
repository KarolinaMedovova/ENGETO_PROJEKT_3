
from playwright.sync_api import sync_playwright

p = sync_playwright().start()

browser = p.chromium.launch()                      
page = browser.new_page()

#otevřít stránku www.w3schools.com
page.goto("https://www.w3schools.com/")

#kliknout na SQL
badge1 = page.locator('a[href="/sql/default.asp"]').nth(2)
badge1.click()
#page.get_by_text("SQL").click()

assert page.url == "https://www.w3schools.com/sql/default.asp", "Test neprošel"
print("1. MEZITest konečně prošel!!! HURÁÁÁÁ ")

badge2 = page.locator('a[href="sql_select.asp"]').nth(0)
badge2.click()

assert page.url == "https://www.w3schools.com/sql/sql_select.asp", "Test neprošel"
print("2. MEZITest prošel")

page.get_by_text("Next ❯").nth(1).click()

assert page.url == "https://www.w3schools.com/sql/sql_distinct.asp", "Test neprošel"
print("3. MEZITest prošel")

print("--- ✅ CELÝ TEST PROBĚHL ÚSPĚŠNĚ!=== ")

browser.close()
p.stop()

""" 
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.w3schools.com/")

    # Počkej na odkaz a klikni
    sql_link = page.locator('a[href="/sql/default.asp"]').nth(2)
    sql_link.wait_for(state="visible", timeout=10000)
    sql_link.click()

    # Ověř URL
    assert page.url == "https://www.w3schools.com/sql/default.asp", "Test neprošel"

    browser.close()
"""