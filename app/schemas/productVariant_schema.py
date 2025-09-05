# app/schemas/product_schema.py
from pydantic import BaseModel

class VariantCreate(BaseModel):
    product_id: int
    size: str | None = None
    color: int
    stock: int
    price: float

class VariantResponse(VariantCreate):
    id: int

    class Config:
        orm_mode = True