Feature: Login with Form

    Scenario: Simple Login
        Given The user navigate to login page
        When The user enters their "username" and "password"
        Then The user redirects to their account page

    Scenario: Simple Logout
        Given The user is successfully login to their page
        When The user is clicked the logout button
        Then The user comes back to the login page

    Scenario: Testing Failed login
        Given The user is on the login page
        When The user enters invalid "username" and "password"
        Then The user is not redirects to their account page
        And The user stays on the login page