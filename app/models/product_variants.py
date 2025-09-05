from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.database import Base

class ProductVariant(Base):
    __tablename__ = "product_variants"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    size = Column(String(20))
    color = Column(String(30))
    stock = Column(Integer)
    price = Column(DECIMAL(10, 2), nullable=False)
    # variant_image_url = Column(Text)

    product = relationship("Product", backref="variants")
    images = relationship("VariantImage", back_populates="variant", cascade="all, delete")