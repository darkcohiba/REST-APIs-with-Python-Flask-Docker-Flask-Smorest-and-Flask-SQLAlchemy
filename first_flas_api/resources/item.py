import uuid
from flask import request
from flask.views import MethodView
from flask_florest import Blueprint, abort
from db import items


# create blueprint
blp = Blueprint("items", __name__, description="Operation on items")

# create a class out of method views
# establish the route with the blueprint
@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id], 200
        except KeyError:
            # without smorest
            # return {"message":"item not found"}, 404
            # with smorest
            abort(404, message="Item not found.")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, "Item not found")