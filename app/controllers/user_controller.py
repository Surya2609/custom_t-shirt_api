# app/controllers/user_controller.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..schemas.user_schema import UserCreateSchema, UserSchema, UserLoginSchema
from ..models.user import User
from ..auth.jwt_handler import create_access_token
from passlib.context import CryptContext
# from app.auth.jwt_handler import verify_password  # ✅ Add this

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@router.post("/register", response_model=UserSchema)
def register_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        firstName=user.firstName,
        lastName=user.lastName,
        mobile=user.mobile,
        city=user.city,
        shippingAddress=user.shippingAddress,
        email=user.email,
        password=get_password_hash(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(user: UserLoginSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token_data = {
        "sub": db_user.email,
        "user_id": db_user.id
    }

    access_token = create_access_token(token_data)

    return {
        "msg": "Login successful",
        "data": [
            {
                "id": db_user.id,
                "firstName": db_user.firstName,
                "lastName": db_user.lastName,
                "mobile": db_user.mobile,
                "city": db_user.city,
                "shippingAddress": db_user.shippingAddress,
                "email": db_user.email,
                "created_at": db_user.created_at,
                "updated_at": db_user.updated_at
            }
        ],
        "access_token": access_token,
        "token_type": "bearer"
    }