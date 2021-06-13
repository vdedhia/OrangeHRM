import os

from time import sleep
from datetime import datetime

# Importing from Project
from Lib.Config import Config
from Lib.Logger import Logger

log = Logger()


class PageBase:
    def __init__(self, driver, name='PageModel'):
        self.driver = driver
        self.page_name = name
        self.image_cnt = 0

    def implicitly_wait(self, wait_time=Config.Wait_Time_Sec.value):
        sleep(wait_time)

    def get_opened_url(self):
        return self.driver.current_url

    def save_image(self):
        if not os.path.isdir('./Screenshot'):
            os.makedirs('./Screenshot')
        self.driver.save_screenshot(
            './Screenshot/' + str(datetime.now())[:-7].replace(" ", "_").replace(":", "_") + ".png")
