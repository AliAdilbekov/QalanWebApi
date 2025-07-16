from api_clients.base_api_client import BaseAPIClient

class PupilClient(BaseAPIClient):
    def create_pupil(self, token, payload):
        headers = {"Authorization": f"Bearer {token}"}
        return self.post("/pupils", json=payload, headers=headers)

    def add_freezing(self, token, freeze_date):
        headers = {"Authorization": f"Bearer {token}"}
        return self.post("/users/newFreezings/byPupil", json={"date": freeze_date}, headers=headers)
