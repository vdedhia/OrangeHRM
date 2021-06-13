import sys

from selenium.webdriver import DesiredCapabilities
from selenium import webdriver

# Importing from Project
from Lib.Config import Config
from Lib.Logger import Logger
from Pages.Base_Page import PageBase
from Pages.Page_Actions.Login_Page_Actions import Login_Page

log = Logger()


def before_all(context):
    log.logger('INFO', 'Executing before all')
    assert context


def before_feature(context, feature):
    log.logger('INFO', 'Executing before ' + str(feature))
    assert context


def get_driver_capabilities(context):
    browser = context.config.userdata.get("browser")
    log.logger('INFO', 'Executing on {} browser'.format(browser))
    capabilities = None
    if browser == 'firefox':
        driver_path = './Drivers/geckodriver'
        capabilities = DesiredCapabilities.FIREFOX.copy()
        if context.config.userdata.get("selenium_hub") == 'local':
            context.driver = webdriver.Firefox(executable_path=driver_path, capabilities=capabilities)
            capabilities = None
    elif browser == 'chrome':
        options = webdriver.ChromeOptions()
        if sys.platform == 'win32':
            driver_path = './Drivers/chromedriver.exe'
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            context.driver = webdriver.Chrome(executable_path=driver_path, options=options)
            capabilities = None
        else:
            driver_path = './Drivers/chromedriver'
            context.driver = webdriver.Chrome(executable_path=driver_path)
            if context.config.userdata.get("selenium_hub") == 'local':
                context.driver = webdriver.Chrome(options=options)
            capabilities = DesiredCapabilities.CHROME.copy()
    elif browser == 'safari':
        capabilities = DesiredCapabilities.SAFARI.copy()
    elif browser == 'opera':
        capabilities = DesiredCapabilities.OPERA.copy()
    elif browser == 'internet_explorer':
        capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
    elif browser == 'edge':
        if sys.platform == 'win32':
            driver_path = './Drivers/msedgedriver.exe'
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            context.driver = webdriver.Edge(executable_path=driver_path)
            capabilities = None
        else:
            driver_path = './Drivers/linux_msedgedriver'
            capabilities = DesiredCapabilities.EDGE.copy()
            capabilities['platform'] = 'LINUX'
            context.driver = webdriver.Edge(executable_path=driver_path, capabilities=capabilities)
            capabilities = None
    return capabilities


def before_scenario(context, scenario):
    log.logger('INFO', 'Executing before ' + str(scenario))
    capabilities = get_driver_capabilities(context)

    browser_name = context.config.userdata.get("browser")
    context.driver.implicitly_wait(Config.Wait_Time_Sec.value)
    context.BasePage = PageBase(context.driver, 'Base Page' + browser_name)
    context.LoginPageAction = Login_Page(context.driver, 'Login Page ' + browser_name)

    log.logger('INFO', 'Opening the page')
    context.driver.maximize_window()


# noinspection PyUnusedLocal
def after_scenario(context, scenario):
    log.logger('INFO', 'Executing after scenario')
    context.driver.quit()


# noinspection PyUnusedLocal
def after_feature(context, feature):
    log.logger('INFO', 'Executing after ' + str(feature))


# noinspection PyUnusedLocal
def after_all(context):
    log.logger('INFO', 'Executing after all')
