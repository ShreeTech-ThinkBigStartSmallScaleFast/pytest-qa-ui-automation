import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import get_logger


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.log = get_logger()
        self.autocomplete = self.driver.find_element(By.ID, "autocomplete")

    def radioButtonExample(self):
        self.log.info("Clicking on radio button example")
        radios = self.driver.find_elements(By.XPATH, "//input[@type='radio']")
        radios[2].click()

    def autoSuggestDropdownExample(self):
        self.log.info("Clicking on autoSuggestDropdown example")
        self.autocomplete.send_keys("Ind")
        wait = WebDriverWait(self.driver, 10)
        suggestions = wait.until(EC.visibility_of_all_elements_located(
            (By.XPATH, "//li[@class='ui-menu-item']/div[@class='ui-menu-item-wrapper']")))

        print("Found suggestions:", [s.text for s in suggestions])

        # Iterate and select India
        for i in range(len(suggestions)):  # re-fetch inside loop to avoid stale exception
            opt = self.driver.find_elements(By.XPATH, "//*[@id='ui-id-1']/li")[i]

            if "India" == opt.text:
                wait.until(EC.element_to_be_clickable(opt)).click()
                return

        raise Exception("India' not found in autosuggest suggestions")

    def dropDownExample(self):
        self.log.info("Clicking on dropDown example")
        dropdownList = Select(self.driver.find_element(By.ID, "dropdown-class-example"))
        dropdownList.select_by_visible_text("Option1")

    def checkBoxExample(self):
        self.log.info("Clicking on checkBox example")
        checkboxList = self.driver.find_elements(By.XPATH, "//*[@type='checkbox']")
        for checkbox in checkboxList:
            checkbox.click()
            time.sleep(1)

    def switchToNewWindowExample(self):
        self.log.info("Clicking on switchToNewWindow example")
        self.driver.find_element(By.XPATH, "//*[@id='openwindow']").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(self.driver.current_url)
        self.driver.switch_to.window(self.driver.window_handles[0])

    def switchToNewTabExample(self):
        self.log.info("Clicking on switchToNewTab example")
        self.driver.find_element(By.ID, "opentab").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(self.driver.current_url)
        title = self.driver.title
        print("Title:", title)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(1)

    def switchToAlertExample(self):
        self.log.info("Clicking on switchToAlert example")
        nameTextbox = self.driver.find_element(By.ID, "name")
        nameTextbox.send_keys("TestUser")
        self.driver.find_element(By.ID, "confirmbtn").click()
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.ID, "alertbtn").click()
        alertText = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return alertText

    def hideAndShowExample(self):
        self.log.info("Clicking on hideAndShow example")
        self.driver.find_element(By.ID, "hide-textbox").click()
        textbox = self.driver.find_element(By.ID, "displayed-text")

        # Verify textbox is NOT displayed
        is_hidden = not textbox.is_displayed()
        print("Textbox hidden:", is_hidden)

        # Verify textbox is displayed
        self.driver.find_element(By.ID, "show-textbox").click()
        textbox.is_displayed()
        return textbox

    def webTableExample(self):
        self.log.info("Clicking on webTable example")
        self.driver.find_element(By.XPATH, "//*[@id='product']/thead/tr/th[4]")
        amount = self.driver.find_elements(By.XPATH, "//*[@id='product]/tbody/tr[2]/td[3]")

    def  iFrameExample(self):
        self.log.info("Clicking on iFrame example")
        iframe = self.driver.find_element(By.XPATH, "//*[@id='courses-iframe']")
        self.driver.switch_to.frame(iframe)
        all_access_link = self.driver.find_element(By.XPATH, "//*[@href='/all-access-subscription']")
        if all_access_link.is_displayed():
            print("All Access Link found")
        self.driver.switch_to.default_content()

    def mouseHoverExample(self):
        self.log.info("Clicking on mouseHover example")
        mouseoverElement = self.driver.find_element(By.ID, "mousehover")
        actions = ActionChains(self.driver)
        actions.move_to_element(mouseoverElement).perform()

        moveUp = self.driver.find_element(By.XPATH, "//*[@href='#top']")
        actions.move_to_element(moveUp).click().perform()
        time.sleep(1)

