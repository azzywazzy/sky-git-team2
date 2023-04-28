from flask import render_template, jsonify, json, request, url_for, redirect, flash
from wtforms import StringField
from wtforms.validators import Optional, Length

from application import app, service, db, bcrypt, login_manager
from application.forms import RegistrationForm, LoginForm, PatientRegistrationForm, PatientUpdateForm, \
    UpdateCustomerForm, UpdatePasswordForm, AdminPatientUpdateForm, AdminUpdateCustomerForm, AdminUpdateProductForm, \
    AdminAddProductForm, AdminUpdateOrderForm
from flask_bcrypt import Bcrypt
from application.models.customer import Customer
from application.models.patient import Patient
from application.models.order_history import OrderHistory
from application.models.product import Product

from application.models.vet_personnel import VetPersonnel
from application.models.credential import Credential
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Our Vet Surgery')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Credential.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.hash_password, form.hash_password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash('You are now logged out', 'success')
    return redirect(url_for('home'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        credential = Credential(email=form.cus_email.data, hash_password=hashed_password, user_type=0)
        customer = Customer(cus_first_name=form.cus_first_name.data, cus_last_name=form.cus_last_name.data,
                            cus_email=form.cus_email.data, address=form.address.data, phone=form.phone.data,
                            cus_status=1)
        db.session.add(credential)
        db.session.add(customer)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/update-customer", methods=['GET', 'POST'])
def update_customer():
    user = Customer.query.filter_by(cus_email=current_user.email).first()
    form = UpdateCustomerForm()
    if request.method == 'GET':
        form.cus_first_name.data = user.cus_first_name
        form.cus_last_name.data = user.cus_last_name
        form.address.data = user.address
        form.phone.data = user.phone
    if form.validate_on_submit():
        user.cus_first_name = form.cus_first_name.data
        user.cus_last_name = form.cus_last_name.data
        user.address = form.address.data
        user.phone = form.phone.data
        db.session.commit()
        flash('Your account details have been updated', 'success')
        return redirect(url_for('account'))
    return render_template('update_customer.html', title='Update-customer', form=form)


@app.route("/update-password", methods=['GET', 'POST'])
def update_password():
    form = UpdatePasswordForm()
    credential = Credential.query.get(current_user.id)
    if form.validate_on_submit():
        if bcrypt.check_password_hash(credential.hash_password, form.old_password.data):
            credential.hash_password = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
        db.session.commit()
        flash('Your password has been updated', 'success')
        return redirect(url_for('account'))
    return render_template('update_password.html', title='Update-password', form=form)


@app.route("/register-pet", methods=['GET', 'POST'])
def register_patient():
    form = PatientRegistrationForm()
    if form.validate_on_submit():
        user = Customer.query.filter_by(cus_email=current_user.email).first()
        patient = Patient(cus_id=user.cus_id, pat_name=form.pat_name.data, species=form.species.data,
                          breed=form.breed.data, sex=form.sex.data, date_of_birth=form.date_of_birth.data,
                          weight=form.weight.data, chip_num=form.chip_num.data,
                          neutered_status=form.neutered_status.data,
                          has_insurance=form.has_insurance.data, )
        db.session.add(patient)
        db.session.commit()
        flash('You have successfully added a pet', 'success')
        return redirect(url_for('account'))
    return render_template('register_pet.html', title='Register Pet', form=form)


@app.route("/update-pet/<pat_id>", methods=['GET', 'POST'])
def update_patient(pat_id):
    form = PatientUpdateForm()
    user = Customer.query.filter_by(cus_email=current_user.email).first()
    patient = Patient.query.get(pat_id)
    if request.method == 'GET':
        form.pat_name.data = patient.pat_name
        form.species.data = patient.species
        form.breed.data = patient.breed
        form.sex.data = patient.sex
        form.date_of_birth.data = patient.date_of_birth
        form.weight.data = patient.weight
        form.chip_num.data = patient.chip_num
        form.neutered_status.data = patient.neutered_status
        form.has_insurance.data = patient.has_insurance
    if form.validate_on_submit():
        patient.cus_id = user.cus_id
        patient.pat_name = form.pat_name.data
        patient.species = form.species.data
        patient.breed = form.breed.data
        patient.sex = form.sex.data
        patient.date_of_birth = form.date_of_birth.data
        patient.weight = form.weight.data
        patient.chip_num = form.chip_num.data
        patient.neutered_status = form.neutered_status.data
        patient.has_insurance = form.has_insurance.data
        db.session.commit()
        flash("You have successfully updated your pet's details", 'success')
        return redirect(url_for('account'))
    return render_template('update_pet.html', title='Update Pet', form=form)


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')


@app.route("/admin/customers", methods=['GET'])
def all_customers():
    error = ""
    customers = service.get_all_customers()
    if len(customers) == 0:
        error = "There are no customers to display"
    return render_template('admin-customers.html', customers=customers, message=error, title = "Admin View all Customers")


@app.route("/admin/orders", methods=['GET'])
def all_orders():
    error = ""
    orders = service.get_all_orders()
    if len(orders) == 0:
        error = "There are no orders to display"
    return render_template('admin-orders.html', orders=orders, message=error, title = "Admin View all Orders")


@app.route("/admin/patients", methods=['GET'])
def all_patients():
    error = ""
    patients = service.get_all_patients()
    if len(patients) == 0:
        error = "There are no patients to display"
    return render_template('admin-patients.html', patients=patients, message=error, title = "Admin View all Patients")


@app.route('/admin/products', methods=['GET'])
def all_products():
    error = ""
    products = service.get_all_products()
    if len(products) == 0:
        error = "There are no products to display"
    return render_template('admin-products.html', products=products, message=error, title = "Admin View all Products")


# just trialling using the current_user value - you need to be logged in as someone for it to work
@app.route("/trial", methods=['GET'])
def trial():
    if current_user.is_authenticated:
        user = Customer.query.filter_by(cus_email=current_user.email).first()
        return [user.cus_email, user.cus_first_name, user.cus_last_name]


@app.route('/pet-care', methods=['GET'])
def pet_care():
    return render_template('pet_care.html')


@app.route('/the-team', methods=['GET'])
def the_team():
    return render_template('the-team.html')


@app.route('/admin', methods=['GET'])
def admin():
    if current_user.is_authenticated and current_user.user_type == 1:
        return render_template('admin.html', title='Admin Tasks')
    else:
        flash("You are not permitted access", 'danger')
        return redirect(url_for('home'))


@app.route('/contact-us', methods=['GET'])
def contact_us():
    return render_template('contact_us.html')

@app.route("/admin/products/update/<prod_id>", methods=['GET', 'POST'])
def admin_update_product(prod_id):
    if current_user.is_authenticated and current_user.user_type == 1:
        form = AdminUpdateProductForm()
        product = service.get_admin_product(prod_id)
        if request.method == 'GET':
            form.prod_name.data = product.prod_name
            form.prod_species.data = product.prod_species
            form.prod_category.data = product.prod_category
            form.prod_description.data = product.prod_description
            form.prod_cost.data = product.prod_cost
            form.quantity_available.data = product.quantity_available
        if form.validate_on_submit():
            product.prod_name = form.prod_name.data
            product.prod_species = form.prod_species.data
            product.prod_category = form.prod_category.data
            product.prod_description = form.prod_description.data
            product.prod_cost = form.prod_cost.data
            product.quantity_available = form.quantity_available.data
            db.session.commit()
            flash('Product updated', 'success')
            return redirect(url_for('all_products'))
        return render_template('admin-products-update.html', form=form, title='Admin Update Product')
    else:
        flash("You are not permitted access", 'danger')
        return redirect(url_for('home'))


@app.route("/admin/orders/update/<ord_id>", methods=['GET', 'POST'])
def admin_update_order(ord_id):
    if current_user.is_authenticated and current_user.user_type == 1:
        form = AdminUpdateOrderForm()
        order = service.get_admin_order(ord_id)
        if request.method == 'GET':
            form.collected.data = order.collected
            form.collection_date.data = order.collection_date
        if form.validate_on_submit():
            order.collected = form.collected.data
            order.collection_date = form.collection_date.data
            db.session.commit()
            flash('Order updated', 'success')
            return redirect(url_for('all_orders'))
        return render_template('admin-orders-update.html', form=form, title="Admin Update Order")
    else:
        flash("You are not permitted access", 'danger')
        return redirect(url_for('home'))

@app.route("/admin/customers/update/<cus_id>", methods=['GET', 'POST'])
def admin_update_customer(cus_id):
    if current_user.is_authenticated and current_user.user_type == 1:
        form = AdminUpdateCustomerForm()
        user = service.get_admin_customer(cus_id)
        if request.method == 'GET':
            form.cus_first_name.data = user.cus_first_name
            form.cus_last_name.data = user.cus_last_name
            form.address.data = user.address
            form.phone.data = user.phone
        if form.validate_on_submit():
            user.cus_first_name = form.cus_first_name.data
            user.cus_last_name = form.cus_last_name.data
            user.address = form.address.data
            user.phone = form.phone.data
            db.session.commit()
            flash('Customer details updated', 'success')
            return redirect(url_for('all_customers'))
        return render_template('admin-customers-update.html', form=form, title='Admin Update Customer Details')
    else:
        flash("You are not permitted access", 'danger')
        return redirect(url_for('home'))


@app.route("/admin/patients/update/<pat_id>", methods=['GET', 'POST'])
def admin_update_patient(pat_id):
    if current_user.is_authenticated and current_user.user_type == 1:
        form = AdminPatientUpdateForm()
        patient = service.get_admin_patient(pat_id)
        if request.method == 'GET':
            form.pat_name.data = patient.pat_name
            form.species.data = patient.species
            form.breed.data = patient.breed
            form.sex.data = patient.sex
            form.date_of_birth.data = patient.date_of_birth
            form.weight.data = patient.weight
            form.chip_num.data = patient.chip_num
            form.neutered_status.data = patient.neutered_status
            form.has_insurance.data = patient.has_insurance
        if form.validate_on_submit():
            patient.pat_name = form.pat_name.data
            patient.species = form.species.data
            patient.breed = form.breed.data
            patient.sex = form.sex.data
            patient.date_of_birth = form.date_of_birth.data
            patient.weight = form.weight.data
            patient.chip_num = form.chip_num.data
            patient.neutered_status = form.neutered_status.data
            patient.has_insurance = form.has_insurance.data
            db.session.commit()
            flash("Patient details updated", 'success')
            return redirect(url_for('all_patients'))
        return render_template('admin-patients-update.html', title="Admin Update Patient Record", form=form)
    else:
        flash("You are not permitted access", 'danger')
        return redirect(url_for('home'))


@app.route("/admin/products/add", methods=['GET', 'POST'])
def admin_add_product():
    if current_user.is_authenticated and current_user.user_type == 1:
        form = AdminAddProductForm()
        if form.validate_on_submit():
            product = Product(prod_name=form.prod_name.data, prod_species=form.prod_species.data,
                              prod_category=form.prod_category.data, prod_description=form.prod_description.data,
                              prod_cost=form.prod_cost.data, quantity_available=form.quantity_available.data)
            db.session.add(product)
            db.session.commit()
            flash('New product added', 'success')
            return redirect(url_for('all_products'))
        return render_template('admin-products-add.html', form=form, title='Admin Add Product')
    else:
        flash("You are not permitted access", 'danger')
        return redirect(url_for('home'))


@app.route('/products', methods=['GET'])
def view_products():
    error = ""
    products = service.get_all_products()
    if len(products) == 0:
        error = "There are no products to display"
    return render_template('products.html', products=products, message=error, title="Products Available")





