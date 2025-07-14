from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from behave import *
from selenium.webdriver.support.wait import WebDriverWait


@step('I wanna open "{pagename}"')
def open_main_page(context, pagename):
    if pagename=='Profitolizer Home Page':
        context.driver.get("https://profitolizer.com/")
    elif pagename=='Google':
        context.driver.get("https://www.google.com/")
    elif pagename=='Profitolizer Login Page':
        context.driver.get("https://app.profitolizer.com/#/login")
    else:
        assert pagename in context.driver.title, f"pagename {pagename} not found"


@step('I wanna verify page title as "{str_title}"')
def verify_title(context, str_title):
    actual_title = context.driver.title
    print(f"Actual title: {actual_title}")
    assert str_title == context.driver.title, f"{actual_title}! = {str_title}"


@step('I click on "{xpath_of_element}" element')
def click_element(context, xpath_of_element):
    element=WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_of_element)))
    element.click()


@step('I wanna type "{text}" into an element with xpath "{text_xpath}"')
def xpath_input(context,text,text_xpath):
    context.driver.find_element(By.XPATH,text_xpath).send_keys(text)


@step("I wanna add new project")
def add_new_project(context):
    xpath = {
        'project': "//div[./label[text()='Project Name']]//input",
        'start_date': "//input[@placeholder='Start date']",
        'description': "//div[./label[text()='Project description']]//textarea",
        'dimension': "//span[text()='Period Dimension']",
        'duration': "//span[text()='",
    }
    for row in context.table:
        type_text(context,row[0],xpath['project'])
        type_text(context, row[1], xpath['start_date'])
        type_text(context, row[2], xpath['description'])
        click_element(context, xpath['dimension'])
        click_element(content,f"")