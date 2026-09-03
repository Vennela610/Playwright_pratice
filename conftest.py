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

ROOT = Path(__file__).parent
SCREENSHOTS = ROOT / "screenshots"
VIDEOS = ROOT / "videos"
TRACES = ROOT / "traces"


@pytest.fixture
def page(request):
    test_name = request.node.name
    SCREENSHOTS.mkdir(parents=True, exist_ok=True)
    VIDEOS.mkdir(parents=True, exist_ok=True)
    TRACES.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--start-maximized"])
        context = browser.new_context(
            no_viewport=True,
            record_video_dir=str(VIDEOS),
            record_video_size ={"width" : 1024, "height":768}
        )
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        try:
            yield page
        finally:
            trace_path = TRACES / f"{test_name}.zip"
            context.tracing.stop(path=str(trace_path))
            video = page.video
            context.close()
            if video:
                video_path = video.path()
                print(f"Video saved: {video_path}")
            browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        page = item.funcargs.get("page")
        if report.failed and page:
            SCREENSHOTS.mkdir(parents=True, exist_ok=True)
            screenshot_path = SCREENSHOTS / f"{item.name}.png"
            page.screenshot(path=str(screenshot_path), full_page=True)
            print(f"Failure screenshot saved: {screenshot_path}")
            
@pytest.fixture
def screenshot(page):
    def take_screenshot(name):
        SCREENSHOTS.mkdir(parents=True, exist_ok=True)
        screenshot_path = SCREENSHOTS / f"{name}.png"
        page.screenshot(path=str(screenshot_path), full_page=True)
        print(f"Screenshot saved: {screenshot_path}")
        return screenshot_path

    return take_screenshot