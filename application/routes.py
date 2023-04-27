from flask import render_template, jsonify, json, request, url_for, redirect, flash
from wtforms import StringField
from wtforms.validators import Optional, Length

from application import app, service, db, bcrypt, login_manager
from application.forms import RegistrationForm, LoginForm, PatientRegistrationForm, PatientUpdateForm, \
    UpdateCustomerForm, UpdatePasswordForm
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
        flash('Your account details have been updated!', 'success')
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
        flash('Your password has been updated!', 'success')
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
        flash('You have successfully added a pet!', 'success')
        return redirect(url_for('account'))
    return render_template('register_pet.html', title='Register Pet', form=form)


@app.route("/update-pet", methods=['GET', 'POST'])
def update_patient():
    pat_id = request.args.get('pat_id')
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
        flash("You have successfully updated your pet's details!", 'success')
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
    return render_template('admin-customers.html', customers=customers, message=error)


@app.route("/admin/orders", methods=['GET'])
def all_orders():
    error = ""
    orders = service.get_all_orders()
    if len(orders) == 0:
        error = "There are no orders to display"
    return render_template('admin-orders.html', orders=orders, message=error)


@app.route("/admin/patients", methods=['GET'])
def all_patients():
    error = ""
    patients = service.get_all_patients()
    if len(patients) == 0:
        error = "There are no patients to display"
    return render_template('admin-patients.html', patients=patients, message=error)


@app.route('/admin/products', methods=['GET'])
def all_products():
    error = ""
    products = service.get_all_products()
    if len(products) == 0:
        error = "There are no products to display"
    return render_template('admin-products.html', products=products, message=error)


# just trialling using the current_user value - you need to be logged in as someone for it to work
@app.route("/trial", methods=['GET'])
def trial():
    if current_user.is_authenticated:
        user = Customer.query.filter_by(cus_email=current_user.email).first()
        return [user.cus_email, user.cus_first_name, user.cus_last_name]
    # return jsonify(products)


@app.route('/pet-care', methods=['GET'])
def pet_care():
    return render_template('pet_care.html')


@app.route('/the-team', methods=['GET'])
def the_team():
    return render_template('the-team.html')


@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')


@app.route('/contact-us', methods=['GET'])
def contact_us():
    return render_template('contact_us.html')

