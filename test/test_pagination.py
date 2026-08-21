from playwright.sync_api import  sync_playwright  
def test_date_pickers():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(3000) 

        table = page.locator("#productTable")
        print("/n pagination Table /n")
        rows = table.locator("tbody tr") 
        rows_count = rows.count()
        print("Total Rows: ",rows_count) 

        # To get the total columns 
        headers = table.locator("thead th")
        headers_count = headers.count() 
        print("Total Columns: ",headers_count)


        # # Current Page
        # for i in range(row_count):
        #     row = rows.nth(i)
        #     cells = row.locator("td")
        #     for j in range(cells.count()):
        #         print(cells.nth(j).inner_text(),end="|")
        # print()     

        # #Product names
        # for i in range(row_count): # 1,2,3,4,5
        #     product = rows.nth(i).locator("td").nth(1).inner_text()
        #     print(product)

        # To show current Page
        for i in range(rows_count):
            row = rows.nth(i)
            cells = row.locator("td")
            for j in range(cells.count()):
                print(cells.nth(j).inner_text(),end = "|")
        for i in range(rows_count):
            products = rows.nth(i).locator("td").nth(i).inner_text()
            print(products)