from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, SelectField, StringField, SelectMultipleField, validators
from wtforms.fields.html5 import DateField


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
