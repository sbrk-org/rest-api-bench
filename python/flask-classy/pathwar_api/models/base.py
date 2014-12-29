# -*- coding: utf-8 -*-

#from sqlalchemy import (
#    Table, Column, Integer, ForeignKey, String, Boolean
#)
#from sqlalchemy.orm import relationship, backref
#from sqlalchemy.ext.declarative import declarative_base

from . import (
    db, Base,
    Column,
    String, Integer, Boolean,
    ForeignKey,
    relationship
)


class Session(Base):
    __tablename__ = 'session'

    # columns
    id = Column(String(16), primary_key=True)
    name = Column(String(64), nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    subscription_opened = Column(Boolean, default=False, nullable=False)

    # relationships
    groups = relationship('SessionGroup', backref='session')
    levels = relationship('SessionLevel', backref='session')


class Group(Base):
    __tablename__ = 'group'

    # columns
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    session_id = Column(Integer, ForeignKey('session.id'), nullable=False)

    # relationships
    #session = relationship('Session')
    #users = relationship('Users')
    #levels = relationship('Level')


class Achievement(Base):
    __tablename__ = 'achievement'

    # columns
    id = Column(Integer, primary_key=True)


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)


class Level(Base):
    __tablename__ = 'level'
    id = Column(Integer, primary_key=True)


class LevelStep(Base):
    __tablename__ = 'level_step'
    id = Column(Integer, primary_key=True)


class LevelHint(Base):
    __tablename__ = 'level_hint'
    id = Column(Integer, primary_key=True)


class Log(Base):
    __tablename__ = 'log'
    id = Column(Integer, primary_key=True)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)


# FIXME:
# - REDEEM/COUPON

class GroupLevel(Base):
    __tablename__ = 'group_level'
    id = Column(Integer, primary_key=True)


class GroupItem(Base):
    __tablename__ = 'group_item'
    id = Column(Integer, primary_key=True)


class GroupLevelHint(Base):
    __tablename__ = 'group_level_hint'
    id = Column(Integer, primary_key=True)


class GroupAchievement(Base):
    __tablename__ = 'group_achievement'
    id = Column(Integer, primary_key=True)


class SessionLevel(Base):
    __tablename__ = 'association_session_level'

    # columns
    session_id = Column(String(16), ForeignKey('session.id'), primary_key=True)
    level_id = Column(Integer, ForeignKey('level.id'), primary_key=True)

    # relationships
    level = relationship('Level', backref='session_assocs')


class SessionGroup(Base):
    __tablename__ = 'association_session_group'

    # columns
    session_id = Column(String(16), ForeignKey('session.id'), primary_key=True)
    group_id = Column(Integer, ForeignKey('group.id'), primary_key=True)

    # relationships
    group = relationship('Group', backref='session_assocs')
