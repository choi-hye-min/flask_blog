from blog import blog_app

@blog_app.route('/')
def index():
    return 'hello index!!'