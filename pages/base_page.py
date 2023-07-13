from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys, ActionChains
from PIL import Image
import logging

logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

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

    def hard_click(self, locator):
        #element = self.wait_for_element(locator)
        #element = self.driver.find_element(By.ID, locator)
        self.driver.execute_script("arguments[0].click();", locator)

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def page_down(self):
        self.driver.find_element(By.XPATH, 'html/body').send_keys(Keys.PAGE_DOWN)

    def select_visible_text_by_id(self,locator, value):
        select = Select(self.driver.find_element(By.ID, locator))
        select.select_by_visible_text(value)

    def mouse_hover_and_click_by_xpath(self, value):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, value)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()


    # Add more common methods, like assertions, etc.
