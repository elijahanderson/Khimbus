import mongoengine as me

class Program(me.Document):
    """
    Class used to represent a program.

    name : the name of the program
    agency_id: ID of the agency the program belongs to -- weak relationship to the programs collection
    """
    name = me.StringField(required=True)

    agency_id = me.ObjectIdField()

    meta = {
        'db_alias': 'core',
        'collection': 'programs'
    }
