from time import sleep

from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#from selenium.webdriver.common.keys import Keys

#import api


@step('Open "{url}"')
def open_url(context, url):
    print(f"Opening url {url}")
    context.driver.get(url)


@step('Open {env} environment')
def open_env(context, env):
    envs = {
        'prod': 'https://www.profitolizer.com/',
        'dev': 'https://www.dev.profitolizer.com/',
        'test': 'https://www.test.profitolizer.com/',
        'uat': 'https://www.uat.profitolizer.com/',
        'qa': 'https://www.qa.profitolizer.com/',
    }
    open_url(context, envs[env])
    sleep(1)
    context.home_window = context.driver.current_window_handle


@step('Wait {sec} seconds')
def wait_sec(context, sec):
    sleep(int(sec))


@step('Click element "{xpath}"')
def click_element(context, xpath):
    # element = context.driver.find_element(By.XPATH, xpath)

    element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()


@step('Type "{text}" into "{xpath}"')
def type_text(context, text, xpath):
    element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    # element = context.driver.find_element(By.XPATH, xpath)
    element.send_keys(text)
    # element.send_keys(Keys.COMMAND, 'a')


@step('Verify page by title "{text}"')
def verify_title(context, text):
    sleep(1)
    title = context.driver.title
    assert title == text, f"Expected title: {text}, actual title: {title}. "


@step('Verify presents of element "{xpath}"')
def verify_presents_of_element(context, xpath):
    # elements = context.driver.find_elements(By.XPATH, xpath)
    elements = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
    assert len(elements) == 1


@step("Fill out following information")
def create_project(context):
    elements = {
        'project': "//div[./label[text()='Project Name']]//input",
        'start_date': "//input[@placeholder='Start date']",
        'description': "//div[./label[text()='Project description']]//textarea",
        'dimension': "//span[text()='Period Dimension']",
        'duration': "//span[text()='",
    }
    for row in context.table:
        type_text(context, row[0], elements['project'])
        type_text(context, row[1], elements['start_date'])
        type_text(context, row[2], elements['description'])
        click_element(context, elements['dimension'])
        sleep(1)
        click_element(context, f"//li/span[text()='{row[3]}']")
        click_element(context, f"{elements['duration']}{row[4]}']")


@step("Fill out following information with keys")
def create_project_keys(context):
    elements = {
        'Project Name': "//div[./label[text()='Project Name']]//input",
        'Start date': "//input[@placeholder='Start date']",
        'Project description': "//div[./label[text()='Project description']]//textarea",
        'Period Dimension': "//span[text()='Period Dimension']",
        'Project Duration': "//div[./label[text()='Project Duration']]//span[text()='",
    }
    for row in context.table:
        if row.cells[0] in ['Project Name', 'Start date', 'Project description']:
            type_text(context, row.cells[1], elements[row.cells[0]])
        elif row.cells[0] == 'Period Dimension':
            click_element(context, elements[row.cells[0]])
            sleep(0.5)
            click_element(context, f"//li/span[text()='{row.cells[1]}']")
        else:
            click_element(context, f"{elements[row.cells[0]]}{row.cells[1]}']")


@step("Login with {user} credentials")
def login(context, user):
    users = {
        'Admin': ('pcs.automationclass@gmail.com', 'Qwerty7'),
        'Sale': ('pcs.automationclass+1@gmail.com', 'Qwerty7+1'),
        'Wrong': ('pcs.automationclass@gmail.com', 'Qwerty'),
        'Manager': ('pcs.automationclass+4@gmail.com', 'Qwerty7'),
    }
    click_element(context, "//a[text()='Login']")
    type_text(context, users[user][0], "//input[@name='username']")
    type_text(context, users[user][1], "//input[@name='password']")
    click_element(context, "//button[contains(text(), 'Login')]")


@step('Get weather in "{city}"')
def get_weather(context, city):
    weather = api.get_weather(city)
    print(weather)


@step("Switch to new window")
def switch_to(context):
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])


@step("Switch to home window")
def switch_to_home(context):
    context.driver.switch_to.window(context.home_window)


@step("Close current window")
def step_impl(context):
    context.driver.close()


@step('Verify that xpath "{xpath}" should contain text "{expected_text}"')
def step_impl(context, xpath, expected_text):
      #element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
      element =  context.driver.find_element(By.XPATH, xpath)
      actual_text = element.text
      print(f"Expected text: {expected_text}")
      print(f"Actual text: {actual_text}")
      # Assert the text matches exactly
      assert actual_text == expected_text, f"Text does not match: '{actual_text}' != '{expected_text}'"
      # Optionally assert that the expected text is contained in the actual text
      assert expected_text in actual_text, f"Expected text '{expected_text}' not found in '{actual_text}'"


@step('Wait for the element with xpath {xpath} to be present')
def step_impl(context, xpath):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located(By.XPATH(xpath)))