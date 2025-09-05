from app.schemas.product_schema import ProductCreate, ProductResponse, ProductFlatResponse
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import text
from app.db.database import get_db
from app.models.products_model import Product
from app.auth.jwt_handler import decode_token
from app.auth.jwt_bearer import JWTBearer
from fastapi import File, UploadFile, Form
from app.models.product_variants import ProductVariant

import shutil
import os
import uuid


router = APIRouter()

@router.post("/products", dependencies=[Depends(JWTBearer())])
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(JWTBearer())
):
    
    token_data = decode_token(credentials.credentials)
    
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product




# 1️⃣ /product_all - full nested list
@router.get("/product_all", response_model=list[ProductResponse], dependencies=[Depends(JWTBearer())])
def get_all_products(
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(JWTBearer())
):
    token_data = decode_token(credentials.credentials)

    products = (
        db.query(Product)
        .options(
            joinedload(Product.variants).joinedload(ProductVariant.images)
        )
        .all()
    )
    return products


@router.get("/products_flat")
def get_products_flat(db=Depends(get_db)):
    sql = text("""
        SELECT *
        FROM (
            SELECT 
                p.id AS product_id,
                p.name AS product_name,
                p.description,
                p.category_id,
                v.id AS variant_id,
                v.size,
                v.color,
                v.stock,
                v.price,
                i.id AS image_id,
                i.image_url,
                ROW_NUMBER() OVER (
                    PARTITION BY p.id
                    ORDER BY 
                        CASE WHEN i.is_main = TRUE THEN 1 ELSE 2 END,
                        v.id ASC,
                        i.id ASC
                ) AS rn
            FROM products p
            LEFT JOIN product_variants v ON p.id = v.product_id
            LEFT JOIN variant_images i ON v.id = i.variant_id
        ) ranked
        WHERE rn = 1;
    """)

    result = db.execute(sql).mappings().all()
    return [dict(row) for row in result]



# ---------- Get single product (all images) ----------
@router.get("/products/{product_id}", response_model=ProductResponse, dependencies=[Depends(JWTBearer())])
def get_product(
    product_id: int,
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(JWTBearer())
):
    token_data = decode_token(credentials.credentials)

    product = (
        db.query(Product)
        .options(
            joinedload(Product.variants).joinedload(ProductVariant.images)
        )
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product