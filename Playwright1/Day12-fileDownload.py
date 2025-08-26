from playwright.sync_api import sync_playwright
with sync_playwright() as p:


    def download_handle(download):
        location_file = './files/test.zip'
        download.save_as(location_file)


    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.imacros.net/Automate/Downloads')

    page.on('download', download_handle)
    page.wait_for_selector('//a[@href="/content/Download.zip"]').click()
    page.wait_for_timeout(5000)
