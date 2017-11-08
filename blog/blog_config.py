class Config(object):
    DB_URL = 'mysql+pymysql://root:1234@localhost/blog?charset=utf8'

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = '84qXU6uv1XyDbM780civoBA7U4mnmKEQ0FnaBQn63go'
    HOST = '0.0.0.0'
    PORT = 80

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'aerga5h4uy56rtujsrRTHRThderfg53dfg35HGERHGRHJ4rheszrgh'
    HOST = '0.0.0.0'
    PORT = 5000

class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = '456y$%U%^UJsezrdfgaw4rgerlogjai89y38%wtGRDS'
    HOST = '0.0.0.0'
    PORT = 5000


ApplicationMode = DevelopmentConfig