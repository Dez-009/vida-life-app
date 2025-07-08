from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import date
from decimal import Decimal

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class UserProfile(BaseModel):
    full_name: Optional[str] = None
    age: Optional[int] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    is_married: Optional[bool] = None
    annual_income: Optional[Decimal] = None
    number_of_children: Optional[int] = None
    sex: Optional[str] = None

class User(UserBase):
    id: int
    is_active: bool
    full_name: Optional[str] = None
    age: Optional[int] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    is_married: Optional[bool] = None
    annual_income: Optional[Decimal] = None
    number_of_children: Optional[int] = None
    sex: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: EmailStr
    password: str
