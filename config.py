import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        'KDDFQDLUF4irAoxolWw6Ibo12v9eX8DMn0C'
