from pages.swag_labs import SwagLabs
from selenium.webdriver.common.by import By

def test_icon_exist(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.exist_icon()

def test_username_field_exists(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    username_field = browser.find_element(By.ID, "user-name")
    assert username_field is not None

def test_password_field_exists(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    password_field = browser.find_element(By.ID, "password")
    assert password_field is not None
