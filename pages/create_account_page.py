import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CreateAccountPage(BasePage):
    # Locators
    ORGANIZATION_NAME = (By.ID, "accountName")
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "emailAddress")
    PHONE_NUMBER = (By.ID, "phoneNumber")
    PASSWORD = (By.ID, "Password")
    REPEAT_PASSWORD = (By.ID, "repeatPassword")
    AGREE_CHECKBOX = (By.ID, "disclaimerAgree")
    HOW_HEARD = (By.ID, "howHeard")
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button.btn-sumo-primary')

    def enter_organization_name(self, organization_name):
        username_input = self.wait_for_element(self.ORGANIZATION_NAME)
        username_input.send_keys(organization_name)

    def enter_first_name(self, first_name):
        username_input = self.wait_for_element(self.FIRST_NAME)
        username_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        username_input = self.wait_for_element(self.LAST_NAME)
        username_input.send_keys(last_name)

    def enter_email(self, email):
        username_input = self.wait_for_element(self.EMAIL)
        username_input.send_keys(email)

    def enter_phone_number(self, phone_number):
        username_input = self.wait_for_element(self.PHONE_NUMBER)
        username_input.send_keys(phone_number)

    def enter_password(self, password):
        password_input = self.wait_for_element(self.PASSWORD)
        password_input.send_keys(password)

    def confirm_password(self, password):
        password_input = self.wait_for_element(self.REPEAT_PASSWORD)
        password_input.send_keys(password)

    def check_tos_and_pp(self):
        login_button = self.wait_for_element(self.AGREE_CHECKBOX)
        self.hard_click(login_button)

    def select_how_heard(self, value):
        how_heard = self.wait_for_element(self.HOW_HEARD)
        self.driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'))",
                                   how_heard, value)

    def click_on_save(self):
        save_button = self.wait_for_element_clickable(self.SAVE_BUTTON)
        self.hard_click(save_button)

    def launch_create_account_page(self, url):
        self.driver.get(url)
