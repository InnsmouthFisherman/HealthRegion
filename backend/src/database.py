import csv
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
import chardet

def connect_to_database():
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    engine.connect()
    return engine

def detect_encoding(path):
    with open(path, 'rb') as f:
        result = chardet.detect(f.read(10000))
        encoding = result['encoding']
        print(f"[Кодировка]: {encoding}")
        return encoding

def detect_delimiter(path, encoding):
    with open(path, 'r', encoding=encoding) as f:
        sample = f.read(2048)
        dialect = csv.Sniffer().sniff(sample)
        print(f"[Разделитель]: {dialect.delimiter}")
        return dialect.delimiter

def load_table(path):
    encoding = detect_encoding(path)
    delimiter = detect_delimiter(path, encoding)

    try:
        df = pd.read_csv(path, encoding=encoding, sep=delimiter, on_bad_lines='skip', quotechar='"')
    except Exception as e:
        print(f"[Ошибка парсинга]: {e}")
        raise e

    df.to_sql("test_table", con=connect_to_database(), if_exists="replace", index=False)

    print("Таблица успешно загружена.")
