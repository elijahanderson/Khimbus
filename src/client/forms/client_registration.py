from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, BooleanField, \
    SelectMultipleField, validators
from wtforms.fields.html5 import DateField

from infrastructure.client_helper import client_choices


class ClientRegistration(FlaskForm):
    # names / identifying info
    clientID = IntegerField('MyEvolve Client ID: ', validators=[validators.required('Please enter valid ID number'),
                                                                validators.
                            optional(strip_whitespace=True),
                                                                validators.number_range(min=0, max=999999)])
    firstname = StringField('First name*: ', validators=[validators.required('Please enter valid first name'),
                                                         validators.length(min=2, max=50),
                                                         validators.optional(strip_whitespace=True)])
    lastname = StringField('Last name*: ', validators=[validators.required('Please enter valid last name'),
                                                       validators.length(min=2, max=50),
                                                       validators.optional(strip_whitespace=True)])
    middlename = StringField('Middle name: ', validators=[validators.length(min=2, max=30),
                                                          validators.optional(strip_whitespace=True)])
    suffix = StringField('Name suffix (Jr, Sr, etc.): ', validators=[validators.length(max=4),
                                                                     validators.optional(strip_whitespace=True)])
    gender = SelectField('Gender (M/F)*: ',
                         validators=[validators.required("Please select either 'M' for male or 'F' for female")],
                         choices=client_choices['gender'])
    genderID = SelectField('Gender ID: ', choices=client_choices['genderID'])
    sexual_orientation = SelectField('Sexual Orientation: ', choices=client_choices['sexual_orientation'])
    race = SelectField('Race*: ', validators=[validators.required('Please select race')],
                       choices=client_choices['race'])
    ethnicity = SelectField('Ethnicity: ', choices=client_choices['ethnicity'])
    religion = SelectField('Religion: ', choices=client_choices['religion'])

    ssn = StringField('Social Security # (No dashes, only numbers)*: ', validators=[validators.
                      required('Please enter a valid SSN'),
                                                                                    validators.
                      optional(strip_whitespace=True),
                                                                                    validators.length(min=9, max=11)])
    dln = StringField('Driver License Number: ', validators=[validators.length(min=10, max=12),
                                                             validators.optional(strip_whitespace=True)])
    site_location = StringField('Client site location*: ', validators=[validators.
                                required('Please enter valid site location'),
                                                                       validators.optional(strip_whitespace=True)])
    # medicaid info -- { medicaid_number: int, effective_date: dt, expiration_date: dt }
    medicaid_number = StringField('Medicaid #: ', validators=[validators.optional(strip_whitespace=True),
                                                              validators.length(min=12, max=14)])
    # medicaid_eff_date = DateField('Medicaid effective date: ', format='%Y-%m-%d')
    # medicaid_exp_date = DateField('Medicaid expiration date: ', format='%Y-%m-%d')

    # contact info
    phone_home = StringField('Home phone #: ', validators=[validators.optional(strip_whitespace=True),
                                                           validators.length(min=10, max=14),
                                                           validators.optional(strip_whitespace=True)])
    phone_cell = StringField('Cell phone #: ', validators=[validators.optional(strip_whitespace=True),
                                                           validators.length(min=10, max=14),
                                                           validators.optional(strip_whitespace=True)])
    phone_work = StringField('Work phone #: ', validators=[validators.optional(strip_whitespace=True),
                                                           validators.length(min=10, max=14),
                                                           validators.optional(strip_whitespace=True)])
    email = StringField('Client email: ', validators=[validators.email(),
                                                      validators.optional(strip_whitespace=True)])
    contact_pref = SelectField('Contact preference: ', choices=client_choices['contact_pref'])

    # Address Info -- { address1: {type: (str: home, mother, father, etc.), street_adr: str, city: str, state: str,
    #                          ZIP: int }, {address2: etc.. }}
    address_type = SelectField('Address type*: ',
                               validators=[validators.required('Please specify address type')],
                               choices=client_choices['type'])
    street_address = StringField('Street Address*: ', validators=[validators.
                                 required('Please enter valid street address'),
                                                                  validators.optional(strip_whitespace=True),
                                                                  validators.length(min=4, max=80)])
    city = StringField('City*: ', [validators.required('Please enter valid city'),
                                   validators.optional(strip_whitespace=True),
                                   validators.length(min=2, max=40)])
    state = StringField('State*: ', [validators.required('Please enter valid state'),
                                     validators.optional(strip_whitespace=True)])
    zip_code = StringField('ZIP code*: ', validators=[validators.required('Please enter valid ZIP code'),
                                                      validators.length(min=5, max=10)])

    address_type2 = SelectField('Address 2 type: ',
                               choices=client_choices['type'])
    street_address2 = StringField('Street Address 2: ', validators=[validators.optional(strip_whitespace=True),
                                                                     validators.length(min=4, max=80)])
    city2 = StringField('City 2: ', [validators.optional(strip_whitespace=True),
                                      validators.length(min=2, max=40)])
    state2 = StringField('State 2: ', [validators.optional(strip_whitespace=True)])
    zip_code2 = StringField('ZIP code 2: ', validators=[validators.length(min=5, max=10)])

    # guardian info -- { person1: {name: str, type: int (codes), effective_date: dt, enddate: dt, phone: int}}
    guardian_name = StringField('Guardian name: ', validators=[validators.optional(strip_whitespace=True),
                                                               validators.length(min=3, max=50)])
    guardian_type = SelectField('Guardian type: ', choices=client_choices['guardian_type'])
    guardian_phone = StringField('Guardian phone #: ', validators=[validators.optional(strip_whitespace=True),
                                                                   validators.length(min=10, max=14),
                                                                   validators.optional(strip_whitespace=True)])

    guardian_name2 = StringField('Guardian 2 name: ', validators=[validators.optional(strip_whitespace=True),
                                                                validators.length(min=3, max=50)])
    guardian_type2 = SelectField('Guardian 2 type: ', choices=client_choices['guardian_type'])
    guardian_phone2 = StringField('Guardian 2 phone #: ', validators=[validators.optional(strip_whitespace=True),
                                                                    validators.length(min=10, max=14),
                                                                    validators.optional(strip_whitespace=True)])

    # emergency contact info -- { person1: {name: str, relationship: int (codes), phone: int, address: str, email: str,
    #                                      can_visit: bool, can_pickup: bool }}
    ER_name = StringField('Emergency contact name*: ', validators=[validators.
                          required('Please enter valid emergency contact name'),
                                                                   validators.optional(strip_whitespace=True),
                                                                   validators.length(min=3, max=50)])
    ER_relationship = SelectField('Relationship to emergency contact: ',
                                  choices=client_choices['ER_relationship'])
    ER_phone = StringField('Emergency contact phone no.*: ', validators=[validators.
                           required('Please enter valid phone number'),
                                                                         validators.optional(strip_whitespace=True),
                                                                         validators.length(min=10, max=14)])
    ER_address = StringField('Street Address*: ', validators=[validators.required('Please enter valid address'),
                                                              validators.optional(strip_whitespace=True),
                                                              validators.length(min=4, max=100)])
    ER_email = StringField('Emergency contact email*: ', validators=[validators.email(),
                                                                     validators.required('Please enter a valid email'),
                                                                     validators.optional(strip_whitespace=True)])
    can_visit = BooleanField('Can emergency contact visit?: ')
    can_pickup = BooleanField('Can emergency contact pick client up?: ')

    ER_name2 = StringField('Emergency contact 2 name: ', validators=[validators.optional(strip_whitespace=True),
                                                                      validators.length(min=3, max=50)])
    ER_relationship2 = SelectField('Relationship to emergency contact 2: ', choices=client_choices['ER_relationship'])
    ER_phone2 = StringField('Emergency contact 2 phone no.: ', validators=[validators.optional(strip_whitespace=True),
                                                                            validators.length(min=10, max=14)])
    ER_address2 = StringField('Emergency contact 2 street address: ', validators=[validators.
                              optional(strip_whitespace=True),
                                                                                   validators.length(min=4, max=100)])
    ER_email2 = StringField('Emergency contact 2 email: ', validators=[validators.email(),
                                                                        validators.optional(strip_whitespace=True)])
    can_visit2 = BooleanField('Can emergency contact 2 visit?: ')
    can_pickup2 = BooleanField('Can emergency contact 2  pick client up?: ')

    # demographic info
    dob = DateField('Date of Birth*: ', validators=[validators.required('Please enter valid DOB')], format='%Y-%m-%d')
    intake_date = DateField('Intake Date*: ', validators=[validators.required('Please enter valid intake date')])
    discharge_date = DateField('Discharge Date: ')
    is_veteran = BooleanField('Is client a veteran?: ')
    veteran_status = SelectField('What is the veteran status of the client?: ', validators=[validators.
                                 optional(strip_whitespace=True)],
                                 choices=client_choices['veteran_status'])
    # marital history -- {status: str (single, etc.), start_date: dt, end_date: dt, div_reason: str}
    marital_status = SelectField('Marital status*: ',
                                 validators=[validators.required('Please select marital status')],
                                 choices=client_choices['marital_status'])
    # marriage_start = DateField('Marriage start date: ')
    # marriage_end = DateField('Marriage end date: ')
    div_reason = StringField('Reason for separation: ', validators=[validators.optional(strip_whitespace=True)])

    # disabilities -- {disability1: {name: str, description: str, accomodations: str }}
    disability = StringField('Enter client primary disability: ', validators=[validators.optional(strip_whitespace=True)])
    disability_desc = StringField('Description of disability: ',
                                  validators=[validators.optional(strip_whitespace=True)])
    accommodations = StringField('Accommodations for disability: ',
                                 validators=[validators.optional(strip_whitespace=True)])

    disability2 = StringField('Enter client secondary disability: ',
                              validators=[validators.optional(strip_whitespace=True)])
    disability_desc2 = StringField('Description of disability 2: ',
                                   validators=[validators.optional(strip_whitespace=True)])
    accommodations2 = StringField('Accommodations for disability 2: ',
                                  validators=[validators.optional(strip_whitespace=True)])


    # employment & education
    employment_status = SelectField('Select employment status: ',
                                    validators=[validators.required('Please select employment status of client')],
                                    choices=client_choices['employment_status'])
    education_level = SelectField('Select highest education level: ',
                                  validators=[validators.required('Please enter highest education level')],
                                  choices=client_choices['education_level'])
    spoken_langs = SelectMultipleField('Select all spoken languages (Press CTRL & click to select multiple)*: ',
                                       validators=[validators.required('Please select any number of spoken languages')],
                                       choices=client_choices['spoken_langs'])
    reading_langs = SelectMultipleField('Select all reading languages (Press CTRL & click to select multiple)*: ',
                                        validators=[
                                            validators.required('Please select any number of reading languages')],
                                        choices=client_choices['reading_langs'])

    submit = SubmitField('Submit')
