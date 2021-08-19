Feature: Проверка ивента sos_button в Сайдбарменю

    Scenario: Открыть Сайдбарменю,клик на SOS

        Given Перед ввходом в Сайдбар SOS
        Then открыть Сайдбар меню
        When Клик на SOS
        Then Проверить в БД ивент sos_button


