# Created by Ivan at 13.01.2019
Feature: Get information about reading time

  Scenario: Show estimated reading time of the whole book
    Given service activated
    When user chooses a book from library
    And user pronounces "estimated reading time"
    And program gets units of measurement from settings
    Then program divides book text length by a number of units of measurement
    And program shows estimated reading time

  Scenario: Show remaining reading time of the book
    Given service activated
    When user chooses a book from library
    And user pronounces "remaining reading time"
    And program gets units of measurement from settings
    And program gets time spent on reading in units of measurement
    And program divides book text length by a number of units of measurement
    Then program subtracts one value from another
    And program shows remaining reading time

  Scenario: Show spent on reading time
    Given service activated
    When user chooses a book from library
    And user pronounces "spent on reading time"
    And program gets units of measurement from settings
    And program gets time spent on reading in units of measurement
    Then program shows spent on reading time