from marshmallow import Schema, fields


class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Integer(required=True)


class UpdateItemSchema(Schema):
    name = fields.String()
    price = fields.Float()


class StoreSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)

class StoreNameOnlySchema(Schema):
    name = fields.String(required=True)