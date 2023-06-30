from marshmallow import Schema, fields


class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float()
    store_id = fields.Integer()


class UpdateItemSchema(Schema):
    name = fields.String()
    price = fields.Float()


class StoreSchema(Schema):
    id = fields.Integer()
    name = fields.String()