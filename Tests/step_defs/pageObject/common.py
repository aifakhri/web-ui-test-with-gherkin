from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains




class Common():

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)
        self._action = ActionChains(self.driver)

    def _wait_for(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def _find(self, locator):
        return self.driver.find_element(*locator)

    def _right_click(self, element):
        return self._action.context_click(element)

    def _alert(self):
        return self._wait(EC.alert_is_present())