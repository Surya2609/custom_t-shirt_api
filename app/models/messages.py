from sqlalchemy import Column, Integer, Text, String, Enum, ForeignKey, DateTime, TIMESTAMP, text
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import ENUM as MySQLEnum
from app.db.database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    message = Column(Text)
    type = Column(String(100))
    video_url = Column(Text)

    sent_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )
