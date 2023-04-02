from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class SearchForJob:
    # Search for a job
    # selcting object and click with js if no other option is available
    # self.listitem = self.driver.find_element(By.ID, self.element_id)
    # self.driver.execute_script("argumant[0].click();", self.lisitem)
    button_search_job = '//button[@data-automation-id="navigationItem-Search for Jobs"]'
    textbox_search_for_job =  '//input[@type="text"]'
    button_search_for_job_xpath = '//button[@data-automation-id="keywordSearchButton"]'
    checkbox_location_xpath = '//button[@data-automation-id="distanceLocation"]'
    checkbox_full_part_time_xpath = '//button[@data-automation-id="employmentType"]'
    checkbox_category_xpath = '//button[@data-automation-id="jobFamilyGroup"]'
    input_location_xpath = '//input[@id="1e4a4eb3adf1013563ba9174bf817fcd"]'
    input_full_part_time_xpath = '//input[@id="dc193d6170de10860883d9bf7c0e01a9"]'
    input_category_xpath = '//input[@id="dc8bf79476611087d67bfec986b5704c"]'
    button_view_jobs_xpath = '//button[@data-automation-id="viewAllJobsButton"]'
    li_roles_list_xpath = '//li[@class="css-1q2dra3"]'
    href_role_link_xpath = '//a[@class="css-19uc56f"]'

    def __init__(self, driver):
        self.driver = driver

    def gotoSearchForJobPage(self):
        clickable = self.driver.find_element(By.XPATH, self.button_search_job)
        ActionChains(self.driver)\
            .move_to_element(clickable)\
            .click()\
            .perform()


    def submitJobRequest(self, position):
        self.driver.find_element(By.XPATH, self.textbox_search_for_job).send_keys(position)
        self.driver.find_element(By.XPATH, self.checkbox_location_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.input_location_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.checkbox_full_part_time_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.input_full_part_time_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.checkbox_category_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.input_category_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.button_search_for_job_xpath).click()
        time.sleep(3)

    def clickOnJobsLink(self):
        arr_list = self.driver.find_elements(By.XPATH, self.li_roles_list_xpath)
        print(f"--------------- numbers of elements: {len(arr_list)}")
        for element in arr_list:
            element.find_element(By.XPATH, self.href_role_link_xpath).click()
            time.sleep(3)