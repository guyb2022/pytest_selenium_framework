from pageObjects.LoginPage import LoginPage
import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import pytest


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("***************** Test_002_DDT_Login *****************")
        self.logger.info("***************** Verifying Login DDT test *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')

        lst_status = []
        time.sleep(5)

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            time.sleep(3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            act_title = self.driver.title
            exp_title1 = 'Candidate Home'

            if act_title == exp_title1:
                if self.exp == "Pass":
                    self.logger.info("**********1. PASS *********")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info(" **********2. FAIL *********")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            else:
                if self.exp == "Pass":
                    self.logger.info("**********3. FAIL *********")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("**********4. PASS *********")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT test PASSED ****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT test FAILED ****")
            self.driver.close()
            assert False

        self.logger.info("******** End of Test_002_DDT_Login *********")
        self.logger.info("***************** Completed Test_002_DDT_Login *****************")













