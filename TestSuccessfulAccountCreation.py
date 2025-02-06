from FillPriorItems import FillPriorItems
from Test import Test
from TestClickLink import TestClickLink


class TestSuccessfulAccountCreation(Test):
    def __init__(self, page):
        super().__init__(page)

    def execute(self):
        newPassword = self.random_text.get(8,20)
        self.newAccountInformation = {'firstName': self.random_text.get(), 'lastName': self.random_text.get(), "Email": self.random_text.get(5,15) + "@familytoolapp.com", "Password": newPassword, "Confirm Password": newPassword}

        fill_previous = FillPriorItems(self.page)
        fill_previous.execute(self.newAccountInformation)

        self.__create_new_account()



    def __create_new_account(self):
        navigate = TestClickLink(self.page)
        navigate.execute("input[exname='AcceptTermsAndPrivacyPolicy']", "https://familytools.app/auth/user/dashboard", "Dashboard and Account Creation")



