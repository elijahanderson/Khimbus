import mongoengine as me

class Client(me.Document):
    """
    Class used to represent a client.

    name : the name of the client
    age : the age of the client
    intake_date: the date the client entered agency care
    discharge_date: the date the client was discharged from agency care
    program_ids: list of IDs of the programs the client is registered in -- weak relationship to the programs collection
    """
    name = me.StringField(required=True)
    age = me.IntField(required=True)
    intake_date = me.DateTimeField(required=True)
    discharge_date = me.DateTimeField(required=True)

    program_ids = me.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'clients'
    }
