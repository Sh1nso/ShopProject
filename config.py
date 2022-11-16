import os

from constans import SQLALCHEMY_DATABASE_URI

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

