from database.base_datos import BaseDatos
from model.modelo import User, Product
from os import system, name


class Controller:
    def __init__(self):
        self.bd = BaseDatos()
        self.inicio()

    def inicio(self):
        print("Api Online Shopping:")

    def add_new_user(self, username, password, name, last_name, email, avatar):
        user = User(username, password, name, last_name, email, avatar)
        return self.bd.add_new_user(user)
        
    def get_all_users(self):
        return self.bd.get_all_users()
    
    def add_new_product(self, product_id, name, description, quantity, price):
        product = Product(product_id, name, description, quantity, price)
        return self.bd.add_new_product(product)
        
    def get_all_products(self):
        return self.bd.get_all_products()

    def login(self, username, password):
        return self.bd.login(username, password)
    def get_user(self, username):
        return self.bd.get_user_by_username(username)
    def get_product(self, product_id):
        return self.bd.get_product(product_id)