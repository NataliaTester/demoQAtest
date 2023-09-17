from pages.base_page import BasePage

class HomePage(BasePage):
    def validate_page_load(self):
        assert '<img class="banner-image" src="/images/WB.svg"' in self.driver.page_source #Gets the source of the current page.

       # banner_image = self.driver.find_element(By.CSS_SELECTOR, 'img.banner-image[src="/images/WB.svg"]')
       # assert banner_image.is_displayed(), "Banner Selenium s t image is not displayed on the page"