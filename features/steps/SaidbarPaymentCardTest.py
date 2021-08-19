import datetime
import time

from appium.webdriver.common.touch_action import TouchAction
from behave import given, then, when


from Pages.PageObject import ContactForm
from utilites.Requesttobd import check_event

timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

@given("Перед ввходом в Сайдбар,к Платёжная карта")
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
    context.cf.opensaidbar()


@when("Прокрутить до кнопки Платёжная карта")
def touchaction(context):
    time.sleep(3)
    TouchAction(context.driver).press(x=550, y=706).move_to(x=549, y=462).release().perform()


@then("клик на кнопку Платёжная карта")
def cliconbutton(context):
    context.cf.clickonpaymentcard()
    time.sleep(8)


@then("Проверить в БД ивент payment_card_screen")
def checkevents(context):
    time.sleep(20)
    actual_event_types = check_event(timestamp)
    expected_event_type = ("payment_card_screen",)
    if expected_event_type not in actual_event_types:
        raise AssertionError(f'{expected_event_type} not in {actual_event_types}')



