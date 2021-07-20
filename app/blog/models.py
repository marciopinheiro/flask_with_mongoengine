"""
Module that define blog models
"""
from datetime import datetime
from app.db import db


class Post(db.orm.Document):
    """
    Post model class
    """
    meta = {
        'collection': 'posts'
    }

    id = db.orm.SequenceField(
        primary_key=True)

    author = db.orm.ReferenceField(
        "User", 
        reverse_delete_rule=db.orm.DENY,
        null=False)

    created = db.orm.DateTimeField(
        null=False, 
        default=datetime.utcnow)

    title = db.orm.StringField(
        unique=True, 
        null=False)

    body = db.orm.StringField(
        null=False)

    def __repr__(self):
        return f'<Post {self.title}>'
