Feature: API to fetch Users Information
  Background: Setup environment
    Given I set base URL to "https://dummy.restapiexample.com"
    And I add path "api/v1" to base URL

    @retrieve
    Scenario: Test scenario to get list of employees
      Then I make a "GET" request to "employees"
      Then the response status code should equal "200"
      And the response status message should equal "OK"
      And the response header "Content-Type" should equal "application/json"
      Then JSON at path "data[1].employee_name" should equal "Garrett Winters"
    # And the response structure should equal "usersData"


  @retrive_byId
  Scenario Outline: Test scenario to Search employee by using employee id
    When I send a "GET" request to "<RETRIVE>" employee
    Then the response header "Content-Type" should equal "application/json"
    And the response status code should equal "200"
    Examples:
      | RETRIVE     |
      | employee/12 |
      | employee/8  |


  @create
  Scenario: Test scenario to create employee record
    When I send a "POST" request to "create" employee
      """
      the response status code should be among "200, 201
      """
      | employee_name | employee_salary | employee_age |
      | Manish        | 2345            | 26           |
      | Xavier        | 4444            | 55           |
      | Tomas         | 7777            | 66           |


  @update
  Scenario: Test scenario to update employee record
    When I send a "PUT" request to "update/@ID" employee
      """
      the response status code should be among "200, 201
      """
      | employee_name | employee_salary | employee_age | @ID |
      | Manish        | 2345            | 36           | 2   |
      | Xavier        | 5555            | 65           | 6   |
      | Tomas         | 8888            | 76           | 4   |
  

  @update_byId
  Scenario Outline: Test scenario to update employee record
    When I send a "PUT" request to "<UPDATE>" employee
      | employee_name | employee_salary | employee_age |
      | Manish        | 2345            | 36           |
      | Xavier        | 5555            | 65           |
      | Tomas         | 8888            | 76           |
    Then the response status code should be among "200, 201"
    Examples:
      | UPDATE   |
      | update/2 |
      | update/6 |
      | update/4 |


@delete
Scenario Outline: Test scenario to delete single employee by id
  When I send a "DELETE" request to "<DELETE>" employee
  Then the response status code should equal "200"
  Examples:
    | DELETE    |
    | delete/9  |
    | delete/24 |


@json_path
Scenario Outline: Test scenario to verify employees data by providing json path
  When I send a "GET" request to "<endpoint>" employee
  Then JSON at path "<id_path>" should equal "<id_value>"
  And JSON at path "<name_path>" should equal "<name_value>"
  Then I want to print it
  Examples:
    | endpoint   | id_path | id_value | name_path          | name_value      |
    | employee/2 | data.id | 2        | data.employee_name | Garrett Winters |
