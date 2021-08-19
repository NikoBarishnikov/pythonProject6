Feature: Проверка ивентов: traffic,current_location_button,fish_place,sectors

    Scenario: Авторизация в приложении,на главном экране тап на кнопки:трафик,сектор,рыбка,локтор

        Given Запуск приложения,переход на главный экран
        When Перетянуть карту для отображение кнопки Локатор
        Then клик на кнопку Сектор
        Then клик на кнопку Рыбка
        Then клик на кнопку Траффик
        Then клик на кнопку Локатор
        Then Проверить в БД ивент traffic,current_location_button,fish_place,sectors

