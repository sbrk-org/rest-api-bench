# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import re

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from . import __version__


class Application(object):
    """ Base class for WSGI applications using the flask framework. """

    def __init__(self, name, version, config=None):
        # create the app
        self.flask_app = Flask(name, instance_relative_config=True)
        self.flask_app.version = __version__
        self.flask_app.url_map.strict_slashed = False
        self.flask_app.testing = True
        if config:
            self.flask_app.config.from_object(config)

    def print_url_map(self, stream=None):
        """ Prints URL map of the application. """
        if not stream:
            stream = sys.stdout

        # if pretty table is not installed, used pprint
        try:
            from prettytable_extras import PrettyTable
        except ImportError:
            from pprint import pprint
            pprint(self.flask_app.url_map, stream=stream)
            return

        fields = ['Path', 'Methods', 'Handler', 'Doc', 'Todo']
        table = PrettyTable(field_names=fields, sortby='Path', auto_width=True,
                            header_color='bold')
        # align left
        for field in fields:
            table._align[field] = 'l'

        for rule in self.flask_app.url_map.iter_rules():
            if rule.endpoint == 'static':
                continue

            methods = set(rule.methods)
            for silent_method in ('OPTIONS', 'HEAD'):
                if silent_method in methods:
                    methods.remove(silent_method)

            doc = self.flask_app.view_functions[rule.endpoint].__doc__
            if doc:
                doc_len = len(doc)
                todo = ' '.join(re.findall(r'todo::\s*(.*)$', doc, flags=re.M))
            else:
                doc_len, todo = 0, ''
            table.add_row([self._colorify_rule(rule.rule),
                           self._colorify_methods(methods),
                           rule.endpoint, doc_len, todo])

        print(table, file=stream)
        print('Total: %d rules' % len(table._rows), file=stream)

    @staticmethod
    def _colorify_methods(methods):
        """ Helper used by print_url_map.
        """
        replacement = {
            'GET':    '\033[1;34mGET\033[22;39m',     # GET:    bold-blue
            'PUT':    '\033[1;35mPUT\033[22;39m',     # PUT:    bold-magenta
            'DELETE': '\033[1;31mDELETE\033[22;39m',  # DELETE: bold-red
            'POST':   '\033[1;33mPOST\033[22;39m',    # POST:   bold-yellow
        }
        return ' '.join([replacement.get(method, method)
                         for method in methods])

    @staticmethod
    def _colorify_rule(rule):
        """ Helper used by print_url_map.
        """
        # Colorize normal parts in bold-blue
        # /abc/<def>/ghi/<klm>
        #  ^^^       ^^^
        rule = re.sub(r'/([^</]+)',
                      r'/\033[34;1m\1\033[39;22m', rule)
        # Colorize dynamic parts in bold-red and <> in gray
        # /abc/<def>/ghi/<klm>
        #      ^^^^^     ^^^^^
        rule = re.sub(r'<([^>]*)>',
                      r'\033[90m<\033[31;1m\1\033[90m>\033[39;22m', rule)
        # Colorize slashes in gray
        # /abc/<def>/ghi/<klm>
        # ^   ^     ^   ^
        rule = rule.replace('/', '\033[90m/\033[39m')
        return rule

    def create_db(self):
        self.db = SQLAlchemy(self.flask_app)
        from dictalchemy import make_class_dictable
        make_class_dictable(self.db.Model)
        return self.db

    def register_views(self):
        from .views import register_views
        register_views(self.flask_app)

    def register_models(self):
        from .models import register_models
        register_models(self.db)


def create_app(testing=False, config=None):
    """ App factory. """

    app = Flask('Pathwar', instance_relative_config=True)
    app.__version__ = __version__

    if config:
        app.config.from_object(config)

    if testing:
        app.testing = True

    return app


app = Application(name='Pathwar API', version=__version__, config='settings')
db = app.create_db()
flask_app = app.flask_app

app.register_views()
app.register_models()

app.print_url_map()

from .seeds import seed_test, seed_base
seed_test(db)
