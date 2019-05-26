# -*- coding:utf-8 -*-
import click
import logging
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from config.setting import config
from config.extensions import db, login_manager
from blueprints import skill_learn_assistant_bp
from utils.data.manager.log.manage import Manage
from algorithms.skill_learn_assistant.apis import algorithms_api


def create_app(config_name=None):
    if config_name is None:
        config_name = "development"

    app = Flask(__name__, static_folder='../data/img', static_url_path='/apis/img')
    CORS(app, supports_credentials=True)  # 跨域注册
    app.config.from_object(config[config_name])  # 加载配置信息
    register_logging(app)  # 注册日志
    register_extensions(app)  # 注册扩展
    register_blueprints(app)  # 注册蓝图
    register_commands(app)  # 注册命令

    # 注册算法管理
    algorithms_api.generate_blr_model(model_type="skill", key='main_skill')
    algorithms_api.generate_blr_model(model_type="occupation", key='main_occupation')
    algorithms_api.generate_blr_model(model_type="skill", key='config_skill')
    algorithms_api.generate_blr_model(model_type="occupation", key='config_occupation')
    return app


def register_logging(app):
    handler = Manage.get_handler("flask.log", logging.ERROR)
    app.logger.addHandler(handler)


def register_extensions(app):
    db.init_app(app)  # 注册数据库扩展类
    migrate = Migrate(app, db)
    login_manager.init_app(app)  # 注册用户管理类


def register_blueprints(app):
    register_blueprint_skill_learn_assistant(app)


def register_blueprint_skill_learn_assistant(app):
    app.register_blueprint(skill_learn_assistant_bp.admin_bp)
    app.register_blueprint(skill_learn_assistant_bp.ordinary_bp)


def register_commands(app):
    @app.cli.command()
    @click.option("--user_name", prompt=True, help="这是用户名")
    @click.option(
        "--password",
        prompt=True,
        hide_input=True,
        confirmation_prompt=True,
        help="这是密码",
    )
    def init(user_name, password):
        from models.skill_learn_assistant.admin_user import AdminUser

        click.echo("正在初始化数据库...")
        admin_user = AdminUser.objects.first()
        if admin_user:
            click.echo("超级管理员已存在，进行更新...")
            admin_user.user_name = user_name
            admin_user.password = password
        else:
            click.echo("新建超级管理员...")
            admin_user = AdminUser()
            admin_user.no = 1
            admin_user.user_name = user_name
            admin_user.password = password
            admin_user.permission = "1"
            admin_user.save()
        click.echo("结束")
