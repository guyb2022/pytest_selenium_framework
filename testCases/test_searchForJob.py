from pageObjects.LoginPage import LoginPage
from pageObjects.SearchForJob import SearchForJob
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string, time, random, pytest


class Test_003_searchForJob:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # @pytest.mark.skip(reason='Already tested, need to skipp for next test')
    @pytest.mark.sanity
    def test_searchForJobPage(self, setup):
        self.logger.info("*************** Test_003_searchForJob *******************")
        self.logger.info("***************** Verifying job searching Page*****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        # first we need to login
        self.lp = LoginPage(self.driver)
        time.sleep(7)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************** Login Soccess ******************")
        self.logger.info("**************** Going to Search For Job page Test ******************")
        time.sleep(7)
        # Now we need to go to the search for a job page
        self.sfj = SearchForJob(self.driver)
        self.sfj.gotoSearchForJobPage()
        time.sleep(7)
        act_title = self.driver.title

        if act_title == 'Careers':
            assert True
            self.logger.info("***************** Search For Job page PASSED *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_searchForJobPage.png")
            self.driver.close()
            self.logger.error("***************** Search For Job page FAILED *****************")
            assert False

    # @pytest.mark.skip(reason='Already tested, need to skipp for next test')
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_SearchJobRequest(self, setup):
        self.logger.info("***************** Verifying Search Job Request *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        # first we need to login
        self.lp = LoginPage(self.driver)
        time.sleep(7)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************** Login Soccess ******************")
        time.sleep(7)
        # Now we need to go to the search for a job page
        self.sfj = SearchForJob(self.driver)
        self.sfj.gotoSearchForJobPage()

        time.sleep(7)
        role = 'software developer'
        act_title = self.driver.title

        if act_title != 'Careers':
            self.driver.save_screenshot(".\\Screenshots\\test_SearchJobRequest.png")
            self.driver.close()
            self.logger.error("***************** Job Request Search FAILED *****************")
            assert False
        else:
            self.logger.info("***************** Search For Job page PASSED *****************")
            self.logger.info("***************** Continue to Search Job Request *****************")
            self.sfj.submitJobRequest(role)
            self.logger.info("***************** Job Request Search PASS *****************")
            self.driver.close()
            assert True

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_clickOnJobsLink(self, setup):
        self.logger.info("***************** Verifying Click on Jobs Link *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        # first we need to login
        self.lp = LoginPage(self.driver)
        time.sleep(7)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************** Login Soccess ******************")
        time.sleep(7)
        # Now we need to go to the search for a job page
        self.sfj = SearchForJob(self.driver)
        self.sfj.gotoSearchForJobPage()

        time.sleep(7)
        role = 'software developer'
        act_title = self.driver.title

        if act_title != 'Careers':
            self.driver.save_screenshot(".\\Screenshots\\test_SearchJobRequest.png")
            self.driver.close()
            self.logger.error("***************** Job Request Search FAILED *****************")
            assert False
        else:
            self.logger.info("***************** Search For Job page PASSED *****************")
            self.logger.info("***************** Continue to Search Job Request *****************")
            self.sfj.submitJobRequest(role)
            self.logger.info("***************** Job Request Search PASS *****************")
            self.logger.info("***************** Continue to Click on Jobs Link Test *****************")
            self.sfj.clickOnJobsLink()
            self.logger.info("***************** Click on Jobs Link Test PASS*****************")
            self.driver.close()
            assert True




