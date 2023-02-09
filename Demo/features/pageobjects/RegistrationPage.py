from features.pageobjects.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from assertpy import assert_that


class RegistrationPage(BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)

    def verify_registration_page(self):
        firstname=self.find_element_by_xpath("registration page", 'firstname_XPATH')
        assert firstname.is_displayed() is True

    def setFirstName(self,fname):
        self.type("registration page","firstname_XPATH",fname)

    def setLastName(self,lname):
        self.type("registration page","lastname_XPATH",lname)

    def setDay(self,day):
        self.type("registration page","day_XPATH",day)

    def setMonth(self,month):
        self.type("registration page","month_XPATH",month)

    def setYear(self,year):
        self.type("registration page","year_XPATH",year)

    def setzipcode(self,zipcode):
        self.type("registration page","zipcode_XPATH",zipcode)

    def setPhoneNumber(self,Phonenumber):
        self.type("registration page","phone_XPATH",Phonenumber)

    def setEmail(self,email):
        self.type("registration page","email_XPATH",email)

    def setPassword(self,password):
        self.type("registration page","password_XPATH",password)

    def submitForm(self):
        self.click("submit_XPATH")
