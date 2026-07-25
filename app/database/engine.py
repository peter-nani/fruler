from sqlmodel import create_engine

DATABASE_URL = "sqlite:///campus.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
)