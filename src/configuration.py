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

class DevelopmentConfiguration(Configuration):
    @classmethod
    def init_app(configuration_class, application):
        Configuration.add_file_logger(application, logging.DEBUG)

class TestConfiguration(Configuration):
    @classmethod
    def init_app(configuration_class, application):
        application.logger.addHandler(logging.NullHandler())

class ProductionConfiguration(Configuration):
    @classmethod
    def init_app(configuration_class, application):
        Configuration.add_file_logger(application, logging.WARNING)

environmentConfigurationDictionary = {
    'development': DevelopmentConfiguration,
    'testing': TestConfiguration,
    'production': ProductionConfiguration
}