from playwright.sync_api import sync_playwright 
import datetime 


def test_dynamic_table():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/") 

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 
        page.screenshot(path=f"screenshots\screenshot_2026-08-24_19-59-24.png{timestamp}.png",full_page = True) 
        table = page.locator("#productTable") 
        rows = table.locator("tbody tr")
        rows_count = rows.count()
        print(rows_count)
        print("The dynamic table count is:", rows_count)

        heading = page.get_by_role("heading", name="Automation Testing Practice")
        heading_text = heading.inner_text()
        heading.screenshot(path=f"screenshots\heading_{timestamp}.png")
        print("The heading text is:", heading_text)