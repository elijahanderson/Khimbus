from flask import Blueprint, render_template, session, abort, url_for
from flask_login import login_required, current_user

home_page = Blueprint('home_page', __name__, template_folder='templates')

@home_page.route('/', defaults={'page': 'home'})
@home_page.route('/home', defaults={'page': 'home'})
@login_required
def show(page):
    """ REST endpoint for the home dashboard. """
    # if 'username' in session:
    #     return f"You are logged in as {session['username']}"
    return render_template('home.html', title='Home')
