import sys, os
base_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(base_dir + "/../..")

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
    pass

class MessageResponse(MessageBase):
    id: int
    user_email: str
    channel_name: str
    created_at: datetime

    class Config:
        from_attributes = True 