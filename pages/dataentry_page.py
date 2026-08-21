from Locators.playwright_reglocators import DataEntryLocators   


class DataEntryPage:
    def __init__(self, page):
        self.page = page

    def get_name_locator(self):
        return self.page.locator(DataEntryLocators.Name).fill("John Doe")

    def get_email_locator(self):
        return self.page.locator(DataEntryLocators.Email).fill("john.doe@example.com")

    def get_phone_locator(self):
        return self.page.locator(DataEntryLocators.Phone).fill("1234567890")

    def get_address_locator(self):
        return self.page.locator(DataEntryLocators.Address).fill("123 Main St, Anytown, USA")
    def get_gender_locator(self):
        return self.page.locator(DataEntryLocators.Gender).click()
    def get_days_locator(self):
        return self.page.locator(DataEntryLocators.Days).click() 
    def get_country_locator(self):
        return self.page.locator("#country").select_option("uk")
    def get_color_locator(self):
        return self. page.locator("#colors").select_option(["red", "blue"])
