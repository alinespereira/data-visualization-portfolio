from flask_user import UserManager
from flask_user.forms import LoginForm
from .forms import *


class CustomUserManager(UserManager):

    def customize(self, app):
        self.RegisterFormClass = CustomRegisterForm
        self.LoginFormClass = CustomLoginForm
