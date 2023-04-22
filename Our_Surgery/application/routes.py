from flask import render_template, jsonify, json, request
from application.models.customer import Customer
from application.models.patient import Patient
from application.models.order_history import OrderHistory
from application.models.product import Product
from application.models.vet_personnel import VetPersonnel

from application import app, service

@app.route('/admin/customers', methods=['GET'])
def all_customers():
    error = ""
    customers = service.get_all_customers()
    if len(customers) == 0:
        error = "There are no customers to display"
    return render_template('admin-customers.html', customers=customers, message=error)
    # return jsonify(customers)

@app.route('/admin/orders', methods=['GET'])
def all_orders():
    error = ""
    orders = service.get_all_orders()
    if len(orders) == 0:
        error = "There are no orders to display"
    return render_template('admin-orders.html', orders=orders, message=error)
    # return jsonify(orders)

@app.route('/admin/patients', methods=['GET'])
def all_patients():
    error = ""
    patients = service.get_all_patients()
    if len(patients) == 0:
        error = "There are no patients to display"
    return render_template('admin-patients.html', patients=patients, message=error)
    # return jsonify(patients)

@app.route('/admin/products', methods=['GET'])
def all_products():
    error = ""
    products = service.get_all_products()
    if len(products) == 0:
        error = "There are no products to display"
    return render_template('admin-products.html', products=products, message=error)
    # return jsonify(products)