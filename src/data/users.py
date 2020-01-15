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
    firstname = me.StringField(required=True)
    lastname = me.StringField(required=True)
    work_email = me.StringField(required=True)
    phone = me.StringField(required=False)
    job_title = me.StringField(required=True)
    supervisor = me.StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }
