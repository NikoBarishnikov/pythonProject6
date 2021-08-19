import datetime
import time

from appium.webdriver.common.touch_action import TouchAction
from behave import given, then, when

from Pages.PageObject import ContactForm
from utilites.Requesttobd import check_event

timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


@given("Запуск приложения и авторизация перед открытием страницы с Фильтрами")
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

@when("Тап на Фильтры")
def turnonfastsearch(context):
    context.cf.clickopenfiltrpage()
    time.sleep(5)





@then("Проверить в БД ивент open_filters_page")
def checkevents(context):
    time.sleep(20)
    actual_event_types = check_event(timestamp)
    expected_event_type = ("open_filters_page",)
    if expected_event_type not in actual_event_types:
        raise AssertionError(f'{expected_event_type} not in {actual_event_types}')
