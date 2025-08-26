"""In this we will learn  how to effectively handle AJAX requests and
responses using Playwright. We'll cover topics such as:

Identifying AJAX calls and their triggers
Intercepting and inspecting AJAX requests and responses
Extracting valuable data from AJAX responses
Handling pagination and infinite scroll scenarios with AJAX
Synchronizing actions with AJAX completion"""

from playwright.sync_api import sync_playwright


def handle_rejex(response):
    if 'https://www.plus2net.com/php_tutorial/dd-ajax.php?' in response.url:
        print(response.url)
        status = response.status
        data = response.text()
        print(f'status:{status} and, data:{data}')


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.plus2net.com/php_tutorial/ajax_drop_down_list-demo.php')
    select = page.wait_for_selector('//select[@id="s1"]')
    page.on('response', lambda response : handle_rejex(response))
    select.select_option('1')
