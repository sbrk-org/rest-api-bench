# -*- coding: utf-8 -*-

import colander as c

from .base import BaseView
from ..models import Session


class SessionSchema(c.MappingSchema):
    name = c.SchemaNode(c.String())


class SessionView(BaseView):
    """ Sessions view. """
    route_base = '/sessions'

    model = Session
    schema = SessionSchema

    #asdict_params = {'only': ['name']}

    def index2(self):
        return json.dumps(Session.query.all())
