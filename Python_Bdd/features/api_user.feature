Feature: API to fetch Users Information
  Background: Setup environment
    Given I set base URL to "https://dummy.restapiexample.com"
    And I add path "api/v1" to base URL

  Scenario Outline: Test scenario to Search employee by using employee id
    When I send a "GET" request to "employee" by <ID>
    Then the response status code should equal "200"
    Examples:
      | ID |
      | 12 |
      | 8  |


Scenario: Test scenario to get list of employees
  Then I make a "GET" request to "employees"
  Then the response status code should equal "200"
  And the response status message should equal "OK"
  And the response header "Content-Type" should equal "application/json"
  Then JSON at path "data[1].employee_name" should equal "Garrett Winters"
# Then the response status code should equal 200
# And the response header "Content-Type" should equal "application/json"
# And the response structure should equal "usersData"

Scenario: Test scenario to create employee record
  When I send a "POST" request to "create" employee
    | employee_name | employee_salary | employee_age |
    | Manish        | 2345            | 26           |
    | Xavier        | 4444            | 55           |
    | Tomas         | 7777            | 66           |
  And the response status code should be among "200, 201"


Scenario: Test scenario to update employee record
  When I send a "PUT" request to "update/@ID" employee
    | employee_name | employee_salary | employee_age | @ID |
    | Manish        | 2345            | 26           | 2   |
    | Xavier        | 4444            | 55           | 6   |
    | Tomas         | 7777            | 66           | 4   |
  And the response status code should be among "200, 201"
  And the response status message should equal "OK"


@json_path
Scenario: Test scenario to verify employees data by providing json path
  When I make a "GET" request to "employee/2"
  Then JSON at path "data.id" should equal "2"
  Then JSON at path "data.employee_name" should equal "Garrett Winters"
  Then I want to print it


Scenario: Test scenario to update employee record
  When I send a "PUT" request to "update/@ID" employee
    | employee_name | employee_salary | employee_age | @ID |
    | Manish        | 2345            | 26           | 2   |
    | Xavier        | 4444            | 55           | 6   |
    | Tomas         | 7777            | 66           | 4   |
  Then the response status code should equal "200"