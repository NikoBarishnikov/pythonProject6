Feature: Проверка ивента payment_card_screen в Сайдбарменю

    Scenario: Открыть Сайдбарменю,прокурутить до Driver Помощник,клик на кнопку Платёжная карта

        Given Перед ввходом в Сайдбар,к Платёжная карта
        When Прокрутить до кнопки Платёжная карта
        Then клик на кнопку Платёжная карта
        Then Проверить в БД ивент payment_card_screen
