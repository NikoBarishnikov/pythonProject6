Feature: Проверка ивента sidebar_udsupport_fb в Сайдбарменю

    Scenario: Страница авторизации,открытие Сайдбарменю,клик на Support,Messenger

        Given Запуск приложения,открыть Сайдбар,для Messenger
        Then Сайдбар меню, Support, Messenger
        When позвонить в Поддержку Messenger
        Then Проверить в БД ивент sidebar_udsupport_fb

