import datetime
import time

from appium.webdriver.common.touch_action import TouchAction
from behave import given, then, when

from Pages.PageObject import ContactForm
from utilites.Requesttobd import check_event

timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


@given("Запуск приложения перед авторизацией")
def classObjects(context):
    context.cf = ContactForm(context.driver)
    context.cf.clickContactFromDutton()
    context.cf.enterCod()
    context.cf.enterUrl()
    TouchAction(context.driver).press(x=696, y=628).move_to(x=693, y=179).release().perform()
    context.cf.enterUrlAnalytic()
    context.cf.submitButton()



@when("Ввод логина и пароля")
def enterDataInForm(context):
    context.cf.enterLogin()
    context.cf.enterPassword()
    time.sleep(3)


@then("клик Войти")
def enterDataInForm(context):
    context.cf.loginButton()
    context.cf.skipPopUp1()
    context.cf.skipPopUp2()

@then("Проверить в БД ивент driver_sign_in")
def checkevents(context):
    time.sleep(20)
    actual_event_types = check_event(timestamp)
    expected_event_type = ("driver_sign_in",)
    if expected_event_type not in actual_event_types:
        raise AssertionError(f'{expected_event_type} not in {actual_event_types}')






