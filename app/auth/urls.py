"""
Module that define auth urls
"""
from app.auth import blueprint
from app.auth.views import *


blueprint.before_app_request(
    load_logged_in_user)

blueprint.add_url_rule(
    '/register', view_func=Register.as_view(name='register'))

blueprint.add_url_rule(
    '/login', view_func=Login.as_view(name='login'))

blueprint.add_url_rule(
    '/logout', view_func=Logout.as_view(name='logout'))
