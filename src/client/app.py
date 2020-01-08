from flask import Flask, session
from flask_login import LoginManager
from flask_mongoengine import MongoEngine
import yaml

from client.views.home_page import home_page
from client.views.about_page import about_page
from client.views.user_views import user_views
from client.views.client_views import client_views
from src.services.user_service import find_user_by_username

with open('config/application.yml', 'r') as yml:
    conf = yaml.safe_load(yml)
    username = conf['mongouser']['username']
    pwd = conf['mongouser']['password']

mongo = MongoEngine()
login_manager = LoginManager()
app = Flask(__name__)
app.register_blueprint(home_page)
app.register_blueprint(about_page)
app.register_blueprint(user_views)
app.register_blueprint(client_views)
app.secret_key = "secret key"
app.config['MONGODB_DB'] = 'khimbus_db-dev'
app.config['MONGODB_ALIAS'] = 'core'
app.config["MONGODB_HOST"] = "mongodb+srv://" + username + ":" + pwd + \
                          "@khimbus-fphpr.gcp.mongodb.net/khimbus_db-dev?retryWrites=true&w=majority"

mongo.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'user_views.login'

@login_manager.user_loader
def load_user(name):
    return find_user_by_username(session['username'])
