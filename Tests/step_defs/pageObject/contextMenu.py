from selenium.webdriver.common.by import By

from .common import Common


class ContextMenu(Common):

    CONTEXT_PAGE = (By.LINK_TEXT, "context_menu")
    CONTEXT_BOX = (By.ID, "hot-spot")

    def navigate_to_context_menu_page(self):
        self._wait_for(self.CONTEXT_PAGE)

    def click_the_context_menu(self):
        context_menu_locator = self.find(self.CONTEXT_BOX)
        self._right_click(context_menu_locator).perform

    def check_alert(self):
        return self._alert().accept()
        

