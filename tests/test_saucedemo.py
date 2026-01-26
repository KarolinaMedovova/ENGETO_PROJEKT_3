from playwright.sync_api import expect

# Test pro zobrazení titulku:
def test_page_title(page):
    page.goto("https://www.saucedemo.com/")
    title = page.get_by_text("Swag Labs")
    expect(title).to_be_visible()


# Funkce pro login:
def login(page):
    page.goto("https://www.saucedemo.com/")
    username = page.get_by_role("textbox", name = "Username")
    username.fill("standard_user")
    password = page.get_by_role("textbox", name = "Password")
    password.fill("secret_sauce")
    login = page.get_by_role("button", name = "Login")
    login.click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


# Test loginu: 
def test_login(page):
    login(page)


# Funkce pro ověření zobrazení produktů, cen, tlačíka pro přidání do košíku:
def verify_products_page(page):
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    products = page.locator(".inventory_item_name")
    expect(products).to_have_count(6)                   # to have count ověřuje i to, že jsou prvky viditelné, tudíž není potřeba ověřovat pomocí .to_be_visible()
    price = page.locator(".inventory_item_price")
    expect(price).to_have_count(6)
    add_to_cart = page.get_by_role("button", name = "Add to cart")
    expect(add_to_cart).to_have_count(6)


# Test pro ověření zobrazení produktů, cen produktů, tlačíka pro přidání do košíku:
def test_verify_products_page(page):
    login(page)
    verify_products_page(page)


# Funkce pro řazení ve filtru podle ceny a lohi:
def select_price_lohi(page):
    price_lohi = page.locator("[data-test=\"product-sort-container\"]")
    price_lohi.select_option("lohi")
    expect(price_lohi).to_have_value("lohi")


# Test pro řazení ve filtru podle ceny lohi:
def test_select_price_lohi(page):
    login(page)
    # verify_products_page(page)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    select_price_lohi(page)


# Funkce pro přidání produktu Backpack do košíku:
def add_backpack_to_cart(page):
    backpack = page.locator("[data-test=\"item-4-title-link\"]")
    backpack.click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory-item.html?id=4")
    add_backpack = page.locator("[data-test=\"add-to-cart\"]")
    add_backpack.click()
    cart = page.locator("[data-test=\"shopping-cart-link\"]")
    cart.click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")


# Test pro přidání produktu Backpack do košíku:
def test_add_backpack_to_cart(page):
    login(page)
    add_backpack_to_cart(page)


# Funkce pro pokračování v nákupu:
def continue_shopping(page):
    continue_shopping_button = page.locator("[data-test=\"continue-shopping\"]")
    continue_shopping_button.click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


# Test pro pokračování v nákupu:
def test_continue_shopping(page):
    login(page)
    add_backpack_to_cart(page)
    continue_shopping(page)


# Funkce pro přidání produktu Onesie do košíku:
def add_onesie_to_cart(page):
    onesie = page.locator("[data-test=\"item-2-title-link\"]")
    onesie.click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory-item.html?id=2")
    add_onesie = page.locator("[data-test=\"add-to-cart\"]")
    add_onesie.click()
    cart = page.locator("[data-test=\"shopping-cart-link\"]")
    cart.click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")


# Test pro přidání produktu Onesie do košíku:
def test_add_onesie_to_cart(page):
    login(page)
    add_onesie_to_cart(page)


# Funkce pro kontrolu obsahu obou produktů v košíku:
def control_cart(page):
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
    expect(page.get_by_text("Sauce Labs Onesie")).to_be_visible()


# Test pro kontrolu obsahu obou produktů v košíku:
def test_control_cart(page):
    login(page)
    add_backpack_to_cart(page)
    continue_shopping(page)
    add_onesie_to_cart(page)
    control_cart(page)


# Funkce pro checkout nákupu:
def checkout(page):
    checkout_button= page.get_by_role("button", name = "Checkout")
    checkout_button.click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")


# Test pro checkout nákupu:
def test_checkout(page):
    login(page)
    add_backpack_to_cart(page)
    continue_shopping(page)
    add_onesie_to_cart(page)
    control_cart(page)
    checkout(page)


# Funkce pro vyplnění údajů k nákupu:
def fill_checkout_info(page):
    first_name = page.get_by_role("textbox", name = "First Name")
    first_name.fill("Karolina")
    last_name = page.get_by_role("textbox", name = "Last Name")
    last_name.fill("Medovova")
    zip = page.get_by_role("textbox", name = "Zip/Postal Code")
    zip.fill("25063")
    button_continue = page.get_by_role("button", name = "Continue")
    button_continue.click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
 

# Test pro vyplnění údajů k nákupu:   
def test_fill_checkout_info(page):
    login(page)
    add_backpack_to_cart(page)
    continue_shopping(page)
    add_onesie_to_cart(page)
    control_cart(page)
    checkout(page)
    fill_checkout_info(page)

"""
    items = page.locator(".cart_item")
    expect(items.nth(0).locator(".inventory_item_price")).to_have_text("$29.99")
    expect(items.nth(1).locator(".inventory_item_price")).to_have_text("$7.99")
"""

# Funkce pro dokončení objednávky: 
def order_completion(page):
    finish = page.get_by_role("button", name = "Finish")
    finish.click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    page.get_by_role("button", name = "Back home").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


# Test pro dokončení objednávky:
def test_order_completion(page):
    login(page)
    add_backpack_to_cart(page)
    continue_shopping(page)
    add_onesie_to_cart(page)
    control_cart(page)
    checkout(page)
    fill_checkout_info(page)
    order_completion(page)

