# Created by Victor at 06.12.2018
Feature: Record a note
  Make a new record with a new tag or existing tag

  Scenario: Record with a new tag
    Given service is active
    When user pronounce "test record"
    And program recognize input
    #And time interval since last record < 3 sec # This is coroutine, so start this from step below
    Then record state is activated
    And user pronounces what has to be recorded
