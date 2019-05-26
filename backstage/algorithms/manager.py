# -*- coding:utf-8 -*-
from algorithms.skill_learn_assistant import recommended_system


class Manager(object):
    __instance = None
    __create = False
    _attr = {}

    def __init__(self):
        if self.__create is False:
            self._register_attr()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Manager, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    @classmethod
    def _register_attr(cls):
        cls.__create = True
        for item in recommended_system.available:
            try:
                setattr(cls, f"__{item.title}_dict", {})
                setattr(cls, f"get_{item.title}_object", cls.__get_get_func(item))
                setattr(cls, f"set_{item.title}_object", cls.__get_set_func(item))
                setattr(cls, f"set_{item.title}_object", cls.__get_del_func(item))
                cls._attr[item.title] = {
                    "attribute": f"__{item.title}_dict",
                    "function": (
                        f"get_{item.title}_object",
                        f"set_{item.title}_object",
                        f"del_{item.title}_object",
                    ),
                }
            except AttributeError:
                continue

    @classmethod
    def __get_get_func(cls, item):
        def get_object(self, key="main"):
            return getattr(cls, f"__{item.title}_dict").setdefault(key, item.create_object())

        return get_object

    @classmethod
    def __get_set_func(cls, item):
        def set_object(self, item_object, key="main"):
            getattr(cls, f"__{item.title}_dict")[key] = item_object

        return set_object

    @classmethod
    def __get_del_func(cls, item):
        def del_object(self, key="main"):
            getattr(cls, f"__{item.title}_dict").setdefault(key, None)
            del getattr(cls, f"__{item.title}_dict")[key]

        return del_object


