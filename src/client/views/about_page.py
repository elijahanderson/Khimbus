from flask import Blueprint, render_template, abort

about_page = Blueprint('about_page', __name__, template_folder='templates')

@about_page.route('/about', defaults={'page': 'about'})
def show(page):
    return render_template('about.html')