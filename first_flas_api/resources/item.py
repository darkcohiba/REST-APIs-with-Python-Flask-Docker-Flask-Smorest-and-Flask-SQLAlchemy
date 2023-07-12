import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
# sqlalchemy exception
from sqlalchemy.exc import SQLAlchemyError
# removing the below line after we added our models folder and sqlite
# from db import items

# sqlite db imports:
from db import db
from models import ItemModel
from schemas import ItemSchema, UpdateItemSchema

# create blueprint
blp = Blueprint("items", __name__, description="Operation on items")

# create a class out of method views
# establish the route with the blueprint
@blp.route("/item/<int:item_id>")
class Item(MethodView):
    # adding a blueprint response, it will return a status code of 200 with a response of the item schema, this is our serialization
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        return ItemModel.query.get_or_404(item_id)
        # removing when we update for sqlalchemy
        # try:
        #     return items[item_id], 200
        # except KeyError:
        #     # without smorest
        #     # return {"message":"item not found"}, 404
        #     # with smorest
        #     abort(404, message="Item not found.")

    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        raise NotImplementedError("Deleting an item is not implemented yet")
        # removing the below code when we update for sqlalchemy
        # try:
        #     del items[item_id]
        #     return {"message": "Item deleted."}
        # except KeyError:
        #     abort(404, "Item not found")

    @blp.arguments(UpdateItemSchema)
    # the blp response must be nested inside the arguments decorator
    @blp.response(200, ItemSchema)
    # the item id that is passed through the url must go last
    def put(self, item_data, item_id):
        item = ItemModel.query.get_or_404(item_id)
        raise NotImplementedError("Put an item is not implemented yet")
        # no longer need to get request data since we are using the decorator
        # item_data = request.get_json()
        # if "price" not in item_data or "name" not in item_data:
        #     abort(400, message="Bad request. Ensure 'price' and 'name' are included in the JSON payload.")
        # removing the below when we update for sqlalchemy
        # try:
        #     item = items[item_id]
        #     item |= item_data

        #     return item
        # except KeyError:
        #     abort(404, message="item not found.")

@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        # before adding the response decorator 
        # return {"items": list(items.values())}
        # after adding the response decorator
        return items.values()

    # we can use the schema to validate the data, first we add it as a decorator, then we recieve it through the function
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
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
        # removing the below for our update to sqlite
        # for item in items.values():
        #     if (
        #         item_data["name"] == item["name"]
        #         and item_data["store_id"] == item["store_id"]
        #     ):
        #         abort(400, message="Item already exists.")

        # item_id = uuid.uuid4().hex
        # item = {**item_data, "id": item_id}
        # items[item_id] = item
        item = ItemModel(**item_data)
        
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return item