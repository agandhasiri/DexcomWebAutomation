*** Settings ***
Documentation    This file contains web automation test case for Login

Library     SeleniumLibrary
Resource  ../Resources/LoginKeywords.robot
Resource  ../pageObjects/variables.robot



*** Test Cases ***
web-02 LoginTest
    [Tags]    LoginTest
    Open my Browswer
    Clarity Site Should Be Open
    Click Element  link:Dexcom CLARITY for Home Users
    Login Page Should Be Open
    Enter Username  ${user}
    Enter Password  ${pwd}
    Click LogIn



