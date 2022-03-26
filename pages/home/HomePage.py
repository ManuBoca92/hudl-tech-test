from locators.HomePage import HomePageLocators
from pages.base import BasePage


class HomePage(BasePage):
    """Home page action methods come here"""

    def get_home_menu_nav(self):
        return self.wait_for_element(*HomePageLocators.HOME_MENU)
