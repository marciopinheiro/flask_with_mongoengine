"""
Module that define auth views
"""
from flask import flash, g, redirect, render_template, request, session, url_for
from flask.views import MethodView
from werkzeug.security import check_password_hash, generate_password_hash

from app.auth.models import User

__all__ = (
    'load_logged_in_user',
    'Register', 
    'Login', 
    'Logout'
)


def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.objects.filter(id=user_id).first()


class Register(MethodView):
    """
    Auth Register View class
    """
    template = 'auth/register.html'

    def get(self):
        return render_template(self.template)

    def post(self):
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif User.objects.filter(username=username).count() > 0:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            User.objects.create(
                username=username,
                password=generate_password_hash(password))

            flash('User has been created')
            return redirect(url_for('auth.login'))

        flash(error)
        return render_template(self.template)


class Login(MethodView):
    """
    Auth Login View class
    """
    template = 'auth/login.html'

    def get(self):
        return render_template(self.template)

    def post(self):
        username = request.form['username']
        password = request.form['password']

        user = User.objects.filter(username=username).first_or_404()
        error = None

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('index'))

        flash(error)
        return render_template(self.template)


class Logout(MethodView):
    """
    Auth Logout View class
    """
    def get(self):
        session.clear()
        return redirect(url_for('index'))
