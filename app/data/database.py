from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Generate Database URL
DATABASE_URL = "sqlite:///./residencial.db"

# Create Database Engine
Engine = create_engine(DATABASE_URL, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)


def get_db_connection():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()
