# # models/customer.py
# import uuid
# from sqlalchemy import Column, String
# from sqlalchemy.dialects.mysql import CHAR
# from app.db.database import Base
# from sqlalchemy import Integer

# class Customer(Base):
#     __tablename__ = "customers"

#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     name = Column(String(100), nullable=False)
#     email = Column(String(100), unique=True, nullable=False)
#     address = Column(String(255), nullable=True)