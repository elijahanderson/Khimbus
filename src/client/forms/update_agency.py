from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, SelectField, StringField, validators
from wtforms.fields.html5 import DateField


class UpdateAgency(FlaskForm):
    cvalue = StringField('Old value: ', render_kw={'disabled': True})
    nvalue = StringField('New value: ', validators=[validators.optional(strip_whitespace=True)])
    update = SubmitField('Update')


class UpdateAgencySelect(FlaskForm):
    cvalue = StringField('Old value: ', render_kw={'disabled': True})
    nvalue = SelectField('Select new value: ')
    update = SubmitField('Update')


class UpdateAgencyBool(FlaskForm):
    cvalue = BooleanField('Old value: ', render_kw={'disabled': True})
    nvalue = BooleanField('Check or uncheck: ')
    update = SubmitField('Update')


class UpdateAgencyDate(FlaskForm):
    cvalue = StringField('Old value: ', render_kw={'disabled': True})
    nvalue = DateField('Enter new value: ', format='%Y-%m-%d')
    update = SubmitField('Update')