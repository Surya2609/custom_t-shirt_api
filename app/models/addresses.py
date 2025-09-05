from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from app.db.database import Base

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(100))
    address_line1 = Column(Text)
    address_line2 = Column(Text)
    city = Column(String(100))
    state = Column(String(100))
    pincode = Column(String(10))
    phone = Column(String(15))
    is_default = Column(Boolean, default=False)
