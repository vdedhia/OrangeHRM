from behave import given, when, then

# Importing from Project
from Lib.Config import Config
from Lib.Logger import Logger

log = Logger()


@given("Orange HRM Login Page opened")
def step_impl(context):
    if context.driver.current_url == Config.Base_URL.value:
        log.logger('INFO', 'Login page opened')
        return
    else:
        context.driver.get(Config.Base_URL.value)


@when("User Logins with User details")
def step_impl(context):
    log.logger('INFO', 'Login page entering login details')
    context.LoginPageAction.Do_LoginAction()


@when("User Logins with {Username} and {Password}")
def step_impl(context, Username, Password):
    log.logger('INFO', 'Login page entering login details')
    context.LoginPageAction.Do_LoginAction(Username, Password)


@then("Orange HRM home page should be opened")
def step_impl(context):
    context.LoginPageAction.Login_Result()


@then("There should be an error MSG shown")
def step_impl(context):
    context.LoginPageAction.Validate_Login()
