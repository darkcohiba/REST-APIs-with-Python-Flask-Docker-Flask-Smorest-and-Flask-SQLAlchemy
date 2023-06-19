import uuid
from flask import request
from flask.views import MethodView
from flask_florest import Blueprint, abort
from db import stores


# create blueprint
blp = Blueprint("stores", __name__, description="Operation on stores")

# create a class out of method views
class Store(MethodView):
    def get(self):
        pass

    def delete(self):
        pass