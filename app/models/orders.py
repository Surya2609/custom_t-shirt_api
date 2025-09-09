from sqlalchemy import Column, Integer, ForeignKey, String, DECIMAL, DateTime, Enum, TIMESTAMP, text
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import ENUM as MySQLEnum
from app.db.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String(100))
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    payment_status = Column(MySQLEnum('paid', 'unpaid'), default='unpaid')
    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )

