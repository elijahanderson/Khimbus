from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, SelectField, validators

from src.infrastructure.user_helper import user_choices


class RegistrationForm(FlaskForm):
    username = StringField('Username: ', validators=[validators.required('Please enter valid username'),
                                                     validators.length(min=3, max=30),
                                                     validators.optional(strip_whitespace=True)])
    password = PasswordField('Password: ', validators=[validators.required('Please enter valid password'),
                                                       validators.length(min=8, max=30),
                                                       validators.equal_to('confirm', 'Passwords must match')])
    firstname = StringField('First name: ', validators=[validators.required('Please enter your first name'),
                                                        validators.length(min=2)])
    lastname = StringField('Last name: ', validators=[validators.required('Please enter your last name'),
                                                      validators.length(min=2),
                                                      validators.optional(strip_whitespace=True)])
    work_email = StringField('Work email: ', validators=[validators.required('Please enter valid email address'),
                                                         validators.email()])
    phone = StringField('Work phone: ', validators=[validators.optional(strip_whitespace=True),
                                                    validators.length(min=10, max=14)])
    job_title = SelectField('Job title: ', validators=[validators.required('Please enter job title')],
                            choices=user_choices['job_title'])

    # users = find_all_users()
    user_list = []
    # for user in list(users):
    #     user_list.append(user.firstname + ' ' + user.lastname)

    supervisor = SelectField('Supervisor: ',
                             validators=[validators.required('Please select supervisor or self supervised')],
                             choices=user_choices['supervisor'])
    confirm = PasswordField('Re-enter password: ')
    submit = SubmitField('Submit')
