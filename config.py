import os


class Config(object):
    ENV = os.environ.get('FLASK_ENV') or 'development'
    DEBUG = os.environ.get('DEBUG') or False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'its-a-secret-to-everyone'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
        os.environ.get('MYSQL_USER'),
        os.environ.get('MYSQL_PASSWORD'),
        os.environ.get('MYSQL_HOST'),
        os.environ.get('MYSQL_PORT'),
        os.environ.get('MYSQL_DB')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_TIMEOUT = 590
    SQLALCHEMY_POOL_RECYCLE = 590
    UPLOAD_FOLDER = 'data/save'
