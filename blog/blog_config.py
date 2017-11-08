class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/blog?charset=utf8'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '84qXU6uv1XyDbM780civoBA7U4mnmKEQ0FnaBQn63go'
    HOST = '0.0.0.0'
    PORT = 80

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'aerga5h4uy56rtujsrRTHRThderfg53dfg35HGERHGRHJ4rheszrgh'
    HOST = '127.0.0.1'
    PORT = 5000

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = '456y$%U%^UJsezrdfgaw4rgerlogjai89y38%wtGRDS'
    HOST = '0.0.0.0'
    PORT = 5000


ApplicationMode = DevelopmentConfig