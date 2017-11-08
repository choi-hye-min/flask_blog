from flask import Flask

from blog.blueprients import main

def print_settings(config):
    print('========================================================')
    print('SETTINGS for PHOTOLOG APPLICATION')
    print('========================================================')
    for key, value in config:
        print('%s=%s' % (key, value))
    print('========================================================')

def create_app():
    blog_app = Flask(__name__)

    blog_app.config.from_object('blog.blog_config.ApplicationMode')
    # print_settings(blog_app.config.items()) # Application Config 설정표시

    from blog.database import DBManager
    from blog.blog_config import ApplicationMode

    DBManager.init(ApplicationMode.SQLALCHEMY_DATABASE_URI)
    DBManager.init_db()

    return blog_app

blog_app = create_app()
from blog.views import main