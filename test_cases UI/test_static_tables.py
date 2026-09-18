from playwright.sync_api import sync_playwright 

def test_static_table():
    with sync_playwright() as P:
        browser = P.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/") 

        # Wait for the table to appear rather than using a fixed sleep
        page.wait_for_selector("//table[@name='BookTable']")

        table = page.locator("//table[@name='BookTable']") 
        print(table) 

        #Up to here browser will go to that particular website and will pickup the the specfic locator
        #which having the name as BookTable 
        #How mamy rows in the table
        #It locate all rows in table
        rows = table.locator("tbody tr") #here under tbody only tr(table rows present) So after finding that specfic table locator will go to table body in that it will go to rows 
        print(rows)
        #th is atable header nothing but table columns(headings) 
        # Which will pick the specfic row 
        specfic_row = table.locator("tr").filter(has = page.locator("td"))
        print(specfic_row)
        # row_count = specfic_row.count() 
        # print(row_count)

        headers = table.locator("tr").first.locator("th") 
        print(headers)
        # Get the total rows count 
        rows_count = rows.count() 
        print(rows_count) 
        #Get the total number of columns
        column_count = headers.count() 
        print(column_count) 

        if rows_count < 2:
            print("Not enough rows to read the second row")
            return

        # To get  the header names 
        # print("\n Header names \n")
        # for i in range(column_count):
        #     header  = headers.nth(i).inner_text()
        #     print(header) 
        # To get the column names 

        # print("\n Row names \n")
        # for i in range(rows_count):
        #     rows1 = rows.nth(i).inner_text()
        #     print(rows1)
        # To print the entire table  
        # print("\n Entire Table \n")
        # for i in range(rows_count):
        #     column = rows.locator("td")
        #     for j in range(column_count): 
        #         print(column.nth(j).inner_text(),end = "|") 
        #         print() 


        #To print second row 
        print("\n Second Row \n")

        second_row = rows.nth(1).locator("td")

        for i in range(column_count):
            print(second_row.nth(i).inner_text(),end = "|")
        print() 

        # #To print the book names 
        # for i in range(row_count):
        #     book = rows.nth(i).locator("td").nth(0).inner_text()
        #     print(book) 

        for i in range(rows_count):
            row = rows.nth(i)
            td_count = row.locator("td").count()
            if td_count < 2:
                print(f"Skipping row {i}: not enough cells ({td_count})")
                continue
            books = row.locator("td").nth(0).inner_text()
            author = row.locator("td").nth(1).inner_text() 
            print(books + "|" + author)

        # # TO print a specfic cell 
        # cell_value = rows.nth(0).locator("td").nth(1)
        # print(cell_value)