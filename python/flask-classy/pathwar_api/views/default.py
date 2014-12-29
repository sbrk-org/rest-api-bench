# -*- coding: utf-8 -*-


from flask.ext.classy import FlaskView, route


class DefaultView(FlaskView):
    route_base = '/'

    @route('/')
    def index(self):
        return 'Hello World.'
