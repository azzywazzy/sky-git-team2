from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#from application.forms import RegistrationForm, LoginForm



user = 'root'
password = 'password'
host = '127.0.0.1'
port = 3306
database = 'surgery'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
    user, password, host, port, database)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://username:password@host/database_name"
# app.config['SQLALCHEMY_DATABASE_URI']=('mysql+pymysql://' + getenv('MYSQL_USER') + ':' + getenv('MYSQL_PASSWORD') + '@' + getenv('MYSQL_HOST') + '/' + getenv('MYSQL_DB'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
#app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
from application import routes