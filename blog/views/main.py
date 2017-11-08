from blog import blog_app
from blog.model import *

@blog_app.route('/')
def index():
    return 'hello index!!'