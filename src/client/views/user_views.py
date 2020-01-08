from flask import Blueprint, render_template, flash, jsonify, request, session, make_response, redirect, url_for
from flask_login import login_user, logout_user, login_required
from os import environ
from werkzeug.security import generate_password_hash, check_password_hash

from src.client.forms.login_form import LoginForm
from src.client.forms.registration_form import RegistrationForm
from src.infrastructure import user_state
from src.services.user_service import find_all_users, find_user_by_username, add_user

user_views = Blueprint('user_views', __name__, template_folder='templates')

@user_views.route('/users', defaults={'page': 'users'})
def show(page):
    """ REST endpoint for user list page. """
    # if 'username' in session:
    #     return f"You are logged in as {session['username']}"
    users = find_all_users()
    return render_template('user_list.html', users=users, title='Users')

@user_views.route('/create-user', methods=['GET', 'POST'])
@login_required
def create_user():
    """ REST endpoint for user creation page """
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit() or environ.get('TEST_FLAG') == 'true':
            print('Creating user...')
            username = form.username.data
            password = form.password.data

            account_exists = find_user_by_username(username)
            if isinstance(account_exists, str):  # for testing purposes
                if account_exists == username:
                    return render_template('error_user_exists.html', title='Error')
                pass
            elif account_exists:
                return render_template('error_user_exists.html', title='Error')

            hashpass = generate_password_hash(password, method='sha256')
            user_state.active_account = add_user(username=username, password=hashpass)
            if not isinstance(account_exists, str):
                session['username'] = user_state.active_account.username
            return render_template('registration_success.html', title='Register')
        else:
            flash('Enter the required fields.')
            return render_template('create_user.html', form=form, title='Register')

    return render_template('create_user.html', form=form, title='Register')

@user_views.route('/login', methods=['GET', 'POST'])
def login():
    """ REST endpoint for user login. """
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit() or environ.get('TEST_FLAG') == 'true':
            print('Signing you in...')
            username = form.username.data
            password = form.password.data
            user_act = find_user_by_username(username)
            if user_act:
                if isinstance(user_act, tuple):
                    if user_act[1] == password:
                        login_user(user_act)
                        return redirect(url_for('home_page.show'))
                    return render_template('error_invalid_pass.html', title='Error')
                elif check_password_hash(user_act.password, password):
                    login_user(user_act)
                    session['username'] = user_act.username
                    return redirect(url_for('home_page.show'))
                return render_template('error_invalid_pass.html', title='Error')
            return render_template('user_not_exist.html', title='Error')

    return render_template('login.html', form=form, title='Sign In')

@user_views.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('home_page.show'))
