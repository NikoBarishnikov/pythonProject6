# This is a Feature file

Feature: Проверка ивентов autotake_on,efir_on,filter_off,switch_off_all_filter на странице Фильтров

    Scenario: Запуск приложения,авторизация,перейти на страницу Фильтров,вкл/выключить необходимый фильтр,выключить все фильтры

        Given Запуск приложения и авторизация перед включение/отключением необходимого фильтра
        When Тап на Фильтры на главном экране
        Then Тап на авто в одном из фильтров
        Then Тап на Выключить все
        Then Тап на Эфир
        Then Тап на Выключить
        Then Проверить в БД ивенты autotake_on,efir_on,filter_off,switch_off_all_filter





