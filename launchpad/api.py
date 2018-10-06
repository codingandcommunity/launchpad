from flask import Blueprint

launchpad_api = Blueprint('launchpad_api', __name__, template_folder='templates')

@launchpad_api.route('/test')
def test():
    return 'API test'
