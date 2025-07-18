from api_clients.base_api_client import BaseAPIClient

class ChatClient(BaseAPIClient):
    def send_message(self, token: str, pupil_id: int, text: str):
        payload = {"pupilId": pupil_id, "text": text}
        headers = {"Authorization": f"Bearer {token}"}
        return self.post("/chatMessages", json=payload, headers=headers)

    def get_messages(self, token: str):
        headers = {"Authorization": f"Bearer {token}"}
        return self.get("/chatMessages", headers=headers)

    def get_last_messages_for_mentor(self, token: str, pupil_id: int):
        headers = {"Authorization": f"Bearer {token}"}
        params = {"pupilId": pupil_id, "withBotMessages": "false"}
        return self.get("/chatMessages/last", headers=headers, params=params)
