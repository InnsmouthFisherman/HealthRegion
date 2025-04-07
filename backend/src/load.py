import tkinter as tk
from tkinter import filedialog, messagebox
import os

from database import load_table
from config import DATABASE_URL 

class TableUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Приложение для загрузки таблицы")
        self.root.geometry("600x350")
        self.root.configure(bg="white")

        self.title_label = tk.Label(
            root,
            text="Приложение для загрузки таблицы",
            font=("Arial", 20, "bold"),
            bg="white"
        )
        self.title_label.pack(pady=20)

        self.upload_frame = tk.Frame(
            root,
            bg="#f0f0f0",
            highlightbackground="gray",
            highlightthickness=2,
            width=400,
            height=60
        )
        self.upload_frame.pack(pady=10)
        self.upload_frame.pack_propagate(False)

        self.upload_label = tk.Label(
            self.upload_frame,
            text="Нажмите для загрузки CSV",
            font=("Arial", 14),
            bg="#f0f0f0"
        )
        self.upload_label.pack(expand=True)

        self.upload_frame.bind("<Button-1>", self.load_csv)
        self.upload_label.bind("<Button-1>", self.load_csv)

        self.db_label = tk.Label(
            root,
            text=f"База данных: {DATABASE_URL}",
            font=("Arial", 10),
            bg="white",
            fg="gray"
        )
        self.db_label.pack(pady=20)

    def load_csv(self, event=None):
        file_path = filedialog.askopenfilename(
            title="Выберите CSV файл",
            filetypes=[("CSV файлы", "*.csv")]
        )
        if not file_path:
            return

        try:
            #validate_table(file_path)  # если нужно
            load_table(file_path)

            filename = os.path.basename(file_path)
            self.upload_label.config(text=f"Загружен файл: {filename}")
            messagebox.showinfo("Успех", f"Файл '{filename}' успешно загружен в базу данных!")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при загрузке: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TableUploaderApp(root)
    root.mainloop()
