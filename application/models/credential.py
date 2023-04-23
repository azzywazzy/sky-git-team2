from application import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    return Credential.query.get(int(id))


class Credential(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    user_type = db.Column(db.Integer, nullable=False)
    hash_password = db.Column(db.String, nullable=False)
