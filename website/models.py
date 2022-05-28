from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Another squema for notes
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # the data typed in the note
    data = db.Column(db.String(10000))
    # atomatically update the date of the note
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # A foriegh key from user squema to specify that this note belong to that user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# register database
# A class that inherit from db (our database) & UserMixin (flask login class)
class User(db.Model, UserMixin):
    # create the columns in the database
    # db.Column(column type, unique identifier) -> for the username and ids to be all unique
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    SSN= db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(250))
    id = db.Column(db.Integer)
