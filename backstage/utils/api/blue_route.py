# -*- coding:utf-8 -*-


class BlueRoute(object):
    def __init__(self, blueprint, url_prefix):
        self.blueprint = blueprint
        self.url_prefix = url_prefix

    def route(self, rule, **options):
        url = self.url_prefix + rule
        return self.blueprint.route(url, **options)
