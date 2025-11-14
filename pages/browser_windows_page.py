from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BrowserWindowsPage(BasePage):

    BROWSER_WINDOWS = (By.XPATH, "//span[text()='Browser Windows']")
    NEW_WINDOW = (By.ID, "windowButton")
    SAMPLE_TEXT = (By.ID, "sampleHeading")

    def open_menu(self):
        self.click(self.BROWSER_WINDOWS)

    def open_new_window(self):
        self.click(self.NEW_WINDOW)

    def validate_new_window(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        text = self.get_text(self.SAMPLE_TEXT)
        return "This is a sample page" in text

    def close_new_window(self):
        self.driver.close()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

