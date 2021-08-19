import datetime
import time

from appium.webdriver.common.touch_action import TouchAction
from behave import given, then, when

from Pages.PageObject import ContactForm
from utilites.Requesttobd import check_event

timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


@given("Запуск приложения,переход на главный экран")
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


@when("Перетянуть карту для отображение кнопки Локатор")
def touchaction(context):
    time.sleep(3)
    TouchAction(context.driver).press(x=141, y=380).move_to(x=576, y=386).release().perform()


@then("клик на кнопку Сектор")
def cliconbuttsector(context):
    context.cf.clickonsectorsButton()
    time.sleep(5)


@then("клик на кнопку Рыбка")
def cliconbuttonfish(context):
    context.cf.clickonfishingButton()
    time.sleep(5)


@then("клик на кнопку Траффик")
def cliconbuttontraffic(context):
    context.cf.clickontrafficButton()
    time.sleep(5)


@then("клик на кнопку Локатор")
def cliconbuttonlocator(context):
    context.cf.clickonlocationButton()
    time.sleep(5)


@then("Проверить в БД ивент traffic,current_location_button,fish_place,sectors")
def checkevents(context):
    time.sleep(20)
    actual_event_types = check_event(timestamp)
    expected_event_types = [("traffic",), ("current_location_button",), ("fish_place",), ("sectors",)]
    for expected_event_type in expected_event_types:
        if expected_event_type not in actual_event_types:
            raise AssertionError(f'{expected_event_type} not in {actual_event_types}')
