from blog import create_app
from blog.blog_config import ApplicationMode

application = create_app()

if __name__ == '__main__':
    application.run(
        host=ApplicationMode.HOST,
        port=ApplicationMode.PORT
    )
