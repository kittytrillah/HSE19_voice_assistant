# Created by Victor at 13.01.2019
Feature: Extract all quotes by tag

  Scenario: Show all quotes
    Given service activated
    When user pronounces "show me the quotes"
    And program recognizes input
    And program shows label "pronounce a tag"
    And user says "tag name" within 5 secs
    Then program searches for the quotes with that tag above
    And program shows all of the tagged quotes


  Scenario: Save all quotes
    Given service activated
    When user pronounces "save the quotes"
    And program recognizes input
    And program shows label "pronounce a tag"
    And user says "tag name" within 5 secs
    Then program searches for the quotes with that tag above
    And program saves all of the tagged quotes


  Scenario: Save all quotes in cloud
    Given service activated
    When user pronounces "save the quotes in cloud"
    And program recognizes input
    And program shows label "pronounce a tag"
    And user says "tag name" within 5 secs
    Then program searches for the quotes with that tag above
    And program saves all of the tagged quotes in cloud


  Scenario: Error (tag not found)
    Given service activated
    When user pronounces "show me the quotes"
    And program recognizes input
    And program shows label "pronounce a tag"
    And user says "non-existing tag name"
    And program recognizes input
    Then program shows label "no tag"


  Scenario: Error (no quotes)
    Given service activated
    When user pronounces "show me the quotes"
    And program recognizes input
    And program shows label "pronounce a tag"
    And user says "tag name" within 5 secs
    Then program searches 0 quotes with that tag above
    And program shows label "no quotes"


  Scenario: Error (no internet connection)
    Given service activated
    And connection is disabled
    When user pronounces "show me the quotes"
    And program recognizes input
    And program shows label "pronounce a tag"
    And user says "tag name" within 5 secs
    Then program searches the quotes with that tag above
    And program shows label "no connection. only local storage is active"