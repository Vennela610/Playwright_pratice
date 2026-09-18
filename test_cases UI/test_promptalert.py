import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Prompt Alert").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)