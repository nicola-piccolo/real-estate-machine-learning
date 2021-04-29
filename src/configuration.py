import logging
from logging.handlers import RotatingFileHandler
import os

class Configuration:
    @staticmethod
    def add_file_logger(application, logging_level):
        base_directory = os.path.abspath(os.path.dirname(__file__))
        default_logs_directory = base_directory + '/logs'
        logs_directory = os.environ.get('LOGS_DIRECTORY') or default_logs_directory
        log_filepath = logs_directory + '/application.log'
        file_logger = RotatingFileHandler(log_filepath, maxBytes=1048576, backupCount=10)
        file_logger.setLevel(logging_level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_logger.setFormatter(formatter)
        application.logger.addHandler(file_logger)
    
    @staticmethod
    def set_database_connection_string(application):
        username = os.environ.get('REAL_ESTATE_ML_DATABASE_USER')
        password = os.environ.get('REAL_ESTATE_ML_DATABASE_PASSWORD')
        hostname = os.environ.get('REAL_ESTATE_ML_DATABASE_HOSTNAME')
        database = os.environ.get('REAL_ESTATE_ML_DATABASE_NAME')
        connection_string = f'mysql+mysqlconnector://{ username }:{ password }@{ hostname }/{ database }'
        application.config['SQLALCHEMY_DATABASE_URI'] = connection_string
        application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class DevelopmentConfiguration(Configuration):

    @classmethod
    def init_app(configuration_class, application):
        Configuration.add_file_logger(application, logging.DEBUG)
        Configuration.set_database_connection_string(application)
        

class ProductionConfiguration(Configuration):

    @classmethod
    def init_app(configuration_class, application):
        Configuration.add_file_logger(application, logging.WARNING)
        Configuration.set_database_connection_string(application)

environmentConfigurationDictionary = {
    'development': DevelopmentConfiguration,
    'production': ProductionConfiguration
}