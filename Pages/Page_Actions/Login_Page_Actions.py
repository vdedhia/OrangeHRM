from Lib.Config import Config
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
        PageBase.save_image(self)
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
        PageBase.save_image(self)
        self.implicitly_wait()
        log.logger('INFO', 'Test Completed')

    def Validate_Login(self):
        log.logger('INFO', 'Validating Login')
        Error_MSG = self.driver.find_element(*LoginPage_XPaths['Invalid_Login'])
        log.logger('INFO', 'Logged User is ' + Error_MSG.text)
        PageBase.save_image(self)
        assert Error_MSG.text == 'Invalid credentials'

    def Read_Testdata(self):
        log.logger('INFO', 'Reading Test data')
        Testdata_file = open(Config.Test_Data.value)
        log.logger('INFO', Testdata_file)

    def TestData_Validate_Login(self):
        Testdata_file = open(Config.Test_Data.value)
        for x in Testdata_file:
            x = x.split()
            if 'Username' in x[0].split(','):
                log.logger('INFO', 'Contains Header')
            else:
                TestData = x[0].split(',')
                username = self.driver.find_element(*LoginPage_XPaths['Username_Input'])
                pwd = self.driver.find_element(*LoginPage_XPaths['Password_Input'])

                username.send_keys(TestData[0])
                pwd.send_keys(TestData[1])
                log.logger('INFO', 'Entered Username & Password')
                Login_Button = self.driver.find_element(*LoginPage_XPaths['Login_Button'])
                PageBase.save_image(self)
                Login_Button.click()
                self.implicitly_wait()
                log.logger('INFO', 'Result should be ' + TestData[2])
                if TestData[2] == 'True':
                    Logged_User = self.driver.find_element(*User_Details['Loggedin_User'])
                    log.logger('INFO', 'Logged User is ' + Logged_User.text)
                    Logged_User = Logged_User.text.split()
                    if Logged_User[1] in Config.Users.value:
                        assert Logged_User[1] in Config.Users.value
                    else:
                        log.logger('ERROR', 'No Match Found')
                    PageBase.save_image(self)
                    self.implicitly_wait()
                    Login_Page.ResetPage(self)
                    self.implicitly_wait()
                elif TestData[2] == 'False':
                    Error_MSG = self.driver.find_element(*LoginPage_XPaths['Invalid_Login'])
                    log.logger('INFO', 'Logged User is ' + Error_MSG.text)
                    assert Error_MSG.text == 'Invalid credentials'
                    PageBase.save_image(self)

    def ResetPage(self):
        User = self.driver.find_element(*User_Details['User'])
        User.click()
        Logout = self.driver.find_element(*User_Details['Logout'])
        Logout.click()
        log.logger('INFO', 'Logged Out')
        self.driver.get(Config.Base_URL.value)
