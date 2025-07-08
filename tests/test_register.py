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

        assert user["phoneNumber"] == expected["phone"], f"Ожидали {expected['phone']}, получили {user['phoneNumber']}"
        assert user["firstname"].lower() == expected["firstname"].lower(), f"Ожидали {expected['firstname']}, получили {user['firstname']}"
        assert user["surname"].lower() == expected["surname"].lower(), f"Ожидали {expected['surname']}, получили {user['surname']}"

    with allure.step("Успешная регистрация — финальное подтверждение"):
        success_message = (
            f"[SUCCESS] Ученик зарегистрирован: "
            f"{user['firstname']} {user['surname']} | Телефон: {user['phoneNumber']}"
        )
        print(success_message)
        allure.attach(
            success_message,
            name="Успешное сообщение",
            attachment_type=allure.attachment_type.TEXT
        )

@allure.title("Регистрация: Номер телефона без одной цифры")
def test_register_missing_digit(auth_client, register_missing_digit_in_phone):
    with allure.step("Отправляем запрос на регистрацию с некорректным номером"):
        response = auth_client.register(register_missing_digit_in_phone)

    with allure.step("Проверяем, что статус 400"):
        assert response.status_code == 400

    with allure.step("Проверяем текст ошибки"):
        error = response.json()["error"]
        assert error["rus"] == "Проверьте правильность номера телефона"

    with allure.step("Тест успешно отработал с ожидаемой ошибкой"):
        success_msg = f"[SUCCESS] Правильно получили ошибку: {error['rus']}"
        print(success_msg)
        allure.attach(success_msg, name="Сообщение об ошибке", attachment_type=allure.attachment_type.TEXT)


@allure.title("Регистрация: Пользователь с таким номером уже существует")
def test_register_existing_number(auth_client, register_existing_phone):
    with allure.step("Отправляем запрос на регистрацию с существующим номером"):
        response = auth_client.register(register_existing_phone)

    with allure.step("Проверяем, что статус 400"):
        assert response.status_code == 400

    with allure.step("Проверяем текст ошибки"):
        error = response.json()["error"]
        assert error["rus"] == "Есть пользователь по номеру телефона."

    with allure.step("Тест успешно отработал с ожидаемой ошибкой"):
        success_msg = f"[SUCCESS] Правильно получили ошибку: {error['rus']}"
        print(success_msg)
        allure.attach(success_msg, name="Сообщение об ошибке", attachment_type=allure.attachment_type.TEXT)


@allure.title("Регистрация: Пустое имя")
def test_register_empty_firstname(auth_client, register_empty_firstname):
    with allure.step("Отправляем запрос на регистрацию с пустым именем"):
        response = auth_client.register(register_empty_firstname)

    with allure.step("Проверяем, что статус 400"):
        assert response.status_code == 400

    with allure.step("Проверяем текст ошибки"):
        error = response.json()["error"]
        assert error["rus"] == "Имя не может быть пустым"

    with allure.step("Тест успешно отработал с ожидаемой ошибкой"):
        success_msg = f"[SUCCESS] Правильно получили ошибку: {error['rus']}"
        print(success_msg)
        allure.attach(success_msg, name="Сообщение об ошибке", attachment_type=allure.attachment_type.TEXT)


@allure.title("Регистрация: Пустая фамилия")
def test_register_empty_surname(auth_client, register_empty_surname):
    with allure.step("Отправляем запрос на регистрацию с пустой фамилией"):
        response = auth_client.register(register_empty_surname)

    with allure.step("Проверяем, что статус 400"):
        assert response.status_code == 400

    with allure.step("Проверяем текст ошибки"):
        error = response.json()["error"]
        assert error["rus"] == "Фамилия не может быть пустой"

    with allure.step("Тест успешно отработал с ожидаемой ошибкой"):
        success_msg = f"[SUCCESS] Правильно получили ошибку: {error['rus']}"
        print(success_msg)
        allure.attach(success_msg, name="Сообщение об ошибке", attachment_type=allure.attachment_type.TEXT)


@allure.title("Регистрация: Цифры в фамилии")
def test_register_digit_surname(auth_client, register_digit_surname):
    with allure.step("Отправляем запрос на регистрацию c цифрой в поле фамилия"):
        response = auth_client.register(register_digit_surname)

    with allure.step("Проверяем, что статус 400"):
        assert response.status_code == 400

    with allure.step("Проверяем текст ошибки"):
        error = response.json()["error"]
        assert error["rus"] == "Поле 'фамилия' должно содержать только буквы"

    with allure.step("Тест успешно отработал с ожидаемой ошибкой"):
        success_msg = f"[SUCCESS] Правильно получили ошибку: {error['rus']}"
        print(success_msg)
        allure.attach(success_msg, name="Сообщение об ошибке", attachment_type=allure.attachment_type.TEXT)

@allure.title ("Регистрация: Цифры в имени")
def test_register_digit_firstname(auth_client, register_digit_firstname):
    with allure.step("Отправляем запрос на регистрацию с цифрой в поле имя"):
        response = auth_client.register(register_digit_firstname)

    with allure.step("Проверяем, что статус 400"):
            assert response.status_code == 400

    with allure.step("Проверяем текст ошибки"):
        error = response.json()["error"]
        assert error["rus"] == "Поле 'имя' должно содержать только буквы"

    with allure.step("Тест успешно отработал с ожидаемой ошибкой"):
        success_msg = f"[SUCCESS] Правильно получили ошибку: {error['rus']}"
        print(success_msg)
        allure.attach(success_msg, name="Сообщение об ошибке", attachment_type=allure.attachment_type.TEXT)

        
@allure.title ("Регистрация: повторный пароль не совпадает")
def test_register_password_mismatch(auth_client, register_password_mismatch):
    with allure.step("Отправляем запрос на регистрацию с несовпадающими паролями"):
        response = auth_client.register(register_password_mismatch)

    with allure.step("Проверяем, что статус 400"):
        assert response.status_code == 400

    with allure.step("Проверяем текст ошибки"):
        error = response.json().get("error", {})
        assert error.get("rus") == "Повторный пароль не совпадает"

    with allure.step("Тест успешно отработал с ожидаемой ошибкой"):
        success_msg = f"[SUCCESS] Правильно получили ошибку: {error.get('rus')}"
        print(success_msg)
        allure.attach(success_msg, name="Сообщение об ошибке", attachment_type=allure.attachment_type.TEXT)


@allure.title("Регистрация: Пароль слишком короткий")
def test_register_password_length(auth_client, register_password_length):
    with allure.step("Отправляем запрос на регистрацию с некорректной длиной пароля"):
        response = auth_client.register(register_password_length)

    with allure.step("Проверяем, что статус 400"):
        assert response.status_code == 400

    with allure.step("Проверяем текст ошибки"):
        error = response.json().get("error", {})
        assert error.get("rus") == "Пароль должен быть длиной не менее 8 символов и не более 15 символов"

    with allure.step("Тест успешно отработал с ожидаемой ошибкой"):
        success_msg = f"[SUCCESS] Правильно получили ошибку: {error.get('rus')}"
        print(success_msg)
        allure.attach(success_msg, name="Сообщение об ошибке", attachment_type=allure.attachment_type.TEXT)


@allure.title("Регистрация: Не выбрана роль")
def test_register_empty_usertype(auth_client, register_empty_usertype):
    with allure.step("Отправляем запрос на регистрацию без выбора роли"):
        response = auth_client.register(register_empty_usertype)

    with allure.step("Проверяем, что статус 400"):
        assert response.status_code == 400

    with allure.step("Проверяем текст ошибки"):
        error = response.json().get("error", {})
        assert error.get("rus") == "Поле не может быть пустым"

    with allure.step("Тест успешно отработал с ожидаемой ошибкой"):
        success_msg = f"[SUCCESS] Правильно получили ошибку: {error.get('rus')}"
        print(success_msg)
        allure.attach(success_msg, name="Сообщение об ошибке", attachment_type=allure.attachment_type.TEXT)

    
    