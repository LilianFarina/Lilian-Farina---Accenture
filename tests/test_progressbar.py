from utils.driver_factory import create_driver
from pages.home_page import HomePage
from pages.progressbar_page import ProgressBarPage

def test_progressbar():
    driver = create_driver()
    driver.get("https://demoqa.com/")

    home = HomePage(driver)
    page = ProgressBarPage(driver)

    home.click_widgets()
    page.open_progressbar()

    page.start()
    page.wait_until_25()
    page.reset()

    driver.quit()

