from flask import Flask, render_template, session
from flask import (flash,
                   request,
                   redirect,
                   abort,
                   url_for)

from flask_user import login_required, roles_required
from src.custom_user_manager import CustomUserManager as UserManager
from src.db import db, User, UserRoles, Role

from src.blueprints import reddit

import os

app = Flask(__name__,
            template_folder='templates',
            static_folder='static',
            static_url_path='/')
app.config.from_object('src.config.Config')

app.register_blueprint(reddit)

db.init_app(app)
user_manager = UserManager(app, db, User)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/index')
@login_required
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')
