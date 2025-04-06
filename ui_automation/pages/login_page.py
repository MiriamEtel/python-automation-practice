# ui_automation/pages/login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def enter_username(self, username):
        self.driver.find_element(By.ID, "username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
