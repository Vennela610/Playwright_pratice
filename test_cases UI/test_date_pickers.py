from playwright.sync_api import  sync_playwright  
def test_date_pickers():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(3000)
        # date_picker1 = page.locator("#datepicker")
        # date_picker1.scroll_into_view_if_needed()
        # date_picker1.fill("11/19/2025")
        # print("date_picker1 is:", date_picker1.input_value())

        date_picker2 = page.locator("#txtDate")
        date_picker2.click()
        # The calendar UI uses spans, not <select> elements. Fill input directly.
        page.locator(".ui-datepicker-month").select_option(label = "Feb")
        page.locator(".ui-datepicker-year").select_option("2016")
        page.locator(".ui-datepicker-calendar td a",has_text = "18").click()
        print("Date_picker2 is: ",date_picker2.input_value())
        page.wait_for_timeout(3000) 

        # date_picker3_start_date= page.locator("#start-date")
        # date_picker3_end_date = page.locator("#end-date")
        # date_picker3_start_date.fill("2026-03-20")
        # date_picker3_end_date.fill("2026-05-21")
        # print("Start Date is: ",date_picker3_start_date.input_value())
        # print("End Date is: ",date_picker3_end_date.input_value())
        # page.wait_for_timeout(4000)

