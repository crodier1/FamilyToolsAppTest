from FillPriorItems import FillPriorItems
from Test import Test


class TestTermsAccepted(Test):
    def __init__(self, page):
        super().__init__(page)
        
    def execute(self):
        fill_prior = FillPriorItems(self.page)
        password = self.random_text.get(8, 20)
        fill_prior.execute({'Password': password, 'Confirm Password': password})
        
        self.__terms_accepted()

    def __terms_accepted(self):
        self.submit.execute()

        error_locator = self.page.locator("text=You must agree to the Terms and Conditions and Privacy Policy.")

        assert error_locator.is_visible(), "Error message did not appear for not agreeing to Terms and Conditions!"

        print("✅ Test Passed: Terms and conditions error appeared as expected.")