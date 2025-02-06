from Test import Test
from TestClickLink import TestClickLink


class TestCreateCalendarEvent(Test):
    def __init__(self, page):
        super().__init__(page)
        self.submit_event_id = "[exid='submitSlideBtn']"

    def execute(self):
        navigate = TestClickLink(self.page)
        navigate.execute("a.group[href='/auth/family/calendar']", "https://familytools.app/auth/family/calendar", "Calendar", False)

        self.__create_event()

        # self.__navigate_to_day_view()

    def __create_event(self):
        self.page.locator("[exid='addEvent']").click()

        self.__event_without_name()

        self.event_name = self.random_text.get()
        self.event_place = self.random_text.get()

        self.page.locator("input[name='Name']").fill(self.event_name)
        self.page.locator("input[name='Location/Note']").fill(self.event_place)

        self.__event_without_group()

        # self.page.locator(f"span:has-text('{self.lat_name}')")

        self.page.locator("[exid='submitSlideBtn']").click()

    def __event_without_name(self):

        self.page.locator(self.submit_event_id).click()

        error_locator = self.page.locator("text=Please enter a valid name for the event.")

        assert error_locator.is_visible(), "Test Failed: Error message did not appear for missing event name!"

        print("✅ Test Passed: Error message appeared for missing event name.")

    def __event_without_group(self):

        self.page.locator(self.submit_event_id).click()

        error_locator = self.page.locator("text=Please assign someone to the event.")

        assert error_locator.is_visible(), "Error message did not appear for missing event assignment!"

        print("✅ Test Passed: Error message appeared for missing event assignment.")

    def set_last_name(self, lastName):
        self.lat_name = lastName

    def __navigate_to_day_view(self):
        self.page.locator("span:has-text('Day View')").click()





