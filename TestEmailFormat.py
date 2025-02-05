from FillPriorItems import FillPriorItems
from RandomTextGenerator import RandomTextGenerator
from SubmitSignUpForm import SubmitSignUpForm
from Test import Test


class TestEmailFormat(Test):
    def __init__(self, page):
        super().__init__(page)
        self.email_field = page.locator("input[name='Email']")

    def execute(self, domain="@familytoolsapp.com"):
        self.__fill_names()
        self.__invalid_email_rejected()
        self.__valid_email_accepted(domain)



    def __invalid_email_rejected(self):

        invalid_email = self.random_text.get()

        self.email_field.fill(invalid_email)

        self.submit.execute()

        is_invalid = self.page.evaluate("document.querySelector('input[type=email]').validity.valid")

        assert not is_invalid, "Test Fail: Invalid email was accepted when it shouldn't be!"

        print("Test Passed: Invalid email correctly triggers validation error.")

    def __fill_names(self):
        fill_prior = FillPriorItems(self.page)
        fill_prior.execute({'firstName': self.random_text.get(), 'lastName': self.random_text.get()})


    def __valid_email_accepted(self, domain):
        valid_email = self.random_text.get() + domain

        self.email_field.fill(valid_email)

        self.submit.execute()

        is_invalid = self.page.evaluate("document.querySelector('input[type=email]').validity.valid")

        assert is_invalid, f"Valid email '{valid_email}' was not accepted!"

        print("Test Passed: Valid email Accepted.")















