from application import db
from sqlalchemy.orm import Mapped
from typing import List
from sqlalchemy.orm import relationship


class Customer(db.Model):
    cus_id = db.Column(db.Integer, primary_key=True, nullable=False)
    cus_first_name = db.Column(db.String(50), nullable=False)
    cus_last_name = db.Column(db.String(50), nullable=False)
    cus_email = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    cus_status = db.Column(db.Integer, nullable=True)
    patients: Mapped[List["Patient"]] = relationship(back_populates="customer")
    orders: Mapped[List["OrderHistory"]] = relationship(back_populates="customer")


