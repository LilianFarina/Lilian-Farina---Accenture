from utils.driver_factory import create_driver
from pages.home_page import HomePage
from pages.forms_page import FormsPage
from faker import Faker
import os

def test_forms():
    driver = create_driver()
    faker = Faker()

    driver.get("https://demoqa.com/")
    home = HomePage(driver)
    forms = FormsPage(driver)

    home.click_forms()
    forms.open_practice_form()

    upload_path = os.path.abspath("data/upload_example.txt")
    forms.fill_form(faker, upload_path)
    forms.submit()

    assert forms.popup_is_visible()

    forms.close_popup()
    driver.quit()

