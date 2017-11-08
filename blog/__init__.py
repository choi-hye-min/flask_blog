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

    return blog_app