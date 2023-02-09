import time
from behave import *
from features.pageobjects.RegistrationPage import RegistrationPage
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.HomePage import HomePage
from features.pageobjects.BasePage import BasePage

# begin of home page
@given('I am on ornikar home page')
def step_impl(context):
    context.homePage = HomePage(context.driver)
    context.homePage.verify_title()

@when('I click connection link')
def step_impl(context):
    context.homePage.click_Connection()
# end login page

# begin of login page
@Then('A login page with signup link is displayed')
def step_impl(context):
    context.login = LoginPage(context.driver)
    context.login.is_signupLink_displayed()

@when('I click signup link')
def step_impl(context):
    context.login.click_signup_link()
# end of login page

# begin of registration page
@Then('A registration page is displayed')
def step_impl(context):
    context.reg = RegistrationPage(context.driver)
    context.reg.verify_registration_page()

@Then('I fill first name "{firstName}"')
def step_impl(context, firstName):
    context.reg.setFirstName(firstName)

@Then('I fill last name "{lastName}"')
def step_impl(context, lastName):
    context.reg.setLastName(lastName)

@Then('I fill day "{day}"')
def step_impl(context, day):
    context.reg.setDay(day)

@Then('I fill month "{month}"')
def step_impl(context, month):
    context.reg.setMonth(month)

@Then('I fill year "{year}"')
def step_impl(context, year):
    context.reg.setYear(year)

@Then('I fill zipcode "{zipcode}"')
def step_impl(context, zipcode):
    context.reg.setzipcode(zipcode)

@Then('I fill phone number "{Phonenumber}"')
def step_impl(context, Phonenumber):
    context.reg.setPhoneNumber(Phonenumber)

@Then('I fill email "{email}"')
def step_impl(context, email):
    context.reg.setEmail(email)

@Then(u'I fill password "{password}"')
def step_impl(context, password):
    context.reg.setPassword(password)

@Then('I click on the submit button')
def step_impl(context):
    context.reg.submitForm()
    assert True
    time.sleep(3)
# end of registration page