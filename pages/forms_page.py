from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FormsPage(BasePage):

    PRACTICE_FORM = (By.XPATH, "//span[text()='Practice Form']")
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    PHONE = (By.ID, "userNumber")
    SUBJECT = (By.ID, "subjectsInput")
    UPLOAD = (By.ID, "uploadPicture")
    SUBMIT = (By.ID, "submit")
    POPUP = (By.ID, "example-modal-sizes-title-lg")
    CLOSE_POPUP = (By.ID, "closeLargeModal")

    def open_practice_form(self):
        self.click(self.PRACTICE_FORM)

    def fill_form(self, faker, upload_path):
        self.write(self.FIRST_NAME, faker.first_name())
        self.write(self.LAST_NAME, faker.last_name())
        self.write(self.EMAIL, faker.email())
        self.write(self.PHONE, "1199999999")

        self.write(self.SUBJECT, "Math")
        self.write(self.SUBJECT, "\n")

        self.driver.find_element(*self.UPLOAD).send_keys(upload_path)

    def submit(self):
        self.click(self.SUBMIT)

    def close_popup(self):
        self.click(self.CLOSE_POPUP)

    def popup_is_visible(self):
        return self.element_exists(self.POPUP)

