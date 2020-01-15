from flask import Blueprint, render_template, abort, url_for, session

about_page = Blueprint('about_page', __name__, template_folder='templates')


@about_page.route('/about', defaults={'page': 'about'})
def show(page):
    """ REST endpoint for the about page. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    return render_template('about.html', title='About', href_var=href, sidebar_header='About', links={})
