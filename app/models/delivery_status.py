from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime, TIMESTAMP, text
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import ENUM as MySQLEnum
from app.db.database import Base

class DeliveryStatus(Base):
    __tablename__ = "delivery_status"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    current_status = Column(String(100))
    tracking_id = Column(String(100))
    courier_name = Column(String(100))
    
    updated_at = Column(
        TIMESTAMP,
        server_default=text("'0000-00-00 00:00:00'"),
        server_onupdate=text("CURRENT_TIMESTAMP")
    )
