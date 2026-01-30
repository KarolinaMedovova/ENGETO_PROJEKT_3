from playwright.sync_api import expect


# KONSTANTY
BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
#BACKPACK = "https://www.saucedemo.com/inventory-item.html?id=4"
#ONESIE = "https://www.saucedemo.com/inventory-item.html?id=2"
CART_URL = "https://www.saucedemo.com/cart.html"
CHECKOUT_STEP_ONE_URL = "https://www.saucedemo.com/checkout-step-one.html"
CHECKOUT_STEP_TWO_URL = "https://www.saucedemo.com/checkout-step-two.html"
CHECKOUT_COMPLETE_URL = "https://www.saucedemo.com/checkout-complete.html"



# ---FUNKCE PRO POZITIVNÍ TESTY---

# Funkce pro zobrazení titulku:
def page_title(page):
    page.goto(BASE_URL)
    title = page.get_by_text("Swag Labs")
    expect(title).to_be_visible()


# Funkce pro login:
def login(page):
    page.goto(BASE_URL)
    username = page.get_by_role("textbox", name = "Username")
    username.fill(USERNAME)
    password = page.get_by_role("textbox", name = "Password")
    password.fill(PASSWORD)
    login = page.get_by_role("button", name = "Login")
    login.click()
    expect(page).to_have_url(INVENTORY_URL)


# Funkce pro ověření zobrazení produktů, cen, tlačíka pro přidání do košíku:
def verify_products_page(page):
    expect(page).to_have_url(INVENTORY_URL)
    product_names = page.locator(".inventory_item_name")
    expect(product_names).to_have_count(6)                   # to have count ověřuje i to, že jsou prvky viditelné, tudíž není potřeba ověřovat pomocí .to_be_visible()
    product_prices = page.locator(".inventory_item_price")
    expect(product_prices).to_have_count(6)
    button_add_to_cart = page.get_by_role("button", name = "Add to cart")
    expect(button_add_to_cart).to_have_count(6)


# Funkce pro řazení ve filtru podle ceny a lohi:
def select_price_lohi(page):
    price_lohi = page.locator("[data-test=\"product-sort-container\"]")
    price_lohi.select_option("lohi")
    expect(price_lohi).to_have_value("lohi")


# Funkce pro přidání produktu do košíku:
def add_item_to_cart(page, item_id):
    page.locator(f"[data-test=\"item-{item_id}-title-link\"]").click()
    expect(page).to_have_url(f"https://www.saucedemo.com/inventory-item.html?id={item_id}")
    button_add_item_to_cart = page.locator("[data-test=\"add-to-cart\"]")
    button_add_item_to_cart.click()
    cart = page.locator("[data-test=\"shopping-cart-link\"]")
    cart.click()
    expect(page).to_have_url(CART_URL)


# Funkce pro pokračování v nákupu:
def continue_shopping(page):
    continue_shopping_button = page.locator("[data-test=\"continue-shopping\"]")
    continue_shopping_button.click()
    expect(page).to_have_url(INVENTORY_URL)

"""
# Funkce pro kontrolu obsahu košíku:
def control_cart(page, name):
    expect(page).to_have_url(CART_URL)
    expect(page.get_by_text(f"{name}")).to_be_visible()
"""

# Funkce pro kontrolu produktů v košíku: 
def control_products_in_cart(page, products):
    expect(page).to_have_url(CART_URL)
    items = page.locator(".cart_item")
    for name, price in products:
        product_block = items.filter(has_text=name)
        product_name = product_block.locator(".inventory_item_name")
        expect(product_name).to_have_text(name)
        product_price = product_block.locator(".inventory_item_price")
        expect(product_price).to_have_text(price)


# Funkce pro checkout nákupu:
def checkout(page):
    checkout_button= page.get_by_role("button", name = "Checkout")
    checkout_button.click()
    expect(page).to_have_url(CHECKOUT_STEP_ONE_URL)


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
    expect(page).to_have_url(CHECKOUT_STEP_TWO_URL)
 

# Funkce pro dokončení objednávky: 
def order_completion(page):
    finish = page.get_by_role("button", name = "Finish")
    finish.click()
    expect(page).to_have_url(CHECKOUT_COMPLETE_URL)
    expect(page.locator("[data-test=\"complete-header\"]")).to_be_visible()
    # expect(page.get_by_text("Thank you for your order!")).to_be_visible()
    page.get_by_role("button", name = "Back home").click()
    expect(page).to_have_url(INVENTORY_URL)


# Funkce pro logout:
def logout(page):
    page.get_by_role("button", name = "Open Menu").click()
    page.get_by_role("link", name = "Logout").click()
    #print(page.url)
    expect(page).to_have_url(BASE_URL)



# ---FUNKCE PRO NEGATIVNÍ TESTY---

# Funkce pro chybné přihlášení:
def login_neg(page):
    page.goto(BASE_URL)
    username = page.get_by_role("textbox", name = "Username")
    username.fill(USERNAME)
    password = page.get_by_role("textbox", name = "Password")
    password.fill("heslo")
    login = page.get_by_role("button", name = "Login")
    login.click()
    expect(page).to_have_url(BASE_URL)
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    #expect(page.get_by_text("Epic sadface: Username and password do not match any user in this service")).to_be_visible()


# Funkce pro chybně vyplněné údaje k nákupu:
def fill_checkout_info_neg(page):
    first_name = page.get_by_role("textbox", name = "First Name")
    first_name.fill("Karolina")
    last_name = page.get_by_role("textbox", name = "Last Name")
    last_name.fill("Medovova")
    zip = page.get_by_role("textbox", name = "Zip/Postal Code")
    zip.fill("")
    button_continue = page.get_by_role("button", name = "Continue")
    button_continue.click()
    #print(page.url)
    expect(page).to_have_url(CHECKOUT_STEP_ONE_URL)
    expect(page.locator("[data-test='error']")).to_be_visible()
    #expect(page.get_by_text("Error: Postal Code is required")).to_be_visible()
 

#----------------------------------------------------------------------------------------------

# ---POZITIVNÍ TESTY---

# Test pro zobrazení titulku:
def test_page_title(page):
    page_title(page)


# Test loginu: 
def test_login(page):
    login(page)


# Test pro ověření zobrazení produktů, cen produktů, tlačíka pro přidání do košíku:
def test_verify_products_page(logged_in_page):
    verify_products_page(logged_in_page)


# Test pro řazení ve filtru podle ceny lohi:
def test_select_price_lohi(logged_in_page):
    # verify_products_page(page)
    select_price_lohi(logged_in_page)


# Test pro přidání produktu Backpack do košíku:   
def test_add_item_to_cart(logged_in_page):
    add_item_to_cart(logged_in_page, 4)
    expect(logged_in_page.locator(".cart_item")).to_have_count(1)

# Test pro pokračování v nákupu:
def test_continue_shopping(logged_in_page):
    add_item_to_cart(logged_in_page, 4)
    continue_shopping(logged_in_page)

"""
# Test pro kontolu obsahu košíku: 
def test_control_cart(logged_in_page):
    add_item_to_cart(logged_in_page, 2)
    control_cart(logged_in_page, "Sauce Labs Onesie")
"""

# Test pro kontrolu produktů v košíku:
def test_control_products_in_cart(logged_in_page):
    products = [
        ("Sauce Labs Onesie", "$7.99"),
        ("Sauce Labs Backpack", "$29.99")]
    add_item_to_cart(logged_in_page, 2)
    continue_shopping(logged_in_page)
    add_item_to_cart(logged_in_page, 4)
    control_products_in_cart(logged_in_page, products)
    expect(logged_in_page.locator(".cart_item")).to_have_count(2)


# Test pro checkout nákupu:
def test_checkout(logged_in_page):
    products = [
        ("Sauce Labs Onesie", "$7.99"),
        ("Sauce Labs Backpack", "$29.99")]
    add_item_to_cart(logged_in_page, 2)
    continue_shopping(logged_in_page)
    add_item_to_cart(logged_in_page, 4)
    control_products_in_cart(logged_in_page, products)
    checkout(logged_in_page)


# Test pro vyplnění údajů k nákupu:   
def test_fill_checkout_info(logged_in_page):
    products = [
        ("Sauce Labs Onesie", "$7.99"),
        ("Sauce Labs Backpack", "$29.99")]   
    add_item_to_cart(logged_in_page, 2)
    continue_shopping(logged_in_page)
    add_item_to_cart(logged_in_page, 4)
    control_products_in_cart(logged_in_page, products)
    checkout(logged_in_page)
    fill_checkout_info(logged_in_page)


# Test End To End:
def test_E2E(logged_in_page):
    products = [
        ("Sauce Labs Onesie", "$7.99"),
        ("Sauce Labs Backpack", "$29.99")]   
    add_item_to_cart(logged_in_page, 2)
    continue_shopping(logged_in_page)
    add_item_to_cart(logged_in_page, 4)
    control_products_in_cart(logged_in_page, products)
    checkout(logged_in_page)
    fill_checkout_info(logged_in_page)
    order_completion(logged_in_page)


def test_logout(logged_in_page):
    logout(logged_in_page)



# ---NEGATIVNÍ TESTY---

# Negativní test pro přihlášení:
def test_login_neg(page):
    login_neg(page)


# Negativní test pro vyplnění údajů k nákupu:   
def test_fill_checkout_info_neg(logged_in_page):
    products = [
        ("Sauce Labs Onesie", "$7.99"),
        ("Sauce Labs Backpack", "$29.99")]   
    add_item_to_cart(logged_in_page, 2)
    continue_shopping(logged_in_page)
    add_item_to_cart(logged_in_page, 4)
    control_products_in_cart(logged_in_page, products)
    checkout(logged_in_page)
    fill_checkout_info_neg(logged_in_page)
    #logged_in_page.pause()
