from api import database
from api.models.Property import Property

class PropertyLoader:

    @staticmethod
    def getAllProperties():
        return Property.query.all()