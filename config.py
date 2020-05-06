import os

dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get(SECRET_KEY)
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SERVER = 'smpt.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE-TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SUBJECT_PREFIX = 'Blog'
    MAIL_SENDER = 'Dankariuki0101@gmail.com'
    FLASK_POST_PER_PAGE = 20
    FLASK_SLOW_DB_QUERY_TIME = 0.05
    FLASK_COMMENTS_PER_PAGE = 20
    FLASK_FOLLOWERS_PAGE = 20


class DevConfig 