import mongoengine as me

alias_core = 'core'
db = 'khimbus_db'

def global_init():
    """ Sets up global values required to connect to the database. """
    me.register_connection(alias=alias_core, name=db)