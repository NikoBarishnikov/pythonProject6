import datetime
import time

from appium.webdriver.common.touch_action import TouchAction
from behave import given, when, then

from Pages.PageObject import ContactForm
from utilites.Requesttobd import check_event

timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


@given("Запуск приложения ,экран Войти,Регистрация")
def classObjects(context):
    context.cf = ContactForm(context.driver)
    context.cf.clickContactFromDutton()
    context.cf.enterCod()
    context.cf.enterUrl()
    TouchAction(context.driver).press(x=696, y=628).move_to(x=693, y=179).release().perform()
    context.cf.enterUrlAnalytic()
    context.cf.submitButton()
    context.cf.clickBackButtonLoginPages()
    time.sleep(3)


@when("Клик на кнопку Регистрация")
def contactformPage(context):
    context.cf.clickonRegisterButton()
    time.sleep(10)


@then("Проверить в БД ивент register_click")
def checkevents(context):
    time.sleep(20)
    actual_event_types = check_event(timestamp)
    expected_event_type = ("register_click",)
    if expected_event_type not in actual_event_types:
        raise AssertionError(f'{expected_event_type} not in {actual_event_types}')
