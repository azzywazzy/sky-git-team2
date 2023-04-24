from application.models.customer import Customer
from application.models.patient import Patient
from application.models.order_history import OrderHistory
from application.models.product import Product
from application.models.vet_personnel import VetPersonnel

from application import db, login_manager
from flask_login import UserMixin


def get_all_customers():
    return db.session.query(Customer).all()


def get_all_patients():
    return db.session.query(Patient).all()


def get_all_orders():
    return db.session.query(OrderHistory).all()


def get_all_products():
    return db.session.query(Product).all()

