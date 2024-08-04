from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from core.config import settings
from typing import Generator

# Database URL from settings
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL is", SQLALCHEMY_DATABASE_URL)

# Create an engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

# Create a configured "Session" class
SESSIONLOCAL = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print("SESSIONLOCAL is a", type(SESSIONLOCAL))

# Function to get a database session
def get_db() -> Generator[Session, None, None]:
    db = SESSIONLOCAL()  # Actually create a new session
    print("db is a", type(db))  # Debug statement to check the type of db
    try:
        yield db
    finally:
        db.close()

