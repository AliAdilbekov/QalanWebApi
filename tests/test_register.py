import requests
from requests.exceptions import RequestException
from utils.data_generator import (
    generate_phone_number,
    generate_firstname,
    generate_surname,
)
from config import BASE_URL


def test_register_user_success():
    phone = generate_phone_number()
    firstname = generate_firstname()
    surname = generate_surname()

    payload = {
        "userType": "pupil",
        "surname": surname,
        "firstname": firstname,
        "gender": None,
        "phoneNumber": phone,
        "countryCode": "kz",
        "password": "12345678",
        "repeatPassword": "12345678"
    }

    try:
        response = requests.post(BASE_URL, json=payload, timeout=10)
    except RequestException as e:
        raise AssertionError(f"[ERROR] Не удалось выполнить POST-запрос: {e}")

    assert response.status_code == 200, f"[ERROR] Ожидали статус 200, получили {response.status_code}, тело ответа: {response.text}"

    try:
        response_data = response.json()
    except ValueError:
        raise AssertionError(f"[ERROR] Ответ не является валидным JSON: {response.text}")

    assert "token" in response_data, "[ERROR] В ответе отсутствует 'token'"
    assert "user" in response_data, "[ERROR] В ответе отсутствует 'user'"

    user = response_data["user"]

    assert isinstance(user.get("id"), int), "[ERROR] ID пользователя должен быть целым числом"
    assert user.get("firstname").lower() == firstname.lower(), f"[ERROR] firstname mismatch: ожидали {firstname}, получили {user.get('firstname')}"
    assert user.get("surname").lower() == surname.lower(), f"[ERROR] surname mismatch: ожидали {surname}, получили {user.get('surname')}"
    assert user.get("phoneNumber") == phone, f"[ERROR] phone mismatch: ожидали {phone}, получили {user.get('phoneNumber')}"

    print(f"[SUCCESS] Зарегистрирован: {firstname} {surname}, телефон: {phone}")
