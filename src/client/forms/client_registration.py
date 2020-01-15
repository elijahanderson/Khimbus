from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateTimeField, SelectField, BooleanField, SelectMultipleField, validators
from wtforms.fields.html5 import DateField


class ClientRegistration(FlaskForm):
    # names / identifying info
    clientID = StringField('MyEvolve Client ID (if applicable): ', validators=[validators.
                           optional(strip_whitespace=True)])
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
                         choices=[('', 'Select'),
                                  ('M', 'Male'),
                                  ('F', 'Female')])
    genderID = SelectField('Gender ID: ', choices=[('', 'Select'),
                                                   ('DA', 'Decline to answer'),
                                                   ('GV', 'Gender Variant'),
                                                   ('GQ', 'Intersex'),
                                                   ('M', 'Man'),
                                                   ('F', 'Woman'),
                                                   ('Ques', 'Questioning'),
                                                   ('Trans', 'Transgender'),
                                                   ('N/A', 'Not applicable due to age (0-17)')])
    sexual_orientation = SelectField('Sexual Orientation: ', choices=[('', 'Select'),
                                                                      ('Asex', 'Asexual'),
                                                                      ('BI', 'Bisexual'),
                                                                      ('DA', 'Decline to answer'),
                                                                      ('HS', 'Gay'),
                                                                      ('SH', 'Heterosexual'),
                                                                      ('Les', 'Lesbian'),
                                                                      ('Ques', 'Questioning'),
                                                                      ('N/A', 'Not applicable due to age (0-17)')])
    race = SelectField('Race*: ', validators=[validators.required('Please select race')],
                                 choices=[('', 'Select'),
                                          ('NA', 'Native American'),
                                          ('AP', 'Asian or Pacific Islander'),
                                          ('B', 'Black'),
                                          ('NH', 'Native Hawaiian'),
                                          ('IN', 'Indian or other Subcontinent Asian'),
                                          ('W', 'White'),
                                          ('OU', 'Other/Unknown')])
    ethnicity = SelectField('Ethnicity: ', choices=[('', 'Select'),
                                                    ('01', 'Hispanic or Latino'),
                                                    ('02', 'Non Hispanic or Latino')])

    ssn = StringField('Social Security # (No dashes, only numbers)*: ', validators=[validators.
                      required('Please enter a valid SSN'),
                                                            validators.optional(strip_whitespace=True),
                                                            validators.length(min=9, max=11)])
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
    contact_pref = SelectField('Contact preference: ', choices=[('', 'Select'),
                                                                ('Home', 'By home phone'),
                                                                ('Cell', 'By cell phone'),
                                                                ('Work', 'By work phone'),
                                                                ('Email', 'By email')])

    # Address Info -- { address1: {type: (str: home, mother, father, etc.), street_adr: str, city: str, state: str,
    #                          ZIP: int }, {address2: etc.. }}
    address_type = SelectField('Address type*: ',
                               validators=[validators.required('Please specify address type')],
                               choices=[('', 'Select'),
                                        ('Perm', 'Permanent Residence'),
                                        ('Rel', 'Relative\'s Home'),
                                        ('Temp', 'Temporary Residence'),
                                        ('Friend', 'Friend\'s Home'),
                                        ('HL', 'Homeless'),
                                        ('Office', 'Office'),
                                        ('OU', 'Other/Unknown')])
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

    # guardian info -- { person1: {name: str, type: int (codes), effective_date: dt, enddate: dt, phone: int}}
    guardian_name = StringField('Guardian name: ', validators=[validators.optional(strip_whitespace=True),
                                                               validators.length(min=3, max=50)])
    guardian_type = SelectField('Guardian type: ', choices=[('', 'Select'),
                                                            ('01', 'Parent'),
                                                            ('02', 'Relative'),
                                                            ('03', 'State Custody or Commissioner'),
                                                            ('04', 'Temporary'),
                                                            ('05', 'Protective'),
                                                            ('06', 'Emergency'),
                                                            ('10', 'Community Advocate'),
                                                            ('99', 'Other')])
    guardian_phone = StringField('Guardian phone #: ', validators=[validators.optional(strip_whitespace=True),
                                                                   validators.length(min=10, max=14),
                                                                   validators.optional(strip_whitespace=True)])
    # emergency contact info -- { person1: {name: str, relationship: int (codes), phone: int, address: str, email: str,
    #                                      can_visit: bool, can_pickup: bool }}
    ER_name = StringField('Emergency contact name*: ', validators=[validators.
                          required('Please enter valid emergency contact name'),
                                                                   validators.optional(strip_whitespace=True),
                                                                   validators.length(min=3, max=50)])
    ER_relationship = SelectField('Relationship to emergency contact: ',
                                  choices=[('', 'Select'),
                                           ('01', 'Punitive Father'),
                                            ('04', 'Mother'),
                                            ('05', 'Father'),
                                            ('06', 'Son'),
                                            ('07', 'Daughter'),
                                            ('08', 'Brother'),
                                            ('09', 'Sister'),
                                            ('10', 'Husband'),
                                            ('11', 'Wife'),
                                            ('12', 'Step Father'),
                                            ('13', 'Step Mother'),
                                            ('14', 'Step Sister'),
                                            ('15', 'Step Brother'),
                                            ('16', 'Aunt'),
                                            ('17', 'Uncle'),
                                            ('18', 'Cousin'),
                                            ('19', 'Niece'),
                                            ('20', 'Nephew'),
                                            ('21', 'Grand Mother'),
                                            ('22', 'Grand Father'),
                                            ('23', 'Grandson'),
                                            ('24', 'Granddaughter'),
                                            ('25', 'County Case Worker'),
                                            ('26', 'Babysitter'),
                                            ('27', 'Probation Officer'),
                                            ('28', 'Neighbor'),
                                            ('29', 'Friend'),
                                            ('30', 'Community Advocate'),
                                            ('31', 'Lawyer'),
                                            ('32', 'Mentor'),
                                            ('33', 'Reference for an Applicant'),
                                            ('34', 'Physician'),
                                            ('37', 'Adopted Child'),
                                            ('38', 'Dentist'),
                                            ('39', 'MH Practitioner'),
                                            ('43', 'Single Point Fixed Responsibility (SPFR)'),
                                            ('44', 'Other'),
                                            ('52', 'Guardian'),
                                            ('HHC', 'Home Health Coordinator')])
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

    # demographic info
    dob = DateField('Date of Birth*: ', validators=[validators.required('Please enter valid DOB')], format='%Y-%m-%d')
    intake_date = DateField('Intake Date*: ', validators=[validators.required('Please enter valid intake date')])
    discharge_date = DateField('Discharge Date: ')
    is_veteran = BooleanField('Is client a veteran?: ')
    veteran_status = SelectField('What is the veteran status of the client?: ', validators=[validators.
                                 optional(strip_whitespace=True)],
                                 choices=[('', 'Select'),
                                          ('Administratively Discharged', 'Administratively Discharged'),
                                          ('Punitively Discharged', 'Punitively Discharged'),
                                          ('Medically Retired', 'Medically Retired'),
                                          ('Career Veteran', 'Career Veteran'),
                                          ('Army', 'Army'),
                                          ('Navy/Marines/Coast Guard', 'Navy/Marines/Coast Guard'),
                                          ('Air Force', 'Air Force')])
    # marital history -- {status: str (single, etc.), start_date: dt, end_date: dt, div_reason: str}
    marital_status = SelectField('Marital status*: ',
                                 validators=[validators.required('Please select marital status')],
                                 choices=[('', 'Select'),
                                          ('Sin', 'Single'),
                                          ('Mar', 'Married'),
                                          ('Div', 'Divorced'),
                                          ('Wid', 'Widowed'),
                                          ('Sep', 'Separated'),
                                          ('DP', 'Domestic Partner'),
                                          ('RDP', 'Registered Domestic Partner'),
                                          ('OU', 'Other/Unknown')])
    # marriage_start = DateField('Marriage start date: ')
    # marriage_end = DateField('Marriage end date: ')
    div_reason = StringField('Reason for separation: ', validators=[validators.optional(strip_whitespace=True)])

    # disabilities -- {disability1: {name: str, description: str, accomodations: str }}
    disability = StringField('Enter client disability(ies): ', validators=[validators.optional(strip_whitespace=True)])
    disability_desc = StringField('Description of disability: ', validators=[validators.optional(strip_whitespace=True)])
    accomodations = StringField('Accomodations for disability: ', validators=[validators.optional(strip_whitespace=True)])

    # employment & education
    employment_status = SelectField('Select employment status: ',
                                    validators=[validators.required('Please select employment status of client')],
                                    choices=[('', 'Select'),
                                             ('01', 'Volunteer'),
                                             ('02', 'Part Time Student'),
                                             ('03', 'Work Adjustment Training'),
                                             ('04', 'Unemployed - seeking'),
                                             ('05', 'Unemployed - not seeking'),
                                             ('06', 'Transitional Employment Placement'),
                                             ('07', 'Homemaker'),
                                             ('09', 'Retired'),
                                             ('10', 'Disabled'),
                                             ('11', 'Inmate of Institution'),
                                             ('17', 'Unpaid Rehabiliational Activity (DUG)'),
                                             ('20', 'Full Time Student (DUG)'),
                                             ('24', 'Employed Full Time (DUG)'),
                                             ('25', 'Employed Part Time (DUG)'),
                                             ('28', 'Other Employment (DUG)'),
                                             ('29', 'Inactive in the community (DUG)'),
                                             ('99', 'Unknown (DUG)'),
                                             ('00', 'Not applicable due to age')])
    education_level = SelectField('Select highest education level: ',
                                  validators=[validators.required('Please enter highest education level')],
                                  choices=[('', 'Select'),
                                           ('AD', 'Associates Degree'),
                                           ('BD', 'Bachelors Degree'),
                                           ('DPG', 'Doctoral or Postgraduate'),
                                           ('ECE', 'Early Childhood Education'),
                                           ('HSGED', 'High School Graduate/GED'),
                                           ('Kin', 'Kindergarden'),
                                           ('Mas', 'Masters Degree'),
                                           ('NGC', 'No Grades Completed'),
                                           ('Pre', 'Preschool'),
                                           ('SC', 'Some College')])
    spoken_langs = SelectMultipleField('Select all spoken languages (Press CTRL & click to select multiple)*: ',
                                       validators=[validators.required('Please select any number of spoken languages')],
                                       choices=[('', 'Select'),
                                                ('Apache', 'Apache'),
                                                ('English', 'English'),
                                                ('Navajo', 'Navajo'),
                                                ('Other Native American', 'Other Native American'),
                                                ('Other/Unknown', 'Other/Unknown'),
                                                ('Sign Language', 'Sign Language'),
                                                ('Spanish', 'Spanish')])
    reading_langs = SelectMultipleField('Select all reading languages (Press CTRL & click to select multiple)*: ',
                                        validators=[validators.required('Please select any number of reading languages')],
                                        choices=[('', 'Select'),
                                                 ('Apache', 'Apache'),
                                                 ('English', 'English'),
                                                 ('Navajo', 'Navajo'),
                                                 ('Other Native American', 'Other Native American'),
                                                 ('Other/Unknown', 'Other/Unknown'),
                                                 ('Sign Language', 'Sign Language'),
                                                 ('Spanish', 'Spanish')])

    submit = SubmitField('Submit')
