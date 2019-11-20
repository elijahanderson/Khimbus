import mongoengine as me

from data.managing_offices import Office

class Agency(me.Document):
    """
    Class used to represent an agency.

    name : the name of the agency
    managing_offices : the embedded collection of offices that belong to an agency
    """
    name = me.StringField(required=True)

    # embedded collections
    managing_offices = me.EmbeddedDocumentListField(Office)

    meta = {
        'db_alias': 'core',
        'collection': 'agencies'
    }
