# This is a Feature file

Feature: Проверка ивента register_click

    Scenario: Экран Войти,Регистрация,клик на кнопку Регистрация

        Given Запуск приложения ,экран Войти,Регистрация
        When Клик на кнопку Регистрация
        Then Проверить в БД ивент register_click




