from pydantic import BaseModel

class VariantImageResponse(BaseModel):
    id: int
    variant_id: int
    image_url: str
    is_main: bool

    class Config:
        from_attributes = True  # ✅ to work with SQLAlchemy models