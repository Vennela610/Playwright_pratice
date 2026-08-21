from playwright.sync_api import sync_playwright
def test_sliders_drag_drop():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")

        # wait for DOMContentLoaded and give widgets a moment to initialize
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_timeout(1000)

        # prefer ID locators when present; otherwise fall back to textual locators
        try:
            drag = page.locator("#draggable")
            drop = page.locator("#droppable")
            drag.wait_for(state="visible", timeout=5000)
            drop.wait_for(state="visible", timeout=5000)
        except Exception:
            drag = page.get_by_text("Drag me to my target")
            drop = page.get_by_text("Dropped!")
            drag.wait_for(state="visible", timeout=5000)
            drop.wait_for(state="visible", timeout=5000)

        # perform drag -> drop with an increased timeout
        drag.drag_to(drop, timeout=20000)
        page.wait_for_timeout(1000)

        print("Drag came to the drop location successfully")

        #Handling the sliders 
        sliders = page.locator("#slider-range")
        handlers = sliders.locator(".ui-slider-handle")
        print("Number of handlers: ",handlers.count())

        #Now handling the first slider 
        first_handle = handlers.nth(0)
        print("Identified the first handler")
        print(first_handle.bounding_box()) 

        #Moving the first slider 
        first_handle.hover()
        page.mouse.down()

        # page.mouse.move(first_handle.bounding_box()["x"] + 100,first_handle.bounding_box()["y"] + 150)
        page.mouse.move(first_handle.bounding_box()["x"] + 300,first_handle.bounding_box()["y"] + 750)

        page.wait_for_timeout(4000)
        browser.close()