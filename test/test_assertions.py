from pytest_check import check
def test_sort_assertions(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    check.equal(page.title(),"Demo webshop")
    check.is_true(page.locator(".ico-register")).is_visible()
    print("Is visible")
    check.is_true(page.locator(".ico-login").is_visible())
    print("Login is visisble in the application")
