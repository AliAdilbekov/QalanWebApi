import requests
from config import BASE_URL, USE_CUSTOM_CERT, CERT_PATH

class PaymentClient:
    def __init__(self):
        self.base_url = BASE_URL

    def create_subscription(self, token, form_data, file_path):
        url = f"{self.base_url}/newPayments"
        headers = {
            "Authorization": f"Bearer {token}"
        }

        verify_cert = CERT_PATH if USE_CUSTOM_CERT else False

        with open(file_path, "rb") as f:
            files = {"checkAttachmentFile": f}
            response = requests.post(
                url,
                headers=headers,
                data=form_data,
                files=files,
                verify=verify_cert 
            )

        return response
