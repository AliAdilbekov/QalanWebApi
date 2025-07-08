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


@allure.title("Логин: Пользователь не найден по номеру")
def test_login_user_not_found(auth_client, invalid_login_user_not_found):
    with allure.step("Отправляем запрос на логин с несуществующим номером"):
        response = auth_client.login(invalid_login_user_not_found)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 403, f"Ожидали 403, получили {response.status_code}"

    with allure.step("Проверяем текст ошибки"):
        error = response.json()["error"]
        assert error["rus"] == "Пользователь по данному номеру не найден"

    with allure.step("Тест успешно отработал с ожидаемой ошибкой"):
        success_msg = f"[SUCCESS] Получена корректная ошибка: {error['rus']}"
        print(success_msg)
        allure.attach(success_msg, name="Ошибка логина", attachment_type=allure.attachment_type.TEXT)


@allure.title("Логин: Неправильный пароль")
def test_login_invalid_password(auth_client, login_invalid_password):
    with allure.step("Отправляем запрос с неправильным паролем"):
        response = auth_client.login(login_invalid_password)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 403, f"Ожидали 403, получили {response.status_code}"

    with allure.step("Проверяем текст ошибки"):
        error = response.json()["error"]
        assert error["rus"] == "Неправильный пароль"

    with allure.step("Тест успешно отработал"):
        msg = f"[SUCCESS] Получена ошибка: {error['rus']}"
        print(msg)
        allure.attach(msg, name="Ошибка логина", attachment_type=allure.attachment_type.TEXT)


@allure.title("Логин: Пустой пароль")
def test_login_empty_password(auth_client, login_empty_password):
    with allure.step("Отправляем запрос с пустым паролем"):
        response = auth_client.login(login_empty_password)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 400, f"Ожидали 400, получили {response.status_code}"

    with allure.step("Проверяем текст ошибки"):
        error = response.json()["error"]
        assert error["rus"] == "Вы должны ввести пароль"

    with allure.step("Тест успешно отработал"):
        msg = f"[SUCCESS] Получена ошибка: {error['rus']}"
        print(msg)
        allure.attach(msg, name="Ошибка логина", attachment_type=allure.attachment_type.TEXT)


@allure.title("Логин: Пустой номер телефона")
def test_login_empty_phone(auth_client, login_empty_phone):
    with allure.step("Отправляем запрос с пустым номером телефона"):
        response = auth_client.login(login_empty_phone)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 400, f"Ожидали 400, получили {response.status_code}"

    with allure.step("Проверяем текст ошибки"):
        error = response.json()["error"]
        assert error["rus"] == "Номер телефона должен содержать не менее 10 цифр"

    with allure.step("Тест успешно отработал"):
        msg = f"[SUCCESS] Получена ошибка: {error['rus']}"
        print(msg)
        allure.attach(msg, name="Ошибка логина", attachment_type=allure.attachment_type.TEXT)

