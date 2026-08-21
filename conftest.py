import pytest
# from constants import *
from Utilities.data_reader import *
from Utilities.data_writer import *
import json

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