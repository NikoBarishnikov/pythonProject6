# This is a Feature file

Feature: Проверка ивента remind_password_button на странице авторизации

    Scenario: Страница авторизации ,Забыли пароль

        Given Запуск приложения,переход к экрану авторизации
        When Клик на кнопку Забыли пароль?
        Then Проверить в БД ивент remind_password_button




