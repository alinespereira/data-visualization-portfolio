from flask import g, request
from flask_babel import Babel

babel = Babel()


@babel.localeselector
def get_locale():
    current_user = g.get('user')
    if current_user and not current_user.is_anonymous:
        babel.app.logger.debug(current_user.locale)
        return current_user.locale
    return request.accept_languages.best_match(['pt', 'en'])


@babel.timezoneselector
def get_timezone():
    current_user = g.get('user')
    if current_user and not current_user.is_anonymous:
        babel.app.logger.debug(current_user.timezone)
        return current_user.timezone
