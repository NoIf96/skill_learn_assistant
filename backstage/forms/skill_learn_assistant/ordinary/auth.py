# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    user_email = StringField('user_email', validators=[DataRequired(), Email(message="邮箱格式不正确")])
    password = PasswordField('password', validators=[DataRequired(), Length(4, 128)])
    submit = SubmitField()


class RegisterForm(FlaskForm):
    user_name = StringField('user_name', validators=[DataRequired(), Length(1, 20)])
    user_email = StringField('user_email', validators=[DataRequired(), Email(message="邮箱格式不正确")])
    password = PasswordField('password', validators=[DataRequired(), Length(4, 128)])
    submit = SubmitField()
