from playwright.sync_api import sync_playwright 
import datetime 
import allure



def test_dynamic_table():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        page.goto("https://demoqa.com/frames/") 
        

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 
        # timestamp =  datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 
        #Partial screenshot for specfic element: 
        # page.screenshot(path = f"screenshots/file-{timestamp}.png") 
        page.screenshot(path = f"screenshots/file-{timestamp}.png") 

        page.locator("#frame1").content_frame.locator("html").click()
        page.locator("#frame1").content_frame.get_by_role("heading", name="This is a sample page").click()
        page.locator("#frame2").content_frame.get_by_role("heading", name="This is a sample page").click()
        page.locator("#frame1").content_frame.get_by_role("heading", name="This is a sample page").click()
        page.get_by_text("Sample Iframe page There are").click()
        
        # page.screenshot(path=f"screenshots/screenshot_{timestamp}.png",full_page = True) 
        # table = page.locator("#productTable") 
        # rows = table.locator("tbody tr")
        # rows_count = rows.count()
        # print(rows_count)
        # print("The dynamic table count is:", rows_count)

        

        # home_link = page.get_by_role("link", name="Home")
        # home_link.screenshot(path=f"screenshots/home_link_{timestamp}.png")
        # print("The Home link text is:", home_link.inner_text()) 

