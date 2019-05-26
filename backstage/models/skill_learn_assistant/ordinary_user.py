# -*- coding:utf-8 -*-
import json
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from config.extensions import db


class OrdinaryUser(db.Document, UserMixin):
    # 字段
    user_name = db.StringField(required=True, unique=True)
    user_email = db.EmailField(required=True, unique=True)
    password_hash = db.StringField(required=True)
    user_skill_list = db.ListField()
    recommend_skill_list = db.ListField()
    recommend_occupation_list = db.ListField()

    @property
    def password(self):
        raise AttributeError('该属性不可读')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

    def dict_to_object(self, dict_):
        self.user_name = str(dict_.get('user_name'))
        self.user_email = str(dict_.get('user_email'))
        if self.password_hash != str(dict_.get('password')):
            self.password_hash = generate_password_hash(str(dict_.get('password')))
        self.user_skill_list = list(dict_.setdefault('user_skill_list', []))
        self.recommend_skill_list = list(dict_.setdefault('recommend_skill_list', []))

    def to_dict(self):
        dict_ = {
            'user_name': self.user_name,
            'user_email': self.user_email,
            'password_hash': self.password_hash,
            'user_skill_list': self.use_skill_list,
            'recommend_skill_list': self.recommend_skill_list
        }
        return dict_

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def get_transform_keys():
        return ['user_skill_list', 'recommend_skill_list', 'recommend_occupation_list']

    @staticmethod
    def is_exist_key():
        return 'user_name'

    def __str__(self):
        return f"user_name:{self.user_name} - user_email:{self.user_email}"
