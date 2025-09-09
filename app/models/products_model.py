# # app/models/product.py
# from sqlalchemy import Column, Integer, String, Float, ForeignKey
# from app.db.database import Base

# class Product(Base):
#     __tablename__ = "products"

#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     name = Column(String(255), nullable=False)
#     description = Column(String(255), nullable=True)
#     price = Column(Float, nullable=False)
#     # quantity = Column(Integer, nullable=False)
#     # user_id = Column(Integer, ForeignKey("users.id"))  # ✅ Link product to user


from sqlalchemy import Column, Integer, String, Text, DECIMAL, ForeignKey, DateTime, text, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    
    # price = Column(DECIMAL(10, 2), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    # stock = Column(Integer, default=0)
    
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))

    category = relationship("Category", back_populates="products")
