# from playwright.sync_api import sync_playwright 

# def test_iframes():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless = False)
#         page = browser.new_page()
#         page.goto("https://demoqa.com/frames")
#         # page.wait_for_timeout(3000)
#         page.wait_for_load_state("domcontentloaded")
#         #Targeting the frames from the demosite and capturing the first heading from the frames 

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/frames")
    page.locator("#frame1").content_frame.locator("html").click()
    page.locator("#frame1").content_frame.get_by_role("heading", name="This is a sample page").click()
    page.locator("#frame2").content_frame.get_by_role("heading", name="This is a sample page").click()
    page.locator("#frame1").content_frame.get_by_role("heading", name="This is a sample page").click()
    page.get_by_text("Sample Iframe page There are").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)