import tkinter as tk
from tkinter import messagebox

# Имитация базы данных (словарь)
database = {
}

def create_record():
    try:
        record_id = int(entry_id.get())
        record_name = entry_name.get()
        database[record_id] = {"id": record_id, "name": record_name}
        messagebox.showinfo("Success", "Record created successfully.")
    except ValueError:
        messagebox.showerror("Error", "Invalid ID. Please enter a valid integer.")

def read_records():
    text_output.delete(1.0, tk.END)
    for record in database.values():
        text_output.insert(tk.END, f"ID: {record['id']}, Name: {record['name']}\n")

def update_record():
    try:
        update_id = int(entry_update_id.get())
        new_name = entry_new_name.get()
        if update_id in database:
            database[update_id]["name"] = new_name
            messagebox.showinfo("Success", "Record updated successfully.")
        else:
            messagebox.showerror("Error", "Record with the specified ID not found.")
    except ValueError:
        messagebox.showerror("Error", "Invalid ID. Please enter a valid integer.")

def delete_record():
    try:
        delete_id = int(entry_delete_id.get())
        if delete_id in database:
            del database[delete_id]
            messagebox.showinfo("Success", "Record deleted successfully.")
        else:
            messagebox.showerror("Error", "Record with the specified ID not found.")
    except ValueError:
        messagebox.showerror("Error", "Invalid ID. Please enter a valid integer.")

# Создаем графический интерфейс
root = tk.Tk()
root.title("CRUD App")

# Создаем элементы интерфейса
label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=5, pady=5)

label_name = tk.Label(root, text="Name:")
label_name.grid(row=1, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1, padx=5, pady=5)

button_create = tk.Button(root, text="Create", command=create_record)
button_create.grid(row=2, column=0, padx=5, pady=5)

button_read = tk.Button(root, text="Read", command=read_records)
button_read.grid(row=2, column=1, padx=5, pady=5)

label_update_id = tk.Label(root, text="ID:")
label_update_id.grid(row=3, column=0, padx=5, pady=5)
entry_update_id = tk.Entry(root)
entry_update_id.grid(row=3, column=1, padx=5, pady=5)

label_new_name = tk.Label(root, text="New Name:")
label_new_name.grid(row=4, column=0, padx=5, pady=5)
entry_new_name = tk.Entry(root)
entry_new_name.grid(row=4, column=1, padx=5, pady=5)

button_update = tk.Button(root, text="Update", command=update_record)
button_update.grid(row=5, column=0, padx=5, pady=5)

label_delete_id = tk.Label(root, text="ID:")
label_delete_id.grid(row=6, column=0, padx=5, pady=5)
entry_delete_id = tk.Entry(root)
entry_delete_id.grid(row=6, column=1, padx=5, pady=5)

button_delete = tk.Button(root, text="Delete", command=delete_record)
button_delete.grid(row=7, column=0, padx=5, pady=5)

text_output = tk.Text(root, width=30, height=10)
text_output.grid(row=7, column=1, padx=5, pady=5)

root.mainloop()
