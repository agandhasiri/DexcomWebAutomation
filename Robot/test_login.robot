*** Settings ***
Documentation    This file contains web automation test case

Library     SeleniumLibrary


*** Variables ***
${browser}  Chrome
${url}  https://clarity.dexcom.com/
${browser_Path}  executable_path=C:/Drivers/drivers/chromedriver.exe

*** Test Cases ***
Web-01 User Login
    [Tags]    DEBUG
    Create Webdriver    ${browser}  executable_path=C:/Drivers/drivers/chromedriver.exe
    Go To    ${url}
    Sleep  5s
    Clarity Site Should Be Open
    Click Element  link:Dexcom CLARITY for Home Users
    Sleep  5s
    Login Page Should Be Open
    Input Text  id:username  codechallenge
    Input Text  id:password  Password123
    Click Element  name:op
    Sleep  5s
    Close Browser

*** Keywords ***
Clarity Site Should Be Open
    Title Should Be    Dexcom CLARITY

Login Page Should Be Open
    Title Should Be    Dexcom - Account Management