""" this  is the docstring that pylint requests """
# from: https://www.youtube.com/watch?v=PTZiDnuC86g
# https://github.com/bradtraversy/flask_sqlalchemy_rest
# look up info on pdb as well
# apt install sqlite3
# pip install flask flask_sqlalchemy flask_marshmallow
#  init db from python
# $python
# from app import db
# db.create_all()
#
# export FLASK_APP=app.py; flask run --host 0.0.0.0 --port 8500
#
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Dadabase
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False

# init db
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Product class/model
class Product(db.Model):
    """ class to hold product data """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

# product schema
class ProductSchema(ma.Schema):
    """ serializer? """
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')
# init schema
product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True)


@app.route('/', methods=['GET'])
def get():
    """ there should be a description until the def, just like this"""
    return jsonify({'msg': 'Hello world'})  # turn dic into json

@app.route('/product', methods=['POST'])
def add_product():
    """ add a single product """
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

# Get all products
@app.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result.data)

# Get single product
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    products = Product.query.get(id)
    return product_schema.jsonify(product)


@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
 
    product.name = name
    product.description = description
    product.price = price
    product.qty = qty
    
    db.session.committ()
    
    return product_schema.jsonify(product)



# run server
if __name__ == '__main__':
    app.run(debug=True)
