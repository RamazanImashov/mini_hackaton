import json

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

class Create:
    def __init__(self, db):
        self.db = db

    def create_record(self, data):
        record_id = data.get('id')
        if record_id is None:
            View.print_message("Ошибка: запись не содержит поля 'id'. Запись не создана.")
            return
        
        if self.db.read(record_id):
            View.print_message(f"Ошибка: запись с id {record_id} уже существует. Запись не создана.")
            return

        model = Model(data)
        if model.validate():
            self.db.create(data)
            View.print_message("Запись успешно создана.")
        else:
            View.print_message("Ошибка валидации данных. Запись не создана.")

class Read:
    def __init__(self, db):
        self.db = db

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

class Update:
    def __init__(self, db):
        self.db = db

    def update_record(self, record_id, new_data):
        if self.db.update(record_id, new_data):
            View.print_message("Запись успешно обновлена.")
        else:
            View.print_message("Запись не найдена. Обновление не выполнено.")

class Delete:
    def __init__(self, db):
        self.db = db

    def delete_record(self, record_id):
        if self.db.delete(record_id):
            View.print_message("Запись успешно удалена.")
        else:
            View.print_message("Запись не найдена. Удаление не выполнено.")

db = Database("data.json")

create_action = Create(db)
read_action = Read(db)
update_action = Update(db)
delete_action = Delete(db)

data1 = {"id": 1, "name": "John", "age": 3}
data2 = {"id": 2, "name": "John", "age": 30}

create_action.create_record(data1)
create_action.create_record(data2)

read_action.read_records()

new_data = {'id': 1, "name": "John Doe", "age": 31}
update_action.update_record(2, new_data)

read_action.read_records()

# delete_action.delete_record(2)
