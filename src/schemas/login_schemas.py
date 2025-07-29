from pydantic import BaseModel, Field
from typing import Optional, Dict, Union


class LoginUserEmployee(BaseModel):
    isHeadOfDepartment: Optional[bool]
    isDeleted: Optional[bool]
    department: Optional[Union[str, None]]
    role: Optional[Union[str, None]]


class LoginUserMentor(BaseModel):
    mentorId: Optional[Union[int, None]]
    qualification: Optional[Union[str, None]]


class LoginUserHunter(BaseModel):
    hunterId: Optional[Union[int, None]]
    sipuniId: Optional[Union[str, None]]


class LoginUserTeacher(BaseModel):
    isB2BTeacher: Optional[Union[bool, None]]
    isB2BAdmin: Optional[bool]
    canOpenSolution: Optional[bool]
    institution: Optional[Union[str, None]]
    code: Optional[Union[str, None]]


class LoginUserPupil(BaseModel):
    isUntSubscribed: Optional[bool]
    hasTeacher: Optional[bool]
    parentFirstname: Optional[Union[str, None]]
    parentPhoneNumber: Optional[Union[str, None]]
    institution: Optional[Union[str, None]]
    language: Optional[str]
    country: Optional[str]
    class_: Optional[Union[str, None]] = Field(alias="class")
    parent: Optional[Union[str, None]]
    label: Optional[str]
    id: int


class LoginUser(BaseModel):
    isUntTester: bool
    isScienceAcademyPupil: bool
    isSarafanEditor: bool
    isSanSchoolClient: bool
    isLeadDivider: bool
    isFarmerLeadDivider: bool
    isDemoClient: bool
    isB2BClient: bool
    isAcceptedTerms: bool
    isAbleToPayout: bool
    contentEmployeePermissions: Dict = Field(default_factory=dict)
    isTeacher: bool
    isMobileUser: bool
    telegramUserId: Optional[Union[int, None]]
    isParent: bool
    employee: LoginUserEmployee
    mentor: LoginUserMentor
    hunter: LoginUserHunter
    teacher: LoginUserTeacher
    pupil: LoginUserPupil
    phoneNumber: str
    surname: str
    firstname: str
    manager: Optional[Union[str, None]]
    id: int


class LoginSuccessResponse(BaseModel):
    token: str
    user: LoginUser
    exp: Optional[int]  # можно опустить, если не всегда приходит

class ErrorMessage(BaseModel):
    with_audio_player: bool
    aze: str
    kgz: str
    uzb: str
    eng: str
    rus: str
    kaz: str
    arsa: str
    areg: str
    module_name: str


class LoginErrorResponse(BaseModel):
    error: ErrorMessage