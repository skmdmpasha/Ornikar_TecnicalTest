# from Utilities import configReader
from Utilities import configReader, helperFunctions
import logging
from Utilities.LogUtil import Logger
from features.pageobjects.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from assertpy import assert_that

log = Logger(__name__, logging.INFO)

#************************[ page locators object repository ]*********************
signUpLink=configReader.readConfig("login page", "signupLink_XPATH")
connection=configReader.readConfig("home page", "connection_XPATH")
# ********************************************************************************

class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver_wait = WebDriverWait(driver, 10)
        self.driver=driver

    # click Connection link of home page
    def click_Connection(self):
        # SignUpLink=configReader.readConfig("login page", "signupLink_XPATH")
        # webLink = self.find_element_by_xpath("home page", "connection_XPATH")

        # -- OR --

        webLink = self.driver.find_element(By.XPATH, connection)
        webLink.click()

        # self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, SignUpLink))) # wait signup link in login page
        helperFunctions.waitForElement(self, 'xpath', signUpLink)
        log.logger.info("click Connection of home page: " + str(webLink.text))
        

    def verify_title(self):
        self.driver_wait.until(EC.title_contains("Ornikar"))
        assert_that(self.driver.title).contains('Ornikar')
        log.logger.info("verify we are in home page: " + str(self.driver.title))