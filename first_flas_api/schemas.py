from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class PlainStoreSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)




class ItemSchema(PlainItemSchema):
    store_id = fields.Integer(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema, dump_only=True)


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema), dump_only=True)



class UpdateItemSchema(Schema):
    name = fields.String()
    price = fields.Float()



class StoreNameOnlySchema(Schema):
    name = fields.String(required=True)