import time

from appium import webdriver

import utilites.СustomLogger as sl

log = sl.customLogger()

def before_scenario(context,scenario):
    log.info("Automation started")
    desired_cap = {
        "platformName": "Android",
        "deviceName": "MTP71762102143",
        "app": "C:\\Users\\User\\debug-3.23.0.159689.apk",
        "automationName": "UiAutomator1",
        "appPackage": "ua.com.uklon.uklondriver.dev",
        "appWaitActivity": "*",
        "appWaitDuration": "30000"
    }

    context.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    context.driver.implicitly_wait(30)


def after_scenario(context,scenario):
    time.sleep(10)
    context.driver.quit()
    log.info("Automation ended")

#def after_all(context):
   # time.sleep(20)
    #print("======================")
   # print("List events after all scenarios")
    #print("======================")
    #check_event(timestamp)








