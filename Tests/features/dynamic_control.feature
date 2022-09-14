Feature: Dynamic Content

    Background: 
        Given The user is navigated to the Dynamic Content page

    Scenario: Removing the Checkbox element on the page
        When The user clicks the Remove button
        Then The Checkbox element is gone
        And The Add button appears

    Scenario: Adding the Checkbox element on the page
        When The user has removed the checkbox element
        And The user is clicked the Add button
        Then The Checkbox element re-appears

    Scenario: Enable the Text Area element on the page
        When The user clicks Enable button
        Then The Text Area element is being enabled

    Scenario: Disable the Text Area element on the page
        When The user has enabled the Text Area on the page
        And The user is clicked the Disabled button
        Then The Text Area is being disabled
    
    
