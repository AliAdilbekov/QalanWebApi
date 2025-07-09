import pytest
import datetime
from utils.data_generator import generate_firstname, generate_surname, generate_phone_number
from utils.get_token import get_token
from api_clients.pupil_client import PupilClient
from api_clients.payment_client import PaymentClient

@pytest.fixture
def admin_token():
    return get_token()

@pytest.fixture
def pupil_client():
    return PupilClient()

@pytest.fixture
def payment_client():
    return PaymentClient()

@pytest.fixture
def pupil_payload():
    phone = generate_phone_number()
    parent_phone = generate_phone_number()
    firstname = generate_firstname()
    surname = generate_surname()

    return {
        "payload": {
            "regionId": 18,
            "firstname": firstname,
            "surname": surname,
            "phoneNumber": phone,
            "parentPhoneNumber": parent_phone,
            "country": "Kazakhstan",
            "countryCode": "kz",
            "label": "6",
            "language": "kaz"
        },
        "expected": {
            "firstname": firstname,
            "surname": surname,
            "phone": phone
        }
    }

@pytest.fixture
def subscription_payload_template():
    def _build(user_id, pupil_phone):
        today = datetime.date.today()
        return {
            "sum": "179500",
            "phoneNumber": pupil_phone,
            "currency": "KZT",
            "bankAccount": "qalankz_halyq",
            "methodType": "halyq_bank",
            "managerId": "3",
            "paidAt": f"{today}T08:00:00.000Z",
            "audioRecordingLink": "https://my.binotel.ua/?module=history&subject=77751182011&sacte=ovl-link-pb-46",
            "isNeedAddSubscription": "true",
            "subscriptionType": "math_course",
            "courseType": "math_course",
            "location": "preprod.qalan.kz",
            "userId": str(user_id),
            "dateFrom": str(today),
            "dateTo": str(today.replace(year=today.year + 1)),
            "subscriptionSum": "179500",
            "managerSum": "10000",
            "isNeedInternalInstalment": "false",
            "engagementSourceType": "sarafan_instagram",
            "amocrmLink": "https://crm.qalan.kz/leads/526844e2-3501-4447-82a0-5bc9140f9d1a"
        }
    return _build
