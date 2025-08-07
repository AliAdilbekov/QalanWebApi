import requests
from config import BASE_URL, CERT_PATH, USE_CUSTOM_CERT

class BaseAPIClient:
    def __init__(self):
        self.base_url = BASE_URL

    def _get_verify(self):
        return CERT_PATH if USE_CUSTOM_CERT else False

    def get(self, path, **kwargs):
        url = self.base_url + path
        print(f"[DEBUG] GET {url}")
        if "params" in kwargs:
            print(f"[DEBUG] PARAMS: {kwargs['params']}")
        kwargs.setdefault("verify", self._get_verify())
        return requests.get(url, **kwargs)

    def post(self, path, **kwargs):
        url = self.base_url + path
        print(f"[DEBUG] POST {url}")
        if "json" in kwargs:
            print(f"[DEBUG] PAYLOAD: {kwargs['json']}")
        kwargs.setdefault("verify", self._get_verify())
        return requests.post(url, **kwargs)

    def patch(self, path, **kwargs):
        url = self.base_url + path
        print(f"[DEBUG] PATCH {url}")
        if "json" in kwargs:
            print(f"[DEBUG] PAYLOAD: {kwargs['json']}")
        kwargs.setdefault("verify", self._get_verify())
        return requests.patch(url, **kwargs)
