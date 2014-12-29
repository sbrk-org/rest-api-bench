from .models import Session, Group


def seed_test(db):
    db.drop_all()
    db.create_all()

    sessions = {}
    sessions[1] = Session(
        name='Test Session #1',
        id='test-1',
        is_active=False,
        subscription_opened=False
    )
    sessions[2] = Session(
        name='Test Session #2',
        id='test-2',
        is_active=True,
        subscription_opened=True
    )
    sessions[3] = Session(
        name='Test Session #3',
        id='test-3',
        is_active=True,
        subscription_opened=True
    )
    for session in sessions.values(): db.session.add(session)

    groups = {}
    for group_id in xrange(1, 50):
        session_id = sessions.keys()[group_id % len(sessions.values())]
        session = sessions[session_id]

        groups[group_id] = Group(
            name='Test Team #{}'.format(group_id),
            session_id=session.id
        )
    for group in groups.values(): db.session.add(group)

    db.session.commit()


def seed_base(db):
    db.drop_all()
    db.create_all()

    sess_42 = Session(
        name='42 #1',
        id='42-1',
        is_active=False,
        subscription_opened=False
    )
    db.session.add(sess_42)

    db.session.commit()
