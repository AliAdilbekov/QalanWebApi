import requests
from config import BASE_URL

class PaymentClient:
    def __init__(self):
        self.base_url = BASE_URL

    def create_subscription(self, token, form_data, file_path):
        url = f"{self.base_url}/newPayments"
        headers = {
            "Authorization": f"Bearer {token}"
        }

        with open(file_path, "rb") as f:
            files = {"checkAttachmentFile": f}
            response = requests.post(url, headers=headers, data=form_data, files=files, verify=False)
        
        return response
