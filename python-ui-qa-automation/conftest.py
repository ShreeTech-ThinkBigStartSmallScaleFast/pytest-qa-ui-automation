import chromedriver_autoinstaller
import pytest
from selenium import webdriver
import pytest
import allure
from datetime import datetime
from utilities.logger import get_logger


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


log = get_logger()


@pytest.fixture(scope="function")
def webDriverSetUp(request):
    browser_name = request.config.getoption("browser_name")
    log.info("=== Starting test: Test ===")
    if browser_name == "chrome":
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--start-maximized")
        chromeOptions.add_argument("--headless=new")
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome(options=chromeOptions)

    elif browser_name == "firefox":
        firefoxOptions = webdriver.FirefoxOptions()
        firefoxOptions.add_argument("--start-maximized")
        firefoxOptions.add_argument("--headless")
        driver = webdriver.Firefox(options=firefoxOptions)

    elif browser_name == "edge":
        edgeOptions = webdriver.EdgeOptions()
        edgeOptions.add_argument("--start-maximized")
        edgeOptions.add_argument("--headless")
        driver = webdriver.Edge(options=edgeOptions)

    else:
        raise Exception("Invalid browser name provided!")

    driver.maximize_window()
    yield driver
    log.info("=== Completed test: Login Test ===")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture screenshot only when test fails
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("webDriverSetUp")  # your fixture name

        if driver:
            screenshot_name = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
            screenshot_path = f"./allure-results/{screenshot_name}"
            driver.save_screenshot(screenshot_path)

            # Attach screenshot to Allure report
            with open(screenshot_path, "rb") as f:
                allure.attach(
                    f.read(),
                    name=screenshot_name,
                    attachment_type=allure.attachment_type.PNG
                )
