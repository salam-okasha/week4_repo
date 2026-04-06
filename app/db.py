from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:123456@localhost/training_db"

engine = create_engine(DATABASE_URL, echo=True)
