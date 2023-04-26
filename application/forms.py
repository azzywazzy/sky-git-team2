from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from application.models.customer import Customer


class RegistrationForm(FlaskForm):
    cus_first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=20)])
    cus_last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=20)])
    cus_email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField('Address', validators=[DataRequired()])
    phone = IntegerField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_cus_email(self, cus_email):
        cus_email = Customer.query.filter_by(cus_email=cus_email.data).first()
        if cus_email:
            raise ValidationError('That email address is already registered')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    hash_password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class PatientRegistrationForm(FlaskForm):
    pat_name = StringField('Pet Name', validators=[DataRequired(), Length(min=1, max=20)])
    species = StringField('Species', validators=[DataRequired(), Length(min=1, max=20)])
    breed = StringField('Breed', validators=[Optional()])
    sex = SelectField('Sex', choices=['F', 'M'], validators=[Optional()])
    date_of_birth = DateField('Date of Birth', format='%d/%m/%Y', validators=[Optional()])
    weight = IntegerField('Weight in Grammes', validators=[Optional()])
    chip_num = StringField('Chip number', validators=[Optional()])
    neutered_status = BooleanField('Neutered Status', validators=[Optional()])
    has_insurance = BooleanField('Has Insurance', validators=[Optional()])
    submit = SubmitField('Add Pet')


class PatientUpdateForm(FlaskForm):
    pat_name = StringField('Pet Name', validators=[DataRequired(), Length(min=1, max=20)])
    species = StringField('Species', validators=[DataRequired(), Length(min=1, max=20)])
    breed = StringField('Breed', validators=[Optional()])
    sex = SelectField('Sex', choices=['F', 'M'], validators=[Optional()])
    date_of_birth = DateField('Date of Birth', format='%d/%m/%Y', validators=[Optional()])
    weight = IntegerField('Weight in Grammes', validators=[Optional()])
    chip_num = StringField('Chip number', validators=[Optional()])
    neutered_status = BooleanField('Neutered Status', validators=[Optional()])
    has_insurance = BooleanField('Has Insurance', validators=[Optional()])
    submit = SubmitField('Save Changes')


class UpdateCustomerForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[Optional()])
    new_password = PasswordField('New Password', validators=[Optional()])
    confirm_password = PasswordField('Confirm Password', validators=[Optional(), EqualTo('new_password')])
    cus_first_name = StringField('First Name', validators=[Optional(), Length(min=1, max=20)])
    cus_last_name = StringField('Last Name', validators=[Optional(), Length(min=1, max=20)])
    address = StringField('Address', validators=[Optional()])
    phone = IntegerField('Phone Number', validators=[Optional()])
    submit = SubmitField('Save Changes')
