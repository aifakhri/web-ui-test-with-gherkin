from selenium.webdriver.common.by import By

from .common import Common



class FormAuth(Common):

    FORM_AUTH_PAGE = (By.LINK_TEXT, "Form Authentication")
    FORM_USERNAME = (By.ID, "username")
    FORM_PASSWORD = (By.ID, "password")
    FORM_LOGIN_BUTTON = (By.XPATH, "//button[@type='submit]")
    FORM_ALERT = (By.ID, "flash")
    FORM_LOGOUT_BUTTON = (By.CLASS_NAME, "button")

    def navigate_to_login_page(self):
        self.wait_for(self.FORM_AUTH_PAGE).click()
    
    def enter_username(self):
        self.wait_for(self.FORM_USERNAME)
    
    def enter_password(self):
        self.find(self.FORM_USERNAME)

    def click_login_button(self):
        self.find(self.FORM_LOGIN_BUTTON).click()

    def click_logout_button(self):
        self.find(self.FORM_LOGOUT_BUTTON).click()

    def check_login_logout_status(self):
        return self.wait_for(self.FORM_ALERT)