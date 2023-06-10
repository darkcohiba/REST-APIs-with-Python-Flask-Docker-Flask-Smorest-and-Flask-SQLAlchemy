from flask import Flask, request

app = Flask(__name__)

# storing our data in a list

stores=[
    {
        "name":"Marzyck",
        "items":[
            {
                "name":"Chicken",
                "price": 12.99
            }
        ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores": stores}

@app.post("/store")
def post_store():
    request_data = request.get_json()
    stores.append(request_data)
    return {"stores": stores}, 201

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
            return {"stores": stores}
    return {"message":"store not found"}
