import pytest
from test_saucedemo import login


# fixtura pro login a zobrazení úvodní stránky:
@pytest.fixture(scope="function")
def logged_in_page(page):
    login(page)
    return page