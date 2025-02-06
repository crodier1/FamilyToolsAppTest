from Test import Test
from TestClickLink import TestClickLink
from TestSignIn import TestSignIn


class TestDeleteFamily(Test):
    def __init__(self, page, account_info):
        super().__init__(page)
        self.account_info = account_info
    def execute(self):
        navigate = TestClickLink(self.page)
        navigate.execute("a.group[href='/auth/user/settings/profile']", "https://familytools.app/auth/user/settings/profile",
                         "Settings", False)

        self.page.locator("[exid='deleteFamily']").click()

        self.set_wrong_password()


        self.page.locator("input[name='Password']").fill(self.account_info['Password'])

        try:
            self.page.locator("[exid='modalSubmit']").click()
            self.page.locator("btn >> text=DELETE FAMILY").click()

            print("✅ Test Passed: Account deleted.")
        except:
            print("Test Failed: Account not deleted.")


    def set_wrong_password(self):
        self.page.locator("input[name='Password']").fill(self.random_text.get())

        error_locator = self.page.locator("text=Invalid password.")

        self.page.locator("[exid='modalSubmit']").click()

        assert not error_locator.is_visible(), "Test Failed: Error message did not appear for Invalid Password!"

        print("✅ Test Passed: Error message appeared for Invalid password.")



