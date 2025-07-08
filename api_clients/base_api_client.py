import requests
from config import BASE_URL

class BaseAPIClient:
    def __init__(self):
        self.base_url = BASE_URL

    def post(self, path, **kwargs):
        url = f"{self.base_url}{path}"
        print(f"[DEBUG] URL: {url}")
        print(f"[DEBUG] PAYLOAD: {kwargs.get('json')}")
        return requests.post(url, **kwargs)
