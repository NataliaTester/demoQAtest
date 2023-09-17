
from PageObject.browser_page_locators import BrowserPageLocators as Locators
from pages.base_page import BasePage

class BrowserWindowsPage(BasePage):

    def select_tab_button(self):
        self.element_is_visible(Locators.tab_btn_loc)

    def validate_tab_button(self):
        assert ("https://demoqa.com/sample" == self.get_url()) and \
               ("This is a sample page" in self.driver.page_source)


