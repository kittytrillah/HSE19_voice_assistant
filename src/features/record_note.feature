# Created by Victor at 06.12.2018
Feature: Record a note
  Make a new record with a new tag or existing tag

  Scenario: Record with a new tag
    Given service is active
    When user pronounce "test record"
    #And time interval since last record < 3 sec # This is coroutine, so we have to use async here
    And program recognize input
    And program starts recording speech
    And program recorded text Any piece of text
    And piece of recorded part is finished
    #And time interval since last record < 3 sec # This is coroutine, so we have to use async here
    Then note is recorded
    And user pronounces A tag
    And tag saved with a note


  Scenario: Record with an existing tag
    Given service is active
    And "some tag" exists
    When user pronounce "test record"
    #And time interval since last record < 3 sec # This is coroutine, so we have to use async here
    And program recognize input
    And program starts recording speech
    And program recorded text Any piece of text
    And piece of recorded part is finished
      #And time interval since last record < 3 sec # This is coroutine, so we have to use async here
    Then note is recorded
    And user pronounces some tag
    And tag saved with a note


  Scenario: Record is failed (command unrecognized)
    Given service is active
    When user falsely pronounce "something else except of right stuff"
    #And time interval since last record < 3 sec # This is coroutine, so we have to use async here
    And program recognize input
    And program can't find existing command
    Then app is asking user to repeat command


  Scenario: Record is failed (page is empty)
    Given service is active
    And page is empty
    When user pronounce "test record"
    Then app notices user about empty page error


  Scenario: Record is failed (text want't pronounced within time limits)
    Given service is active
    When user pronounce "test record"
    #And time interval since last record > 3 sec # This is coroutine, so we have to use async here
    And user silent for 3+ seconds
    Then app resets command
    And app notices user about standby mode


  Scenario: Record is failed (text unrecognized)
    Given service is active
    When user pronounce "test record"
    #And time interval since last record < 3 sec # This is coroutine, so we have to use async here
    And program recognize input
    And program starts recording speech
    And program recorded text non text stuff
    And piece of recorded part is finished
    And text unrecognized
    Then app notices user about text couldn't be recognized


  Scenario: Record is failed (tag want't pronounced within time limits)
    Given service is active
    When user pronounce "test record"
    #And time interval since last record < 3 sec # This is coroutine, so we have to use async here
    And program recognize input
    And program starts recording speech
    And program recorded text Any piece of text
    And piece of recorded part is finished
    #And time interval since last record > 3 sec # This is coroutine, so we have to use async here
    And user fails to pronounce a tag
    Then note is recorded
    And app notices user about note was saved without tag