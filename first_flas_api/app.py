from flask import Flask, request

# importing our two dicts from our db.py
# using blueprints we dont need this
# from db import items, stores

# next refactor is adding flask smorest to do our error handling
# using blueprints we dont need this
# from flask_smorest import abort

# import flask smorest from flask_smorest for blueprints
from flask_smorest import Api

# using this for our ids for our db.py database
# using blueprints we dont need this
# import uuid

# import our blueprints
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint


app = Flask(__name__)

# blueprint set up:

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores Rest API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] ="/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/" 


# create our api endpoints
api = Api(app)
api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)



# no longer needed because we are using blueprints
# storing our data in a list then we changed to storing our data in a dictionary



# # get all stores
# @app.get("/store")
# def get_stores():
#     # original with the database as the list stored in this file:
#     # return {"stores": stores}
#     print(stores)
#     # updated for the db.py
#     return {"stores": list(stores.values())}, 200



# #  create a new store
# # first version
# # @app.post("/store")
# # def post_store():
# #     request_data = request.get_json()
# #     stores.append(request_data)
# #     return {"stores": stores}, 201

# # new version with db.py
# @app.post("/store")
# def post_store():
#     store_data = request.get_json()

#     # make sure our json data sent through the name
#     if "name" not in store_data:
#         abort(
#             400,
#             message="Bad request. Ensure 'name' is included in the JSON payload.",
#         )
#     print("hello")
#     # make sure our store doesn't already exist
#     for store in stores.values():
#         if store_data["name"] == store["name"]:
#             abort(400, message="Store already exists")
#     store_id = uuid.uuid4().hex
#     new_store = {
#         **store_data,
#         "id": store_id
#     }
#     stores[store_id]= new_store
#     return new_store, 201

# # delete store
# @app.delete("/store/<int:store_id>")
# def delete_store(store_id):
#     try:
#         del stores[store_id]
#         return {"message": "Store deleted."}
#     except KeyError:
#         abort(404, "Store not found")

    
# # will post items to the store provided in the url
# # @app.post("/store/<string:name>/item")
# # def create_item(name):
# #     request_data = request.get_json()
# #     # print(request_data)
# #     for store in stores:
# #         print(store["name"])
# #         if store["name"] == name.title():
# #             new_item = {
# #                 "name": request_data["name"],
# #                 "price": request_data["price"]
# #             }
# #             store["items"].append(new_item)
# #             return {"stores": stores}, 201
# #     return {"message":"store not found"}, 404

# @app.get("/item")
# def get_all_items():
#     return {"items": list(items.values())}, 200


# # updated create item with db.py
# @app.post("/item")
# def create_item():
#     item_data = request.get_json()
#     # my error catching
#     # try:
#     #     if item_data["store_id"] not in stores:
#     #         return {"message": "store not found"}, 404
#     # except KeyError:
#     #     # return {"message": "store not found"}, 404
#     #     # with smorest
#     #     abort(404, message="store not found.")
#     # course error catching
#     # checking to see if each expected attribute is in the data recieved
#     if (
#         "price" not in item_data
#         or "store_id" not in item_data
#         or "name" not in item_data
#     ):
#         abort(400, message="Bad request, ensure price, name and store_id are")
#     # check to see if the item already exists in our system under the same store
#     for item in items.values():
#         if (
#             item_data["name"] == item["name"]
#             and item_data["store_id"] == item["store_id"]
#         ):
#             abort(404, "Item already exists.")
#     # check to see if the store from the item exists, if not abort
#     if item_data["store_id"] not in stores:
#         abort(404, message="Store not found.")
#     item_id = uuid.uuid4().hex
#     new_item = {
#         **item_data,
#         "id": item_id
#     }
#     items[item_id]= new_item
#     return new_item, 201

# # delete item
# @app.delete("/item/<string:item_id>")
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message": "Item deleted."}
#     except KeyError:
#         abort(404, "Item not found")





# # original based on store name
# #  returns the store based on url parameters
# # @app.get("/store/<string:name>")
# # def get_store(name):
# #     for store in stores:
# #         if store["name"] == name.title():
# #             return store
# #     return {"message":"store not found"}, 404

# # new version working with the id system using the db.py
# #  returns the store based on url parameters


# @app.get("/store/<int:store_id>")
# def get_store(store_id):
#     try:
#         return stores[store_id], 200
#     except KeyError:
#         # without smorest
#         # return {"message":"store not found"}, 404
#         # with smorest
#         abort(404, message="store not found.")
    

# # new route to return the item by the id
# @app.get("/items/<string:item_id>")
# def get_item_in_store(item_id):
#     try:
#         return items[item_id], 200
#     except KeyError:
#         # return {"message":"item not found"}, 404
#         # with smorest
#         abort(404, message="item not found.")


# # update item
# @app.put("/items/<string:item_id>")
# def update_item(item_id):
#     item_data = request.get_json()
#     if "price" not in item_data or "name" not in item_data:
#         abort(400, message="Bad request. Ensure 'price' and 'name' are included in the JSON payload.")

#     try:
#         item = items[item_id]
#         item |= item_data

#         return item
#     except KeyError:
#         abort(404, message="item not found.")


