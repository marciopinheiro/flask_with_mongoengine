from flask import Blueprint

blueprint = Blueprint("blog", __name__)

from . import urls
