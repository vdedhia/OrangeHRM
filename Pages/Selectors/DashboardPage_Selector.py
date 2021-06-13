from selenium.webdriver.common.by import By

User_Details = {
    'User': (By.XPATH, '/html/body/div[1]/div[1]/a[2]'),
    'Loggedin_User': (By.ID, 'welcome'),
    'Logout': (By.XPATH, '/html/body/div[1]/div[1]/div[9]/ul/li[3]/a')
}