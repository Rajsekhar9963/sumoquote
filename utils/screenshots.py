from datetime import datetime
from PIL import Image

class Screenshots:
    @staticmethod
    def capture_screenshot(driver, screenshot_path):
        driver.save_screenshot(screenshot_path)

    @staticmethod
    def save_screenshot_with_timestamp(driver, screenshot_folder):
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = f"{screenshot_folder}/screenshot_{now}.png"
        Screenshots.capture_screenshot(driver, screenshot_path)
        return screenshot_path