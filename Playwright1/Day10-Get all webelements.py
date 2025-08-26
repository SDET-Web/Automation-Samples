from playwright.sync_api import sync_playwright
from typing_extensions import Final

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Selectable.html')

    #elements = page.query_selector_all('b')
    #print(len(elements))
    #for i in elements:
         #print(i.text_content())
    # This will pick all links or urls from the page

    try :
        elements = page.query_selector_all('a')
        print(len(elements))
        for i in elements:
            #print(i.text_content())
            print(i.get_attribute('href'))
            page.wait_for_timeout(3000)
    except Exception as e:
        print(str(e))
    finally:
        print("Done")
# Fianlly mean what ever code written will must Execute in finally

