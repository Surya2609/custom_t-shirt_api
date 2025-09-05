from fastapi import FastAPI
# from .controllers.customer_controller import router as customer_router
from .controllers.products_controller import router as product_router
from .controllers.productVariant_controller import router as product_variant_router
from .controllers.variants_images_controller import router as variant_image_router

from .controllers.categories_controller import router as category_router
from .controllers.user_controller import router as user_router
from fastapi.middleware.cors import CORSMiddleware
from .db.database import Base, engine

from .models.user import User
# from .models.customer import Customer  # Import all your models here
from .models.category import Category
from .models.products_model import Product
from .models.product_variants import ProductVariant
from .models.carts import Cart
from .models.cart_items import CartItem
from .models.orders import Order
from .models.order_items import OrderItem
from .models.addresses import Address
from .models.payments import Payment
from .models.delivery_status import DeliveryStatus
from .models.messages import Message
from fastapi.staticfiles import StaticFiles
import os


import app.models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create folder if not exists
os.makedirs("uploads/categories", exist_ok=True)

# Mount /static/variant_images to point to uploads/categories
app.mount(
    "/static/variant_images",
    StaticFiles(directory="uploads/categories"),
    name="variant_images"
)

# ✅ Mount static folder (for uploaded images)
os.makedirs("uploads", exist_ok=True)
app.mount("/static", StaticFiles(directory="uploads"), name="static")
# os.makedirs("uploads/categories", exist_ok=True)
# app.mount("/static/variant_images", StaticFiles(directory="uploads/categories"), name="category_images")

app.include_router(product_router, prefix="/api", tags=["Products"])
app.include_router(product_variant_router, prefix="/api", tags=["Product Variants"])
app.include_router(category_router, prefix="/api", tags=["Categories"])
app.include_router(user_router, prefix="/api", tags=["Users"])
app.include_router(variant_image_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI CRUD API"}

@app.get("/ren")
def root():
    return {"message": "Hello from Render!"}

# ✅ Now SQLAlchemy knows all models — tables will be created
Base.metadata.create_all(bind=engine)