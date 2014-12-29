# -*- coding: utf-8 -*-

import logging
import os

from pathwar_api import __version__
from pathwar_api.app import flask_app


def main(environ=None, start_response=None):
    env = os.environ.get('API_ENV', 'dev')

    if env == 'production':
        # FIXME:
        # - sentry
        # - syslog
        pass
    else:
        logging.basicConfig(level=logging.INFO)

    with flask_app.app_context():
        if environ:
            flask_app.wsgi_app(environ, start_response)
        else:
            flask_app.run(
                host='0.0.0.0',
                port=9191,
                debug=env != 'production',
            )

if __name__ == "__main__":
    main()
