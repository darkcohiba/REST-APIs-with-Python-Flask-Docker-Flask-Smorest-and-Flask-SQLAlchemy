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
