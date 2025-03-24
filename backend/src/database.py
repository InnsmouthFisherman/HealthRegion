from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
import pandas as pd

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def load_table(path):    
    df = pd.read_csv(path)
    
    df.to_sql("test_table", con=engine, if_exists="replace", index=False)

    print(f"Таблица 'test_table' успешно загружена в базу данных.")