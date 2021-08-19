Feature: Проверка ивента driver_helper_click в Сайдбарменю

    Scenario: Открыть Сайдбарменю,прокурутить до Driver Помощник,клик на кнопку Driver Помощник

        Given Перед ввходом в Сайдбар,к Driver Помощник
        When Прокрутить до кнопки Driver Помощник
        Then клик на кнопку Driver Помощник
        Then Проверить в БД ивент driver_helper_click

