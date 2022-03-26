from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, *locator, timeout=15):
        element = None
        try:
            print(f"Waiting for maximum :: {timeout} "
                  f"seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout)
            element = wait.until(EC.element_to_be_clickable(locator))
            print("Element appeared on the web page")
        except NoSuchElementException:
            print("Element not appeared on the web page")
            print_stack()
        return element
