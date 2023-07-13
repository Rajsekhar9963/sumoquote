import time

import pytest
from pages.create_account_page import CreateAccountPage
from utils.config import get_data
from utils.logger import logger
from utils.screenshots import Screenshots
from conftest import driver


@pytest.mark.parametrize("url, organization_name, first_name, last_name, email, phone_number, password, ad_option", get_data())
def test_successful_create_account(driver, url, organization_name, first_name, last_name, email, phone_number, password, ad_option):
    # Test Case: Successful Login
    create_account_page = CreateAccountPage(driver)
    create_account_page.launch_create_account_page(url)
    create_account_page.enter_organization_name(organization_name)
    create_account_page.enter_first_name(first_name)
    create_account_page.enter_last_name(last_name)
    create_account_page.enter_email(email)
    create_account_page.page_down()
    create_account_page.enter_phone_number(phone_number)
    create_account_page.enter_password(password)
    create_account_page.confirm_password(password)
    create_account_page.page_down()
    create_account_page.select_how_heard(ad_option)
    create_account_page.check_tos_and_pp()
    create_account_page.click_on_save()
    time.sleep(10)
    logger.info("Login successful.")
    screenshot_folder = "screenshots"
    screenshot_path = Screenshots.save_screenshot_with_timestamp(driver, screenshot_folder)
    logger.info(f"Screenshot saved: {screenshot_path}")