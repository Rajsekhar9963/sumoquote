import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="session")
def driver():
    # Setup: Create the WebDriver session
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver

    # Teardown: Quit the WebDriver session
    driver.quit()
