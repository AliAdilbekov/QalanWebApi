import requests
from config import BASE_URL

DEFAULT_PUPIL_CODE = "100"
DEFAULT_PASSWORD = "12345678"

def get_token(pupil_code: str = DEFAULT_PUPIL_CODE, password: str = DEFAULT_PASSWORD) -> str:
    url = f"{BASE_URL}/users/login"
    payload = {
        "pupilCode": pupil_code,
        "password": password
    }

    print(f"[DEBUG] POST {url}")
    print(f"[DEBUG] PAYLOAD: {payload}")

    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"[AUTH ERROR] {response.status_code}: {response.text}"

    data = response.json()
    token = data.get("token")
    assert token, "[AUTH ERROR] Token not found in response"
    return token

def get_employee_token() -> str:
    url = f"{BASE_URL}/users/login"
    payload = {
        "phoneNumber": "77000000000",  
        "password": "12345678",
        "countryCode": "kz",
        "isParent": False
    }

    print(f"[DEBUG] POST {url}")
    print(f"[DEBUG] PAYLOAD: {payload}")

    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"[AUTH ERROR] {response.status_code}: {response.text}"

    data = response.json()
    token = data.get("token")
    assert token, "[AUTH ERROR] Token not found in response"
    return token

def get_mentor_token() -> str:
    url = f"{BASE_URL}/users/login"
    payload = {
        "phoneNumber": "77022738232",  
        "password": "87654321",
        "countryCode": "kz",
        "isParent": False
    }

    print(f"[DEBUG] POST {url}")
    print(f"[DEBUG] PAYLOAD: {payload}")

    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"[AUTH ERROR] {response.status_code}: {response.text}"

    data = response.json()
    token = data.get("token")
    assert token, "[AUTH ERROR] Token not found in response"
    return token
