"""
Configure the database schema
Create database models for the users
Create database models for the notes
"""

from . import db
from flask_login import UserMixin
# Look up on flask sqlalchemy for the relationships,
# here we have one to many, but it exists as well
# one to one
# many to one...
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # To associate the notes to a user, because they belong to a user,
    # we need to create a relationship between two object from different
    # dataase models. We do this with a FOREIGN KEY RELATIONSHIP.
    # It references and id to a differente database column
    # this is called one to many relationship because user with many notes
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    """
    Create a User instance.
    Define what information we want to be store in the instance,
    Configure the schema for the database store for the object.
    The first parameter of the .Columm() is the data type (the type of column).
    """
    # Create a unique key to identify uniquely a new object
    # so we can differenciate one user to another.
    id = db.Column(db.Integer, primary_key=True)
    # unique=True define that no user will have the same email address
    # It makes it invalid to create a user with an email address
    #  that already exist
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    # Everytime we create a note, add this note id
    # into the user notes relationship
    notes = db.relationship('Note')  # Ref the name of the class in capital
