import pytest
from base.WebDriverFactory import WebDriverFactory


@pytest.fixture()
def setUp(request, browser):
    web_driver_factory =  WebDriverFactory(browser)
    driver = web_driver_factory.get_web_driver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")