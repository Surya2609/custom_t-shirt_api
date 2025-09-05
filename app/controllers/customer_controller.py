# # app/controllers/customer_controller.py

# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.db.database import get_db
# from app.models.customer import Customer
# from app.schemas.customer_schema import CustomerSchema
# from app.utils.response_wrapper import api_response

# router = APIRouter()

# # @router.post("/customers")
# # def create_customer(customer: CustomerSchema, db: Session = Depends(get_db)):
# #     db_customer = Customer(**customer.dict())
# #     db.add(db_customer)
# #     db.commit()
# #     db.refresh(db_customer)
# #     return api_response(data=db_customer, message="Customer created")

# @router.get("/customers")
# def get_customers(db: Session = Depends(get_db)):
#     customers = db.query(Customer).all()
#     return api_response(data=customers) 

# # READ Single Customer
# @router.get("/customers/{customer_id}")
# def get_customer(customer_id: str, db: Session = Depends(get_db)):
#     customer = db.query(Customer).filter(Customer.id == customer_id).first()
#     if customer is None:
#         raise HTTPException(status_code=404, detail="Customer not found")
#     return api_response(data=customer, message="Customer retrieved successfully")

# @router.post("/customers")
# def create_or_update_customer(customer_data: CustomerSchema, db: Session = Depends(get_db)):
#     customer = db.query(Customer).filter(Customer.id == customer_data.id).first()

#     if customer:
#         # Update existing customer
#         for field, value in customer_data.dict(exclude_unset=True).items():
#             setattr(customer, field, value)
#         db.commit()
#         db.refresh(customer)
#         return api_response(data=customer, message="Customer updated successfully")
#     else:
#         # Create new customer
#         new_customer = Customer(**customer_data.dict())
#         db.add(new_customer)
#         db.commit()
#         db.refresh(new_customer)
#         return api_response(data=new_customer, message="Customer created successfully")
    
# # DELETE Customer
# @router.delete("/customers/{customer_id}")
# def delete_customer(customer_id: str, db: Session = Depends(get_db)):
#     customer = db.query(Customer).filter(Customer.id == customer_id).first()
#     if not customer:
#         raise HTTPException(status_code=404, detail="Customer not found")
    
#     db.delete(customer)
#     db.commit()
#     return api_response(message="Customer deleted successfully")