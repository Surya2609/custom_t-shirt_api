from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ✅ New Clever-Cloud DB URL
DATABASE_URL = (
    "mysql+mysqlconnector://uafweadkhrfidg6l:egPFBXbQSHHHXUnZYzU1"
    "@bv7b5zx4lhfaorgyrwbv-mysql.services.clever-cloud.com:3306/bv7b5zx4lhfaorgyrwbv"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
