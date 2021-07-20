"""
Module that defines app DB adapter class
"""
from flask_mongoengine import MongoEngine


class Database:
    """
    Database adapter class
    """
    orm = MongoEngine()

    def init_app(self, app):
        """
        Init database on app context
        :param app:
        :return:
        """
        self.orm.init_app(app)

db = Database()
