from flask import Blueprint

curriculum_api = Blueprint('curriculum_api', __name__, template_folder='templates')

@curriculum_api.route('/test')
def test():
    return 'API test'
