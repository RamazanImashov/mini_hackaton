import json
from jinja2 import Environment, FileSystemLoader

class Database:
    def __init__(self, filename):
        self.filename = filename
        self.prod_name = self._load_data()

    def _load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.prod_name, file, indent=2)
            
    def create(self, product):
        self.prod_name.append(product)
        self._save_data()

    def read(self, product_id=None):
        if product_id is None:
            return self.prod_name
        for product in self.prod_name:
            if product['id'] == product_id:
                return product
        return None

    def update(self, product_id, new_name):
        for product in self.prod_name:
            if product['id'] == product_id:
                product.update(new_name)
                self._save_data()
                return True
        return False

    def delete(self, product_id):
        for index, product in enumerate(self.prod_name):
            if product['id'] == product_id:
                del self.prod_name[index]
                self._save_data()
                return True
        return False


class Model:
    def __init__(self, data):
        self.prod_name = data

    def validate(self):
        return True

class View:
    @staticmethod
    def print_products(products):
        for product in products:
            print(product)

    @staticmethod
    def print_message(message):
        print(message)

class Controller:
    def __init__(self, db):
        self.db = db

    def create_product(self, name):
        model = Model(name)
        if model.validate():
            self.db.create(name)
            View.print_message("Запись успешно создана.")
        else:
            View.print_message("Ошибка валидации данных. Запись не создана.")
        
    def read_products(self, product_id=None):
        if product_id is not None:
            product = self.db.read(product_id)
            if product:
                View.print_products([product])
            else:
                View.print_message("Запись не найдена.")
        else:
            products = self.db.read()
            View.print_products(products)

    def update_product(self, product_id, new_name):
        if self.db.update(product_id, new_name):
            View.print_message("Запись успешно обновлена.")
        else:
            View.print_message("Запись не найдена. Обновление не выполнено.")

    def delete_product(self, product_id):
        if self.db.delete(product_id):
            View.print_message("Запись успешно удалена.")
        else:
            View.print_message("Запись не найдена. Удаление не выполнено.")

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


