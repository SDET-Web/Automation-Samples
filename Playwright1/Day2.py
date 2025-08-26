from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # CSS selector id = # and class = . and for attribute tagname{attribute="value"}
    """ page.goto("https://demo.automationtesting.in/")
    emailTxtbox = page.wait_for_selector('#email')
    emailTxtbox.type('test@gmail.com')
    buttonLogin = page.wait_for_selector('#enterimg')
    buttonLogin.click() """

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username = page.wait_for_selector('input[name="username"]')
    username.type('Admin')
    password= page.wait_for_selector('input[type="password"]')
    password.type('admin123')
    loginbutton= page.wait_for_selector('button[type="submit"]')
    loginbutton.click()
    page.wait_for_timeout(3000)
    #browser.close()

