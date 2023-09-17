from selenium.webdriver.common.by import By
from random import randint

class FormPageLocators:
    LAST_NAME = (By.CSS_SELECTOR, '#lastName')
    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    GENDER = (By.CSS_SELECTOR, f"label[for='gender-radio-{randint(1, 3)}']")
    MOBILE = (By.CSS_SELECTOR, '#userNumber')
    SUBJECT = (By.CSS_SELECTOR, '#subjectsContainer')
    HOBBIES = (By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{randint(1, 3)}']")
    FILE_INPUT = (By.CSS_SELECTOR, "#uploadPicture")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    SUBMIT = (By.CSS_SELECTOR, "#submit")
    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
    date_picker = (By.CSS_SELECTOR, "#dateOfBirthInput")
    date_picker_month = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    date_picker_year = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    select_state = (By.CSS_SELECTOR, "#state")
    select_city = (By.CSS_SELECTOR, "#city")
    HOME_PAGE = (By.XPATH, '//header/a[1]')
