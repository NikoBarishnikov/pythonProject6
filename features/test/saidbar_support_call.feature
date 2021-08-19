Feature: Проверка ивент call_center_button в Сайдбарменю

    Scenario: Открыть Сайдбарменю,клик на SOS,клик на Support

        Given Перед входом в Сайдбар
        Then открыть Сайдбар меню
        When клик на Support
        Then Проверить в БД ивент call_center_button

