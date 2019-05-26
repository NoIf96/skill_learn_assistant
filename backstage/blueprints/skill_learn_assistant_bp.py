# -*- coding:utf-8 -*-
from flask import Blueprint

admin_bp = Blueprint('api_skill_learn_assistant_admin_bp', __name__, url_prefix='/api/skill_learn_assistant/admin')
ordinary_bp = Blueprint('api_skill_learn_assistant_bp', __name__, url_prefix='/api/skill_learn_assistant')

from apis import skill_learn_assistant


