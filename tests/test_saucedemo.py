from playwright.sync_api import expect

# test zobrazení titulku :
def test_saucedemo_title(page):
    page.goto("https://www.saucedemo.com/")
    title = page.get_by_text("Swag Labs")
    expect(title).to_be_visible()

# test přihlášení a načtení stránky s produkty, vložení do košíku, 
def test_saucedemo(page):
    page.goto("https://www.saucedemo.com/")
    username = page.get_by_role("textbox", name = "Username")
    username.fill("standard_user")
    password = page.get_by_role("textbox", name = "Password")
    password.fill("secret_sauce")
    login = page.get_by_role("button", name = "Login")
    expect(login).to_be_visible()
    login.click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    products = page.locator(".inventory_item_name")
    expect(products).to_have_count(6)                     # to have count ověřuje i to, že jsou prvky viditelné, tudíž není potřeba ověřovat pomocí .to_be_visible()
    price = page.locator(".inventory_item_price")
    expect(price).to_have_count(6)
    add_to_cart = page.get_by_role("button", name = "Add to cart")
    expect(add_to_cart).to_have_count(6)
    sort_by_price = page.locator("[data-test=\"product-sort-container\"]").select_option("lohi")
    backpack = page.locator("[data-test=\"item-4-title-link\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory-item.html?id=4")
    add_backpack = page.locator("[data-test=\"add-to-cart\"]").click()
    cart = page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
