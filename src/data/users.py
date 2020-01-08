import mongoengine as me
from flask_login import UserMixin

class User(UserMixin, me.Document):
    """
    Class used to represent a user.

    username : the name of the user
    password : the password of the user
    """
    username = me.StringField(required=True, min_length=3)
    password = me.StringField(required=True, min_length=8)

    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }
