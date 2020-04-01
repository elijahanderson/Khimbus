import mongoengine as me


class Office(me.EmbeddedDocument):
    """
    Class used to represent a managing office of an agency.

    name : the name of the managing office
    agency_id : the ID of the agency the office belongs to
    """
    name = me.StringField(required=True)
    agency_id = me.ObjectIdField(required=True)
