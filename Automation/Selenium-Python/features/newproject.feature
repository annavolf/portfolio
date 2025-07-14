# Created by annavolf at 1/17/25
Feature: Selenuim WebDriver Practice

  Scenario: Login to the app using custom methods
    Given I wanna open "Profitolizer Home Page"
    Then Wait 2 seconds
    Then I wanna verify page title as "Home - Profitolizer"
    And I click on "//a[text()='Login']" element
    Then Verify presents of element "//h5[text()='Login to Your Account']"
    Then Wait 2 seconds
    And I wanna type "annaverpcs+3@gmail.com" into an element with xpath "//input[@type='text']"
    And I wanna type "12345678" into an element with xpath "//input[@type='password']"
    Then I click on "//button[@type='submit']" element
    Then Wait 2 seconds
    And I wanna verify page title as "Profotolizer - Projects"
    Then Wait 1 seconds
  # Fill out the form for the New Project
#    And I wanna add new project
#    | project | start_date | description | dimension | duration
#    | AnnaV | 01/19/2025 | This is my first project | Month | 2 Years

