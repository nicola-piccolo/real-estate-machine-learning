from api.models.Property import Property

class PropertyRequestMapper:

    @staticmethod
    def mapRequestIntoProperty(requestPayload):
        property = Property(
            rooms = requestPayload['rooms'],
            distance = requestPayload['distance'],
            postCode = requestPayload['postCode'],
            propertyCount = requestPayload['propertyCount'],
            price = requestPayload['price'],
            propertyType = requestPayload['propertyType']
        )
        return property