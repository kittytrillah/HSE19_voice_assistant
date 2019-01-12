# Created by Victor at 06.12.2018
Feature: Record a note
  Make a new record with a new tag or existing tag

  Scenario: Record with a new tag
    Given service is active
    When user pronounce "test record"
    And program recognize input
    And program starts recording speech
    And program recorded text Any piece of text
    And piece of recorded part is finished
    #And time interval since last record < 3 sec # This is coroutine, so start this from step below
    Then note is recorded
    And user pronounces A tag
    And tag saved with a note


    Scenario: Record with an existing tag
    Given service is active
    When user pronounce "test record"
    And program recognize input
    And program starts recording speech
    And program recorded text Any piece of text
    And piece of recorded part is finished
    #And time interval since last record < 3 sec # This is coroutine, so start this from step below
    Then note is recorded
    And user pronounces A tag
    And tag saved with a note
