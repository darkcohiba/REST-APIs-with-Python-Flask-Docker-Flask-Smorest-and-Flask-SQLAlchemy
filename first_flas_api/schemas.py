from marshmallow import Schema, fields


class ItemSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    price = fields.Float()
    description = fields.String()
    image = fields.String()

class UpdateItemSchema(Schema):
    name = fields.String()
    price = fields.Float()
    description = fields.String()
    image = fields.String()