import sys, os
base_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(base_dir + "/../..")

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[int] = None
    workspace_id: Optional[int] = None
    role_id: Optional[int] = None
    is_workspace_admin: Optional[bool] = None
    is_contractor: Optional[bool] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None

class EmailVerificationRequest(BaseModel):
    email: EmailStr

class EmailVerification(BaseModel):
    token: str 