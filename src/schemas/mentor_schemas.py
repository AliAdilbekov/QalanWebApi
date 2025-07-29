from pydantic import BaseModel
from typing import Dict

class MentorCreateResponseSchema(BaseModel):
    id: int
    teacherId: int
    userId: int
    firstname: str
    surname: str
    fullname: str
    phoneNumber: str
    telegramUserId: Dict[str, int] 
    qualification: int
    department: str
    country: str
