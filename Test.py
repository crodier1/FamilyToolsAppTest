from RandomTextGenerator import RandomTextGenerator
from SubmitSignUpForm import SubmitSignUpForm


class Test:
    def __init__(self, page):
        self.page = page
        self.random_text = RandomTextGenerator()
        self.submit = SubmitSignUpForm(page)