Feature: Проверка ивента sidebar_udsupport_viber в Сайдбарменю

    Scenario: Страница авторизации,открытие Сайдбарменю,клик на Support,Viber

        Given Запуск приложения для Сайдбар Viber
        Then Сайдбар меню, Support, Viber
        When позвонить в Поддержку Viber
        Then Проверить в БД ивент sidebar_udsupport_viber

