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
        "propertyCount": {
            "type": "integer",
            "minimum": 1
        },
        "h": {
            "type": "integer",
            "minimum": 0,
            "maximum": 1
        },
        "u": {
            "type": "integer",
            "minimum": 0,
            "maximum": 1
        },
        "t": {
            "type": "integer",
            "minimum": 0,
            "maximum": 1
        }
    },
    "required": ["rooms","distance","postCode","propertyCount","h","u","t"]
}