from pageObjects.LoginPage import LoginPage
import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("***************** Test_001_Login *****************")
        self.logger.info("***************** Verifying Home Page Title *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(5)
        act_title = self.driver.title

        if act_title == 'Workday':
            assert True
            self.driver.close()
            self.logger.info("***************** Home Page Title PASSED *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            self.logger.error("***************** Home Page Title FAILED *****************")
            assert False

    def test_login(self, setup):

        self.logger.info("***************** Verifying Login test*****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        time.sleep(7)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************ login Success **********************")
        time.sleep(5)
        act_title = self.driver.title

        if act_title == 'Candidate Home':
            assert True
            self.lp.clickLogout()
            self.driver.close()
            self.logger.info("***************** Loging test PASSED *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            self.driver.close()
            self.logger.error("***************** Loging test Failed *****************")
            assert False











