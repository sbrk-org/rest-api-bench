# -*- coding: utf-8 -*-

from flask.ext.alchemyview import AlchemyView


class BaseView(AlchemyView):
    def _response(self, data, template, status=200):
        print(data, template, status)
