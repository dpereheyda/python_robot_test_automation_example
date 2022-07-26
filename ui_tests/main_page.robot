*** Settings ***
Documentation       Suite description
Library             page_objects.steps

*** Test Cases ***
Open main page
    [Tags] Smoke
    open portal
    check main page loaded

Check tabs navigation
    Open portal
    Select tab              Products
    Check tab is selected   Products

*** Keywords ***
Open portal
    open portal
    check main page loaded