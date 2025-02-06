from FillPriorItems import FillPriorItems
from Test import Test
from TestEveryOtherField import TestEveryOtherField


class TestPasswords(Test):
    def __init__(self, page):
        super().__init__(page)
        self.passwordIds = ['Password', 'Confirm Password']

    def execute(self):
        fill_prior = FillPriorItems(self.page)
        fill_prior.execute({'firstName': self.random_text.get(), 'lastName': self.random_text.get(), "Email": self.random_text.get() + "@familytoolapp.com"})
        
        self.__missing_password_fields()

        self.__password_too_short()
        
        self.__password_doesnt_match()

    def __missing_password_fields(self):
        test_every_other_name = TestEveryOtherField(self.page, self.passwordIds)
        test_every_other_name.execute()

    def __password_too_short(self):
        password_too_short = self.random_text.get(1, 7)

        for id in self.passwordIds:
            current = self.page.locator(f"input[name='{id}']")
            current.fill(password_too_short)

        self.submit.execute()

        error_locator = self.page.locator("text=Your password should be at least 8 characters long.")

        assert error_locator.is_visible(), "Error message did not appear for short password!"

        print("✅ Test Passed: Password validation error appeared as expected for password less than 8 characters.")

    def __password_doesnt_match(self):

        for id in self.passwordIds:
            password = self.random_text.get(8, 20)
            current = self.page.locator(f"input[name='{id}']")
            current.fill(password)

        self.submit.execute()

        error_locator = self.page.locator("text=Passwords do not match.")

        assert error_locator.is_visible(), "Error message did not appear for passwords that do no match!"

        print("✅ Test Passed: Password validation error appeared as expected for passwords that don't match.")





    
