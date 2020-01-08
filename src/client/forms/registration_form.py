from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, validators

class RegistrationForm(FlaskForm):
    username = StringField('Username: ', validators=[validators.required('Please enter valid username'),
                                                     validators.length(min=3, max=30)])
    password = PasswordField('Password: ', validators=[validators.required('Please enter valid password'),
                                                       validators.length(min=8, max=30),
                                                       validators.equal_to('confirm', 'Passwords must match')])
    confirm = PasswordField('Re-enter password: ')
    submit = SubmitField('Submit')
