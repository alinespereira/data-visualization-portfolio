from flask_user.forms import RegisterForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, DataRequired, EqualTo, Email
from flask_babel import lazy_gettext


class CustomRegisterForm(RegisterForm):
    username = StringField(lazy_gettext('Username'), [Length(min=4, max=25)])
    email = StringField(lazy_gettext('Email'), [
                        Length(min=6, max=35), Email()])

    first_name = StringField(lazy_gettext('First Name'), [DataRequired()])
    last_name = StringField(lazy_gettext('Last Name'), [DataRequired()])

    password = PasswordField(lazy_gettext('Password'), [DataRequired()])
    retype_password = PasswordField(lazy_gettext('Confirm your password'), [DataRequired(),
                                                                            EqualTo(
        'password', message='Passwords must match')
    ])
