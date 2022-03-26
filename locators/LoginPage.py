from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """A class for login page locators."""

    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'logIn')
    LOGIN_ERROR_CONTAINER = (By.CLASS_NAME, 'login-error-container')
