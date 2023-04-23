from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models.customer import Customer


class RegistrationForm(FlaskForm):
    cus_first_name = StringField('First Name',
                                 validators=[DataRequired(), Length(min=1, max=20)])
    cus_last_name = StringField('Last Name',
                                 validators=[DataRequired(), Length(min=1, max=20)])

    cus_email = StringField('Email',
                            validators=[DataRequired(), Email()])
    address = StringField('Address',
                          validators=[DataRequired()])
    phone = IntegerField('Phone Number',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_cus_email(self, cus_email):
        cus_email = Customer.query.filter_by(cus_email=cus_email.data).first()
        if cus_email:
            raise ValidationError('That email address is already registered')

class LoginForm(FlaskForm):
    cus_email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')