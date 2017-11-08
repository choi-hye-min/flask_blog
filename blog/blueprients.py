from flask import Blueprint

def _factory(partial_module_string, static_folder):
    name = partial_module_string
    import_name = 'blog.{}'.format(partial_module_string)
    template_folder = 'templates'
    blueprint = Blueprint(name, import_name, template_folder=template_folder, static_folder=static_folder)
    return blueprint

main = _factory('main', '../../static')
#photolog = Blueprint('photolg', __name__, template_folder='../templates', static_folder='../static')

__all__ = ['main']