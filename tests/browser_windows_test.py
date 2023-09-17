
from conftest import driver
from pages.browser_windows_page import BrowserWindowsPage


class TestBrowserWindows:

    def browser_windows_page(self, driver):
        browser_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
        browser_page.open()
        browser_page.select_tab_button()
        browser_page.validate_tab_button()
        browser_page.close()


