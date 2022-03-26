from locators.LoginPage import LoginPageLocators

from pages.base import BasePage


class LoginPage(BasePage):
    """Login page action methods come here"""

    def get_email_field(self):
        return self.wait_for_element(*LoginPageLocators.EMAIL_FIELD)

    def get_password_field(self):
        return self.wait_for_element(*LoginPageLocators.PASSWORD_FIELD)

    def get_login_button(self):
        return self.wait_for_element(*LoginPageLocators.LOGIN_BUTTON)

    def get_login_error_container(self):
        return self.wait_for_element(*LoginPageLocators.LOGIN_ERROR_CONTAINER)

    def login(self, email, password):
        self.get_email_field().send_keys(email)
        self.get_password_field().send_keys(password)
        self.get_login_button().click()
