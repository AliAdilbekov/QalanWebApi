import allure
import pytest
from src.enums.global_enums import GlobalErrorMessages
from src.schemas.login_schemas import LoginSuccessResponse, LoginErrorResponse


@allure.title("Логин: Успешный логин пользователя")
def test_user_can_login(auth_client, valid_login_payload):
    with allure.step("Отправляем запрос на логин"):
        res = auth_client.login(valid_login_payload)
        print(f"[DEBUG] Login Status: {res.status_code}")
        print(f"[DEBUG] Login Body: {res.text}")

    with allure.step("Проверяем статус-код"):
        assert res.status_code == 200, f"Ожидали 200, получили {res.status_code}"

    with allure.step("Валидируем тело ответа через схему"):
        login_data = LoginSuccessResponse.model_validate_json(res.text)
        assert login_data.user.surname == "ИСАКОВА", \
            f"Ожидали фамилию 'ИСАКОВА', получили '{login_data.user.surname}'"

    with allure.step("✅ Успешный логин"):
        msg = f"[LOGIN OK] {login_data.user.firstname} {login_data.user.surname} | {login_data.user.phoneNumber}"
        print(msg)
        allure.attach(msg, name="Успешный логин", attachment_type=allure.attachment_type.TEXT)


@pytest.mark.parametrize("payload, expected_status, expected_error", [
    pytest.param(
        {"phoneNumber": "7708346422", "password": "12345678", "countryCode": "kz", "isParent": False},
        403,
        "Пользователь по данному номеру не найден",
        id="Логин: Пользователь не найден"
    ),
    pytest.param(
        {"phoneNumber": "77083464227", "password": "1234567", "countryCode": "kz", "isParent": False},
        403,
        "Неправильный пароль",
        id="Логин: Неправильный пароль"
    ),
    pytest.param(
        {"phoneNumber": "77083464227", "password": "", "countryCode": "kz", "isParent": False},
        400,
        "Вы должны ввести пароль",
        id="Логин: Пустой пароль"
    ),
    pytest.param(
        {"phoneNumber": "", "password": "123", "countryCode": "kz", "isParent": False},
        400,
        "Номер телефона должен содержать не менее 10 цифр",
        id="Логин: Пустой номер телефона"
    ),
])
def test_login_negative_cases(auth_client, payload, expected_status, expected_error):
    with allure.step("Отправляем запрос на логин"):
        res = auth_client.login(payload)
        print(f"[DEBUG] Login Status: {res.status_code}")
        print(f"[DEBUG] Login Body: {res.text}")

    with allure.step("Проверяем статус-код"):
        assert res.status_code == expected_status, f"Ожидали {expected_status}, получили {res.status_code}"

    with allure.step("Валидируем тело ошибки через схему"):
        error_data = LoginErrorResponse.model_validate_json(res.text)
        assert error_data.error.rus == expected_error, \
            f"Ожидали ошибку '{expected_error}', получили '{error_data.error.rus}'"

    with allure.step("✅ Тест негативного логина прошёл корректно"):
        msg = f"[SUCCESS] Получена ошибка: {error_data.error.rus}"
        print(msg)
        allure.attach(msg, name="Ошибка логина", attachment_type=allure.attachment_type.TEXT)
