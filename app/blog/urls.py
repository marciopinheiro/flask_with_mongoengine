"""
Module that define blog urls
"""
from app.blog import blueprint
from app.blog.views import *


blueprint.add_url_rule(
    '/', view_func=Index.as_view(name='index'))

blueprint.add_url_rule(
    '/create', view_func=Create.as_view(name='create'))

blueprint.add_url_rule(
    '/<int:id>/update', view_func=Update.as_view(name='update'))

blueprint.add_url_rule(
    '/<int:id>/delete', view_func=Delete.as_view(name='delete'))
