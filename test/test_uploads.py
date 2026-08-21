from playwright.sync_api import sync_playwright 

from pathlib import * 
def test_upload_files(): 
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/") 

        page.wait_for_timeout(3000)
        # Get the project root folder
        project_path = Path(__file__).resolve().parents[1]
        filepath = project_path/"data"/"test_input1.txt" 
        file_2 = project_path/"data"/"test_input2.txt"
        file_3 = project_path/"data"/"test_input3.txt"

        file_upload = page.locator('input[type = "file"]').nth(0)
        file_upload.set_input_files(str(filepath))
        print(filepath.name)
        page.get_by_role("button",name = "Upload Single File").click()
        page.wait_for_timeout(3000)
        print("Single File Uploaded Successfully") 

        multiple_file_upload = page.locator('input[type = "file"]').nth(1)
        multiple_file_upload.set_input_files([str(file_2),str(file_3)])
        print(file_2.name)
        print(file_3.name) 
        page.get_by_role("button",name = "Upload Multiple Files").click()
        page.wait_for_timeout(3000)
        print("Multiple file uploads successfully") 

        project_path = Path(__file__).resolve().parents[1]
        data_folder = project_path/"data"
        files = list(data_folder.iterdir()) #Iterate the contents of the directory 
        for file in files:
            print(file.name) 
        file_uploads = page.locator('input[type = "file"]').nth(1)
        file_uploads.set_input_files([str(file) for file in files if file.is_file()])

        print("All files selected")
        page.get_by_role("button",name = "Upload Multiple files").click()
        page.wait_for_timeout(3000)
        browser.close()




