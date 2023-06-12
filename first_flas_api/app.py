from flask import Flask, request

# importing our two dicts from our db.py
from db import items, stores

# next refactor is adding flask smorest to do our error handling
from flask_smorest import abort

# using this for our ids for our db.py database
import uuid

app = Flask(__name__)

# storing our data in a list then we changed to storing our data in a dictionary



# get all stores
@app.get("/store")
def get_stores():
    # original with the database as the list stored in this file:
    # return {"stores": stores}
    print(stores)
    # updated for the db.py
    return {"stores": list(stores.values())}, 200

@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}, 200

#  create a new store
# first version
# @app.post("/store")
# def post_store():
#     request_data = request.get_json()
#     stores.append(request_data)
#     return {"stores": stores}, 201

# new version with db.py
@app.post("/store")
def post_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {
        **store_data,
        "id": store_id
    }
    stores[store_id]= new_store
    return new_store, 201

# will post items to the store provided in the url
# @app.post("/store/<string:name>/item")
# def create_item(name):
#     request_data = request.get_json()
#     # print(request_data)
#     for store in stores:
#         print(store["name"])
#         if store["name"] == name.title():
#             new_item = {
#                 "name": request_data["name"],
#                 "price": request_data["price"]
#             }
#             store["items"].append(new_item)
#             return {"stores": stores}, 201
#     return {"message":"store not found"}, 404

# updated create item with db.py
@app.post("/item")
def create_item():
    item_data = request.get_json()
    try:
        if item_data["store_id"] not in stores:
            return {"message": "store not found"}, 404
    except KeyError:
        # return {"message": "store not found"}, 404
        # with smorest
        abort(404, message="store not found.")
    item_id = uuid.uuid4().hex
    new_item = {
        **item_data,
        "id": item_id
    }
    items[item_id]= new_item
    return new_item, 201

# original based on store name
#  returns the store based on url parameters
# @app.get("/store/<string:name>")
# def get_store(name):
#     for store in stores:
#         if store["name"] == name.title():
#             return store
#     return {"message":"store not found"}, 404

# new version working with the id system using the db.py
#  returns the store based on url parameters
@app.get("/store/<int:store_id>")
def get_store(store_id):
    try:
        return stores[store_id], 200
    except KeyError:
        # without smorest
        # return {"message":"store not found"}, 404
        # with smorest
        abort(404, message="store not found.")
    

# new route to return the item by the id
@app.get("/items/<string:item_id>")
def get_item_in_store(item_id):
    try:
        return items[item_id], 200
    except KeyError:
        # return {"message":"item not found"}, 404
        # with smorest
        abort(404, message="item not found.")


