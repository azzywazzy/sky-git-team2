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
    # return jsonify(albums)

@app.route('/admin/patients', methods=['GET'])
def all_patients():
    error = ""
    patients = service.get_all_patients()
    if len(patients) == 0:
        error = "There are no patients to display"
    return render_template('admin-patients.html', patients=patients, message=error)
    # return jsonify(albums)


