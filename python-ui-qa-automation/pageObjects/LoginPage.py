from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.userName = (By.ID, "username")
        self.password = (By.ID, "password")
        self.user = (By.CLASS_NAME, "checkmark")
        self.admin_user = (By.ID, "admin")
        self.user_category = (By.XPATH, "//*[@id='login-form']/div[5]/select")
        self.terms_condition = (By.ID, "terms")
        self.loginButton = (By.ID, "signInBtn")

    def enter_username_and_password(self, username, password):
        self.driver.find_element(*self.userName).clear()
        self.driver.find_element(*self.userName).send_keys(username)
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(password)

    def check_terms_condition(self):
        self.driver.find_element(*self.terms_condition).click()

    def click_on_signIn_button(self):
        self.driver.find_element(*self.loginButton).click()

    def get_page_title(self):
        return self.driver.find_element(*self.loginButton).text

    def select_user_type(self, user_type):
        if user_type == "User":
            self.driver.find_element(*self.user).click()
        elif user_type == "Admin":
            self.driver.find_element(*self.admin_user).click()
        else:
            raise Exception("Invalid user type")

    def select_user_category(self, user_category):
        dropdown_values = Select(self.driver.find_element(*self.user_category))
        if user_category == "Student":
            dropdown_values.select_by_value("stud")
        elif user_category == "Teacher":
            dropdown_values.select_by_value("teach")
        elif user_category == "Consultant":
            dropdown_values.select_by_value("consult")
        else:
            raise Exception("Invalid user category")
