from Utilities import configReader, helperFunctions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import os
import time
import logging
from Utilities.LogUtil import Logger
log = Logger(__name__, logging.INFO)
__TIMEOUT = 20

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
    if browserName == "edge":
        options = webdriver.EdgeOptions()
    if browserName == "ie":
        options = webdriver.IeOptions()
    if browserName == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        options.add_argument("start-maximized")
        options.add_argument('--disable-extensions')
        # options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": True})
        # options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
    if browserName == "firefox":
        options = webdriver.FirefoxOptions()

        # profile = webdriver.FirefoxProfile()
        # profile.set_preference("network.cookie.cookieBehavior", 2)  # block all third-party cookies
        # profile.set_preference("network.cookie.cookieBehavior", 4)  # block all cookies
        # profile.set_preference("network.cookie.cookieBehavior", 1)  # accept cookies from the same site
        # options.set_preference("browser.startup.homepage", "https://www.google.com")
        # options.profile = profile
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference("browser.privatebrowsing.autostart", True)
        # profile.set_preference("network.cookie.cookieBehavior", 4) # block all cookies
        # context.driver = webdriver.Firefox(service=Service(
        #     GeckoDriverManager().install()), options=options, firefox_profile=profile)
        
        # Get the path to the Firefox binary using the 'which' command
        firefox_binary_path = os.popen('which firefox').read().strip()
        options.binary_location = firefox_binary_path

        
        # options.binary_location = "C:\\Users\\ACER\\AppData\\Local\\Mozilla Firefox\\Firefox.exe"
        options.headless = False
        options.set_preference("browser.privatebrowsing.autostart", True)
        # options.set_preference("dom.webnotifications.enabled", False)
        # options.set_preference("network.cookie.cookieBehavior", 4)
    # options.add_argument("disable-infobars")
    # options.add_argument("disable-popup-blocking")
    # options.add_argument("--log-level=3")
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


def WaitForWebElement(self, _by, _locator, __TIMEOUT=20):
    """_by can be an  "id" or "xpath" or "link text" or "partial link text" or "name" 
         or "tag name" or "class name" or "css selector"""
    self.driver_wait = WebDriverWait(self.driver, __TIMEOUT)
    element = self.driver_wait.until(
        EC.visibility_of_element_located((_by, _locator)))
    return element


# _To highlight an web element
def highlight(self, element):
    """Highlights (blinks) a Selenium Webdriver element"""
    try:
        self.driver = element._parent
        self.driver.implicitly_wait(20)

        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

        original_style = element.get_attribute('style')
        apply_style("background: yellow;  border: 3px solid Red;")

        time.sleep(.3)
        apply_style(original_style)
    except:
        pass


# _Run JavaScript to scroll until the element is in view
def scroll_to_View(self, element):
    """scroll into view of Webdriver element"""
    try:
        self.driver = element._parent
        """scroll until the desired element is in view using JavaScript"""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    except:
        pass
