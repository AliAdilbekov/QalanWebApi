from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ChatMessageSchema(BaseModel):
    id: int
    text: str
    sentAt: datetime
    pupilId: int
    senderUserId: int
    senderFullname: str

    receiverUserId: Optional[int]
    templateName: Optional[str]
    whatsappStatus: Optional[str]
    whatsappMessageId: Optional[str]
    telegramFileId: Optional[str]
    caption: Optional[str]
    mlLogId: Optional[int]
    isUnread: Optional[bool]
    isDelivered: Optional[bool]
    isMlApproved: Optional[bool]
    isMlModeApproved: Optional[bool]
    type: Optional[str]
