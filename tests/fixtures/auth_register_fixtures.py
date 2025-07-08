import pytest
from api_clients.auth_client import AuthClient
from utils.data_generator import (
    generate_phone_number,
    generate_firstname,
    generate_surname,
)

@pytest.fixture
def auth_client():
    return AuthClient()

@pytest.fixture
def valid_register_payload():
    phone = generate_phone_number()
    firstname = generate_firstname()
    surname = generate_surname()
    password = "12345678"

    return {
        "payload": {
            "userType": "pupil",
            "surname": surname,
            "firstname": firstname,
            "gender": None,
            "phoneNumber": phone,
            "countryCode": "kz",
            "password": password,
            "repeatPassword": password
        },
        "expected": {
            "phone": phone,
            "firstname": firstname,
            "surname": surname
        }
    }

@pytest.fixture
def register_missing_digit_in_phone():
    return {
        "userType": "pupil",
        "surname": "test",
        "firstname": "test",
        "gender": None,
        "phoneNumber": "7708493931",  # 1 цифра отсутствует
        "countryCode": "kz",
        "password": "12345678",
        "repeatPassword": "12345678"
    }

@pytest.fixture
def register_existing_phone():
    return {
        "userType": "pupil",
        "surname": "test",
        "firstname": "test",
        "gender": None,
        "phoneNumber": "77084939312",  # должен быть уже зарегистрирован
        "countryCode": "kz",
        "password": "12345678",
        "repeatPassword": "12345678"
    }

@pytest.fixture
def register_empty_firstname():
    return {
        "userType": "pupil",
        "surname": "test",
        "firstname": "",
        "gender": None,
        "phoneNumber": "77084939312",
        "countryCode": "kz",
        "password": "12345678",
        "repeatPassword": "12345678"
    }

@pytest.fixture
def register_empty_surname():
    return {
        "userType": "pupil",
        "surname": "",
        "firstname": "test",
        "gender": None,
        "phoneNumber": "77084939312",
        "countryCode": "kz",
        "password": "12345678",
        "repeatPassword": "12345678"
    }
    
@pytest.fixture
def register_digit_surname():
    return {
        "userType": "pupil",
        "surname": "2323",
        "firstname": "testtttttt",
        "gender": None,
        "phoneNumber": "77994939312",
        "countryCode": "kz",
        "password": "12345678",
        "repeatPassword": "12345678"
}

@pytest.fixture
def register_digit_firstname():
    return {
        "userType": "pupil",
        "surname": "testt",
        "firstname": "321313",
        "gender": None,
        "phoneNumber": "77994939312",
        "countryCode": "kz",
        "password": "12345678",
        "repeatPassword": "12345678"
}

@pytest.fixture
def register_password_mismatch():
    return {
        "userType": "pupil",
        "surname": "test",
        "firstname": "testtttttt",
        "gender": None,
        "phoneNumber": "77084939312",
        "countryCode": "kz",
        "password": "1234567",
        "repeatPassword": "12345678"
}

@pytest.fixture
def register_password_length():
    return {
        "userType": "pupil",
        "surname": "test",
        "firstname": "testtttttt",
        "gender": None,
        "phoneNumber": "77084939312",
        "countryCode": "kz",
        "password": "1234",
        "repeatPassword": "1234"
}

@pytest.fixture
def register_empty_usertype():
    return {
        "userType": "",
        "surname": "test",
        "firstname": "testtttttt",
        "gender": None,
        "phoneNumber": "77084939312",
        "countryCode": "kz",
        "password": "12345678",
        "repeatPassword": "12345678"
}

@pytest.fixture
def valid_login_payload():
    return {
        "phoneNumber": "77083464227",
        "password": "12345678",
        "countryCode": "kz",
        "isParent": False
    }


