# This is a Feature file

Feature: Проверка ивента LoginScreenShown на странице авторизации

    Scenario: Страница авторизации ,клик Войти

        Given Запуск приложения
        When Клик на кнопку Войти
        Then Ввод код для перехода выбора энв
        Then Ввод урл стейджинга
        Then возврат на страницу авторизации
        Then Проверить в БД ивент LoginScreenShown



