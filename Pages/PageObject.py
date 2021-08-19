from Base.BasePage import BaseClass

import utilites.СustomLogger as sl


class ContactForm(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator value in App

    _contactFromButton = "ua.com.uklon.uklondriver.dev:id/signInButton"  # id
    _enterCod = "ua.com.uklon.uklondriver.dev:id/loginEditable"  # id
    _enterUrl = "ua.com.uklon.uklondriver.dev:id/endpointsEditable"  # id
    _enterUrlAnalytic = "ua.com.uklon.uklondriver.dev:id/analyticsEndpointsEditable"  # id
    _submitButton = "Готово"  # accessibilityid
    _enterLogin = "ua.com.uklon.uklondriver.dev:id/loginEditable"  # id
    _enterPassword = "ua.com.uklon.uklondriver.dev:id/passwordEditable"  # id
    _loginButton = "ua.com.uklon.uklondriver.dev:id/loginButton"  # id
    _skipPopUp1 = "ua.com.uklon.uklondriver.dev:id/btnOk"  # id
    _skipPopUp2 = "ua.com.uklon.uklondriver.dev:id/btnDismiss"  # id
    _opensaidbar = "//android.view.View[2]/android.widget.FrameLayout/android.view.View/android.widget.ImageButton"  # xpath
    _clickbuttonSOS = "ua.com.uklon.uklondriver.dev:id/buttonSos"  # id
    _clickSOStoconfirm = "ua.com.uklon.uklondriver.dev:id/btnConfirm"  # id
    _clickbuttonTechSupport = "ua.com.uklon.uklondriver.dev:id/buttonTechSupport"  # id
    _calltoSupport = "ua.com.uklon.uklondriver.dev:id/cellCallToSupport"  # id
    _calltoSupportViber = "ua.com.uklon.uklondriver.dev:id/cellViber"  # id
    _clickonDisebleEnable = "ua.com.uklon.uklondriver.dev:id/tv_title"  # id
    _registerButon = "ua.com.uklon.uklondriver.dev:id/registerButton"  # id
    _remindpasswordbutton = "ua.com.uklon.uklondriver.dev:id/recoverPasswordText"  # id
    _clickonChangePhone = "ua.com.uklon.uklondriver.dev:id/tripleCellChangePhone"  # id
    _goUp = "Перейти вверх"  # accessibilityid
    _logout = "ua.com.uklon.uklondriver.dev:id/tripleCellClose"  # id
    _changeaccountbutton = "ua.com.uklon.uklondriver.dev:id/changeAccountButton"  # id
    _calltoSupportTg = "ua.com.uklon.uklondriver.dev:id/cellTelegram"  # id
    _calltoSupportMessenger = "ua.com.uklon.uklondriver.dev:id/cellFacebookMessenger"  # id
    _vehicle = "ua.com.uklon.uklondriver.dev:id/tripleCellVehicle"  # id
    _walletscreen = "ua.com.uklon.uklondriver.dev:id/tripleCellWallet"  # id
    _screenstatistics = "ua.com.uklon.uklondriver.dev:id/tripleCellStatistics"  # id
    _sectorsButton = "ua.com.uklon.uklondriver.dev:id/sectorsButton"  # id
    _trafficButton = "ua.com.uklon.uklondriver.dev:id/trafficButton"  # id
    _fishingButton = "ua.com.uklon.uklondriver.dev:id/fishingButton"  # id
    _paymentcard = "ua.com.uklon.uklondriver.dev:id/tripleCellPaymentCard"  # id
    _driverhelper = "ua.com.uklon.uklondriver.dev:id/tripleCellDriverHelper"  # id
    _driverclub = "ua.com.uklon.uklondriver.dev:id/tripleCellDriverClub"  # id
    _locationButton = "ua.com.uklon.uklondriver.dev:id/locationButton"  # id
    _clickonBonuses = "ua.com.uklon.uklondriver.dev:id/tripleCellBonuses"  # id
    _clickBackButtonPagelogin = "ua.com.uklon.uklondriver.dev:id/backButton"  # id
    _clickonfastsearch = "ua.com.uklon.uklondriver.dev:id/ibControl"  # id
    _clickofffastsearch ="ua.com.uklon.uklondriver.dev:id/lavFastSearch" #id
    _openefir = "ua.com.uklon.uklondriver.dev:id/etherIcon"  # id
    _openfiltrpage = "ua.com.uklon.uklondriver.dev:id/filtersBox"  # id
    _clickfilterautotake = "//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RadioGroup/android.widget.RadioButton[1]"  # xpath
    _clickswitchallfilters = "ua.com.uklon.uklondriver.dev:id/disableAllFiltersButton"  # id
    _clickefironfilter = "//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RadioGroup/android.widget.RadioButton[2]"  # xpath
    _clickfilteroff = "//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RadioGroup/android.widget.RadioButton[3]"  # xpath





    def clickfiltrautotake(self):
        self.clickElement(self._clickfilterautotake, "xpath")
        sl.allureLogs("Click on filter Auto.")

    def clickswitchallfilters(self):
        self.clickElement(self._clickswitchallfilters, "id")
        sl.allureLogs("Click on button switch off all filters.")

    def clickefironfilter(self):
       self.clickElement(self._clickefironfilter, "xpath")
       sl.allureLogs("Click on filter Efir.")

    def clickfilteroff(self):
        self.clickElement(self._clickfilteroff, "xpath")
        sl.allureLogs("Click on filter off.")


    def clickContactFromDutton(self):
        self.clickElement(self._contactFromButton, "id")
        sl.allureLogs("Click on button Enter before authorisation.")

    def enterCod(self):
       self.sendText("666", self._enterCod, "id")
       sl.allureLogs("Enter the code to go to env. selection screen.")

    def enterUrl(self):
        self.sendText("https://driver-staging.uklon.com.ua", self._enterUrl, "id")
        sl.allureLogs("Enter Url a required env.")

    def enterUrlAnalytic(self):
        self.sendText("https://as-staging.uklon.com.ua/", self._enterUrlAnalytic, "id")
        sl.allureLogs("Enter Url a AnalyticServis.")

    def submitButton(self):
        self.clickElement(self._submitButton, "accessibilityid")
        sl.allureLogs("Click to confirm the env selection.")

    def enterLogin(self):
        self.sendText("qaz@com.ua", self._enterLogin, "id")
        sl.allureLogs("Enter login users.")

    def enterPassword(self):
        self.sendText("Qwerty1", self._enterPassword, "id")
        sl.allureLogs("Enter password users.")

    def loginButton(self):
        self.clickElement(self._loginButton, "id")

        sl.allureLogs("Click on loginButton for authorisation in App.")

    def skipPopUp1(self):
        self.clickElement(self._skipPopUp1, "id")

        sl.allureLogs("Close pop-up info Attention.")

    def skipPopUp2(self):
        self.clickElement(self._skipPopUp2, "id")

        sl.allureLogs("Close pop-up info Order chain.")

    def opensaidbar(self):
        self.clickElement(self._opensaidbar, "xpath")

        sl.allureLogs("Click to open Sidebar.")

    def clickbuttonSOS(self):
        self.clickElement(self._clickbuttonSOS, "id")

        sl.allureLogs("Click on button SOS.")

    def clickcSOStoconfirm(self):
        self.clickElement(self._clickSOStoconfirm, "id")

        sl.allureLogs("Click to confirm SOS in pop-up.")

    def clickTechSupport(self):
        self.clickElement(self._clickbuttonTechSupport, "id")

        sl.allureLogs("Click on button TechSupport.")

    def calltosupport(self):
        self.clickElement(self._calltoSupport, "id")

        sl.allureLogs("Click to call cell TechSupport.")

    def calltosupportviber(self):
       self.clickElement(self._calltoSupportViber, "id")

       sl.allureLogs("Click to call viber TechSupport.")

    def calltosupportTg(self):
        self.clickElement(self._calltoSupportTg, "id")

        sl.allureLogs("Click to call telegram TechSupport.")

    def calltosupportMessenger(self):
        self.clickElement(self._calltoSupportMessenger, "id")

        sl.allureLogs("Click to call telegram Messenger.")

    def clickonDisebleEnable(self):
        self.clickElement(self._clickonDisebleEnable, "id")

        sl.allureLogs("Click on button Disable/Enable.")

    def enterLoginincorrect(self):
        self.sendText("qqqqqqq@com.ua", self._enterLogin, "id")

        sl.allureLogs("Enter wrong login.")

    def clickonRegisterButton(self):
        self.clickElement(self._registerButon, "id")

        sl.allureLogs("Click on button Register.")

    def remindPasswordbutton(self):
        self.clickElement(self._remindpasswordbutton, "id")

        sl.allureLogs("Click on button remained Password.")

    def clickonCangePhone(self):
        self.clickElement(self._clickonChangePhone, "id")

        sl.allureLogs("Click on button Change Phone.")

    def goUp(self):
        self.clickElement(self._goUp, "accessibilityid")

        sl.allureLogs("Click on button to go back on mein screen.")

    def clickonlogout(self):
        self.clickElement(self._logout, "id")

        sl.allureLogs("Click on button to logout.")

    def clickonchangeaccountbutton(self):
        self.clickElement(self._changeaccountbutton, "id")

        sl.allureLogs("Click on button to change account.")

    def clickdrivervehicle(self):
        self.clickElement(self._vehicle, "id")

        sl.allureLogs("Click on button to go driver vehicle.")

    def clickonwallet(self):
        self.clickElement(self._walletscreen, "id")

        sl.allureLogs("Click on button to wallet.")

    def clickonstatistics(self):
        self.clickElement(self._screenstatistics, "id")
        sl.allureLogs("Click on button to statistics.")

    def clickonsectorsButton(self):
        self.clickElement(self._sectorsButton, "id")
        sl.allureLogs("Click on button Sector.")

    def clickontrafficButton(self):
        self.clickElement(self._trafficButton, "id")
        sl.allureLogs("Click on button Traffic.")

    def clickonfishingButton(self):
        self.clickElement(self._fishingButton, "id")
        sl.allureLogs("Click on button Fishing.")

    def clickonlocationButton(self):
        self.clickElement(self._locationButton, "id")
        sl.allureLogs("Click on button Location.")

    def clickonpaymentcard(self):
        self.clickElement(self._paymentcard, "id")
        sl.allureLogs("Click on button PaymentCard.")

    def clickondriverhelper(self):
        self.clickElement(self._driverhelper, "id")
        sl.allureLogs("Click on button DriverHelper.")

    def clickondriverclub(self):
        self.clickElement(self._driverclub, "id")
        sl.allureLogs("Click on button DriverClub.")

    def clickonBonuses(self):
        self.clickElement(self._clickonBonuses, "id")
        sl.allureLogs("Click on button DriverClub.")

    def clickBackButtonLoginPages(self):
        self.clickElement(self._clickBackButtonPagelogin, "id")
        sl.allureLogs("Click on BackButton on page Login .")

    def clickonfastsearch(self):
        self.clickElement(self._clickonfastsearch, "id")
        sl.allureLogs("Click on FastSearch.")

    def clickofffastsearch(self):
        self.clickElement(self._clickofffastsearch, "id")
        sl.allureLogs("Click off FastSearch.")

    def clickopenefir(self):
        self.clickElement(self._openefir, "id")
        sl.allureLogs("Click on Button Efir.")

    def clickopenfiltrpage(self):
        self.clickElement(self._openfiltrpage, "id")
        sl.allureLogs("Click on Button Filtrs.")
