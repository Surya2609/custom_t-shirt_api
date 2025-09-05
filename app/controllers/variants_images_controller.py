from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.varients_image import VariantImage
from app.auth.jwt_bearer import JWTBearer
from app.auth.jwt_handler import decode_token
import os, uuid, shutil

router = APIRouter()

UPLOAD_DIR = "uploads/variant_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/variant_images")
def upload_variant_image(
    variant_id: int = Form(...),
    is_main: bool = Form(False),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    credentials=Depends(JWTBearer())
):
    # ✅ Decode token (optional, depends on your auth system)
    token_data = decode_token(credentials.credentials)

    # Generate unique filename
    file_ext = file.filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Store in DB
    image_url = f"/static/variant_images/{unique_filename}"  # if you serve via static files
    new_image = VariantImage(
        variant_id=variant_id,
        image_url=image_url,
        is_main=is_main
    )
    db.add(new_image)
    db.commit()
    db.refresh(new_image)

    return new_image


@router.delete("/variant_images/{image_id}")
def delete_variant_image(
    image_id: int,
    db: Session = Depends(get_db),
    credentials=Depends(JWTBearer())
):
    # ✅ Decode token
    token_data = decode_token(credentials.credentials)

    # Get image from DB
    image = db.query(VariantImage).filter(VariantImage.id == image_id).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")

    # Delete file from disk
    file_path = os.path.join("uploads/variant_images", os.path.basename(image.image_url))
    if os.path.exists(file_path):
        os.remove(file_path)

    # Delete DB record
    db.delete(image)
    db.commit()

    return {"message": "Image deleted successfully", "image_id": image_id}