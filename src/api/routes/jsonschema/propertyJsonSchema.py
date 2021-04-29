schema = {
    "type": "object",
    "properties": {
        "rooms": {
            "type": "integer",
            "minimum": 1
        },
        "distance": {
            "type": "number",
            "minimum": 0
        },
        "postCode": {
            "type": "integer",
            "minimum": 1
        },
        "price": {
            "type": "number",
            "minimum": 0
        },
        "propertyCount": {
            "type": "integer",
            "minimum": 1
        },
        "propertyType": {
            "type": "string",
            "pattern": "^[uht]$"
        }
    },
    "required": ["rooms","distance","postCode","price","propertyCount","propertyType"]
}