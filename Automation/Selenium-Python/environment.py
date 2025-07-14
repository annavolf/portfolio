from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def before_all(context):
    """
    Initialize the test environment, including headless Chrome WebDriver setup, log file management,
    and logging configuration, before any test scenarios are executed.

    :param context: The Behave context object that holds shared data between steps and hooks.
    """

    chrome_options = Options()
    # chrome_options.add_argument("--incognito")

    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    context.driver.maximize_window()
    context.home_window = context.driver.current_window_handle



def after_all(context):
    """
    Clean up the testing environment after all tests have run.

    :param context: The Behave context object that holds shared data between steps and hooks.
    """
    context.driver.quit()
