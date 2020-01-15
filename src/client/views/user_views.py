from flask import Blueprint, render_template, flash, jsonify, request, session, make_response, redirect, url_for
from flask_login import login_user, logout_user, login_required
from os import environ
from werkzeug.security import generate_password_hash, check_password_hash

from src.client.forms.login_form import LoginForm
from src.client.forms.registration_form import RegistrationForm
from src.client.forms.user_search import UserSearchForm
from src.infrastructure import user_state
from src.services.user_service import find_all_users, find_user_by_username, find_user_by_name, find_user_by_phone, \
    find_user_by_email, add_user

user_views = Blueprint('user_views', __name__, template_folder='templates')
links = {}


@user_views.route('/users', methods=['GET', 'POST'])
def users():
    """ REST endpoint for user list page. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    form = UserSearchForm()
    user_list = find_all_users()
    if request.method == 'POST':
        if form.validate_on_submit():
            search_by = form.search_by.data
            criteria = form.search.data

            if search_by == 'Username':
                user = find_user_by_username(criteria)
                if user:
                    return redirect(url_for('user_views.display_user', username=user.username, href_var=href,
                                            sidebar_header='User', links=links))
                else:
                    return render_template('error_user_dne.html', title='Error', href_var=href, sidebar_header='User',
                                           links=links)
            elif search_by == 'Name':
                user = find_user_by_name(criteria)
                if user:
                    return redirect(url_for('user_views.display_user', username=user.username, href_var=href,
                                            sidebar_header='User', links=links))
                else:
                    return render_template('error_user_dne.html', title='Error', href_var=href, sidebar_header='User',
                                           links=links)
            elif search_by == 'Phone Number':
                user = find_user_by_phone(criteria)
                if user:
                    return redirect(url_for('user_views.display_user', username=user.username, href_var=href,
                                            sidebar_header='User', links=links))
                else:
                    return render_template('error_user_dne.html', title='Error', href_var=href, sidebar_header='User',
                                           links=links)
            elif search_by == 'Email':
                user = find_user_by_email(criteria)
                if user:
                    return redirect(url_for('user_views.display_user', username=user.username, href_var=href,
                                            sidebar_header='User', links=links))
                else:
                    return render_template('error_user_dne.html', title='Error', href_var=href, sidebar_header='User',
                                           links=links)
            else:
                return render_template('user_list.html', users=user_list, form=form, title='Users', href_var=href,
                                       sidebar_header='User', links=links)

    return render_template('user_list.html', form=form, users=user_list, title='Users', href_var=href,
                           sidebar_header='User', links=links)


@user_views.route('/user/<username>', methods=['GET'])
def display_user(username):
    """ REST endpoint for a specific client. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    user = find_user_by_username(username)
    return render_template('display_user.html', username=username, user=user, title=user.firstname, href_var=href,
                           sidebar_header='User', links=links)


@user_views.route('/create-user', methods=['GET', 'POST'])
@login_required
def create_user():
    """ REST endpoint for user creation page """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit() or environ.get('TEST_FLAG') == 'true':
            print('Creating user...')
            username = form.username.data
            password = form.password.data

            account_exists = find_user_by_username(username)
            if isinstance(account_exists, str):  # for testing purposes
                if account_exists == username:
                    return render_template('error_user_exists.html', title='Error', href_var=href,
                                           sidebar_header='User', links=links)
                pass
            elif account_exists:
                return render_template('error_user_exists.html', title='Error', href_var=href, sidebar_header='User',
                                       links=links)

            hashpass = generate_password_hash(password, method='sha256')
            user_state.active_account = add_user(username=username,
                                                 password=hashpass,
                                                 firstname=form.firstname.data,
                                                 lastname=form.lastname.data,
                                                 work_email=form.work_email.data,
                                                 phone=form.phone.data,
                                                 job_title=form.job_title.data,
                                                 supervisor=form.supervisor.data)
            if not isinstance(account_exists, str):
                session['username'] = user_state.active_account.username
            return render_template('registration_success.html', title='Register', href_var=href, sidebar_header='User',
                                   links=links)
        else:
            flash('Enter the required fields.')
            return render_template('create_user.html', form=form, title='Register', href_var=href,
                                   sidebar_header='User', links=links)

    return render_template('create_user.html', form=form, title='Register', href_var=href, sidebar_header='User',
                           links=links)


@user_views.route('/login', methods=['GET', 'POST'])
def login():
    """ REST endpoint for user login. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
        return redirect(url_for('home_page.show', href_var=href, sidebar_header='User', links=links))
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
                    return render_template('error_invalid_pass.html', title='Error', href_var=href,
                                           sidebar_header='User', links=links)
                elif check_password_hash(user_act.password, password):
                    login_user(user_act)
                    session['username'] = user_act.username
                    return redirect(url_for('home_page.show', href_var=href, sidebar_header='User', links=links))
                return render_template('error_invalid_pass.html', title='Error', href_var=href, sidebar_header='User',
                                       links=links)
            return render_template('user_not_exist.html', title='Error', href_var=href, sidebar_header='User',
                                   links=links)

    return render_template('login.html', form=form, title='Log In', href_var=href, sidebar_header='User', links=links)


@user_views.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    return render_template('logged_out.html', title='Logout', href_var='/users', sidebar_header='Home', links=links)
