import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema



# create blueprint
blp = Blueprint("stores", __name__, description="Operation on stores")

# create a class out of method views
# establish the route with the blueprint
@blp.route("/store/<int:store_id>")
class Store(MethodView):
    def get(self, store_id):
        # print(type(store_id))
        try:
            return stores[store_id], 200
        except KeyError:
            # without smorest
            # return {"message":"store not found"}, 404
            # with smorest
            abort(404, message="store not found.")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, "Store not found")


@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}

    # we can use the schema to validate the data, first we add it as a decorator, then we recieve it through the function
    @blp.arguments(StoreSchema)
    def post(self, store_data):
        # we no longer need to request the data since it is going to be recieved through the decorator.
        # item_data = request.get_json()
        # we no longer need to do this validation since we will use the schemas
        # Here not only we need to validate data exists,
        # But also what type of data. Price should be a float,
        # for example.
        # if (
        #     "price" not in item_data
        #     or "store_id" not in item_data
        #     or "name" not in item_data
        # ):
        #     abort(
        #         400,
        #         message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.",
        #     )
        for store in stores.values():
            if (
                store_data["name"] == store["name"]
                and store_data["store_id"] == store["store_id"]
            ):
                abort(400, message=f"Item already exists.")

        store_id = uuid.uuid4().int
        store = {**store_data, "id": store_id}
        stores[store_id] = store

        return store