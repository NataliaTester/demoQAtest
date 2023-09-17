from selenium.webdriver.common.by import By


class BrowserPageLocators:
    brw_wdw_path = "/browser-windows"
    sample_path = "/sample"
    tab_btn_loc = (By.CSS_SELECTOR, "#tabButton")
    wdw_btn_loc = (By.CSS_SELECTOR, "#windowButton")
    msg_wdw_btn_loc = (By.CSS_SELECTOR, "#messageWindowButton")
    confirm_msg = "Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization."
