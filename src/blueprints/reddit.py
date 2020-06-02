from flask import Blueprint, render_template, abort, request
from flask_user import login_required
import requests
from uuid import uuid4
import urllib

import os

bp = Blueprint('reddit', __name__, url_prefix='/reddit')


@bp.route('/')
@login_required
def home():
    params = {
        "client_id": os.getenv('REDDIT_CLIENT_ID'),
        "response_type": "code",
        "state": str(uuid4()),
        "redirect_uri": os.getenv('REDDIT_REDIRECT_URI'),
        "duration": "temporary",
        "scope": "identity"
    }

    save_state(params)

    url = "https://ssl.reddit.com/api/v1/authorize?" + \
        urllib.parse.urlencode(params)

    return render_template('reddit/home.html', url=url)


def save_state(params):
    pass


def is_valid_state(params):
    return True


@bp.route('/authorize_callback')
@login_required
def authorize_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    state = request.args.get('state', '')
    if not is_valid_state(state):
        abort(403)

    code = request.args.get('code')
    token = get_token(code)
    user = get_user(token)
    return render_template('reddit/home.html', user=user)


def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth(os.getenv('REDDIT_CLIENT_ID'),
                                              os.getenv('REDDIT_CLIENT_SECRET'))
    post_data = {"grant_type": "authorization_code",
                 "code": code,
                 "redirect_uri": os.getenv('REDDIT_REDIRECT_URI')}
    response = requests.post("https://ssl.reddit.com/api/v1/access_token",
                             auth=client_auth,
                             data=post_data)
    response.raise_for_status()
    token_json = response.json()
    return token_json["access_token"]


def get_user(access_token):
    headers = {"Authorization": "bearer " + access_token}
    response = requests.get(
        "https://oauth.reddit.com/api/v1/me", headers=headers)
    me_json = response.json()
