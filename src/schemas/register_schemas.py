from pydantic import BaseModel, constr
from typing import Optional, Dict


class RegisterPayload(BaseModel):
    userType: str
    surname: constr(min_length=1)
    firstname: constr(min_length=1)
    gender: Optional[str]
    phoneNumber: constr(pattern=re.compile(r"^\d{11}$"))  
    countryCode: str
    password: constr(min_length=8, max_length=15)
    repeatPassword: constr(min_length=8, max_length=15)


class UserData(BaseModel):
    id: int
    firstname: str
    surname: str
    phoneNumber: str


class RegisterResponse(BaseModel):
    token: str
    user: UserData
    exp: int


class ErrorResponse(BaseModel):
    error: Dict[str, str]
