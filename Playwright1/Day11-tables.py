from playwright.sync_api import sync_playwright
with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html')

    table= page.wait_for_selector('//table[@id="customers"]')
    tr = table.query_selector_all('tr')
    #for i in tr:
        #print(i.text_content())
    print(len(tr))
    td = table.query_selector_all('td')
    #for i in td:
    print(len(td))

    for row in tr:
        cells = row.query_selector_all('td')
        for cell in cells:
            print(cell.text_content())


    page.wait_for_timeout(5000)