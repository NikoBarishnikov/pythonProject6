# This is a Feature file

Feature: Проверка ивента open_efir при открытии Эфира на главном экране

    Scenario: Запуск приложения и авторизация,тап на Эфир

        Given Запуск приложения и авторизация перед открытием Эфира
        When Тап на Эфир
        Then Проверить в БД ивент open_efir





