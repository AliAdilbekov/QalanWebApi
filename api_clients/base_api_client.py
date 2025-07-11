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
    
    def get(self, path, **kwargs):
        url = self.base_url + path
        print(f"[DEBUG] GET {url}")
        if "params" in kwargs:
            print(f"[DEBUG] PARAMS: {kwargs['params']}")
        return requests.get(url, **kwargs)

    def post(self, path, **kwargs):
        url = self.base_url + path
        print(f"[DEBUG] POST {url}")
        if "json" in kwargs:
            print(f"[DEBUG] PAYLOAD: {kwargs['json']}")
        return requests.post(url, **kwargs)

    def patch(self, path, **kwargs):
        url = self.base_url + path
        print(f"[DEBUG] PATCH {url}")
        if "json" in kwargs:
            print(f"[DEBUG] PAYLOAD: {kwargs['json']}")
        return requests.patch(url, **kwargs)
