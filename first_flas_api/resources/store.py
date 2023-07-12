import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
# sqlalchemy exception
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
# removing the below line after we added our models folder and sqlite
# from db import stores

# imports for sqlalchemy
from db import db
from models import StoreModel
from schemas import StoreSchema, StoreNameOnlySchema

# create blueprint
blp = Blueprint("stores", __name__, description="Operation on stores")

# create a class out of method views
# establish the route with the blueprint
@blp.route("/store/<int:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        return StoreModel.query.get_or_404(store_id)
        # removing when we update for sqlalchemy
        # try:
        #     return stores[store_id], 200
        # except KeyError:
        #     # without smorest
        #     # return {"message":"store not found"}, 404
        #     # with smorest
        #     abort(404, message="store not found.")


    def delete(self, store_id):
        
        # removing the below when we update to sqlalchemy
        # try:
        #     del stores[store_id]
        #     return {"message": "Store deleted."}
        # except KeyError:
        #     abort(404, "Store not found")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        # return {"stores": list(stores.values())}
        return stores.values()
    

    # we can use the schema to validate the data, first we add it as a decorator, then we recieve it through the function
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
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
        # removing the below when we adjust for sqlalchemy
        # for store in stores.values():
        #     if (
        #         store_data["name"] == store["name"]
        #         and store_data["store_id"] == store["store_id"]
        #     ):
        #         abort(400, message="Item already exists.")

        # store_id = uuid.uuid4().int
        # store = {**store_data, "id": store_id}
        # stores[store_id] = store

        store = StoreModel(**store_data)

        try:
            db.sesson.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A store with that name already exists")
        except SQLAlchemyError:
            abort(500, message="An error occurred while creating the store.")

        

        return store
    
