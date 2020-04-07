import mongoengine as me

from data.events import Event


class Service(me.Document):
    """
    Class used to represent a service.

    name : the name of the service
    events : the embedded collection of events that belong to a service
    """
    name = me.StringField(required=True)

    # embedded collections
    events = me.EmbeddedDocumentListField(Event)

    meta = {
        'db_alias': 'core',
        'collection': 'services'
    }
