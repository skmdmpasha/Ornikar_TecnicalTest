from Utilities import configReader, helperFunctions
from features.pageobjects.BasePage import BasePage
from assertpy import assert_that

import logging
from Utilities.LogUtil import Logger
log = Logger(__name__, logging.INFO)

# ************************[ page locators object repository ]*********************
signUpLink = configReader.readConfig("login page", "signupLink_XPATH")
# ********************************************************************************

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # click 'Connection' link of home page
    def ClickConnection(self):
        webLink = self.FindWebElement("home page", "connection_XPATH")
        webLink.click()
        # wait for 'signup' link of login page
        helperFunctions.WaitForWebElement(self, 'xpath', signUpLink)

        log.logger.info("click Connection of home page: " + str(webLink.text))

    def VerifyPageTitle(self, titletext):
        assert_that(self.driver.title).contains(titletext)

        log.logger.info(
            f"Verifying we are in {str(self.driver.title)} home page")
