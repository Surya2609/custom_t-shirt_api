from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://sql12797955:PXSPlB75N3@sql12.freesqldatabase.com:3306/sql12797955"



# DATABASE_URL = "mysql+mysqlconnector://root:Surya%4026@localhost:3306/tshirt_store"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()