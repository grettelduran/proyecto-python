import json
from model.modelo import User, Product
from os import system, name
import re 
  
email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

class BaseDatos:
    def load_existing_users(self):
        with open('existing_users.json') as json_file:
            data = json.load(json_file)
            existing_users = []
            for value in data:
                user = User(
                value.get("username"),
                value.get("password"),
                value.get("name"),
                value.get("last_name"),
                value.get("email"),
                value.get("cart_id"))
                existing_users.append(user)
            return existing_users
    def load_existing_products(self):
        with open('existing_products.json') as json_file:
            data = json.load(json_file)
            existing_products = []
            for value in data:
                product = Product(
                value.get("id"),
                value.get("name"),
                value.get("description"),
                value.get("quantity"),
                value.get("price"))
                existing_products.append(product)
            return existing_products
    def pass_user_validations(self, obj_user):
        for player in self.existing_users:
            #valido si el usuario o el email es repetido
            if player.username == obj_user.username or player.email == obj_user.email:
                print("User or Email already exists")
                return False
        #valido si el email tiene el formato correcto con regex
        if re.search(email_regex,obj_user.email):  
            if re.search(r"\s", obj_user.username):
                print("username shouldn't have spaces")
                #TODO missing validation for password
                return False
            else:
                return True
        else:
            print("Invalid email")
            return False  
    def add_new_user(self, obj_user):
        if self.pass_user_validations(obj_user):
            self.existing_users.append(obj_user)
            users_json = []
            for user in self.existing_users:
                users_json.append(user.to_JSON_string())
            separator =","
            result = "["+separator.join(users_json)+"]"
            print(result)
            #como al tratar de devolver un arreglo de jsons con json.dump a un archivo generaba extra comillas
            #decidi crear una cadena del json y escribirlo como un archivo normal
            with open("existing_users.json", "w") as outfile:
                outfile.write(result)
            return "New user added successfuly"
        else:
            return "User couldn't be added"
    def pass_product_validations(self, obj_product):
        for product in self.existing_products:
            #valido si el usuario o el email es repetido
            if product.id == obj_product.id:
                print("Product already exists")
                return False
        #valido si el email tiene el formato correcto con regex
        if obj_product.price == None:  
            print("Product price can't be null")
            return False
        if obj_product.quantity == None:    
            print("Product quantity can't be null")
            return False
        return True  
    def add_new_product(self, obj_product):
        if self.pass_product_validations(obj_product):
            self.existing_products.append(obj_product)
            products_json = []
            for product in self.existing_products:
                products_json.append(product.to_JSON_string())
            separator =","
            result = "["+separator.join(products_json)+"]"
            print(result)
            #como al tratar de devolver un arreglo de jsons con json.dump a un archivo generaba extra comillas
            #decidi crear una cadena del json y escribirlo como un archivo normal
            with open("existing_products.json", "w") as outfile:
                outfile.write(result)
            return "New product added successfuly"
        else:
            return "Product couldn't be added"        
    def get_all_products(self):
        return self.existing_products
    def __init__(self):
        self.existing_users = self.load_existing_users()
        self.existing_products = self.load_existing_products()

    def get_all_users(self):
        return self.existing_users
    def get_user_by_username(self, username):
        for user in self.existing_users:
            if user.username == username:
                return user
        return None
    def get_product(self, product_id):
        for product in self.existing_products:
            if product.id == product_id:
                return product
        return None
    def login(self, username, password):
        temp_user = self.get_user_by_username(username)
        #primero valido si existe el usuario
        if temp_user != None:
            #segundo valido si el password es correcto
            if temp_user.password == password:
                return "Correct credentials"
            else:
                return "Wrong password"    
        else:
            return "User doesn't exists"
