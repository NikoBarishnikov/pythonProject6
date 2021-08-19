Feature: Проверка ивента driver_club_click в Сайдбарменю

    Scenario: Открыть Сайдбарменю,прокурутить до Driver Помощник,клик на кнопку Driver Помощник

        Given Перед ввходом в Сайдбар,к Driver Клуб
        When Прокрутить до кнопки Driver Клуб
        Then клик на кнопку Driver Клуб
        Then Проверить в БД ивент driver_club_click

