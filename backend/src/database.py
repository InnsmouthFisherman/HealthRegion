from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
import pandas as pd
import psycopg2

def connect_to_database():
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    engine.connect()
    print(engine)


def load_table(path):    

    df = pd.read_csv(path,  encoding='UTF8', sep=';')
    
    df.to_sql("test_table", con=connect_to_database(), if_exists="replace", index=False)

    print(f"Таблица 'test_table' успешно загружена в базу данных.")