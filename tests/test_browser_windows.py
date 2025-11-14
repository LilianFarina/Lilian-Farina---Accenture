from utils.driver_factory import create_driver
from pages.home_page import HomePage
from pages.browser_windows_page import BrowserWindowsPage

def test_browser_windows():
    driver = create_driver()
    driver.get("https://demoqa.com/")

    home = HomePage(driver)
    page = BrowserWindowsPage(driver)

    home.click_alerts()
    page.open_menu()
    page.open_new_window()

    assert page.validate_new_window()
    page.close_new_window()

    driver.quit()

