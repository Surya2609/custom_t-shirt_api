# models/customer.py
import uuid
from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.dialects.mysql import CHAR
from app.db.database import Base
from sqlalchemy import Integer
from sqlalchemy.sql import func 

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String(255), nullable=False)
    lastName = Column(String(255), nullable=True)
    mobile = Column(String(255), nullable=True)
    city = Column(String(255), nullable=True)
    shippingAddress = Column(String(255), nullable=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())