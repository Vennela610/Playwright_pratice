from playwright.sync_api import sync_playwright 
def new_tab():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")

        page.wait_for_timeout(3000) 

        page.locator("")