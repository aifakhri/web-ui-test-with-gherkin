from ast import For
import pytest

from selenium.webdriver import Firefox
from .pageObject.contextMenu import ContextMenu
from .pageObject.dynamicControl import DynamicControl
from .pageObject.formAuth import FormAuth

URL = "http://the-internet.herokuapp.com"



@pytest.fixture
def driver():
    driver = Firefox()
    yield driver.get(URL)
    driver.close()

@pytest.fixture
def form_auth(driver):
    return FormAuth(driver)

@pytest.fixture
def dynamic_Control(driver):
    return DynamicControl(driver)

@pytest.fixture
def context_menu(driver):
    return ContextMenu(driver)