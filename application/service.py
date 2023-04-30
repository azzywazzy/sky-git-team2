from application.models.customer import Customer
from application.models.patient import Patient
from application.models.order_history import OrderHistory
from application.models.product import Product
from application.models.vet_personnel import VetPersonnel
from flask_login import current_user

from application import db, login_manager
from flask_login import UserMixin


def get_all_customers():
    return db.session.query(Customer).all()


def get_all_patients():
    full_patients = []
    display_patients = db.session.query(Patient).all()
    for row in display_patients:
        customer = db.session.query(Customer).filter_by(cus_id=row.cus_id).first()
        dict_info = {"pat_id": row.pat_id, "cus_id": row.cus_id, "pat_name": row.pat_name, "species": row.species.capitalize(), "breed": row.breed.capitalize(), "sex": row.sex.capitalize(), "date_of_birth": row.date_of_birth, "weight": row.weight, "chip_num": row.chip_num, "neutered_status": row.neutered_status, "has_insurance": row.has_insurance, "cus_last_name": customer.cus_last_name}
        full_patients.append(dict_info)
    return full_patients


def get_all_orders():
    full_orders = []
    display_orders = db.session.query(OrderHistory).all()
    for row in display_orders:
        customer = db.session.query(Customer).filter_by(cus_id=row.cus_id).first()
        product = db.session.query(Product).filter_by(product_id=row.product_id).first()
        dict_info = {"order_id": row.order_id, "product_id": row.product_id, "cus_id": row.cus_id, "quantity_ordered": row.quantity_ordered, "order_date": row.order_date, "collection_date": row.collection_date, "collected": row.collected, "cus_last_name": customer.cus_last_name, "prod_name": product.prod_name.capitalize()}
        full_orders.append(dict_info)
    return full_orders


def get_all_products():
    products = db.session.query(Product).all()
    for e in products:
        e.prod_category = e.prod_category.capitalize()
        e.prod_species = e.prod_species.capitalize()
    return products


def get_admin_product(prod_id):
    return Product.query.filter_by(product_id=prod_id).first()


def get_admin_order(ord_id):
    return OrderHistory.query.filter_by(order_id=ord_id).first()


def get_admin_customer(cus_id):
    return Customer.query.filter_by(cus_id=cus_id).first()


def get_admin_patient(pat_id):
    return Patient.query.filter_by(pat_id=pat_id).first()


def get_prod_cust(prod_id):
    product = Product.query.filter_by(product_id=prod_id).first()
    customer = Customer.query.filter_by(cus_email=current_user.email).first()
    return product, customer
