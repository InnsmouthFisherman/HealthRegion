import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

SUPPORTED_FORMATS = [
    ("Все поддерживаемые файлы", "*.csv *.xlsx *.xls *.json *.xml *.parquet *.tsv *.feather"),
    ("CSV файлы", "*.csv"),
    ("Excel файлы", "*.xlsx *.xls"),
    ("JSON файлы", "*.json"),
    ("XML файлы", "*.xml"),
    ("Parquet файлы", "*.parquet"),
    ("TSV файлы", "*.tsv"),
    ("Feather файлы", "*.feather"),
]

def load_table(file_path, table_name, db_url):
    ext = os.path.splitext(file_path)[1].lower()
    try:
        if ext == '.csv':
            df = pd.read_csv(file_path)
        elif ext in ['.xls', '.xlsx']:
            df = pd.read_excel(file_path)
        elif ext == '.json':
            df = pd.read_json(file_path)
        elif ext == '.xml':
            df = pd.read_xml(file_path)
        elif ext == '.parquet':
            df = pd.read_parquet(file_path)
        elif ext == '.tsv':
            df = pd.read_csv(file_path, sep='\t')
        elif ext == '.feather':
            df = pd.read_feather(file_path)
        else:
            raise ValueError(f"Формат файла {ext} не поддерживается.")
    except Exception as file_error:
        raise RuntimeError(f"Ошибка при чтении файла: {file_error}")

    try:
        engine = create_engine(db_url)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
    except SQLAlchemyError as db_error:
        raise RuntimeError(f"Ошибка при подключении к базе данных или записи: {db_error}")

class TableUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Приложение для загрузки таблицы")
        self.root.geometry("600x600")
        self.root.configure(bg="white")

        tk.Label(root, text="Приложение для загрузки таблицы",
                 font=("Arial", 20, "bold"), bg="white").pack(pady=10)

        self.table_name_entry = tk.Entry(root, font=("Arial", 14), width=30, justify='center')
        self.table_name_entry.insert(0, "Введите имя таблицы")
        self.table_name_entry.pack(pady=5)

        self.db_params = {}
        for label in ["Пользователь", "Пароль", "Хост", "Порт", "База данных"]:
            frame = tk.Frame(root, bg="white")
            frame.pack(pady=2)
            tk.Label(frame, text=label + ":", width=15, anchor='w', bg="white").pack(side="left")
            entry = tk.Entry(frame, font=("Arial", 12), width=30, show="*" if label == "Пароль" else "")
            entry.pack(side="left")
            self.db_params[label] = entry

        self.upload_button = tk.Button(root, text="Выбрать файл и загрузить",
                                       command=self.select_file, font=("Arial", 14),
                                       bg="#f0f0f0", relief="solid", borderwidth=1, padx=20, pady=10)
        self.upload_button.pack(pady=15)

        self.upload_label = tk.Label(root, text="", font=("Arial", 12), bg="white")
        self.upload_label.pack(pady=5)

    def build_db_url(self):
        try:
            user = self.db_params["Пользователь"].get().strip()
            password = self.db_params["Пароль"].get().strip()
            host = self.db_params["Хост"].get().strip()
            port = self.db_params["Порт"].get().strip()
            dbname = self.db_params["База данных"].get().strip()

            if not all([host, port, user, password, dbname]):
                raise ValueError("Все поля подключения должны быть заполнены.")

            return f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
        except Exception as e:
            messagebox.showerror("Ошибка подключения", str(e))
            return None

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=SUPPORTED_FORMATS)
        if not file_path:
            return

        table_name = self.table_name_entry.get().strip()
        db_url = self.build_db_url()

        if not db_url:
            return

        if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", table_name):
            messagebox.showerror("Ошибка", "Некорректное имя таблицы.")
            return

        try:
            load_table(file_path, table_name, db_url)
            self.upload_label.config(text=f"Загружен файл: {os.path.basename(file_path)}")
            messagebox.showinfo("Успех", f"Файл загружен в таблицу '{table_name}'")
        except RuntimeError as err:
            messagebox.showerror("Ошибка", str(err))
        except Exception as unexpected:
            messagebox.showerror("Неизвестная ошибка", f"Что-то пошло не так: {unexpected}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TableUploaderApp(root)
    root.mainloop()
