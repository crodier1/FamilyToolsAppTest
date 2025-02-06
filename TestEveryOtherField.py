from Test import Test


class TestEveryOtherField(Test):
    def __init__(self, page, ids):
        super().__init__(page)
        self.ids = ids

    def execute(self):
        for idx, input in enumerate(self.ids):

            name_field = self.page.locator(f"input[name='{input}']")
            name_field.fill(self.random_text.get())

            other_id = self.ids[(idx + 1) % len(self.ids)]

            other_field = self.page.locator(f"input[name='{other_id}']")

            other_field.clear()

            self.submit.execute()

            is_invalid = self.page.evaluate(f"document.querySelector('input[name=\"{other_id}\"]').validity.valid")

            assert not is_invalid, f"Test Fail: {other_id} was accepted when it shouldn't be!"

            print(f"✅ Test Passed: missing {other_id} correctly triggers validation error.")

