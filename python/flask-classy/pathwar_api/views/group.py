# -*- coding: utf-8 -*-

import colander as c

from .base import BaseView
from ..models import Group


class GroupSchema(c.MappingSchema):
    name = c.SchemaNode(c.String())


class GroupView(BaseView):
    """ Groups view. """
    route_base = '/groups'

    model = Group
    schema = GroupSchema

    #asdict_params = {'only': ['name']}
