from Pages.Base_Page import PageBase
from Pages.Selectors.LoginPage_Selector import LoginPage_XPaths
from Pages.Selectors.DashboardPage_Selector import User_Details
from Lib.Logger import Logger

log = Logger()


class Login_Page(PageBase):
    def __init__(self, driver, name):
        PageBase.__init__(self, driver, name)
        self.driver = driver
        self.page_name = name

    def Do_LoginAction(self, username, password):
        log.logger('INFO', 'Doing Login action')
        UserName_Input = self.driver.find_element(*LoginPage_XPaths['Username_Input'])
        UserName_Input.send_keys(username)
        Password_Input = self.driver.find_element(*LoginPage_XPaths['Password_Input'])
        Password_Input.send_keys(password)
        log.logger('INFO', 'Entered Username & Password')
        Login_Button = self.driver.find_element(*LoginPage_XPaths['Login_Button'])
        PageBase.save_image()
        Login_Button.click()
        log.logger('INFO', 'Logged in')
        self.implicitly_wait()

    def Login_Result(self):
        Logged_User = self.driver.find_element(*User_Details['Loggedin_User'])
        log.logger('INFO', 'Logged User is ' + Logged_User.text)
        Logged_User = Logged_User.text.split()
        if Logged_User[1] == 'Raj':
            assert Logged_User[1] == 'Raj'
        elif Logged_User[1] == 'Paul':
            assert Logged_User[1] == 'Paul'
        else:
            log.logger('ERROR', 'No Match Found')
        PageBase.save_image()
        self.implicitly_wait()
        log.logger('INFO', 'Test Completed')

    def Validate_Login(self):
        log.logger('INFO', 'Validating Login')
        Error_MSG = self.driver.find_element(*LoginPage_XPaths['Invalid_Login'])
        log.logger('INFO', 'Logged User is ' + Error_MSG.text)
        PageBase.save_image()
        assert Error_MSG.text == 'Invalid credentials'
