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

    @staticmethod
    def save_image(delay_sec=0):
        def save_screenshot(method):
            def wrapper(*args, **kwargs):
                args[0].image_cnt += 1
                value = method(*args, **kwargs)
                if delay_sec != 0:
                    sleep(delay_sec)
                if not os.path.isdir('./Screenshot'):
                    os.makedirs('./Screenshot')
                args[0].driver.save_screenshot('./Screenshot/' + str(args[0].image_cnt) + "_" + args[0].page_name + "_"
                                               + str(datetime.now())[:-7].replace(" ", "_").replace(":", "_") + ".png")
                return value

            return wrapper

        return save_screenshot
