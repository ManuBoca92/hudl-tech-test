import pytest
from pages.home.HomePage import HomePage
from pages.login.LoginPage import LoginPage


@pytest.mark.usefixtures("setUp")
class TestsLogin:
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("ebonom.n.mfam@gmail.com", "askmeforpassword")
        home_page = HomePage(self.driver)
        home_menu = home_page.get_home_menu_nav().is_displayed()
        assert home_menu is True

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("test@example.com", "useanyrandometext")
        error_message = login_page.get_login_error_container().is_displayed()
        assert error_message is True

    def test_missing_email_field_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("", "tester123")
        error_message = login_page.get_login_error_container().is_displayed()
        assert error_message is True

    def test_missing_password_field_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("test@example.com", "")
        error_message = login_page.get_login_error_container().is_displayed()
        assert error_message is True
