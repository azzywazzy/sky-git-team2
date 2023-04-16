from application import db


class VetPersonnel(db.Model):
    __tablename__ = "vet_personnel"
    vet_id = db.Column(db.Integer, primary_key=True, nullable=False)
    vet_first_name = db.Column(db.String(50), nullable=False)
    vet_last_name = db.Column(db.String(50), nullable=False)
    vet_department = db.Column(db.String(50), nullable=True)
    vet_role = db.Column(db.String(50), nullable=True)


