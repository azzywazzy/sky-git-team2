from flask import render_template, jsonify, json, request, url_for, redirect, flash
from application import app, service, db, bcrypt
from application.forms import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt
from application.models.customer import Customer
from application.models.patient import Patient
from application.models.order_history import OrderHistory
from application.models.product import Product
from application.models.vet_personnel import VetPersonnel
from application.models.credential import Credential
# from application import app, service
from flask_login import login_user

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

    # return jsonify(albums)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        credential = Credential(email=form.cus_email.data, hash_password=hashed_password, user_type=0)
        customer = Customer(cus_first_name=form.cus_first_name.data, cus_last_name=form.cus_last_name.data, cus_email=form.cus_email.data, address=form.address.data, phone=form.phone.data, cus_status=1 )
        db.session.add(credential)
        db.session.add(customer)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Customer.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(application.models.credential.hash_password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('admin/patients'))
        else:
            flash('Login Unsuccessful. Please check email and password','dangerous')
    return render_template('login.html', title='Login', form=form)

# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#     return render_template('login.html', title='Login', form=form)


# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = Credential.query.filter_by(email=form.email.data).first()
#         if user and bcrypt.check_password_hash(user.password, form.password.data):
#             # login_user(user, remember=form.remember.data)
#             # next_page = request.args.get('next')
#             return redirect(url_for('admin/customers'))
#         else:
#             flash('Login Unsuccessful. Please check email and password', 'danger')
#     return render_template('login.html', title='Login', form=form)


@app.route('/admin/products', methods=['GET'])
def all_products():
    error = ""
    products = service.get_all_products()
    if len(products) == 0:
        error = "There are no products to display"
    return render_template('admin-products.html', products=products, message=error)
    # return jsonify(products)