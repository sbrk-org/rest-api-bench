# -*- coding: utf-8 -*-

import logging

from .models import (
    Session, Group, User
)


def seed(session):
    logging.info('Seeding')

    session_test = Session(
        id='test',
        name='Testing',
        is_active=True,
        subscription_opened='closed'
    )

    session_42 = Session(
        id='2014-42',
        name='Pathwar WEB 42 - 2014',
        is_active=False,
        subscription_opened='opened',
    )

    session.commit()
