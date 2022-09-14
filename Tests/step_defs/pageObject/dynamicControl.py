from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from .common import Common


class DynamicControl(Common):

    DYNAMIC_CONTROL_PAGE = (By.LINK_TEXT, "Dynamic Control")
    CHECKBOX_LOCATOR = (By.XPATH, "//input[@type='checkbox']")
    INPUT_TEXT_LOCATOR = (By.XPATH, "//input[@type='text']")
    STATE_CHANGE_LOCATOR = (By.ID, "message")

    def navigate_to_dynanic_control_page(self):
        self._wait_for(self.CHECKBOX_LOCATOR).click()

    def check_checkbox_element(self):
        try:
            self._wait_for(self.CHECKBOX_LOCATOR)
            return "Checkbox Element Present"
        except TimeoutException:
            return "No Checkbox Element"

    def check_input_text_element(self):
        return self._wait_for(self.INPUT_TEXT_LOCATOR).is_enabled()

    def click_control_button(self, element):
        if (element == 'checkbox') or (element == 'input'):
            control_btn_xpath = f"//form[@id='{element}'-example]/button"
            control_btn_locator = (By.XPATH, control_btn_xpath) 
        else:
            return "Element not found"
        
        self._find(control_btn_locator).click()
        self._wait_for(self.STATE_CHANGE_LOCATOR)