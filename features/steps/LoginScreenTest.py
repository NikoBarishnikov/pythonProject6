import datetime
import time

from appium.webdriver.common.touch_action import TouchAction
from behave import given, when, then

timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

from Pages.PageObject import ContactForm
from utilites.Requesttobd import check_event


@given("Запуск приложения")
def classObjects(context):
    context.cf = ContactForm(context.driver)


@when("Клик на кнопку Войти")
def contactformPage(context):
    context.cf.clickContactFromDutton()


@then("Ввод код для перехода выбора энв")
def verifyContactForm(context):
    context.cf.enterCod()


@then("Ввод урл стейджинга")
def enterDataInForm(context):
    context.cf.enterUrl()
    TouchAction(context.driver).press(x=696, y=628).move_to(x=693, y=179).release().perform()
    context.cf.enterUrlAnalytic()


@then("возврат на страницу авторизации")
def cliconbutton(context):
    context.cf.submitButton()
    time.sleep(5)


@then("Проверить в БД ивент LoginScreenShown")
def checkevents(context):
    time.sleep(20)
    actual_event_types = check_event(timestamp)
    expected_event_type = ("LoginScreenShown",)
    if expected_event_type not in actual_event_types:
        raise AssertionError(f'{expected_event_type} not in {actual_event_types}')
