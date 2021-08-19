import datetime
import time

from appium.webdriver.common.touch_action import TouchAction
from behave import given, then, when

from Pages.PageObject import ContactForm
from utilites.Requesttobd import check_event

timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


@given("Запуск приложения и авторизация перед включение/отключением необходимого фильтра")
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
    time.sleep(3)


@when("Тап на Фильтры на главном экране")
def turnonfastsearch(context):
    context.cf.clickopenfiltrpage()


@then("Тап на авто в одном из фильтров")
def autoonfilter(context):
    context.cf.clickfiltrautotake()
    time.sleep(5)


@then("Тап на Выключить все")
def switchallfilters(context):
    context.cf.clickswitchallfilters()
    time.sleep(5)


@then("Тап на Эфир")
def efironfilter(context):
    context.cf.clickefironfilter()
    time.sleep(5)


@then("Тап на Выключить")
def filteroff(context):
    context.cf.clickfilteroff()
    time.sleep(5)


@then("Проверить в БД ивенты autotake_on,efir_on,filter_off,switch_off_all_filter")
def checkevents(context):
    time.sleep(20)
    actual_event_types = check_event(timestamp)
    expected_event_types = [("autotake_on",), ("efir_on",), ("filter_off",), ("switch_off_all_filter",)]
    for expected_event_type in expected_event_types:
        if expected_event_type not in actual_event_types:
            raise AssertionError(f'{expected_event_type} not in {actual_event_types}')
