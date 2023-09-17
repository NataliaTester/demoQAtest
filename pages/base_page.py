
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    _handles = None

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.close()
        self.update_window_handles()

    def update_window_handles(self):
        self._handles = self.driver.window_handles

    def get_url(self):
        return self.driver.current_url

    def click(self, locator):
        self.find_element(locator).click()

    def find_element(self, locator):
        return self.driver.find_element(locator[0], locator[1])

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def dropdown_byvalue(self, value):
        actions = ActionChains(self.driver)
        actions.send_keys(value).perform()
        time.sleep(2)
        actions.send_keys(Keys.ENTER).perform()

    def scroll_vertical(self, y_value):
        self.driver.execute_script(f'scrollTo(0,{y_value})')

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script('document.getElementById("fixedban").style.display = "none";')

    def go_to_main_page(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def validate_page_load(self):
        assert '<img class="banner-image" src="/images/WB.svg"' in self.driver.page_source
