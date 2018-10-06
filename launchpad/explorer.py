from flask import Blueprint

explorer = Blueprint('explorer', __name__, template_folder='templates')

@explorer.route('/')
def index():
    return 'Explorer index'

@explorer.route('/test')
def test():
    return 'Explorer test'
