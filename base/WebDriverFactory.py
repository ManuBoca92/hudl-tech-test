from selenium.webdriver.chrome.service import Service


"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations
"""
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    def get_web_driver_instance(self):
        """
        Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        base_url = "https://www.hudl.com/login"
        if self.browser == "chrome":
            service = Service("./drivers/chromedriver.exe")
            driver = webdriver.Chrome(service=service)
        else:
            service = Service("./drivers/geckodriver.exe")
            driver = webdriver.Firefox(service=service)
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(base_url)
        return driver
