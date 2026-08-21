from playwright.sync_api import sync_playwright


def test_sorted_list():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_selector("#animals option")

        animals_list = page.locator("#animals option").all_inner_texts()
        print("Animals list (as shown):", animals_list)

        alphabetical = sorted(animals_list, key=lambda s: s.lower())
        print("Alphabetical sorted list:", alphabetical)

        if animals_list == alphabetical:
            print("Sorted list Verified")
        else:
            print("List is not sorted; printed alphabetical order above.")

        browser.close()

