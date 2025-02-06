from Test import Test
from TestEveryOtherField import TestEveryOtherField


class TestNames(Test):
    def __init__(self, page):
        super().__init__(page)
        self.ids = ['firstName', 'lastName']

    def execute(self):

        test_every_other_name = TestEveryOtherField(self.page, ['firstName', 'lastName'])
        test_every_other_name.execute()







