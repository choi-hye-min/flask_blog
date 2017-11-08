from flask import Flask, render_template, request, url_for

def create_app():
    blog_app = Flask(__name__)

    return blog_app