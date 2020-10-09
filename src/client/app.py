from flask import Flask, session
from flask_login import LoginManager
from flask_mongoengine import MongoEngine
from logging.handlers import RotatingFileHandler
import logging
import sys
import yaml

from src.client.views.home_page import home_page
from src.client.views.about_page import about_page
from src.client.views.user_views import user_views
from src.client.views.client_views import client_views
from src.client.views.agency_views import agency_views
from src.services.user_service import find_user_by_username

with open('src/config/application.yml', 'r') as yml:
    conf = yaml.safe_load(yml)
    username = conf['mongo']['username']
    pwd = conf['mongo']['password']
    uri = conf['mongo']['uri']
    db = conf['mongo']['db']

mongo = MongoEngine()
login_manager = LoginManager()
# clear the contents of the log file
open('info.log', 'w').close()
log_hdlr = RotatingFileHandler('info.log', maxBytes=1000, backupCount=1)
log_hdlr.setLevel(logging.INFO)

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
app.logger.addHandler(log_hdlr)
app.register_blueprint(home_page)
app.register_blueprint(about_page)
app.register_blueprint(user_views)
app.register_blueprint(client_views)
app.register_blueprint(agency_views)
app.secret_key = "secret key"
app.config['MONGODB_DB'] = db
app.config['MONGODB_ALIAS'] = 'core'
app.config['MONGODB_HOST'] = "mongodb+srv://" + username + ":" + pwd + uri


mongo.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'user_views.login'
app.logger.info('App initialized')
# for some cruel, unknown, and godforsaken reason, mongodb will return an internal server error upon login unless some
# db query is executed in app.py:
user = find_user_by_username('')
# why???


@login_manager.user_loader
def load_user(name):
    return find_user_by_username(session['username'])
