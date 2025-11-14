from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base_page import BasePage

class SortablePage(BasePage):

    SORTABLE = (By.XPATH, "//span[text()='Sortable']")
    ITEMS = (By.CSS_SELECTOR, "#demo-tabpane-list div")

    def open_sortable(self):
        self.click(self.SORTABLE)

    def sort_items(self):
        items = self.driver.find_elements(*self.ITEMS)
        action = ActionChains(self.driver)

        for i in range(len(items) - 1):
            action.drag_and_drop(items[i+1], items[i]).perform()

