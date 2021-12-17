"""
Desc: backend for the online store
author: Oscar Rodriguez 

"""

from flask import Flask, abort, request, render_template
from mock_data import catalog
import json
from config import db, json_parse  
from bson import ObjectId
from bson.errors import InvalidId

app = Flask(__name__)

about_me = {
    "name": "Oscar",
    "last": "Rodriguez", 
    "age": 26,
    "hobbies":[],
    "address": {
        "street":"42 evergreen",
        "city":"Springfield"
    }
}
 
@app.route("/")
def home():
     return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")




#********************API ENDPOINT**********************

@app.route("/api/catalog", methods=["get"])
def retrieve_catalog():
    #read data from the database (with no filter)
    cursor = db.products.find({})
    list = []
    for prod in cursor:
        list.append(prod)
    return json_parse(list) # parse catalog into a string and return it

@app.route("/api/catalog", methods=["post"])
def save_catalog(): 
    #get the payload (the objects/data that client is sending)
    product = request.get_json()
    # save the product object to database 

    db.products.insert_one(product)
    
    return json_parse(product)

@app.route("/api/product/<id>")
def get_product(id):

    try:
        objectId_instance = ObjectId(id)

        prod = db.products.find_one({"_id":objectId_instance})
        if prod is not None:
            return json_parse(prod)
    
        return abort(404) #return a 404 (not found) error
    except InvalidId: 
        print("Error: Invaild Object ID", id )
        return abort(400) # return bad request 

@app.route("/api/catalog/<category>")
def get_product_by_category(category):

    cursor = db.products.find({"category": category})
    list = []
    for prod in cursor:
        list.append(prod)
    return json_parse(list)


@app.route("/api/products/cheapest")
def get_cheapest_product():
    # migrate to DB
    # get all the prods from the DB
    cursor = db.products.find({})
    cheapest_prod = cursor[0]
    for prod in cursor:
        if (prod["price"] < cheapest_prod["price"]):
            cheapest_prod = prod
    return json_parse(cheapest_prod)

@app.route("/api/products/categories")
def get_unique_categories():
 
    cursor = db.products.find({})
    categories = []
    for prod in cursor:
            cat = prod["category"]
            if cat not in categories:
                categories.append(cat)
    return json_parse(categories)


@app.route("/test/onetime/filldb")
def fill_db():
    for prod in catalog:
        prod.pop("_id")
        db.products.insert_one(prod)

    return "done!"

@app.route("/api/reports/total")
def get_products_total():

    cursor = db.products.find({})
    total = 0
    for prod in cursor:

        price = prod["price"]
        total += price

    return json_parse(total)



#TODO remove debug before deploying
app.run(debug=True)



