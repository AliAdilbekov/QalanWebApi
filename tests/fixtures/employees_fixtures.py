import pytest
from utils.data_generator import generate_firstname, generate_surname, generate_phone_number
from api_clients.employee_client import EmployeeClient

@pytest.fixture
def employee_payload_template():
    def _build(role="sbb_employee", department="kaz"):
        return {
            "firstname": generate_firstname(),
            "surname": generate_surname(),
            "phoneNumber": generate_phone_number(),
            "telegramId": "21332",
            "sipuniId": "123",
            "role": role,
            "department": department,
            "countryCode": "kz"
        }
    return _build

@pytest.fixture
def employee_client():
    return EmployeeClient()

@pytest.fixture
def employee_token():
    return get_employee_token()


@pytest.fixture
def mentor_payload_template():
    def _build(department="kaz", qualification=10):
        return {
            "firstname": generate_firstname().capitalize(),
            "surname": generate_surname().upper(),
            "phoneNumber": generate_phone_number(),
            "telegramUserId": "32",
            "qualification": qualification,
            "department": department,
            "country": "Kazakhstan",
            "countryCode": "kz"
        }
    return _build
 