Feature: Проверка ивента sidebar_udsupport_tg в Сайдбарменю

    Scenario: Страница авторизации,открытие Сайдбарменю,клик на Support,Telegram

        Given Запуск приложения,открыть Сайдбар,для Telegram
        Then Сайдбар меню, Support, Telegram
        When позвонить в Поддержку Telegram
        Then Проверить в БД ивент sidebar_udsupport_tg

