from flask import Flask
from flask_pymongo import PyMongo
import yaml

from client.views.home_page import home_page
from client.views.about_page import about_page

with open('config/application.yml', 'r') as yml:
    conf = yaml.safe_load(yml)
    username = conf['mongouser']['username']
    pwd = conf['mongouser']['password']

app = Flask(__name__)
app.register_blueprint(home_page)
app.register_blueprint(about_page)
app.secret_key = "secret key"
app.config["MONGO_URI"] = "mongodb+srv://" + username + ":" + pwd + \
                          "@khimbus-fphpr.gcp.mongodb.net/test?retryWrites=true&w=majority"

mongo = PyMongo(app)
