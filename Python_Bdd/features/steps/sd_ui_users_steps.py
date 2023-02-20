from behave import *
from features.pageobjects.RegistrationPage import RegistrationPage
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.HomePage import HomePage


#  begin of home page
@given('I am on ornikar home page')
def step_impl(context):
    context.homePage = HomePage(context.driver)
    context.homePage.VerifyPageTitle("Ornikar")

@when('I click connection link')
def step_impl(context):
    context.homePage.ClickConnection()
#  end login page

#  begin of login page
@Then('A login page with signup link is displayed')
def step_impl(context):
    context.login = LoginPage(context.driver)
    context.login.is_signupLink_displayed()

@when('I click signup link')
def step_impl(context):
    context.login.click_signup_link()
#  end of login page

# Begin of registration page
@Then('A registration page is displayed')
def step_impl(context):
    context.reg = RegistrationPage(context.driver)
    context.reg.verify_registration_page()

@Then('I fill {field_name} "{field_value}"')
def fill_form_field(context, field_name, field_value):
    match field_name:
        case "first name":
            context.reg.setFirstName(field_value)
        case "last name":
            context.reg.setLastName(field_value)
        case "day":
            context.reg.setDay(field_value)
        case "month":
            context.reg.setMonth(field_value)
        case "year":
            context.reg.setYear(field_value)
        case "zipcode":
            context.reg.setzipcode(field_value)
        case "phone number":
            context.reg.setPhoneNumber(field_value)
        case "email":
            context.reg.setEmail(field_value)
        case "password":
            context.reg.setPassword(field_value)

@Then('I accept general condition')
def accept_cgu(context):
    context.reg.check_WebCheckBox()
    print()

@Then('I click on the submit button')
def submit_Form(context):
    # context.reg.submitForm()
    pass
    print()
# End of registration page