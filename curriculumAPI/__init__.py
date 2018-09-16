from flask import Flask
from curriculumAPI.api import curriculum_api
from curriculumAPI.explorer import explorer

app = Flask(__name__)
app.register_blueprint(curriculum_api, url_prefix='/api')
app.register_blueprint(explorer)
