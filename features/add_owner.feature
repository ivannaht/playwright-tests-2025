Feature: Add Owner
  Test text

Scenario: Add new owner - positive
  Given I am on add owner page
  When I populate all required fields
  And I click on Save button
  Then I see owner info
