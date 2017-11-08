from blog import blog_app
from blog.blog_config import ApplicationMode

if __name__ == '__main__':
    blog_app.run(
        host=ApplicationMode.HOST,
        port=ApplicationMode.PORT
    )
