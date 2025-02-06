from playwright.sync_api import sync_playwright
class CheckUrlStatus:
    def execute(self, url):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            try:
                response = page.goto(url)  # Wait for the response

                status = response.status

                if status in (200, 201, 204):
                    print(f"✅ Test Passed: {url} returned a successful status code: {status}")
                    browser.close()
                    return True  # Success!
                elif status in (404, 401, 403, 408, 500, 502, 503, 504):
                    print(f"Test Failed: {url} returned an error status code: {status}")
                    browser.close()
                    return False  # Failure!
                else:
                    print(f"{url} returned an unexpected status code: {status}")
                    browser.close()
                    return False  # Treat other codes as failures for this example. You might want to handle them differently.

            except Exception as e:
                print(f"Error navigating to {url}: {e}")
                browser.close()
                return False  # Failure due to navigation error