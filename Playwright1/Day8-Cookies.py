from playwright.sync_api import sync_playwright
with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
# cookies store some information on browser and server both for fast browsing experience on website.
# Cachea only store info on browser not on client server
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://redbus.in/')

# code to show all the cookies
    my_cookies = page.context.cookies()
    print(my_cookies)

# Clearing all the cookies.
    #page.context.clear_cookies()

    new_cookies = {'name':'Ayesha','Age':'40','Uid':'1234567890'}
#Setting new cookies to page.
    #page.context.add_cookies([new_cookies])

#Taking screenshot and storing the path
    page.screenshot(path='test.png', full_page=True)