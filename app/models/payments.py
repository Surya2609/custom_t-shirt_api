from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import ENUM as MySQLEnum
from app.db.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    method = Column(String(50))
    transaction_id = Column(String(100))
    amount = Column(DECIMAL(10, 2), nullable=False)
    status = Column(String(100))
    payment_date = Column(DateTime(timezone=True), server_default=func.now())