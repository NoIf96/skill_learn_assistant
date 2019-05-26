# -*- coding:utf-8 -*-
import base64
from Crypto.Cipher import AES
from flask import jsonify


def json_data(data):
    return jsonify({"success": True, "data": data})


def json_data_error(data):
    return jsonify({"success": False, "data": data})


def json_list_data(data):
    return jsonify(
        {
            "success": True,
            "data": {"list": data.get("list")},
            "total": data.get("total"),
        }
    )


def json_list_data_error(data):
    return jsonify({"success": False, "data": {"list": data.get("list")}, "total": 0})


def is_exist(model, params, key):
    value = params.get(key)
    return model.objects(__raw__={key: value}).first()


def transform_key_value(model_objects, model_transform, transform_keys):
    new_model_objects = []
    for model_object in model_objects:
        for transform_key in transform_keys:
            model_object[transform_key] = {
                "label": model_transform[transform_key].get(
                    model_object[transform_key]
                ),
                "value": model_object[transform_key],
            }
        new_model_objects.append(model_object)
    return new_model_objects


key = 'NoIf-199796-IfNo'
iv = 'NoIf-199796-IfNo'
def aes_encrypt(data):
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(bytes(cryptor.encrypt(data))).decode('utf-8')


def aes_decrypt(encrypted):
    pass


if __name__ == '__main__':
    print(key)
    a = 'Hello, this is a secret message!'
    print(len(a))
    print(aes_encrypt(a))
