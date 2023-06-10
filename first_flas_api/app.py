from flask import Flask, request

from db import items, stores

app = Flask(__name__)

# storing our data in a list



# get all stores
@app.get("/store")
def get_stores():
    return {"stores": stores}

#  create a new store
@app.post("/store")
def post_store():
    request_data = request.get_json()
    stores.append(request_data)
    return {"stores": stores}, 201

# will post items to the store provided in the url
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    # print(request_data)
    for store in stores:
        print(store["name"])
        if store["name"] == name.title():
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            store["items"].append(new_item)
            return {"stores": stores}, 201
    return {"message":"store not found"}, 404

#  returns the store based on url parameters
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name.title():
            return store
    return {"message":"store not found"}, 404

# foute to return the stores items by the store name
@app.get("/store/<string:name>/items")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name.title():
            return {"items": store["items"]}
    return {"message":"store not found"}, 404

