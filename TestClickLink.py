from Test import Test


class TestClickLink(Test):
    def __init__(self, page):
        super().__init__(page)

    def execute(self, id, url, page_name, create_account = True):
        self.page.locator(id).click()

        if create_account:
            self.submit.execute()

        try:  # Wrap in a try-except block to catch assertion errors
            self.page.wait_for_url(url)
            print(f"✅ Test Passed: Navigation to {page_name} successful!")  # Success message
        except AssertionError as e:  # Catch assertion errors
            print(f"Test Failed: Navigation to {page_name} failed!: {e}")  # Failure message, include the error

