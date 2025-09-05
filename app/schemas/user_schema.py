from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class UserCreateSchema(BaseModel):
    firstName: str
    lastName: str
    mobile: str
    city: str
    shippingAddress: str
    email: EmailStr
    password: str

class UserSchema(BaseModel):
    id: int
    firstName: str
    lastName: str
    mobile: str
    city: str
    shippingAddress: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:   
        orm_mode = True
