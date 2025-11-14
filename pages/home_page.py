from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    FORMS = (By.XPATH, "//h5[text()='Forms']")
    ALERTS = (By.XPATH, "//h5[text()='Alerts, Frame & Windows']")
    ELEMENTS = (By.XPATH, "//h5[text()='Elements']")
    WIDGETS = (By.XPATH, "//h5[text()='Widgets']")
    INTERACTIONS = (By.XPATH, "//h5[text()='Interactions']")

    def click_forms(self):
        self.click(self.FORMS)

    def click_alerts(self):
        self.click(self.ALERTS)

    def click_elements(self):
        self.click(self.ELEMENTS)

    def click_widgets(self):
        self.click(self.WIDGETS)

    def click_interactions(self):
        self.click(self.INTERACTIONS)

