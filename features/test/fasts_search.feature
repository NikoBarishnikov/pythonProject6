# This is a Feature file

Feature: Проверка ивентов fast_search_tap,fast_search_disable,fast_search_enable при влючении/отключении Быстрго поиска

    Scenario: Запуск приложения и авторизация,включить/выклчить Быстрый поиск

        Given Запуск приложения и авторизация перед включением Быстрого поиска
        When Включить Быстрый поиск
        Then Выключить Быстрый поиск
        Then Проверить в БД ивент fast_search_tap,fast_search_disable,fast_search_enable




