#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
 @description:
        
 @Time       : 17/11/15 下午11:16
 @Author     : guomianzhuang
"""
import sqlalchemy
from sqlalchemy import *
from config import config_default
from tables import Base

engine = None


def _create_engine():
    global engine
    if engine is not None:
        engine.connect().close()
    else:
        engine = create_engine("mysql+pymysql://%s:%s@%s:%s/%s?charset=%s", )
    return engine


def create_tables():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    print sqlalchemy.__version__
    engine = _create_engine()
    create_tables()

