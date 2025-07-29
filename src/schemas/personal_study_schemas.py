from pydantic import BaseModel, Field
from typing import Optional, List


class ParentSchema(BaseModel):
    unreadMessagesQuantity: int
    lastMessageSentAt: str
    hasPhoneNumber: bool
    phoneNumber: str
    fullname: str


class PersonalStudyPupilSchema(BaseModel):
    userId: int
    id: int
    fullname: str
    phoneNumber: str
    subscriptionType: Optional[str]
    allSubscriptionTypes: List[str]

    isPaymentActive: bool
    paymentId: Optional[int]
    isNewPayment: bool
    isNewPaid: bool
    isMobileUser: bool
    isPersonalStudyFinished: bool
    personalStudyProgress: Optional[str]

    unreadMessagesQuantity: int
    lastMessageSentAt: Optional[str]
    parent: Optional[ParentSchema]

    isMentorSessionDiscontent: Optional[bool]
    isMentorSessionConsulting: Optional[bool]
    isMentorSessionReturn: Optional[bool]
    isMentorSessionTaskExplanation: Optional[bool]

    sessionId: Optional[str]
    sessionType: Optional[str]
    openedAt: Optional[str]
    senderType: Optional[str]

    isUntPupil: Optional[bool]
    isOldUntPupil: Optional[bool]
    isScienceAcademyPupil: Optional[bool]
    isB2BPupil: Optional[bool]

    country: Optional[str]
    language: Optional[str]
    label: Optional[str]

    importance: Optional[str]
    engagementSourceType: Optional[str]
    sourceType: Optional[str]
    returnReason: Optional[str]
    presence: Optional[int]

    isParent: Optional[bool]
    isParentMobile: Optional[bool]
    isParentProblem: Optional[bool]
    isPupilProblem: Optional[bool]
    isProblemPupil: Optional[bool]
    isCommentExist: Optional[bool]
    isSanSchoolAccountFreezed: Optional[bool]
    isSanSchoolTaskFinished: Optional[bool]
    isPassedDiagnostics: Optional[bool]
    isAccountFreezed: Optional[bool]

    actions: List = Field(default_factory=list)
