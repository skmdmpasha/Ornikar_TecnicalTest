from features.pageobjects.BasePage import BasePage
from Utilities.helperFunctions import *
from assertpy import assert_that

#************************[ page locators object repository ]*********************
# checkboxes=configReader.readConfig("registration page", "checkbox_XPATH")
# ********************************************************************************

class RegistrationPage(BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)

    def verify_registration_page(self):
        firstname=self.FindWebElement("registration page", 'firstname_XPATH')
        assert firstname.is_displayed() is True

    def setFirstName(self,fname):
        self.SetText("registration page","firstname_XPATH",fname)

    def setLastName(self,lname):
        self.SetText("registration page","lastname_XPATH",lname)

    def setDay(self,day):
        self.SetText("registration page","day_XPATH",day)

    def setMonth(self,month):
        self.SetText("registration page","month_XPATH",month)

    def setYear(self,year):
        self.SetText("registration page","year_XPATH",year)

    def setzipcode(self,zipcode):
        self.SetText("registration page","zipcode_XPATH",zipcode)

    def setPhoneNumber(self,Phonenumber):
        self.SetText("registration page","phone_XPATH",Phonenumber)

    def setEmail(self,email):
        self.SetText("registration page","email_XPATH",email)

    def setPassword(self,password):
        self.SetText("registration page","password_XPATH",password)
    
    def check_WebCheckBox(self):
        webcheckboxs = self.FindWebElements("registration page","checkbox_XPATH")
        for index, cb in enumerate(webcheckboxs):
            if (not cb.is_selected() and index==1):
                scroll_to_View(self, cb)
                highlight(self,cb)
                cb.click()
                print()
    
    def submitForm(self):
        self.click("submit_XPATH")
