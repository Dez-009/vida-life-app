from sqlalchemy import Column, Integer, String, Boolean, Date, Numeric
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    # Profile information
    full_name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    date_of_birth = Column(Date, nullable=True)
    address = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    is_married = Column(Boolean, nullable=True)
    annual_income = Column(Numeric(precision=10, scale=2), nullable=True)
    number_of_children = Column(Integer, nullable=True)
    sex = Column(String, nullable=True)
