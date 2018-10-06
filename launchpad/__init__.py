from flask import Flask
from launchpad.api import launchpad_api
from launchpad.explorer import explorer

app = Flask(__name__)
app.register_blueprint(launchpad_api, url_prefix='/api')
app.register_blueprint(explorer)
