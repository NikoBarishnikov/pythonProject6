Feature: Проверка ивента sidebar_udsupport_call в Сайдбарменю

    Scenario: Открыть Сайдбарменю,клик на SOS,клик на Support

        Given Перед ввходом в Сайдбар,Поддержка
        Then открыть Сайдбар,для звонка в поддержку
        When позвонить в поддержку
        Then Проверить в БД ивент sidebar_udsupport_call


