from flask import Blueprint, render_template, flash, request, session, redirect, url_for
from flask_login import login_user, logout_user, login_required
from os import environ
import sys
from werkzeug.security import generate_password_hash, check_password_hash

from src.client.forms.login_form import LoginForm
from src.client.forms.registration_form import RegistrationForm
from src.client.forms.update_user import UpdateUser, UpdateUserBool, UpdateUserSelect
from src.client.forms.user_search import UserSearchForm
from src.infrastructure import user_state
from src.infrastructure.user_helper import user_choices
from src.services.user_service import find_all_users, find_user_by_username, find_user_by_name, find_user_by_phone, \
    find_user_by_email, add_user, destroy_user, repopulate_user

user_views = Blueprint('user_views', __name__, template_folder='templates')
links = {'Register New User': '/create-user'}


@user_views.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    """ REST endpoint for user list page. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
        is_admin = find_user_by_username(session['username']).is_admin
    form = UserSearchForm()
    user_list = find_all_users()
    user_urls = []
    for user in user_list:
        user_urls.append('/user/' + user.username)

    if request.method == 'POST':
        if form.validate_on_submit():
            search_by = form.search_by.data
            criteria = form.search.data

            if search_by == 'Username':
                user = find_user_by_username(criteria)
                if user:
                    return redirect(url_for('user_views.display_user', username=user.username, href_var=href,
                                            sidebar_header='User', links=links, is_admin=is_admin))
                else:
                    return render_template('user_dashboard.html', form=form, users=user_list, user_urls=user_urls,
                                           title='Users', href_var=href, sidebar_header='User', links=links,
                                           user_exists='False')
            elif search_by == 'Name':
                user = find_user_by_name(criteria)
                if user:
                    return redirect(url_for('user_views.display_user', username=user.username, href_var=href,
                                            sidebar_header='User', links=links, is_admin=is_admin))
                else:
                    return render_template('user_dashboard.html', form=form, users=user_list, user_urls=user_urls,
                                           title='Users', href_var=href, sidebar_header='User', links=links,
                                           user_exists='False')
            elif search_by == 'Phone Number':
                user = find_user_by_phone(criteria)
                if user:
                    return redirect(url_for('user_views.display_user', username=user.username, href_var=href,
                                            sidebar_header='User', links=links, is_admin=is_admin))
                else:
                    return render_template('user_dashboard.html', form=form, users=user_list, user_urls=user_urls,
                                           title='Users', href_var=href, sidebar_header='User', links=links,
                                           user_exists='False', is_admin=is_admin)
            elif search_by == 'Email':
                user = find_user_by_email(criteria)
                if user:
                    return redirect(url_for('user_views.display_user', username=user.username, href_var=href,
                                            sidebar_header='User', links=links, is_admin=is_admin))
                else:
                    return render_template('user_dashboard.html', form=form, users=user_list, user_urls=user_urls,
                                           title='Users', href_var=href, sidebar_header='User', links=links,
                                           user_exists='False')
            else:
                return redirect(url_for('user_views.users'))

    return render_template('user_dashboard.html', form=form, users=user_list, user_urls=user_urls, title='Users',
                           href_var=href, sidebar_header='User', links=links)


@user_views.route('/user/<username>', methods=['GET'])
@login_required
def display_user(username):
    """ REST endpoint for a specific client. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
        is_admin = find_user_by_username(session['username']).is_admin
    user = find_user_by_username(username)
    update_url = '/update-user/' + username
    delete_url = '/delete-user/' + username
    return render_template('display_user.html', update_url=update_url, delete_url=delete_url, user=user,
                           title=user.firstname, href_var=href, sidebar_header='User', links=links, is_admin=is_admin)


@user_views.route('/create-user', methods=['GET', 'POST'])
@login_required
def create_user():
    """ REST endpoint for user creation page """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
        is_admin = find_user_by_username(session['username']).is_admin
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit() or environ.get('TEST_FLAG') == 'true':
            print('Creating user...')
            username = form.username.data
            password = form.password.data

            account_exists = find_user_by_username(username)
            if account_exists:
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
                                                 supervisor=form.supervisor.data,
                                                 is_admin=form.is_admin.data)
            session['username'] = user_state.active_account.username
            return render_template('registration_success.html', title='Register', href_var=href, sidebar_header='User',
                                   links=links)
        else:
            flash('Enter the required fields.')
            return render_template('create_user.html', form=form, title='Register', href_var=href,
                                   sidebar_header='User', links=links, is_admin=is_admin)

    return render_template('create_user.html', form=form, title='Register', href_var=href, sidebar_header='User',
                           links=links, is_admin=is_admin)


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
                if check_password_hash(user_act.password, password):
                    login_user(user_act)
                    session['username'] = user_act.username
                    return redirect(url_for('home_page.show', href_var=href, sidebar_header='User', links=links))
                return render_template('login.html', title='Error', href_var=href, sidebar_header='User',
                                       links=links, form=form, pass_success='False')
            return render_template('login.html', title='Error', href_var=href, sidebar_header='User',
                                   links=links, form=form, user_found='False')

    return render_template('login.html', form=form, title='Log In', href_var=href, sidebar_header='User', links=links)


@user_views.route('/logout')
@login_required
def logout():
    """ REST endpoint for user logout. """
    logout_user()
    session.clear()
    return render_template('logged_out.html', title='Logout', href_var='/users', sidebar_header='Home', links=links)


@user_views.route('/update-user/<username>', methods=['GET'])
@login_required
def update_user(username):
    """ REST endpoint for updating user information. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
        is_admin = find_user_by_username(session['username']).is_admin
    user = find_user_by_username(username)
    if session['username'] == username or session['username'] == 'eanderson':
        return render_template('update_user.html', title='Update User', href_var=href, sidebar_header='User',
                               links=links, user=user)
    update_url = '/update-user/' + username
    delete_url = '/delete-user/' + username
    return render_template('display_user.html', update_url=update_url, delete_url=delete_url, user=user,
                           title=username, href_var=href, sidebar_header='User', links=links,
                           update_success='False', is_admin=is_admin)


@user_views.route('/update-user-field/<username>-<field>', methods=['GET', 'POST'])
@login_required
def update_field(username, field):
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
        is_admin = find_user_by_username(session['username']).is_admin
    update_url = '/update-user/' + username
    delete_url = '/delete-user/' + username
    user = find_user_by_username(username)
    form = UpdateUser()
    if field == 'job_title' or field == 'supervisor':
        form = UpdateUserSelect()
        form.cvalue.data = user[field]
        form.nvalue.choices = user_choices[field]
    elif field == 'is_admin':
        form = UpdateUserBool()
        form.cvalue.data = user[field]
    else:
        form.cvalue.data = user[field]

    if request.method == 'POST':
        if form.validate_on_submit():
            updated_user = repopulate_user(username, field, form.nvalue.data)
            if updated_user:
                return render_template('display_user.html', user=updated_user, title='Update Success',
                                       sidebar_header='User', href_var=href, links=links, delete_url=delete_url,
                                       update_url=update_url, update_success='True', is_admin=is_admin)
            return render_template('display_user.html', user=user, title='Update Success', sidebar_header='User',
                                   href_var=href, links=links, delete_url=delete_url, update_url=update_url,
                                   update_success='False', is_admin=is_admin)

    return render_template('update_field.html', title='Update User', href_var=href, sidebar_header='User',
                           links=links, form=form)


@user_views.route('/delete-user/<username>', methods=['GET'])
@login_required
def delete_user(username):
    """ REST endpoint to handle user destruction. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
        is_admin = find_user_by_username(session['username']).is_admin
    update_url = '/update-user/' + username
    delete_url = '/delete-user/' + username
    user = find_user_by_username(username)
    # must be logged in as user or sys admin to delete
    if session['username'] == username or session['username'] == 'eanderson' or is_admin:
        delete_successful = destroy_user(username)
        if delete_successful:
            return render_template('user_deleted.html', title='User', href_var=href, sidebar_header='User', links=links)
        return render_template('display_user.html', title='User', href_var=href, sidebar_header='User', links=links,
                               delete_success='False-Server')
    return render_template('display_user.html', update_url=update_url, delete_url=delete_url, user=user,
                           title=username, href_var=href, sidebar_header='User', links=links,
                           delete_success='False-Admin')

