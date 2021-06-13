Feature: Login to OrangeHRM

#  Scenario Outline: Login with Correct details
#    Given Orange HRM Login Page opened
#    When User Logins with <Username> and <Password>
#    Then Orange HRM home page should be opened

 #   Examples: Correct Data
 #     | Username | Password |
 #     | Admin    | admin123 |


 # Scenario Outline: Try to Login with incorrect details
 #   Given Orange HRM Login Page opened
 #   When User Logins with <Username> and <Password>
 #   Then There should be an error MSG shown

 #   Examples: Incorrect Data
 #   |     Username    |     Password    |
 #   |test             |test             |
 #   |Testing          |Test123          |
 #   |@123             |@123             |

    Scenario: Validate Login Process
      Given Orange HRM Login Page opened
      When Logins with User details
      Then Validate Login