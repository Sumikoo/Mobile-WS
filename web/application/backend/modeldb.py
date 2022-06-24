from application import db

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    password = db.Column(db.Text)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(100))
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.Text)
    token = db.Column(db.String(100))
    face = db.Column(db.String(100))
    created_at = db.Column(db.String(100))
    
class Files(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String(100))
    type_file = db.Column(db.String(100))
    size_file = db.Column(db.String(100))
    owner_file = db.Column(db.String(100))
    uploaded_at = db.Column(db.String(200))

db.create_all()