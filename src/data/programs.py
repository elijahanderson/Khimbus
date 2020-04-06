import mongoengine as me

from src.data.events import Event


class Program(me.EmbeddedDocument):
    """
    Class used to represent a program.

    agency_id : object ID of the agency the program belongs to -- weak relationship to the programs collection
    programID : friendly ID of the program
    name : the name of the program
    description : short description of the program
    modifiers : list of modifiers for the program (e.g. Adults only)
    services : embedded object list of services the program offers
    """
    # parent doc ID
    agency_id = me.ObjectIdField(required=True)

    programID = me.IntField(required=True)
    name = me.StringField(required=True)
    description = me.StringField(required=False)
    modifiers = me.ListField(required=False)

    # embedded collections
    services = me.EmbeddedDocumentListField(Event)

    meta = {
        'db_alias': 'core',
        'collection': 'programs'
    }
