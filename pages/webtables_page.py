from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class WebTablesPage(BasePage):

    WEB_TABLES = (By.XPATH, "//span[text()='Web Tables']")
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    AGE = (By.ID, "age")
    SALARY = (By.ID, "salary")
    DEPT = (By.ID, "department")
    SUBMIT = (By.ID, "submit")
    EDIT_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")

    def open_webtables(self):
        self.click(self.WEB_TABLES)

    def create_record(self, faker):
        self.click(self.ADD_BUTTON)
        self.write(self.FIRST_NAME, faker.first_name())
        self.write(self.LAST_NAME, faker.last_name())
        self.write(self.EMAIL, faker.email())
        self.write(self.AGE, "30")
        self.write(self.SALARY, "5000")
        self.write(self.DEPT, "QA")
        self.click(self.SUBMIT)

    def edit_first_record(self):
        self.click(self.EDIT_BUTTON)
        self.write(self.DEPARTMENT, "Automation")
        self.click(self.SUBMIT)

    def delete_first_record(self):
        self.click(self.DELETE_BUTTON)

