# -*- coding:utf-8 -*-
"""
    入口文件
"""
from config import factory
from flask import url_for

# 通过工厂函数构建app实例
app = factory.create_app("development")
# app = factory.create_app("production")

@app.route("/")
def hello_world():
    print(app.config)
    print(app.url_map)
    print(url_for('static', filename='img/1.jpg'))

    # print(app.url_map)
    return "hello"


# 请求钩子，往cookie中写入csrf_token
# @app.after_request
# def after_request(response):
#     csrf_token = generate_csrf()
#     response.set_cookie("csrf_token", csrf_token)
#     return response


if __name__ == "__main__":
    # 运行flask app
    app.run()
