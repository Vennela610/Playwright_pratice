import pytest
# from constants import *
from Utilities.data_reader import *
from Utilities.data_writer import *
import json 
from pathlib import *

from playwright.sync_api import sync_playwright


@pytest.fixture
def data_entry():
    return load_json("data/Data_Entry.json")


@pytest.fixture
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        yield page
        browser.close() 

# @pytest.hookimpl(hookwrapper = True)    
# def pytest_makereport(item,call):
#     outcome = yield 
#     report = outcome.get_result() 

#     if report.when == "call" and report.failed: #Like Actual text execution
#         page = item.funcargs.get("page")
#         if page:
#             screenshot_folder = Path("screenshots")
