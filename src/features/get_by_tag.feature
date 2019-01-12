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