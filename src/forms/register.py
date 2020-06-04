from flask_user.forms import RegisterForm
from wtforms import StringField, PasswordField, validators
from flask_babel import lazy_gettext


class CustomRegisterForm(RegisterForm):
    username = StringField(lazy_gettext('Username'), [
                           validators.Length(min=4, max=25)])
    email = StringField(lazy_gettext('Email'), [
                        validators.Length(min=6, max=35), validators.Email()])

    first_name = StringField(lazy_gettext('First Name'), [
                             validators.DataRequired()])
    last_name = StringField(lazy_gettext('Last Name'), [
                            validators.DataRequired()])

    password = PasswordField(lazy_gettext('Password'), [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField(lazy_gettext('Confirm your password'))
