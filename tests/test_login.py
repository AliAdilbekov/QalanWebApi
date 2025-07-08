import allure

@allure.title("Успешный логин пользователя")
def test_user_can_login(auth_client, valid_login_payload):
    with allure.step("Отправляем запрос на логин"):
        response = auth_client.login(valid_login_payload)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"

    with allure.step("Проверяем тело ответа"):
        data = response.json()
        assert "token" in data, "Нет токена"
        assert "user" in data, "Нет данных о пользователе"

        user = data["user"]
        assert user["surname"] == "ИСАКОВА", f"Ожидали фамилию 'ИСАКОВА', получили '{user['surname']}'"

    with allure.step("Успешный логин"):
        print(f"[LOGIN OK] {user['firstname']} {user['surname']} | {user['phoneNumber']}")
