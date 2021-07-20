import os

from flask import Flask
from app.db import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=False)
    else:
        app.config.from_mapping(test_config)

    print(app.config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    from .auth import auth
    app.register_blueprint(auth)

    from .blog import blog
    app.register_blueprint(blog)

    app.add_url_rule('/', endpoint='index')

    return app
