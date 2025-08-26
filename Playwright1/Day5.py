from selectors import SelectSelector

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")
    # Script for Radio Button: //input[@value="value"]
    radio_button = page.query_selector('//input[@value="FeMale"]')
    #radio_button.click()
    radio_button.check()
    if radio_button.is_checked():
       print('Pass')
    else:
        print('Fail')

    #Script for check boxes:

    checkbox1 = page.query_selector('//input[@value="Cricket"]')
    checkbox2 = page.query_selector('//input[@value="Movies"]')
    checkbox3 = page.query_selector('//input[@value="Hockey"]')
    checkbox1.check()
    checkbox2.check()
    checkbox3.check()

    if checkbox1.is_checked() and checkbox2.is_checked() and checkbox3.is_checked():
        print('All Check Pass')
    else:
        print('All Check Fail')

# Script for check boxes using List and for


page.wait_for_timeout(5000)