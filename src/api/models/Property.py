from .. import database

class Property(database.Model):
    __tablename__ = 'property'
    id = database.Column(database.Integer, primary_key=True)
    rooms = database.Column(database.Integer)
    distance = database.Column(database.Float)
    post_code = database.Column(database.Integer)
    property_count = database.Column(database.Integer)
    price = database.Column(database.Float)
    property_type = database.Column(database.String(1))

    def __init__(self, rooms, distance, postCode, propertyCount, price, propertyType):
        self.rooms = rooms
        self.distance = distance
        self.post_code = postCode
        self.property_count = propertyCount
        self.price = price
        self.property_type = propertyType

    def __repr__(self):
        return '<Property %r>' % self.id
    
    @property
    def serialized(self):
        return {
            'id': self.id,
            'rooms': self.rooms,
            'distance': self.distance,
            'postCode': self.post_code,
            'propertyCount': self.property_count,
            'price': self.price,
            'propertyType': self.property_type
        }