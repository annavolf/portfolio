
Feature: example

  Scenario: First scenario
    Given Open "https://www.google.com"
    Then Wait 1 seconds
    
  Scenario: search for Python
    Given Open "https://www.google.com"
    Then Verify page by title "Google"
    And Verify presents of element "//textarea[@class='gLFyf']"
    When Type "Python" into "//textarea[@class='gLFyf']"
    When Click element "(//input[@class='gNO89b'])[1]"
    Then Verify that xpath "//textarea" should contain text "Python"
    And Wait 5 seconds

