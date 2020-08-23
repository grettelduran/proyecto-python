import json

class Product:
    def __init__(self, product_id, name, description, quantity, price):
        self.id = product_id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price

    def to_JSON_string(self):
        #esto permite convertir el objeto en json string
        cad = json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)
        print(cad)
        return cad
class User:
    def __init__(self, username, password, name, last_name, email, cart_id):
        self.username = username
        self.password = password
        self.name = name
        self.last_name = last_name
        self.email = email
        self.cart_id = cart_id

    def to_JSON_string(self):
        #esto permite convertir el objeto en json string
        cad = json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)
        print(cad)
        return cad