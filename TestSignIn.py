from Test import Test


class TestSignIn(Test):
    def __init__(self, page, account_info):
        super().__init__(page)
        self.account_info = account_info
    def execute(self):
        self.page.goto("https://familytools.app/sign_in")
        self.page.locator("input[name='Email']").fill(self.account_info['Email'])
        self.page.locator("input[name='Password']").fill(self.account_info['Password'])
        self.page.locator("[exid='signInButton']").click()

        error_locator = self.page.locator("text=Failed to sign you in. Please verify your email and password.")

        assert not error_locator.is_visible(), "Test Failed: Error message did not appear for Invalid email and Password!"

        print("✅ Test Passed: Error message appeared for Invalid email and password.")
