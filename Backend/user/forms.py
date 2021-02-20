from flask_wtf import FlaskForm
from wtforms import (BooleanField, FileField, PasswordField, StringField TextAreaField)
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
