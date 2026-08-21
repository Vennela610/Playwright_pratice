from playwright.sync_api import sync_playwright, expect


def test_scrolling_down():
    with sync_playwright() as p:        
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(3000)

        combo_box = page.locator("#comboBox")
        combo_box.click()

        drop_down = page.locator("#dropdown")
        options = drop_down.locator(".option")

        count = options.count()
        print("The Scrolling dropdown count is:", count)
        assert count >= 0 

        for i in range(options.count()):
            print(i,options.nth(i).inner_text())
        page.wait_for_timeout(1000)
        item = drop_down.locator(".option").filter(has_text="Item 35") 

        # Ensure the element is scrolled into view within the custom container
        item.scroll_into_view_if_needed()

        # Click the option
        item.click()
        page.wait_for_timeout(1000)
        expect(combo_box).to_have_value("Item 35")  # Verify the selected value
        print(combo_box)
        print("Selected the item")