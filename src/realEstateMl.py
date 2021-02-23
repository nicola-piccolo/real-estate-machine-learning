import os
from rest import create_application

environment = os.getenv('APPLICATION_ENVIRONMENT') or 'development'
application = create_application(environment)