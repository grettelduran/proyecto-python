from controller.controller import Controller
from model.modelo import User, Product
from flask import Flask, jsonify, request, make_response, abort
import json

controller = Controller()
app = Flask(__name__)
app.config["SECRET_KEY"] = "mykey"
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False


@app.route("/")
def index():
    return "Players Application"


@app.route("/users", methods=["POST"])
def add_new_user():
    if (
        not request.json
        or not "username" in request.json
        or not "password" in request.json
        or not "name" in request.json
        or not "last_name" in request.json
        or not "email" in request.json
        or not "cart_id" in request.json
    ):
        abort(400)
    result = controller.add_new_user(
        request.json.get("username"),
        request.json.get("password"),
        request.json.get("name"),
        request.json.get("last_name"),
        request.json.get("email"),
        request.json.get("cart_id")
    )
    return jsonify({"result": result}), 201


@app.route("/users", methods=["GET"])
def get_all_users():
    users = controller.get_all_users()
    #genero un arreglo de jsonstrings para la visualizacion
    return jsonify({"users": [pn.to_JSON_string() for pn in users]}), 201

@app.route("/products", methods=["POST"])
def add_new_product():
    if (
        not request.json
        or not "id" in request.json
        or not "name" in request.json
        or not "description" in request.json
        or not "quantity" in request.json
        or not "price" in request.json
    ):
        abort(400)
    result = controller.add_new_product(
        request.json.get("id"),
        request.json.get("name"),
        request.json.get("description"),
        request.json.get("quantity"),
        request.json.get("price")
    )
    return jsonify({"result": result}), 201
@app.route("/products/<string:product_id>", methods=["GET"])
def get_product(product_id):
    product = controller.get_product(product_id)
    if product != None:
        return jsonify({"product": product.to_JSON_string()}), 201
    return jsonify({"product": None}), 404
@app.route("/users/<string:username>", methods=["GET"])
def get_user(username):
    user = controller.get_user(username)
    if user != None:
        return jsonify({"user": user.to_JSON_string()}), 201
    return jsonify({"user": None}), 404

@app.route("/products", methods=["GET"])
def get_all_products():
    products = controller.get_all_products()
    #genero un arreglo de jsonstrings para la visualizacion
    return jsonify({"users": [pn.to_JSON_string() for pn in products]}), 201

@app.route("/login", methods=["POST"])
def login():
    if (
        not request.json
        or not "username" in request.json
        or not "password" in request.json
    ):
        abort(400)
    result = controller.login(
        request.json.get("username"), request.json.get("password")
    )
    if result != None:
        return jsonify({"message": result}), 201
    return jsonify({"result": "An error occurred"}), 500
if __name__ == "__main__":
    app.run(debug=True)
