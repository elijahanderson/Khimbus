import mongoengine as me

class User(me.Document):
    """
    Class used to represent a user.

    username : the name of the user
    password : the password of the user
    """
    name = me.StringField(required=True, min_length=3)
    password = me.StringField(required=True, min_length=8)

    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }
