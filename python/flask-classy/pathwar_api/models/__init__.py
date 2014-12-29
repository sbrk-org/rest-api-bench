# -*- coding: utf-8 -*-

from ..app import db


keys = (
    'Column',
    'String', 'Integer', 'Boolean',
    'ForeignKey',
    'relationship',
)


for key in keys:
    locals()[key] = getattr(db, key)
Base = db.Model


from .base import (
    Group, Session, User
)

from .base import Session

def register_models(db):
    pass
