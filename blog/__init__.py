from flask import Flask, render_template, request, url_for

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
    print_settings(blog_app.config.items())

    # from flask_sqlalchemy import SQLAlchemy
    # global db
    # db = SQLAlchemy(blog_app)

    from blog.database import DBManager
    from blog.blog_config import ApplicationMode

    DBManager.init(ApplicationMode.SQLALCHEMY_DATABASE_URI)
    DBManager.init_db()

    # Views
    from blog.views import main

    @blog_app.route('/')
    def main():
        return 'main'

    return blog_app