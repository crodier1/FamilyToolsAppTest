class SubmitSignUpForm:
    def __init__(self, page):
        self.page = page

    def execute(self):
        button = self.page.locator("[exid='createAccount']")
        button.click()