from selenium.webdriver.common.by import By


class HomePageLocators(object):
    """A class for home page locators."""

    HOME_MENU = (By.CSS_SELECTOR, '[data-qa-id="webnav-globalnav-home"]')
