Feature: Adding Items to Cart

  Scenario: Add One Item
    Given we are on a browser
    And we are on the inventory page
    When we add an item to the cart
    Then we should see one item in our cart

  Scenario: Adding Two Items
    Given we are on a browser
    And we are on the inventory page
    When we add two items to the cart
    Then we should see two items in our cart