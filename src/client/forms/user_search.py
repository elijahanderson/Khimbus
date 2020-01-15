from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators


class UserSearchForm(FlaskForm):
    choices = [('Name', 'Name'),
               ('Username', 'Username'),
               ('Phone Number', 'Phone Number'),
               ('Email', 'Email')]
    search_by = SelectField('Search by: ', validators=[validators.required('Please select search category')],
                                           choices=choices)
    search = StringField('', validators=[validators.optional(strip_whitespace=True)])
