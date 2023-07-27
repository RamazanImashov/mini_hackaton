import json

class Database:
    # Инициализирует файл для записи и прочитки
    def __init__(self, filename):
        self.filename = filename
        self.prod_name = self._load_data()
        
    # открыте, прочитка и подготова к записи
    def _load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    # запись
    def _save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.prod_name, file, indent=2)
            
    # дабавление
    def create(self, product):
        self.prod_name.append(product)
        self._save_data()

    # прочитка
    def read(self, product_id=None):
        if product_id is None:
            return self.prod_name
        for product in self.prod_name:
            if product['id'] == product_id:
                return product
        return None

    # обновление
    def update(self, product_id, new_name):
        for product in self.prod_name:
            if product['id'] == product_id:
                product.update(new_name)
                self._save_data()
                return True
        return False

    # удаление
    def delete(self, product_id):
        for index, product in enumerate(self.prod_name):
            if product['id'] == product_id:
                del self.prod_name[index]
                self._save_data()
                return True
        return False

# Инициализация объекта модели.
class Model:
    def __init__(self, data):
        self.prod_name = data

    def validate(self):
        return True

# Методы для отображения информации пользователю, например, печать списка записей или простых сообщений.
class View:
    @staticmethod
    def print_products(products):
        for product in products:
            print(product)

    @staticmethod
    def print_message(message):
        print(message)

# выполнение всех данных
class Controller:
    # инициализация данных
    def __init__(self, db):
        self.db = db
        
    # запись
    def create_product(self, name):
        model = Model(name)
        if model.validate():
            self.db.create(name)
            return print("Запись успешно создана.")
        else:
            return print("Ошибка валидации данных. Запись не создана.")
        
    # показ всех данных
    def read_products(self, product_id=None):
        if product_id is not None:
            product = self.db.read(product_id)
            if product:
                return print([product])
            else:
                return print("Запись не найдена.")
        else:
            products = self.db.read()
            return print(products)

    # изменение данных
    def update_product(self, product_id, new_name):
        if self.db.update(product_id, new_name):
            return print("Запись успешно обновлена.")
        else:
            return print("Запись не найдена. Обновление не выполнено.")

    # удаление данных
    def delete_product(self, product_id):
        if self.db.delete(product_id):
            return print("Запись успешно удалена.")
        else:
            return print("Запись не найдена. Удаление не выполнено.")

db = Database("data.json")
controller = Controller(db)

data1 = {"id": 1, "name": "John"}
# data1 = {"id": 2, "name": "John", "age": 30}
controller.create_product(data1)

# controller.read_products()


# new_name = {'id': 2 ,"name": "John Doe", "age": 31}
# controller.update_product(2, new_name)


# controller.delete_product(2)
# controller.delete_product(1)
controller.read_products()


