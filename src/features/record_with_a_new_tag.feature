# Created by Victor at 06.12.2018
Feature: Record with a new tag
  Make a new record with a new tag

  Scenario: Record with a new tag
    Given record of quote completed
    When user pronounce {tag_name}
    And time interval since last record < 4 sec
    Then tag recorded
    And succeed code in status bar
