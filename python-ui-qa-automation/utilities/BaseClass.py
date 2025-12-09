import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions


@pytest.mark.usefixtures("setUp")
class BaseClass:

    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self, pixels=500):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def scroll_up(self, pixels=500):
        self.driver.execute_script(f"window.scrollBy(0, -{pixels});")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def waitForVisibilityOfElement(self, element, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.visibility_of(element))

    def waiForElementToBeClickable(self, element, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.element_to_be_clickable(element))

    def waitForPresenceOfElement(self,  locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.presence_of_element_located(locator))

    def waitForTitleContains(self,  title, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.title_contains(title))

    def waitForAlertIsPresent(self,  timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.alert_is_present())

    def waitForNewWindowIsOpened(self,  number_of_windows, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.new_window_is_opened(number_of_windows))