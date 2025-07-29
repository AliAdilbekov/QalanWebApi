from pydantic import BaseModel

class EmployeeCreateResponseSchema(BaseModel):
    id: int
    firstname: str
    surname: str
    phoneNumber: str
    telegramId: int
    sipuniId: str
    role: str
    department: str
