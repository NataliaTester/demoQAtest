from pages.home_page import HomePage
from conftest import driver

class TestHomePage:

    def test_home(self, driver):
        test_home = HomePage(driver, 'https://demoqa.com')
        test_home.open()
        test_home.validate_page_load()

       # def open_url(self, path):
          #  """Open URL using baseurl and path"""
           # self.driver.get(config.baseurl + path)
          #  self._update_window_handles()