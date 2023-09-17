import time
from selenium.webdriver import Keys, ActionChains
from PageObject.form_page_locators import FormPageLocators as Locators
from pages.base_page import BasePage
class FormPage(BasePage):
    def fill_fields_and_submit(self):
        first_name = 'Test'
        last_name = 'LastTest'
        email = 'testemail@test.com'
        self.remove_footer()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        #self.scroll_vertical(800)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys('8888888888')
        self.element_is_visible(Locators.SUBJECT).click()
        actions = ActionChains(self.driver)
        actions.send_keys("Maths").perform()
        time.sleep(2)
        actions.send_keys(Keys.ENTER).perform()
        self.element_is_visible(Locators.HOBBIES).click()
        self.element_is_visible(Locators.FILE_INPUT).send_keys(r'D:\project\newTest\fileTest.txt')
        self.scroll_vertical(800)
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys("Test Address %$!@@!^%@ Line 1")
        self.element_is_visible(Locators.select_state).click()
        self.dropdown_byvalue("NCR")
        self.element_is_visible(Locators.select_city).click()
        self.dropdown_byvalue("Delhi")
        time.sleep(2)
        self.element_is_visible(Locators.SUBMIT).click()
        time.sleep(5)
        return first_name, last_name, email

    def form_result(self):
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)

        result_text = [i.text for i in result_list]
           # for i in result_list: or we can use it
           # result_text.append(i.text)

        return result_text

