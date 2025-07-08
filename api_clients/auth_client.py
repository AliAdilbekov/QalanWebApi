from api_clients.base_api_client import BaseAPIClient

class AuthClient(BaseAPIClient):
    def register(self, payload):
        return self.post("/users/register", json=payload)
