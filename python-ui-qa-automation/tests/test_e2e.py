import json

import pytest

from conftest import webDriverSetUp
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.logger import get_logger

# Load test data
with open("test_data/test_data.json") as f:
    data = json.load(f)["data"]
    username = data[0]
    password = data[1]

log = get_logger()

def test_launch_signIn_automationPractice_application(webDriverSetUp):
    driver = webDriverSetUp
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login = LoginPage(driver)
    login.enter_username_and_password(username, password)
    login.select_user_type("User")
    login.select_user_category("Teacher")
    login.check_terms_condition()
    login.click_on_signIn_button()


def test_launch_automationPractice_application(webDriverSetUp):
    driver = webDriverSetUp
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    homepage = HomePage(driver)
    homepage.radioButtonExample()
    homepage.autoSuggestDropdownExample()
    homepage.dropDownExample()
    homepage.checkBoxExample()
    homepage.switchToNewWindowExample()
    homepage.switchToNewTabExample()
    homepage.switchToAlertExample()
    homepage.hideAndShowExample()
    homepage.iFrameExample()
    homepage.mouseHoverExample()
