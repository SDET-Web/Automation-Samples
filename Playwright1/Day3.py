from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Its also a method to find element by using
    # xpath - Relative xpath '//'
    # Using attribute - //tagname[@attributename="value"]
    username_element = page.wait_for_selector('//input[@name="username"]')
    username_element.type('Admin')
    password_element = page.wait_for_selector('//input[@placeholder="Password"]')
    password_element.type('admin123')
    login_element = page.wait_for_selector('//button[@type="submit"]')
    login_element.click()


    """ There is text method that we will use to find a specific text or link on page """
    #text - //tagname[text() = "text"]
    page.wait_for_selector('//p[text()="Forgot your password? "]').click()


    """contains is used to find the dynamic contents on a page most important interview question
    attributes - //tagname[contains(@attribute,"value")]
    //input[contains(@placeholder,"User")]
    dynamic - prasanth123,prasanth13454,prasanth987
    starts-with - //tagname[starts-with(@id,'prasanth')]
    ends-with - 2343user
    family
    parent - //tagname[@id = "xy"]/parent::input[]
    child - //tagname[@id = "xy"]/child::input[]
    ancestor -  //tagname[@id = "xy"]/ancestor::input[]
    sibling - //td[text()="Microsoft"]//following-sibling:: td[2]"""


    page.wait_for_timeout(3000)
