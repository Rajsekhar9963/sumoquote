import pytest
from pages.login_page import LoginPage
from utils.config import get_login_credentials
from utils.logger import logger
from utils.screenshots import Screenshots
from conftest import driver


@pytest.mark.parametrize("username, password", get_login_credentials())
def test_successful_login(driver, username, password):
    # Test Case: Successful Login
    login_page = LoginPage(driver)
    login_page.navigate_to_login_page()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()
    # Assertion and further test steps
    logger.info("Login successful.")
    screenshot_folder = "screenshots"
    screenshot_path = Screenshots.save_screenshot_with_timestamp(driver, screenshot_folder)
    logger.info(f"Screenshot saved: {screenshot_path}")