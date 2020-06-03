from flask_user.forms import RegisterForm
from wtforms import StringField, PasswordField, validators


class CustomRegisterForm(RegisterForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField(
        'Email Address', [validators.Length(min=6, max=35), validators.Email()])

    first_name = StringField('First Name', [validators.DataRequired()])
    last_name = StringField('Last Name', [validators.DataRequired()])

    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
