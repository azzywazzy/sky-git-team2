from application import db
from application.models.customer import Customer
from application.models.patient import Patient
from application.models.product import Product
from application.models.vet_personnel import VetPersonnel
from application.models.order_history import OrderHistory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

user = 'root'
password = 'password'
host = '127.0.0.1'
port = 3306
database = 'surgery'


def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database))


engine = get_connection()
Session = sessionmaker(bind=engine)

session = Session()

cus_orders = session.query(Customer).all()
for e in cus_orders:
    print(e.cus_last_name, e.orders)