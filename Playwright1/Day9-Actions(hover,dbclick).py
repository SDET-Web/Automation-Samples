from playwright.sync_api import sync_playwright
with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Selectable.html')

# Mouse Actions Hover the dropdown
    page.wait_for_selector('//a[text()="SwitchTo"]').hover()
# Click on element
    page.wait_for_selector('//a[text()="SwitchTo"]').click()
# Double Click
    page.wait_for_selector('//a[text()="SwitchTo"]').dblclick()
# Right on Element
    page.wait_for_selector('//a[text()="SwitchTo"]').click(button="right")
# Shift Click
    page.wait_for_selector('//a[text()="SwitchTo"]').click(modifiers=["Shift"])
# Press A Keyboard
#page.wait_for_selector('//a[text()="SwitchTo"]').press("A")
# A-Z , 0-9,F1-F12 all special character drop down and up enter pageup etc
    page.wait_for_selector('//a[text()="SwitchTo"]').press("PageDown")
    page.wait_for_timeout(5000)
    browser.close()