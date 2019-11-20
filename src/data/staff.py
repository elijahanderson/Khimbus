import mongoengine as me


class Staff(me.Document):
    """
    Class used to represent a staff member.

    name : the name of the staff member
    job_title : the job title of the staff member
    can_supervise: the boolean value indicating if staff member can supervise
    start_date: the date the staff member started employment
    email: the email of the staff member
    """
    name = me.StringField(required=True)
    job_title = me.StringField(required=True)
    can_supervise = me.BooleanField(default=False)
    start_date = me.DateTimeField(required=True)
    email = me.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'staff'
    }
