from sqlalchemy import Column, Integer, ForeignKey, DateTime, TIMESTAMP, text
from sqlalchemy.sql import func
from app.db.database import Base

class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )
