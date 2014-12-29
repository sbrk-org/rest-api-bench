import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

#SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/pathwar_api.db'
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
CSRF_SESSION_LKEY = ''

SECRET_KEY = ''

SITE_TITLE = 'Pathwar API'
