from application import db
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship


class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True, nullable=False)
    prod_cost = db.Column(db.Integer, nullable=False)
    prod_category = db.Column(db.String(50), nullable=False)
    prod_name = db.Column(db.String(150), nullable=False)
    prod_description = db.Column(db.String, nullable=True)
    prod_image = db.Column(db.String(255), nullable=True)
    prod_species = db.Column(db.String(50), nullable=False)
    quantity_available = db.Column(db.Integer, nullable=False)
    order: Mapped["OrderHistory"] = relationship(back_populates="product")

