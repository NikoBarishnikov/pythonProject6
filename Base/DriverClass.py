from appium import webdriver


class Driver:
    def getDriverMethod(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "MTP71762102143",
            "app": "C:\\Users\\User\\debug-3.21.0.149466.apk",
            "automationName": "UiAutomator1",
            "appPackage": "ua.com.uklon.uklondriver.dev",
            "appWaitActivity": "*",
            "appWaitDuration": "30000"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap=desired_cap)
        self.driver.implicitly_wait(30)

        return self.driver
