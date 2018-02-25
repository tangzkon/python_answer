import os


DEBUG = True

SECRET_KEY = os.urandom(24)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/db'

SQLALCHEMY_TRACK_MODIFICATIONS = False
