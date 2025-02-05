from Test import Test


class FillPriorItems(Test):
    def __init__(self, page):
        super().__init__(page)

    def execute(self, prior):
        for key, value in prior.items():
            current = self.page.locator(f"input[name=\"{key}\"]")
            current.fill(value)