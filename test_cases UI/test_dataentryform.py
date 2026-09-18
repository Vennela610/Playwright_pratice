from pages.dataentry_page import DataEntryPage 

class TestDataEntry:
    def test_data_entry(self, browser_page, data_entry):
        data_entry_page = DataEntryPage(browser_page)
        data_entry_page.get_name_locator()
        data_entry_page.get_email_locator()
        data_entry_page.get_phone_locator()
        data_entry_page.get_address_locator() 
        data_entry_page.get_gender_locator()
        data_entry_page.get_days_locator()
        data_entry_page.get_country_locator()
        data_entry_page.get_color_locator()

        data_entry_page.page.wait_for_timeout(9000)  # Wait for 5 seconds before closing the browser