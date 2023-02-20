@enroll, @UI
Feature: User Registration Feature
  "As a new user, I want to signup so that i can do login to my account and can takeup driving classes online"
  Scenario Outline: signup to create an login account
    Given I am on ornikar home page
    When I click connection link
    Then A login page with signup link is displayed
    When I click signup link
    Then A registration page is displayed
    And I fill first name "<firstName>"
    And I fill last name "<lastName>"
    And I fill day "<day>"
    And I fill month "<month>"
    And I fill year "<year>"
    And I fill zipcode "<zipcode>"
    And I fill phone number "<Phonenumber>"
    And I fill email "<email>"
    And I fill password "<password>"
    And I accept general condition
    And I click on the submit button
    Examples:
      | firstName | lastName | day | month | year | zipcode | Phonenumber | email           | password      |
      | Rahul     | SHETTY   | 12  | 12    | 2004 | 10600   | 0604477478  | Rahul@gmail.com | Paswword@1234 |
