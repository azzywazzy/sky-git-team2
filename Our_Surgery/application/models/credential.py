from application import db


class Credential(db.Model):
    cred_id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    user_type = db.Column(db.Integer, nullable=False)
    hash_password = db.Column(db.String(50), nullable=False)

