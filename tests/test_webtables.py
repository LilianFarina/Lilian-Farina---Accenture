from utils.driver_factory import create_driver
from pages.home_page import HomePage
from pages.webtables_page import WebTablesPage
from faker import Faker

def test_webtables():
    driver = create_driver()
    faker = Faker()

    driver.get("https://demoqa.com/")
    home = HomePage(driver)
    page = WebTablesPage(driver)

    home.click_elements()
    page.open_webtables()

    page.create_record(faker)
    page.edit_first_record()
    page.delete_first_record()

    driver.quit()

