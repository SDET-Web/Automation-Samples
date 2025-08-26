from playwright.sync_api import sync_playwright
text_alert = []


def handle_dialog(dialog):
    #message = dialog.message
    #text_alert.append(message)
    #dialog.accept()
    print(f"Dialog message: {dialog.message}")  # Debug log
    text_alert.append(dialog.message)  # Store the message
    if dialog.type == "prompt":
            prompt_text = "My Name"  # Text to input into the dialog
            print(f"Entering text: {prompt_text}")
            dialog.accept(prompt_text)  # Pass text to the prompt
    else:
            print("Accepting dialog...")
            dialog.accept()  # Accept normal alerts & confirmations

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')

    # code to click or select the  TABs Automaticaly and then click the button to show alert dialog,
    # playwright automatically click the OK in alertbox but if need to force to accept or dismiss we will use lambda dialog
    # that have option to accept dismiss and message

    #page.wait_for_selector('//a[@href="#OKTab"]').click()
    #page.wait_for_timeout(2000)
    #page.on("dialog", lambda dialog: dialog.accept())
    #page.on("dialog", lambda dialog : print(dialog.message))
    #page.wait_for_selector('//div[@id="OKTab"]/button').click()

    page.wait_for_selector('//a[@href="#Textbox"]').click()
    page.wait_for_timeout(2000)
    page.on("dialog", lambda dialog: dialog.accept())
    page.on("dialog", handle_dialog)
    page.wait_for_selector('//div[@id="Textbox"]/button').click()
    page.wait_for_timeout(2000)
    print(text_alert[0])
    page.wait_for_timeout(2000)

    #page.wait_for_selector('//a[@href="#CancelTab"]').click()
    #page.wait_for_timeout(2000)
    #page.on("dialog", handle_dialog)
    #page.wait_for_selector('//div[@id="CancelTab"]/button').click()
    #page.wait_for_timeout(2000)
    #print(text_alert[0])
    #page.wait_for_timeout(2000)