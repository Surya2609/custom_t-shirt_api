from pydantic import BaseModel
from typing import List, Optional


# ---------------- Variant Image ----------------
class VariantImageResponse(BaseModel):
    id: int
    image_url: str
    is_main: bool

    class Config:
        orm_mode = True


# ---------------- Product Variant ----------------
class ProductVariantResponse(BaseModel):
    id: int
    size: Optional[str]
    color: Optional[str]
    stock: Optional[int]
    price: float
    images: List[VariantImageResponse] = []

    class Config:
        orm_mode = True


# ---------------- Product ----------------
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    category_id: int


class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    category_id: int
    variants: List[ProductVariantResponse] = []

    class Config:
        orm_mode = True


# For flat product list
class ProductFlatResponse(BaseModel):
    product_id: int
    name: str
    description: Optional[str]
    category_id: int
    variant_id: Optional[int]
    size: Optional[str]
    color: Optional[str]
    stock: Optional[int]
    price: Optional[float]
    image_url: Optional[str]

    class Config:
        orm_mode = True