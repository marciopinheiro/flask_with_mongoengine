"""
Module that define auth models
"""
from app.db import db

__all__ = (
    'User',
)

class User(db.orm.Document):
    """
    Auth model class
    """
    meta = {
        'collection': 'users'
    }

    id = db.orm.SequenceField(
        primary_key=True)

    username = db.orm.StringField(
        unique=True, 
        null=False)

    password = db.orm.StringField(
        null=False)

    # posts = db.orm.relationship(
    #     "Post", back_populates="author", lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'
