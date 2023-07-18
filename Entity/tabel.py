import email
from enum import unique
from app import app
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:P@ssword191394@localhost/flask_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class tabel1(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True)
    email=db.Column(db.String(80),unique=True)

    def __init__(self,username,email) -> None:
        self.username=username
        self.email=email
        

db.create_all()

