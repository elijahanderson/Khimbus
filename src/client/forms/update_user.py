from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField, validators


class UpdateUser(FlaskForm):
    cvalue = StringField('Old value: ', render_kw={'disabled': True})
    nvalue = StringField('New value: ', validators=[validators.optional(strip_whitespace=True)])
    update = SubmitField('Update')


class UpdateUserSelect(FlaskForm):
    cvalue = StringField('Old value: ', render_kw={'disabled': True})
    nvalue = SelectField('Select new value: ')
    update = SubmitField('Update')
