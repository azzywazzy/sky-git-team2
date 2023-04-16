from application import db
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


class OrderHistory(db.Model):
    __tablename__ = "order_history"
    order_id = db.Column(db.Integer, primary_key=True, nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.product_id"))
    cus_id: Mapped[int] = mapped_column(ForeignKey("customer.cus_id"))
    quantity_ordered = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.Date, nullable=True)
    collected = db.Column(db.Integer, nullable=True)
    collection_date = db.Column(db.Date, nullable=True)
    customer: Mapped["Customer"] = relationship(back_populates="orders")
    product: Mapped["Product"] = relationship(back_populates="order")



