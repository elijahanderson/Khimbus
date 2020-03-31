from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, SelectField, StringField, SelectMultipleField, validators
from wtforms.fields.html5 import DateField

from src.infrastructure.client_helper import client_choices

class UpdateClient(FlaskForm):
    cvalue = StringField('Old value: ', render_kw={'disabled': True})
    nvalue = StringField('New value: ', validators=[validators.optional(strip_whitespace=True)])
    update = SubmitField('Update')


class UpdateClientSelect(FlaskForm):
    cvalue = StringField('Old value: ', render_kw={'disabled': True})
    nvalue = SelectField('Select new value: ')
    update = SubmitField('Update')


class UpdateClientSelectMultiple(FlaskForm):
    cvalue = StringField('Old value: ', render_kw={'disabled': True})
    nvalue = SelectMultipleField('Select new value: ')
    update = SubmitField('Update')


class UpdateClientDate(FlaskForm):
    cvalue = StringField('Old value: ', render_kw={'disabled': True})
    nvalue = DateField('Enter new value: ', format='%Y-%m-%d')
    update = SubmitField('Update')


class UpdateClientBool(FlaskForm):
    cvalue = BooleanField('Old value: ', render_kw={'disabled': True})
    nvalue = BooleanField('Check or uncheck: ')
    update = SubmitField('Update')


class UpdateClientDict(FlaskForm):
    field_to_update = SelectField('Select field to update: ')
    nvalue = StringField('New value: ', validators=[validators.optional(strip_whitespace=True)])
    update = SubmitField('Update')


class AddAddress(FlaskForm):
    type = SelectField('Address type*: ',
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
    update = SubmitField('Update')


class AddDisability(FlaskForm):
    disability = StringField('Enter client primary disability: ',
                             validators=[validators.optional(strip_whitespace=True)])
    disability_desc = StringField('Description of disability: ',
                                  validators=[validators.optional(strip_whitespace=True)])
    accommodations = StringField('Accommodations for disability: ',
                                 validators=[validators.optional(strip_whitespace=True)])
    update = SubmitField('Update')


class AddEmergencyContact(FlaskForm):
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
    update = SubmitField('Update')


class AddGuardian(FlaskForm):
    guardian_name = StringField('Guardian name: ', validators=[validators.optional(strip_whitespace=True),
                                                               validators.length(min=3, max=50)])
    guardian_type = SelectField('Guardian type: ', choices=client_choices['guardian_type'])
    guardian_phone = StringField('Guardian phone #: ', validators=[validators.optional(strip_whitespace=True),
                                                                   validators.length(min=10, max=14),
                                                                   validators.optional(strip_whitespace=True)])
    update = SubmitField('Update')
