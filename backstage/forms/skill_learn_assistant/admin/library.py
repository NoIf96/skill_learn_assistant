# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class LibraryData(FlaskForm):
    no = StringField('no', validators=[DataRequired(), Length(1, 10)])
    name = StringField('name', validators=[DataRequired(), Length(1, 20)])
    sort_major = StringField('sort_major', validators=[DataRequired(), Length(1, 8)])
    sort_secondary = StringField('sort_secondary', validators=[DataRequired(), Length(1, 8)])
    sort_language = StringField('sort_language', validators=[DataRequired(), Length(1, 8)])
    submit = SubmitField()
