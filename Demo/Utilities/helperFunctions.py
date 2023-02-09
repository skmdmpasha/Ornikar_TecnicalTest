from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import configReader
import logging
from Utilities.LogUtil import Logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

__TIMEOUT = 20
log = Logger(__name__, logging.INFO)

# lauch application


def launchBrowser(self, UIappurl):
    logo_xpath = configReader.readConfig("home page", "logo_xpath")
    self.driver_wait = WebDriverWait(self.driver, __TIMEOUT)
    self.driver.implicitly_wait(10)
    self.driver.get(UIappurl)
    handle_cookies(self, "Continuer sans accepter")
    self.driver_wait.until(
        EC.visibility_of_element_located((By.XPATH, logo_xpath)))
    print(self.driver.title)

    log.logger.info("Launching application url: " + str(UIappurl))

# function to deal cookies popup


def handle_cookies(self, eleText):
    cookie_xpath = configReader.readConfig("locators", "cookie_xpath")
    self.driver_wait = WebDriverWait(self.driver, __TIMEOUT)
    cookieElement = self.driver_wait.until(
        EC.visibility_of_element_located((By.XPATH, cookie_xpath)))
    self.driver_wait.until(EC.text_to_be_present_in_element(
        (By.XPATH, cookie_xpath), eleText))
    # self.driver.find_element(By.XPATH, cookie_xpath).click()
    cookieElement.click()

    log.logger.info("Clicking on the link: " + str(eleText))


def set_browser_options(browserName):
    if browserName == "chrome":
        options = webdriver.ChromeOptions()
    if browserName == "firefox":
        options = webdriver.FirefoxOptions()
    options.add_argument('--incognito')
    options.add_argument("start-maximized")
    options.add_argument("disable-popup-blocking")
    options.add_argument("disable-infobars")
    options.add_argument("--log-level=3")
    # options.add_argument("--disable-application-cache")
    # options.add_argument("--window-size=1366x768")
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--hide-scrollbars")
    # options.add_argument("--enable-logging")
    # options.add_argument("--single-process")
    # options.add_argument("--ignore-certificate-errors")
    # options.add_argument("--homedir=/tmp")
    # options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": True})
    # options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return options


# def waitForElement(self, _by, _locator, __TIMEOUT=20):
#     self.driver_wait = WebDriverWait(self.driver, __TIMEOUT)
#     if _by.endswith('XPATH'):
#         element = self.driver_wait.until(
#             EC.visibility_of_element_located((By.XPATH, _locator)))
#     if _by.endswith('ID'):
#         element = self.driver_wait.until(
#             EC.visibility_of_element_located((By.IDXPATH, _locator)))
#     if _by.endswith('CSS_SELECTOR'):
#         element = self.driver_wait.until(
#             EC.visibility_of_element_located((By.CSS_SELECTOR, _locator)))
#     return element


def waitForElement(self, _by, _locator, __TIMEOUT=20):
    """_by =  "id" or "xpath" or "link text" or "partial link text" or "name" 
         or "tag name" or "class name" or "css selector"""
    self.driver_wait = WebDriverWait(self.driver, __TIMEOUT)
    element = self.driver_wait.until(
        EC.visibility_of_element_located((_by, _locator)))
    return element

