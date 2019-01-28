# Created by Victor at 13.01.2019
Feature: Info output

  Scenario: Output info onto a screen
    Given service is enabled
    When user chooses a quote
    And user pronounce: "source"
    And program recognizes operation
    Then program reads meta
    And program shows meta info


  Scenario: Output info onto a screen
    Given service is enabled
    When user chooses a quote
    And user pronounce: "find author John Doe"
    And program recognizes operation
    Then program reads meta
    And looks for author info using Wikipedia API
    And program shows info