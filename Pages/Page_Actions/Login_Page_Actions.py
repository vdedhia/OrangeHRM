from pandas._testing import assert_timedelta_array_equal

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

    @PageBase.save_image()
    def Do_LoginAction(self, username, password):
        log.logger('INFO', 'Doing Login action')
        UserName_Input = self.driver.find_element(*LoginPage_XPaths['Username_Input'])
        UserName_Input.send_keys(username)
        Password_Input = self.driver.find_element(*LoginPage_XPaths['Password_Input'])
        Password_Input.send_keys(password)
        log.logger('INFO', 'Entered Username & Password')
        Login_Button = self.driver.find_element(*LoginPage_XPaths['Login_Button'])
        Login_Button.click()
        log.logger('INFO', 'Logged in')
        self.implicitly_wait()

    @PageBase.save_image()
    def Login_Result(self):
        Logged_User = self.driver.find_element(*User_Details['Loggedin_User'])
        log.logger('INFO', 'Logged User is ' + Logged_User.text)
        Logged_User = Logged_User.text.split()
        assert Logged_User[1] == 'Raj'
        self.implicitly_wait()
        log.logger('INFO', 'Test Completed')

    @PageBase.save_image()
    def Validate_Login(self):
        log.logger('INFO', 'Validating Login')
        Error_MSG = self.driver.find_element(*LoginPage_XPaths['Invalid_Login'])
        log.logger('INFO', 'Logged User is ' + Error_MSG.text)
        assert Error_MSG.text == 'Invalid credentials'
