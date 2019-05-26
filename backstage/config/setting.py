# -*- coding:utf-8 -*-
from utils.data.manager.mongo.constant import *


class BaseConfig(object):
    SECRET_KEY = "qWErNoIfMnbV"
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(BaseConfig):
    # 开发环境mongodb配置
    MONGODB_SETTINGS = {"db": DB, "host": CLIENT_DEVELOPMENT_HOST, "port": CLIENT_PORT}


class ProductionConfig(BaseConfig):
    # 生产环境mongodb配置
    MONGODB_SETTINGS = {
        "db": DB,
        "host": CLIENT_PRODUCTION_HOST,
        "port": CLIENT_PORT,
        "username": USER_NAME,
        "password": USER_PW,
        "authentication_source": AUTHENTICATION_SOUCRE,
    }


config = {"development": DevelopmentConfig, "production": ProductionConfig}
