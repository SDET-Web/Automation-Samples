from playwright.sync_api import sync_playwright
with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    # we will use context instead of page because its for multitabs
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Windows.html')
    page.wait_for_selector('//button[contains(text(),"    click   ")]').click()
    page.wait_for_timeout(3000)

    # How to find the total pages - that will save all pages in list
    total_pages = context.pages
    print(len(total_pages))
    for i in total_pages:
        print(i)
        print(page.title())
    # How to store the new page 0 is for parent page and 1 for child page
    new_page = total_pages[1]
    old_page = total_pages[0]
    # How to switch to new page interview question
    new_page.bring_to_front()
    page.wait_for_timeout(3000)
    print(new_page.title())

    # This will open the old page and one more new page
    old_page.bring_to_front()
    page.wait_for_selector('//button[contains(text(),"    click   ")]').click()
    page.wait_for_timeout(3000)

    # This will close the new tab page only
    new_page.close()
    page.wait_for_timeout(3000)
    # That will close all open tabs at once
    browser.close()