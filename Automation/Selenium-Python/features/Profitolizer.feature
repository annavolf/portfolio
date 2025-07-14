# Created by annavolf at 1/12/25
Feature: Login
Background:
      Given Open "https://profitolizer.com/"
    Then Verify page by title "Home - Profitolizer"
    And Click element "//a[text()='Login']"
    And Wait 5 seconds
    Then Verify page by title "Profotolizer - Login"
    And Verify that xpath "//h5[text()='Login to Your Account']" should contain text "Login to Your Account"

  Scenario: Correct username/correct password

    # fill out the form with valid username and valid password
    When Type "annaverpcs+2@gmail.com" into "//input[@type='text']"
    When Type "12345678" into "//input[@type='password']"
    And Click element "//button[@type='submit']"
    Then Verify presents of element "//span[text()='annaverpcs2']"
    And Wait 10 seconds

    Scenario: Valid username/incorrect password
    #Given Open "https://profitolizer.com/"
    #Then Verify page by title "Home - Profitolizer"
    #And Click element "//a[text()='Login']"
    #And Wait 5 seconds
    #Then Verify page by title "Profotolizer - Login"
    #And Verify that xpath "//h5[text()='Login to Your Account']" should contain text "Login to Your Account"
    # fill out the form with valid username and incorrect password
    When Type "annaverpcs+2@gmail.com" into "//input[@type='text']"
    When Type "1234567" into "//input[@type='password']"
    And Click element "//button[@type='submit']"
    Then Verify presents of element "//p[text()='Invalid username or password']"
    And Wait 10 seconds

    Scenario: No username/no password
        #Given Open "https://profitolizer.com/"
   # Then Verify page by title "Home - Profitolizer"
   # And Click element "//a[text()='Login']"
   # And Wait 5 seconds
   # Then Verify page by title "Profotolizer - Login"
   # And Verify that xpath "//h5[text()='Login to Your Account']" should contain text "Login to Your Account"
    # leave the form without username and password
    Then Click element "//button[@type='submit']"
    And Verify presents of element "//div[text()='Email is required']"
    And Verify presents of element "//div[text()='Password is required']"
    Then Wait 3 seconds


    Scenario: No username/valid password
   # Given Open "https://profitolizer.com/"
   # Then Verify page by title "Home - Profitolizer"
   # And Click element "//a[text()='Login']"
   # And Wait 5 seconds
   # Then Verify page by title "Profotolizer - Login"
  #  And Verify that xpath "//h5[text()='Login to Your Account']" should contain text "Login to Your Account"
    # fill out the form with empty username text field and valid password
    When Type "1234567" into "//input[@type='password']"
    And Click element "//button[@type='submit']"
    Then Verify presents of element "//div[text()='Email is required']"


    Scenario: Valid username/no password
      Given Open "https://profitolizer.com/"
    Then Verify page by title "Home - Profitolizer"
    And Click element "//a[text()='Login']"
    And Wait 5 seconds
    Then Verify page by title "Profotolizer - Login"
    And Verify that xpath "//h5[text()='Login to Your Account']" should contain text "Login to Your Account"
    # fill out the form with valid username and empty password text field
    When Type "annaverpcs+2@gmail.com" into "//input[@type='text']"
    And Click element "//button[@type='submit']"
    Then Verify presents of element "//div[text()='Password is required']"