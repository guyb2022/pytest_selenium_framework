from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class LoginPage:
    textbox_username_xpath = "//input[@type='text']"
    textbox_password_xpath = "//input[@type='password']"
    button_sign_xpath = '//button[@data-automation-id="signInSubmitButton"]'
    button_signout_pre_xpath = '//button[@id="accountSettingsButton"]'
    button_signout_post_xpath = '//button[@id="item1"]'

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        # listitem = self.driver.find_element(By.XPATH, self.button_sign_xpath)
        # self.driver.execute_script("argumant[0].click();", listitem)
        clickable = self.driver.find_element(By.XPATH, self.button_sign_xpath)
        ActionChains(self.driver)\
            .move_to_element(clickable)\
            .click()\
            .perform()

    def clickLogout(self):
        clickable = self.driver.find_element(By.XPATH, self.button_signout_pre_xpath)
        ActionChains(self.driver)\
            .move_to_element(clickable)\
            .click()\
            .perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.button_signout_post_xpath).click()


