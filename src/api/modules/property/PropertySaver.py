from api import database

class PropertySaver:

    @staticmethod
    def saveNewProperty(property):
        database.session.add(property)
        database.session.commit()