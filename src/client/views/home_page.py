from flask import Blueprint, render_template, abort

home_page = Blueprint('home_page', __name__, template_folder='templates')

@home_page.route('/', defaults={'page': 'home'})
def show(page):
    return render_template('home.html')