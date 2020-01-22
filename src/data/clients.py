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
    # names / identifying info
    clientID = me.StringField(required=False)
    firstname = me.StringField(required=True)
    lastname = me.StringField(required=True)
    middlename = me.StringField(required=False)
    suffix = me.StringField(required=False)
    gender = me.ListField(required=True)
    genderID = me.ListField(required=False)
    sexual_orientation = me.ListField(required=False)
    race = me.ListField(required=True)  # required, but can decline to provide
    ethnicity = me.ListField(required=False)
    ssn = me.IntField(required=True)
    site_location = me.StringField(required=True)
    # medicaid info -- { medicaid_number: int, effective_date: dt, expiration_date: dt }
    medicaid = me.DictField(required=False)

    # contact info
    phone_home = me.StringField(required=True)
    phone_cell = me.StringField(required=False)
    phone_work = me.StringField(required=False)
    email = me.StringField(required=True)
    contact_pref = me.StringField(required=False)
    # address info -- { address1: {type: (str: home, mother, father, etc.), street_adr: str, city: str, state: str, date: dt,
    #                          ZIP: int }, {address2: etc.. }}
    addresses = me.DictField(required=True)

    # guardian info -- { person1: {name: str, type: int (codes), effective_date: dt, enddate: dt, phone: int}}
    guardian_info = me.DictField(required=False)

    # emergency contact info -- { person1: {name: str, relationship: int (codes), phone: int, address: str, email: str,
    #                                      can_visit: bool, can_pickup: bool }}
    emergency_contacts = me.DictField(required=True)

    # demographic info
    dob = me.DateTimeField(required=True)
    intake_date = me.DateTimeField(required=True)
    discharge_date = me.DateTimeField(required=False)
    is_veteran = me.BooleanField(required=True)
    veteran_status = me.StringField(required=False)
    # marital history -- {status: str (single, etc.), start_date: dt, end_date: dt, div_reason: str}
    marital_hist = me.DictField(required=False)
    # disabilities -- {disability1: {name: str, description: str, accomodations: str }}
    disabilities = me.DictField(required=False)

    # employment / education
    employment_status = me.ListField(required=True)
    education_level = me.ListField(required=False)

    # languages
    spoken_langs = me.ListField(required=True)
    reading_langs = me.ListField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'clients'
    }
