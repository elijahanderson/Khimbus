import mongoengine as me
import datetime as dt

class Event(me.EmbeddedDocument):
    """
    Class used to represent an event.

    name : the name of the event
    datetime: date & time the event took place
    duration: the duration of the event
    staff_id: ID of the staff member involved -- weak relationship to the staff collection
    client_ids: the list of IDs of the clients involved -- weak relationship to the clients collection
    """
    name = me.StringField(required=True)
    datetime = me.DateTimeField(default=dt.datetime.now, required=True)
    duration = me.IntField(default=0)

    staff_id = me.ObjectIdField(required=True)
    client_ids = me.ListField()

    staff_id = None
    client_id_list = list()