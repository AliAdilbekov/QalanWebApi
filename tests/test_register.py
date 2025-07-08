# tests/test_register.py

import allure

@allure.title("Успешная регистрация пользователя")
def test_user_can_register(auth_client, valid_register_payload):
    with allure.step("Отправляем запрос на регистрацию"):
        response = auth_client.register(valid_register_payload["payload"])

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"

    with allure.step("Проверяем поля в ответе"):
        data = response.json()
        assert "token" in data, "В ответе нет токена"
        assert "user" in data, "В ответе нет данных пользователя"

        user = data["user"]
        expected = valid_register_payload["expected"]

        assert user["phoneNumber"] == expected["phone"]
        assert user["firstname"].lower() == expected["firstname"].lower()
        assert user["surname"].lower() == expected["surname"].lower()
