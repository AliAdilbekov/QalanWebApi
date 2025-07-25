from src.api_clients.base_api_client import BaseAPIClient

class EmployeeClient(BaseAPIClient):
    def create_employee(self, token, payload):
        headers = {"Authorization": f"Bearer {token}"}
        return self.post("/employees", json=payload, headers=headers)

    def create_mentor(self, token, payload):
        headers = {"Authorization": f"Bearer {token}"}
        return self.post("/mentors", json=payload, headers=headers)

    def get_employees(self, token, department="kaz"):
        headers = {"Authorization": f"Bearer {token}"}
        params = {"department": department}
        return self.get("/employees", params=params, headers=headers)



