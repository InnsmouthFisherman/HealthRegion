from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
import pandas as pd

def connect_to_database():
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    engine.connect()
    return engine

def load_table(path, table_name):
    df = pd.read_csv(path, encoding="Windows-1251", sep=';')
    df.to_sql(table_name, con=connect_to_database(), if_exists="replace", index=False)
    print(f"Таблица успешно загружена в базу данных как '{table_name}'")
