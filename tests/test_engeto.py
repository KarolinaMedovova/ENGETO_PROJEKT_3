from playwright.sync_api import expect

# test titulku ENGETO:
def test_engeto_title(page):
    page.goto("https://engeto.cz/")
    #title = page.title()
    #print(title)                          #print(page.title())
    assert "ENGETO" in page.title()

# test zobrazení termínu kurzů Python Akademie:
def test_engeto_kurzy(page):
    page.goto("https://engeto.cz/")
    # odkliknutí lišty cookies
    cookie = page.get_by_role("button", name = "CHÁPU A PŘIJÍMÁM!")
    if cookie.is_visible():
        cookie.click()
    """
    # přesná identifikace lokátoru Kurzy"
    loc = page.get_by_role("link", name= "Kurzy")
    print(loc.count())
    for i in range(loc.count()):
        print(i, loc.nth(i).inner_text())
    """
    # button Kurzy:
    kurzy_button = page.get_by_role("link", name="Kurzy").nth(0)
    expect(kurzy_button).to_be_visible()
    kurzy_button.click()
    expect(page).to_have_url("https://engeto.cz/prehled-kurzu/")
    # button pro Python akademii:
    #page.pause()
    #python_akademie_button = page.locator("h3", has_text="Python Akademie")
    python_akademie_button = page.get_by_role("link", name="Python Akademie Python je")
    expect(python_akademie_button).to_be_visible()
    page.mouse.move(10,10)                     # probudí layout
    page.mouse.wheel(0, 500)                   # posune stránku dolů, aby se nic nepřekrývalo
    python_akademie_button.click()              
    expect(page).to_have_url("https://engeto.cz/python-akademie/")
    # button pro zobrazení termínu kurzů:
    zobrazit_terminy_kurzu_button = page.get_by_role("link", name = "Zobrazit termíny kurzu")
    expect(zobrazit_terminy_kurzu_button).to_be_visible()
    zobrazit_terminy_kurzu_button.click()
    expect(page).to_have_url("https://engeto.cz/python-akademie/#terminy")
    # button pro detail termínu:
    detail = page.get_by_role("link", name="Python Akademie Od 12. února")
    expect(detail).to_be_visible()
    detail.click()
    expect(page).to_have_url("https://engeto.cz/product/detail-terminu-python-akademie-12-2-30-4-2026/")