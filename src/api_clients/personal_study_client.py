from src.api_clients.base_api_client import BaseAPIClient

class PersonalStudyClient(BaseAPIClient):
    def search_by_phone(self, token, phone_number):
        headers = {"Authorization": f"Bearer {token}"}
        params = {"searchText": phone_number}
        return self.get("/userActions/filteredBySearchText", params=params, headers=headers)

   
    def get_mentor_sessions(self, token):
        headers = {"Authorization": f"Bearer {token}"}
        return self.get("/userActions/mentorSessions", headers=headers)
