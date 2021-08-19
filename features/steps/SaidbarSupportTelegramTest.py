import datetime
import time

from appium.webdriver.common.touch_action import TouchAction
from behave import given, then, when

from Pages.PageObject import ContactForm
from utilites.Requesttobd import check_event

timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

@given("Запуск приложения,открыть Сайдбар,для Telegram")
def classObjects(context):
    context.cf = ContactForm(context.driver)
    context.cf.clickContactFromDutton()
    context.cf.enterCod()
    context.cf.enterUrl()
    TouchAction(context.driver).press(x=696, y=628).move_to(x=693, y=179).release().perform()
    context.cf.enterUrlAnalytic()
    context.cf.submitButton()
    context.cf.enterLogin()
    context.cf.enterPassword()
    context.cf.loginButton()
    context.cf.skipPopUp1()
    context.cf.skipPopUp2()


@then("Сайдбар меню, Support, Telegram")
def cliconbutton(context):
    context.cf.opensaidbar()
    context.cf.clickTechSupport()
    time.sleep(5)

@when("позвонить в Поддержку Telegram")
def calltoSupportViber(context):
    context.cf.calltosupportTg()
    time.sleep(8)


@then("Проверить в БД ивент sidebar_udsupport_tg")
def checkevents(context):
    time.sleep(20)
    actual_event_types = check_event(timestamp)
    expected_event_type = ("sidebar_udsupport_tg",)
    if expected_event_type not in actual_event_types:
        raise AssertionError(f'{expected_event_type} not in {actual_event_types}')
