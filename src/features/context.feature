# Created by Ivan at 13.01.2019
Feature: Go to quotation context

  Scenario: Open quote left context (text before quote)
    Given service activated
    When user chooses a quote from saved quotes
    And user pronounces "find left context"
    And program recognizes operation
    Then program reads meta
    And program looks for a source book in a library
    And program looks for a chosen quote in source book text
    And program opens text a quote to be at the bottom of the page
    And program highlights quote

  Scenario: Open quote right context (text after quote)
    Given service activated
    When user chooses a quote from saved quotes
    And user pronounces "find right context"
    And program recognizes operation
    Then program reads meta
    And program looks for a source book in a library
    And program looks for a chosen quote in source book text
    And program opens text a quote to be at the top of the page
    And program highlights quote

  Scenario: Open all source text
    Given service activated
    When user chooses a quote from saved quotes
    And user pronounces "open book"
    And program recognizes operation
    Then program reads meta
    And program looks for a source book in a library
    And program opens book

  Scenario: Open chapter that contains quote
    Given service activated
    When user chooses A quote from saved quotes
    And user pronounces "open chapter"
    And program recognizes operation
    Then program reads meta
    And program looks for a source book in a library
    And program looks for a chosen quote in source book text
    And program looks for a chapter that contains chosen quote
    And program opens a chapter


