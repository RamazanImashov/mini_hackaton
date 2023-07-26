import json

import tkinter as tk
from tkinter import messagebox

class Database:
    def __init__(self, filename):
        self.filename = filename
        self.data = self._load_data()

    def _load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=2)
            
    def create(self, record):
        self.data.append(record)
        self._save_data()

    def read(self, record_id=None):
        if record_id is None:
            return self.data
        for record in self.data:
            if record['id'] == record_id:
                return record
        return None

    def update(self, record_id, new_data):
        for record in self.data:
            if record['id'] == record_id:
                record.update(new_data)
                self._save_data()
                return True
        return False

    def delete(self, record_id):
        for index, record in enumerate(self.data):
            if record['id'] == record_id:
                del self.data[index]
                self._save_data()
                return True
        return False


class Model:
    def __init__(self, data):
        self.data = data

    def validate(self):
        return True

class View:
    @staticmethod
    def print_records(records):
        for record in records:
            print(record)

    @staticmethod
    def print_message(message):
        print(message)

class Controller:
    def __init__(self, db):
        self.db = db

    def create_record(self, data):
        model = Model(data)
        if model.validate():
            self.db.create(data)
            View.print_message("Запись успешно создана.")
        else:
            View.print_message("Ошибка валидации данных. Запись не создана.")
            
        try:
            record_id = int(entry_id.get())
            record_name = entry_name.get()
            db[record_id] = {"id": record_id, "name": record_name}
            messagebox.showinfo("Success", "Record created successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid ID. Please enter a valid integer.")

    def read_records(self, record_id=None):
        if record_id is not None:
            record = self.db.read(record_id)
            if record:
                View.print_records([record])
            else:
                View.print_message("Запись не найдена.")
        else:
            records = self.db.read()
            View.print_records(records)

    def update_record(self, record_id, new_data):
        if self.db.update(record_id, new_data):
            View.print_message("Запись успешно обновлена.")
        else:
            View.print_message("Запись не найдена. Обновление не выполнено.")

    def delete_record(self, record_id):
        if self.db.delete(record_id):
            View.print_message("Запись успешно удалена.")
        else:
            View.print_message("Запись не найдена. Удаление не выполнено.")

db = Database("data.json")
controller = Controller(db)

# data1 = {"id": 1, "name": "John", "age": 3}
# data1 = {"id": 2, "name": "John", "age": 30}
# controller.create_record(data1)

#     # Просмотр всех записей
# controller.read_records()

#     # Обновление записи
# new_data = {"name": "John Doe", "age": 31}
# controller.update_record(1, new_data)

#     # Просмотр одной записи по идентификатору
# controller.read_records(1)

#     # Удаление записи
# controller.delete_record(2)

#     # Проверка, что запись удалена
# controller.read_records(1)

root = tk.Tk()
root.title("CRUD")

# Создаем элементы интерфейса
label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=5, pady=5)

label_name = tk.Label(root, text="Name:")
label_name.grid(row=1, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1, padx=5, pady=5)

button_create = tk.Button(root, text="Create", command=controller.create_record)
button_create.grid(row=2, column=0, padx=5, pady=5)

button_read = tk.Button(root, text="Read", command=controller.read_records)
button_read.grid(row=2, column=1, padx=5, pady=5)

label_update_id = tk.Label(root, text="ID:")
label_update_id.grid(row=3, column=0, padx=5, pady=5)
entry_update_id = tk.Entry(root)
entry_update_id.grid(row=3, column=1, padx=5, pady=5)

label_new_name = tk.Label(root, text="New Name:")
label_new_name.grid(row=4, column=0, padx=5, pady=5)
entry_new_name = tk.Entry(root)
entry_new_name.grid(row=4, column=1, padx=5, pady=5)

button_update = tk.Button(root, text="Update", command=controller.update_record)
button_update.grid(row=5, column=0, padx=5, pady=5)

label_delete_id = tk.Label(root, text="ID:")
label_delete_id.grid(row=6, column=0, padx=5, pady=5)
entry_delete_id = tk.Entry(root)
entry_delete_id.grid(row=6, column=1, padx=5, pady=5)

button_delete = tk.Button(root, text="Delete", command=controller.delete_record)
button_delete.grid(row=7, column=0, padx=5, pady=5)

text_output = tk.Text(root, width=30, height=10)
text_output.grid(row=7, column=1, padx=5, pady=5)

root.mainloop()




    # Создание записи

