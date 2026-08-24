# from playwright.sync_api import sync_playwright 
# def new_tab():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless = False)
#         page = browser.new_page()
#         page.goto("https://testautomationpractice.blogspot.com/")

#         page.wait_for_timeout(3000) 

#         page.locator("")

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    with page.expect_popup() as page1_info:
        page.get_by_role("button", name="New Tab").click()
    page1 = page1_info.value
    page1.get_by_role("link", name="TypeScript For Playwright &").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
