from sqlalchemy import Column, String, Integer, TIMESTAMP, text
from app.db.database import Base

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

    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at = Column(
        TIMESTAMP,
        server_default=text("'0000-00-00 00:00:00'"),
        server_onupdate=text("CURRENT_TIMESTAMP")
    )
