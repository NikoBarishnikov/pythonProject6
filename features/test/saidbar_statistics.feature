Feature: Проверка ивента statistics_screen в Сайдбарменю

    Scenario: Страница авторизации,открытие Сайдбарменю,клик на Статистика

        Given Перед ввходом в Сайдбар,к Статистика
        Then клик на Статистика
        Then Проверить в БД ивент statistics_screen


