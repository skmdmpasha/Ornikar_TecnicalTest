from features.pageobjects.BasePage import BasePage
from assertpy import assert_that

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def is_signupLink_displayed(self):
        signupLink= self.FindWebElement("login page", "signupLink_XPATH")
        assert_that(signupLink.text).contains('inscris')

    def click_signup_link(self):
        signupLink=self.FindWebElement("login page", "signupLink_XPATH")
        signupLink.click()
    