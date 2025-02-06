from Test import Test


class TestTextField(Test):
    def __init__(self, page):
        super().__init__(page)
        self.ids = ["firstName", "lastName", "Email", "Password", "Confirm Password"]

    def execute(self):
        for input in self.ids:
            self.__text_field_fillable(input)

    def __text_field_fillable(self, input_name):
        text_field = self.page.locator(f"input[name='{input_name}']")
        random_text = self.random_text.get()

        text_field.fill(random_text)

        assert text_field.input_value() == random_text, "Test Failed: Input field did not accept text!"

        print(f"Test Passed: User is able to enter text into the {input_name}.")

        text_field.clear()

