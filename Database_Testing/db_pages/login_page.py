class LoginPage:
    def __init__(self,page):
        self.page = page
        self.email = page.locator("#Email")
        self.password_locator = page.locator("#password")
        self.login_button_locator = page.locator("#login-button")

    def navigate_to_login_page(self):
        self.page.goto("https://parabank.parasoft.com/parabank/index.htm") 


    def login(self, username, password):
        self.username_locator.fill(username)
        self.password_locator.fill(password)
        self.login_button_locator.click()        