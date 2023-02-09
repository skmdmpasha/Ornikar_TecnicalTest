from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import logging
from Utilities.LogUtil import Logger
from Utilities import configReader

log = Logger(__name__, logging.INFO)


class BasePage:

    __TIMEOUT = 20

    def __init__(self, driver):
        self.driver_wait = WebDriverWait(driver, BasePage.__TIMEOUT)
        self.driver = driver
 
    def launchBrowser(self,url):
        self.driver.get(url)


    def find_element_by_xpath(self, locatorPage, locator):
        locator_xpath= configReader.readConfig(locatorPage, locator)
        self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, locator_xpath)))
        return self.driver.find_element(By.XPATH, locator_xpath)

    def type(self, locatorPage, locator, textvalue):
        by_locator = configReader.readConfig(locatorPage, locator)
        
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, by_locator).send_keys("")
            self.driver.find_element(By.XPATH, by_locator).send_keys(textvalue)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, by_locator).send_keys("")
            self.driver.find_element(By.CSS_SELECTOR, by_locator).send_keys(textvalue)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, by_locator).send_keys("")
            self.driver.find_element(By.ID, by_locator).send_keys(textvalue)

        log.logger.info("Typing in an element: " + str(locator) + " value entered as : " + str(textvalue))       

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).click()
        
        log.logger.info("Clicking on an element: " + str(locator))

    # def type(self, locator, value):
    #     if str(locator).endswith("_XPATH"):
    #         self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).send_keys(value)
    #     elif str(locator).endswith("_CSS"):
    #         self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).send_keys(value)
    #     elif str(locator).endswith("_ID"):
    #         self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).send_keys(value)

    #     log.logger.info("Typing in an element: " + str(locator) + " value entered as : " + str(value))

    # def select(self, locator, value):
    #     global dropdown
    #     if str(locator).endswith("_XPATH"):
    #         dropdown = self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator))
    #     elif str(locator).endswith("_CSS"):
    #         dropdown = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator))
    #     elif str(locator).endswith("_ID"):
    #         dropdown = self.driver.find_element(By.ID, configReader.readConfig("locators", locator))

    #     select = Select(dropdown)
    #     select.select_by_visible_text(value)

    #     log.logger.info("Selecting from an element: " + str(locator) + " value selected as : " + str(value))

    # def moveTo(self, locator):
    #     #added comments
    #     if str(locator).endswith("_XPATH"):
    #         element = self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator))
    #     elif str(locator).endswith("_CSS"):
    #         element = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator))
    #     elif str(locator).endswith("_ID"):
    #         element = self.driver.find_element(By.ID, configReader.readConfig("locators", locator))

    #     action = ActionChains(self.driver)
    #     action.move_to_element(element).perform()

    #     log.logger.info("Moving to an element: " + str(locator))
