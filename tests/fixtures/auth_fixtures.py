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
