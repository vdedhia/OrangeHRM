from typing import Dict, Tuple

from selenium.webdriver.common.by import By

HomePage_logo = '//*[@id="divLogo"]/img'

# XPaths to fields
# Din't Work using ID, Need to check
XPath = {
    'Username_Input': (By.ID, '//*[@id="txtUsername"]'),
    'Password_Input': (By.ID, '//*[@id="txtPassword"]'),
    'Login_Button': (By.ID, '//*[@id="btnLogin"]'),
    'Forgot_Password_link': (By.ID, '//*[@id="forgotPasswordLink"]/a')
}

# Long XPath to fields
Common_XPath = '/html/body/div[1]/div/div[3]/div[2]/div[2]/form/'

# Full XPath
LoginPage_XPaths = {
    'Username_Input': (By.XPATH, Common_XPath + 'div[2]/input'),
    'Password_Input': (By.XPATH, Common_XPath + 'div[3]/input'),
    'Login_Button':  (By.XPATH, Common_XPath + 'div[5]/input'),
    'Forgot_Password_link': (By.XPATH, Common_XPath + 'div[5]/div/a'),
    'Invalid_Login': (By.XPATH, Common_XPath + 'div[5]/span')
 }
