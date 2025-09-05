# app/controllers/product_controller.py
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.category import Category
from ..models.user import User
from app.schemas.category_schema import CategoryCreate, CategoryResponse
from app.auth.jwt_handler import decode_token
from app.auth.jwt_bearer import JWTBearer
from fastapi.security import HTTPAuthorizationCredentials   
import os, uuid, shutil

router = APIRouter()

UPLOAD_DIR = "uploads/categories"
os.makedirs(UPLOAD_DIR, exist_ok=True)

from fastapi import Form

@router.post("/categories", response_model=CategoryResponse, dependencies=[Depends(JWTBearer())])
def create_category(
    name: str = Form(...),
    description: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(JWTBearer())
):
    token_data = decode_token(credentials.credentials)
    user_id = token_data.get("user_id")

    # Generate unique filename
    file_ext = file.filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    image_url = f"/static/variant_images/{unique_filename}"

    new_category = Category(
        name=name,
        description=description,
        image_url=image_url
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


@router.get("/categories", response_model=list[CategoryResponse], dependencies=[Depends(JWTBearer())])
def get_categories(
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(JWTBearer())
):
    token_data = decode_token(credentials.credentials)
    # user_id = token_data.get("user_id")

    return db.query(Category).all()