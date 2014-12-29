from .default import DefaultView
from .group import GroupView
from .session import SessionView

def register_views(app):
    # DEFAULT
    DefaultView.register(app)

    # GROUP
    GroupView.register(app)

    # SESSION
    SessionView.register(app)
