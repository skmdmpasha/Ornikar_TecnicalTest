@enroll, @UI
Feature: User Registration Feature
  "As a new user, I want to signup so that i can do login to my account so that I can takeup drving classes online"
  Scenario Outline: signup to create an login account
    Given I am on ornikar home page
    When I click connection link
    Then A login page with signup link is displayed
    When I click signup link
    Then A registration page is displayed
    Then I fill first name "<firstName>"
    Then I fill last name "<lastName>"
    Then I fill day "<day>"
    Then I fill month "<month>"
    Then I fill year "<year>"
    Then I fill zipcode "<zipcode>"
    Then I fill phone number "<Phonenumber>"
    Then I fill email "<email>"
    Then I fill password "<password>"
    Examples:
      | firstName | lastName | day | month | year | zipcode | Phonenumber | email           | password      |
      | Rahul     | SHETTY   | 12  | 12    | 2004 | 10600   | 9712345558  | Rahul@gmail.com | paswword@1234 |
