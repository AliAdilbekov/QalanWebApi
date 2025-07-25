from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AddFreezingResponse(BaseModel):
    id: int
    date: str  
    userId: int
    userFullname: Optional[str]
    authorUserId: int
    authorFullname: Optional[str]
    createdAt: datetime
