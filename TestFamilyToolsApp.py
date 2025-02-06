from CheckUrlStatus import CheckUrlStatus
from TestCreateCalendarEvent import TestCreateCalendarEvent
from TestDeleteFamily import TestDeleteFamily
from TestEmailFormat import TestEmailFormat
from TestNames import TestNames
from TestPasswords import TestPasswords
from TestSignIn import TestSignIn
from TestSuccessfulAccountCreation import TestSuccessfulAccountCreation
from TestTermsAccepted import TestTermsAccepted
from TestTextField import TestTextField
from playwright.sync_api import sync_playwright, expect


class TestFamilyToolsApp:
    def __init__(self):
        self.testUlr = CheckUrlStatus()

    def execute(self):
        if not self.testUlr.execute("https://familytools.app/"):
            return

        self.__run_test()
    def __run_test(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            self.page = browser.new_page()
            self.page.goto("https://familytools.app/")

            for class_name in [TestTextField, TestNames, TestEmailFormat, TestPasswords, TestTermsAccepted]:
                current_class = class_name(self.page)
                current_class.execute()

            create_account = TestSuccessfulAccountCreation(self.page)
            create_account.execute()

            create_calender_event = TestCreateCalendarEvent(self.page)
            create_calender_event.set_last_name(create_account.newAccountInformation['lastName'])
            create_calender_event.execute()

            delete_family = TestDeleteFamily(self.page, create_account.newAccountInformation)

            delete_family.execute()

            sign_in = TestSignIn(self.page, create_account.newAccountInformation)
            sign_in.execute()


            browser.close()


