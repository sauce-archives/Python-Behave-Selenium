Feature: Manipulating the guinea pig test website

  Scenario: We want to check the first box and populate the email field
    Given we are on a browser
    And we are looking at the guinea pig website
    When we click on the uncheck box
    Then it should be checked
    When I populate the email field 
    Then it should contain the value I entered

  Scenario: We want to click on the link and verify it takes us to a new page
    Given we are on a browser
    And we are on the guinea pig website
    When I click on the link
    Then I should see a new page  
