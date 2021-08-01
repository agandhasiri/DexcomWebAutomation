*** Settings ***
Library  SeleniumLibrary
Variables   ../pageObjects/Locators.py

*** Keywords ***
Open my Browswer
    Create Webdriver    ${browser}  executable_path=C:/Drivers/drivers/chromedriver.exe
    Go To    ${url}

Click Home User
    Click button    ${button_Home_User}

Enter Username
    [Arguments]  ${username}
    Input Text  ${txt_loginUserName}   ${username}

Enter Password
    [Arguments]  ${password}
    Input Text  ${txt_loginPassword}   ${password}

Click LogIn
    Click button    ${button_login}

Clarity Site Should Be Open
    wait until page contains     Dexcom CLARITY for Home Users
    Title Should Be    Dexcom CLARITY

Login Page Should Be Open
    set selenium implicit wait  10 seconds
    Title Should Be    Dexcom - Account Management