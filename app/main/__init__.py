# from flask import flask
from flask import Blueprint
# from .config import DevConfig
#Initializing application
main = Blueprint('main',__name__)
from . import view,error
def create_app(config_name):
    app = Flask(__name__,instance_relative_config = True)
# creating the app configuration
app.config.from_object(config_options[config_name])
app.config.from_pyfile('config.py')
from app import views
# Initializing flask extensions
bootstrap.init_app(app)

    # Registering the blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

# return app
