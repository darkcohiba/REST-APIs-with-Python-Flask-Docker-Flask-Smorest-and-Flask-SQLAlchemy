import uuid
from flask import request
from flask.views import MethodView
from flask_florest import Blueprint, abort
from db import stores


# create blueprint
blp = Blueprint("stores", __name__, description="Operation on stores")

# create a class out of method views
# establish the route with the blueprint
@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        pass

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, "Store not found")