# -*- coding:utf-8 -*-
import json
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from config.extensions import db


class AdminUser(db.Document, UserMixin):
    # 字段
    user_name = db.StringField(required=True, unique=True)
    password_hash = db.StringField(required=True)
    permission = db.StringField(required=True)

    @property
    def password(self):
        raise AttributeError("该属性不可读")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

    def dict_to_object(self, dict_):
        self.user_name = str(dict_.get("user_name"))
        if self.password_hash != str(dict_.get("password")):
            self.password_hash = generate_password_hash(str(dict_.get("password")))
        self.permission = str(dict_.get("permission"))

    def to_dict(self):
        dict_ = {
            "user_name": self.user_name,
            "password_hash": self.password_hash,
            "permission": self.permission,
        }
        return dict_

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def get_transform_keys():
        return ["permission"]

    @staticmethod
    def is_exist_key():
        return 'user_name'

    def __str__(self):
        return f"user_name:{self.user_name}"
