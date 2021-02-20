import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    # database parameters
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

   
