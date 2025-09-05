from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base


class VariantImage(Base):
    __tablename__ = "variant_images"

    id = Column(Integer, primary_key=True, index=True)
    variant_id = Column(Integer, ForeignKey("product_variants.id"), nullable=False)
    image_url = Column(Text, nullable=False)
    is_main = Column(Boolean, default=False)  # For default image in product list

    # Relationships
    variant = relationship("ProductVariant", back_populates="images")