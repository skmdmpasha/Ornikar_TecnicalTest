from features.pageobjects.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from assertpy import assert_that

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def is_signupLink_displayed(self):
        SignupLink= self.find_element_by_xpath("login page", "signupLink_XPATH")
        assert SignupLink.is_displayed() is True
        assert_that(SignupLink.text).contains('inscris')

    def click_signup_link(self):
        SignupLink=self.find_element_by_xpath("login page", "signupLink_XPATH")
        SignupLink.click()
    