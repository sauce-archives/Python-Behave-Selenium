Feature: Login to Swag Labs

  Scenario: Valid Login
    Given we are on a browser
    And we are on the swag labs site
    When we login as a standard user
    Then we should be on the inventory page

  Scenario: Invalid Login
    Given we are on a browser
    And we are on the swag labs site
    When we login as an invalid user 
    Then it should raise an error