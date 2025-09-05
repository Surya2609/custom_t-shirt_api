from app.schemas.productVariant_schema import VariantCreate, VariantResponse
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.product_variants import ProductVariant
from app.auth.jwt_handler import decode_token
from app.auth.jwt_bearer import JWTBearer
from fastapi import File, UploadFile, Form
import shutil
import os
import uuid


router = APIRouter()

@router.post("/product_variant", dependencies=[Depends(JWTBearer())])
def create_product_variant(
    variant: VariantCreate,
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(JWTBearer())
):
    
    token_data = decode_token(credentials.credentials)
    
    new_variant = ProductVariant(**variant.dict())
    db.add(new_variant)
    db.commit()
    db.refresh(new_variant)
    return new_variant

@router.get("/product_variant", response_model=list[VariantResponse], dependencies=[Depends(JWTBearer())])
def get_products(
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(JWTBearer())
):
    token_data = decode_token(credentials.credentials)
    # user_id = token_data.get("user_id")

    return db.query(ProductVariant).all()
