"""
Module that define blog utils
"""
from flask import g, abort
from .models import Post


def get_post(post_id, check_author=True):
    """
    Get post by id and check owner
    :param post_id:
    :param check_author:
    :return:
    """
    post = Post.objects.get(id=post_id)

    if post is None:
        abort(404, f"Post id {post_id} doesn't exist.")

    if check_author and post.author.id != g.user.id:
        abort(403)

    return post
