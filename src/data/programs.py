import mongoengine as me

from src.data.events import Event


class Program(me.Document):
    """
    Class used to represent a program.

    programID : friendly ID of the program
    name : the name of the program
    description : short description of the program
    modifiers : list of modifiers for the program (e.g. Adults only)
    service_ids : list of services the program offers
    """

    programID = me.IntField(required=True)
    name = me.StringField(required=True)
    description = me.StringField(required=False)
    modifiers = me.ListField(required=False)

    # weak relationships
    service_ids = me.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'programs'
    }