Automatizované testy pomocí frameworku Playwright

Tento projekt obsahuje tři automatizované testy vytvořené pomocí frameworku Playwright a knihovny pytest-playwright.
Testy jsou napsané v jazyce Python a ověřují funkčnost webové aplikace saucedemo.com.


Zadání projektu:
- Vybrat libovolnou webovou stránku.
- Vytvořit tři automatizované testy pomocí Playwrightu.
- Použít plugin pytest-playwright.


Použité technologie: 
- Python
- Playwright
- pytest
- pytest-playwright plugin


Spouštění testů:
Testy se spouští v kořenové složce projektu příkazem pytest, anebo s viditelným prohlížečem příkazem pytest --headed.


Popis testů:
Projekt obsahuje více než tři testy — součástí je i kompletní E2E scénář a negativní testy.
Pozitivní testy:
- Zobrazení titulku
- Přihlášení uživatele
- Ověření zobrazení produktů
- Řazení ve filtru podle ceny lo-hi
- Přidání produktů do košíku
- Pokračování v nákupu
- Kontrola obsahu košíku
- Checkout
- Checkout - vyplnění údajů adresáta
- Dokončení objednávky (E2E test)
- Odhlášení uživatele

Negativní testy:
- Neplatné přihlášení
- Neplatné vyplnění údajů v checkoutu


Screenshoty:
Ve složce 'screenshots' jsou uloženy:
- tests_passed.png – výsledek běhu testů  
- project_structure.png – struktura projektu  
- code_example.png – ukázka části kódu  


Autor:
Karolina Medovová