from playwright.sync_api import sync_playwright, expect

def test_alerts_popups():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")

        page.wait_for_load_state("domcontentloaded")

        # print("-----------------Handling Simple Alert----------------------")

        # def handle_dialog(dialog):
        #     print("Alert message", dialog.message)
        #     page.wait_for_timeout(2000)
        #     dialog.accept()

        # page.once("dialog", handle_dialog)
        # page.get_by_role("button", name="Simple Alert").click()
       

        # print("----------------------------Handling Confirmation Alert-----------------")

        # def handling_dialog(dialog):
        #     print("Confirmation Alert",dialog.message)
        #     page.wait_for_timeout(3000)
        #     dialog.accept()

        # page.once("dialog",handling_dialog) 
        # page.get_by_role("button",name = "Confirmation Alert").click()
        # browser.close() 

        print("------------------Handling Prompt Alert----------------------")
        def prompt_alert(dialog):
            print("Prompt Alert",dialog.message)
            page.wait_for_timeout(3000)

            dialog.accept("Welecome to the class")
            page.wait_for_timeout(2000)
            page.once("dialog",prompt_alert)
            page.wait_for_selector("#promptBtn",timeout = 3000).click()
            page.wait_for_timeout(6000)
