from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def enter_username(self, username):
        username_input = self.wait_for_element(self.USERNAME_INPUT)
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.wait_for_element(self.PASSWORD_INPUT)
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.wait_for_element(self.LOGIN_BUTTON)
        login_button.click()

    # Add more specific login-related methods
    def navigate_to_login_page(self):
        pass