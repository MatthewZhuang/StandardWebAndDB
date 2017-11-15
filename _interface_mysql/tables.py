#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
 @description:
        we can create tables use orm way directly.
        But not use metadata way.
 @Time       : 17/11/15 下午11:39
 @Author     : guomianzhuang
"""
from sqlalchemy import Column
from sqlalchemy import Integer, Float, Numeric, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base(bind=None)


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)


class Train(Base):
    __tablename__ = 'train'
    id = Column(Integer, primary_key=True)
    train_info = Column(String(100))


