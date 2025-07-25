import pytest
from src.api_clients.auth_client import AuthClient
from src.utils.data_generator import (
    generate_phone_number,
    generate_firstname,
    generate_surname,
)

@pytest.fixture
def auth_client():
    return AuthClient()

@pytest.fixture
def valid_login_payload():
    return {
        "phoneNumber": "77083464227",
        "password": "12345678",
        "countryCode": "kz",
        "isParent": False
    }

@pytest.fixture
def invalid_login_user_not_found():
    return {
        "phoneNumber": "7708346422", 
        "password": "12345678",
        "countryCode": "kz",
        "isParent": False
    }

@pytest.fixture
def login_invalid_password():
    return {
        "phoneNumber": "77083464227",  
        "password": "1234567",         
        "countryCode": "kz",
        "isParent": False
    }

@pytest.fixture
def login_empty_password():
    return {
        "phoneNumber": "77083464227",
        "password": "",                
        "countryCode": "kz",
        "isParent": False
    }

@pytest.fixture
def login_empty_phone():
    return {
        "phoneNumber": "",           
        "password": "123",
        "countryCode": "kz",
        "isParent": False
    }
