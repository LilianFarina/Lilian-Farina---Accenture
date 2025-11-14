from utils.driver_factory import create_driver
from pages.home_page import HomePage
from pages.sortable_page import SortablePage

def test_sortable():
    driver = create_driver()
    driver.get("https://demoqa.com/")

    home = HomePage(driver)
    page = SortablePage(driver)

    home.click_interactions()
    page.open_sortable()
    page.sort_items()

    driver.quit()

