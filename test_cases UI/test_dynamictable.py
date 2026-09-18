from playwright.sync_api import sync_playwright 

def test_dynamic_table():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")

        page.wait_for_selector("//table[@id='taskTable']")

        table = page.locator("//table[@id='taskTable']") 
        print(table) 

        # Locate the rows
        rows = table.locator("tbody tr")
        rows_count = rows.count()
        print(rows_count) 

        #Locate the columns 
        headers = table.locator("thead  th")
        headers_count = headers.count()
        print(headers_count) 

        # Pick the data from row 
        # rows = table.locator("tr").filter(has = page.locator("td"))
        # print(rows) 
        # row_count = rows.count()
        # print(row_count) 
        # # Locate all header columns 
        # headers = table.locator("tr").first.locator("th")
        # print(headers) 


        #To print the Complete Table

        for i in range(rows_count):
            columns = rows.nth(i).locator("td")
            for j in range(headers_count):
                print(columns.nth(j).inner_text(),end = "|")
            print()  


        #Picking the chrome fro  dynamic table and checking the value
        chrome_row = rows.filter(has_text = "Chrome").first 
        assert chrome_row.count() 
        print("We found the chrome") 




