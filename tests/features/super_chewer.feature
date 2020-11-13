Feature: super chewer
  As a barkbox customer,
  I want to subscribe for 1-month,
  so that I buy super chewer.

  Scenario: verify tax is displayed correctly
    Given the home page as launch
    When I select super chewer
    When I choose a plan
    When I enter the dogs name
    When I select the size of the dog
    When I enter the breed of the dog
    When I enter the dog date of birth
    When I select treats
    When I enter my email address
    When I select type of subscription
    When I decline extra toy
    When I select the theme
    Then I should be on the checkout page
    And I  select credit card as means of payment
    And I fill shipping address form
    And I should assert the tax is displayed correctly


