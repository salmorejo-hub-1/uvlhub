# Generated by Selenium IDE
from selenium.webdriver.common.by import By

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver


class TestSignup():
    def setup_method(self, method):
        self.driver = initialize_driver()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_signup(self):
        
        self.driver.get(get_host_for_selenium_testing())
        self.driver.find_element(By.XPATH, "//a[span[text()='Sign Up']]").click()
        self.driver.find_element(By.ID, "email").send_keys("user1@example.com")
        self.driver.find_element(By.ID, "password").send_keys("1234")
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("Hola")
        self.driver.find_element(By.ID, "surname").send_keys("Juan")
        self.driver.find_element(By.ID, "email").send_keys("holajuan@example.com")
        self.driver.find_element(By.ID, "password").send_keys("holajuan")
        self.driver.find_element(By.ID, "submit").click()
