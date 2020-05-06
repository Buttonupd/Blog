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
    FLASK_ADMIN = os.environ.get('FLASKY_ADMIN')

class DevConfig (Config):
    DEBUG= True
    SQLALCHEMY_DATABASE_URI = ''

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''

    @classmethod
    def __init__(cls, app):
        Config.init_app(app)
        import logging
        from logging.handlers import SMTPHandler
        credits = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None ) is not None:
            credits = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIN_USE_TLS', None):
                secure = ()
        

        mail_handler = SMTPHandler(
          host = (cls.MAIL_SERVER, cls.MAIL_PORT),
          from = cls.MAIL_SENDER
          to = cls.FLASK_ADMIN
          subject = cls.SUBJECT_PREFIX
          credits = credits
          secure = secure)
          mail_handler.setLevel(logging.ERROR)
          app.logger.addHandler = (mail_handler)
          

        



