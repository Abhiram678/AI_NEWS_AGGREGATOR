import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

def get_database_url() -> str:
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        return database_url
    
    # Use SQLite for local development
    db_path = os.getenv("SQLITE_DB_PATH", "ai_news_aggregator.db")
    return f"sqlite:///{db_path}"

engine = create_engine(get_database_url(), connect_args={"check_same_thread": False} if get_database_url().startswith("sqlite") else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    return SessionLocal()

