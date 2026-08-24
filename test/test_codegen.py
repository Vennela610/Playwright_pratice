import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_role("textbox", name="Enter Name").click()
    page.get_by_role("textbox", name="Enter Name").fill("Venni")
    page.get_by_role("textbox", name="Enter EMail").click()
    page.get_by_role("textbox", name="Enter EMail").fill("Venni@gmail.com")
    page.get_by_role("textbox", name="Enter Phone").click()
    page.get_by_role("textbox", name="Enter Phone").fill("1234567890")
    page.locator("div:nth-child(9)").first.click()
    page.locator("div:nth-child(9)").first.click()
    page.get_by_role("textbox", name="Address:").fill("Hyderabad.")
    page.get_by_role("radio", name="Male", exact=True).check()
    page.get_by_role("checkbox", name="Sunday").check()
    page.get_by_role("checkbox", name="Monday").check()
    page.get_by_label("Country:").select_option("india")
    page.get_by_label("Colors:").select_option("blue")
    page.get_by_label("Sorted List:").select_option("deer")
    page.locator("#datepicker").click()
    page.locator("#ui-datepicker-div").get_by_role("link", name="2", exact=True).click()
    page.locator("#txtDate").click()
    page.get_by_role("link", name="31").click()
    page.get_by_placeholder("Start Date").fill("2026-11-13")
    page.get_by_placeholder("End Date").fill("2027-03-05")
    page.locator("#post-body-1307673142697428135").get_by_role("button", name="Submit").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright) 



import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_role("link", name="2", exact=True).click()
    page.locator("td:nth-child(4) > input").first.check()
    page.get_by_role("link", name="3", exact=True).click()
    page.locator("tr:nth-child(3) > td:nth-child(4) > input").check()
    page.get_by_role("link", name="4", exact=True).click()
    page.locator("tr:nth-child(5) > td:nth-child(4) > input").check()
    page.get_by_role("textbox", name="Select an item").click()
    page.get_by_text("Item 43").click()
    page.locator(".ui-slider-handle").first.click()
    page.locator(".ui-slider-range").click()
    page.locator(".svg-container").click()
    page.locator("#draggable").click()
    page.locator("#draggable").click()
    page.locator("#draggable").click()
    page.locator("#draggable").click()
    page.locator("#draggable").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)



