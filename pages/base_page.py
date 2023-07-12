from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from PIL import Image
import logging

logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def capture_screenshot(self, screenshot_path):
        self.driver.save_screenshot(screenshot_path)
        logger.info(f"Screenshot saved: {screenshot_path}")

    def save_screenshot_with_timestamp(self, screenshot_folder):
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = f"{screenshot_folder}/screenshot_{now}.png"
        self.capture_screenshot(screenshot_path)
        return screenshot_path

    def click(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    # Add more common methods, like assertions, etc.