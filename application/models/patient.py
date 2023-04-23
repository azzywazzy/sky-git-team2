from application import db
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


class Patient(db.Model):
    pat_id = db.Column(db.Integer, primary_key=True, nullable=False)
    cus_id: Mapped[int] = mapped_column(ForeignKey("customer.cus_id"))
    pat_name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    breed = db.Column(db.String(50), nullable=True)
    sex = db.Column(db.String(1), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    chip_num = db.Column(db.String(50), nullable=True)
    neutered_status = db.Column(db.Integer, nullable=True)
    has_insurance = db.Column(db.Integer, nullable=True)
    customer: Mapped["Customer"] = relationship(back_populates="patients")

