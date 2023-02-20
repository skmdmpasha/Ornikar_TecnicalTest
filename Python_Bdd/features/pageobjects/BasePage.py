from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.helperFunctions import *
from Utilities import configReader

import logging
from Utilities.LogUtil import Logger
log = Logger(__name__, logging.INFO)


class BasePage:

    __TIMEOUT = 20

    def __init__(self, driver):
        self.driver_wait = WebDriverWait(driver, BasePage.__TIMEOUT)
        self.driver = driver
 
    def launchBrowser(self,url):
        self.driver.get(url)

    def FindWebElements(self, locatorPage, locator):
        locator_path= configReader.readConfig(locatorPage, locator)
        if str(locator).endswith("_XPATH"):
            return self.driver.find_elements(By.XPATH, locator_path)

    def FindWebElement(self, locatorPage, locator):
        locator_path= configReader.readConfig(locatorPage, locator)
        if str(locator).endswith("_XPATH"): 
            self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, locator_path)))
            e=self.driver.find_element(By.XPATH, locator_path)
            scroll_to_View(self, e)
            highlight(self,e)
            return e
        if str(locator).endswith("_CSS"): 
            self.driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator_path)))
            e=self.driver.find_element(By.CSS_SELECTOR, locator_path)
            scroll_to_View(self, e)
            highlight(self,e)
            return e
        if str(locator).endswith("_ID"): 
            self.driver_wait.until(EC.visibility_of_element_located((By.ID, locator_path)))
            e=self.driver.find_element(By.ID, locator_path)
            scroll_to_View(self, e)
            highlight(self,e)
            return e

    def SetText(self, locatorPage, locator, textvalue):
        by_locator = configReader.readConfig(locatorPage, locator)        
        if str(locator).endswith("_XPATH"):
            e=self.driver.find_element(By.XPATH, by_locator)
            scroll_to_View(self, e)
            highlight(self,e)
            e.send_keys("")
            e.send_keys(textvalue)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, by_locator).send_keys("")
            self.driver.find_element(By.CSS_SELECTOR, by_locator).send_keys(textvalue)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, by_locator).send_keys("")
            self.driver.find_element(By.ID, by_locator).send_keys(textvalue)

        log.logger.info("Typing in an element: " + str(locator) + " value entered as : " + str(textvalue))       

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            e=self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator))
            scroll_to_View(self, e)
            highlight(self,e)
            e.click()
        elif str(locator).endswith("_CSS"):
            e=self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator))
            scroll_to_View(self, e)
            highlight(self,e)
            e.click()           
        elif str(locator).endswith("_ID"):
            e=self.driver.find_element(By.ID, configReader.readConfig("locators", locator))
            scroll_to_View(self, e)
            highlight(self,e)
            e.click()         
        log.logger.info("Clicking on an element: " + str(locator))
