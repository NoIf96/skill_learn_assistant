# -*- coding:utf-8 -*-
import json
from config.extensions import db


class Skill(db.Document):
    # 字段
    no = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    sort_major = db.StringField(required=True)
    sort_secondary = db.StringField(required=True)
    sort_language = db.StringField(required=True)
    sort_level = db.StringField()
    introduction = db.StringField()

    def dict_to_object(self, dict_):
        self.no = str(dict_.get("no"))
        self.name = str(dict_.get("name"))
        self.sort_major = str(dict_.get("sort_major"))
        self.sort_secondary = str(dict_.get("sort_secondary"))
        self.sort_language = str(dict_.get("sort_language"))
        self.introduction = str(dict_.get("introduction"))

    def to_dict(self):
        dict_ = {
            "no": self.no,
            "name": self.name,
            "sort_major": self.sort_major,
            "sort_secondary": self.sort_secondary,
            "sort_language": self.sort_language,
            "introduction": self.introduction,
        }
        return dict_

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def get_transform_keys():
        return ["sort_major", "sort_secondary", "sort_language"]

    @staticmethod
    def is_exist_key():
        return "no"

    def __str__(self):
        return f"no:{self.no} - name:{self.name}"
