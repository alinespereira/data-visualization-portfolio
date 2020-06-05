from flask_user.forms import LoginForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Length, DataRequired
from flask_babel import lazy_gettext


class CustomLoginForm(LoginForm):
    username = StringField(lazy_gettext(
        'Username or e-mail'), [Length(min=4, max=25)])
    password = PasswordField(lazy_gettext('Password'),
                             validators=[DataRequired()])

    remember_me = BooleanField(lazy_gettext('Remember me'))
