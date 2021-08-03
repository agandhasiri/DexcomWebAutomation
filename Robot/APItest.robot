*** Settings ***
Documentation       This file contains API automation test case

Library    ../Keywords/APIKeywords.py


*** Test Cases ***
API-01 AnalysisTest
    [Tags]    LoginTest
    ${signURL_2}  ${idsrv} =  Call to Account Management
    ${callBack} =  Callback Post  ${signURL_2}  ${idsrv}
    ${access_token} =  CAll to get Access Token  ${callBack}
    ${analysisSessionId} =  Analysis Session Post  ${access_token}
    Assert Session Id  ${analysisSessionId}





