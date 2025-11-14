import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProgressBarPage(BasePage):

    PROGRESS = (By.XPATH, "//span[text()='Progress Bar']")
    START = (By.ID, "startStopButton")
    RESET = (By.ID, "resetButton")
    VALUE = (By.CSS_SELECTOR, "div[role='progressbar']")

    def open_progressbar(self):
        self.click(self.PROGRESS)

    def start(self):
        self.click(self.START)

    def wait_until_25(self):
        while True:
            value = int(self.driver.find_element(*self.VALUE).get_attribute("aria-valuenow"))
            if value >= 25:
                break
            time.sleep(0.1)

    def reset(self):
        self.click(self.RESET)

