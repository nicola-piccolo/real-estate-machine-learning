from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configuration import environmentConfigurationDictionary

database = SQLAlchemy()

def create_application (environment_name):
    application = Flask(__name__)
    environmentConfigurationDictionary[environment_name].init_app(application)
    database.init_app(application)

    from .routes import realEstateMl as realEstateMl_blueprint
    application.register_blueprint(realEstateMl_blueprint, url_prefix='/api')

    return application