from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # the name can not be longer then 80 characters, it must be unique and it can not be null
    item = db.relationship("ItemModel", back_populates="store", lazy="dynamic")
    # lazy = dynamic means the items wont be fetched until we fetch it
