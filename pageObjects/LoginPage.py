from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class LoginPage:
    textbox_username_xpath = "//input[@data-automation-id='email']"
    textbox_password_xpath = "//input[@type='password']"
    button_signin_xpath = "//button[@class='css-1mkyvo7']"
    button_searc_job = '//button[@data-automation-id="navigationItem-Search for Jobs"]'
    button_sign_xpath = '//button[@data-automation-id="signInSubmitButton"]'
    button_signout_id = 'sign_out_link'

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def sighin(self):
        self.driver.find_element(By.XPATH, self.button_signin_xpath).click()

    def clickLogin(self):
        clickable = self.driver.find_element(By.XPATH, self.button_sign_xpath)
        ActionChains(self.driver)\
            .move_to_element(clickable)\
            .pause(1)\
            .click_and_hold()\
            .pause(1)\
            .perform()

    def clickLogout(self):
        self.driver.find_element(By.ID, self.button_signout_id).click()


