# app/schemas/product_schema.py
from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str
    image_url: str
    description: str | None = None   

class CategoryResponse(CategoryCreate):
    id: int

    class Config:
        orm_mode = True
