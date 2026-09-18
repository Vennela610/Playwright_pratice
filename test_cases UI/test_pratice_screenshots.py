from playwright.sync_api import sync_playwright 
import datetime 

def test_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        page.wait_for_timeout(3000) 
        # Partial Screenshot: 
        # page.screenshot(path = f"screenshots/file-{timestamp}.png")

        # animals_list = page.locator("#animals option").all_inner_texts()
        # print("Animals list (as shown):", animals_list)

        # alphabetical = sorted(animals_list, key=lambda s: s.lower())
        # print("Alphabetical sorted list:", alphabetical)

        # if animals_list == alphabetical:
        #     print("Sorted list Verified")
        # else:
        #     print("List is not sorted; printed alphabetical order above.") 

        # heading_text = page.get_by_role("heading",name = "Automation Testing Practice")
        # heading_text.screenshot(path = f"screenshots/file-{timestamp}.png")

        # footer_home_link = page.locator("#PageList1").get_by_role("link", name = "Home")
        # footer_home_link.screenshot(path = f"screenshots/file-{timestamp}.png")

        choose_file_input = page.locator("#shadow_host").locator('input[type="file"]')
        choose_file_input.screenshot(path = f"screenshots/choose_file-{timestamp}.png")


        


   
